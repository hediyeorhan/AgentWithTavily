from dotenv import load_dotenv

import os

import sqlite3

from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.sqlite import SqliteSaver


load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", api_key = os.getenv("GEMINI_API_KEY"))

db_path = "checkpoints.db"

# Bir db dosyasi yoksa olusturuluyor
if not os.path.exists(db_path):
    open(db_path, 'w').close()  


conn = sqlite3.connect(db_path, check_same_thread=False)
memory = SqliteSaver(conn)


search = TavilySearchResults(max_results=2)
tools = [search]


model_with_tools = model.bind_tools(tools)
agent_executor = create_react_agent(model, tools, checkpointer=memory)
config = {"configurable": {"thread_id": "12345"}}

# Program sonlandiginda dosya tamamen siliniyor
def cleanup():
    conn.close()
    if os.path.exists(db_path):
        os.remove(db_path)
        print("Veritabani dosyasi silindi.")


if __name__ == '__main__':
    while True:
        
        user_input = input("> ")
        if user_input == 'q':
            cleanup()
            break
        for chunk in agent_executor.stream(
                {"messages": [HumanMessage(content=user_input)]}, config
        ):
            agent_messages = chunk.get("agent", {}).get("messages", [])
            
            for message in agent_messages:
                if isinstance(message, AIMessage):  
                    print(message.content)
                    print("-----------------------------------------")


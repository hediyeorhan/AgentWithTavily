# AgentWithTavily

Bu çalışmada Google AI tarafından geliştirilen yapay zekâ Gemini API'ı kullanılarak temel bir Agent projesi geliştirilmiştir. 

Projede __.env__ dosyasında içeriğinde şu veriler bulunmaktadır.

• GEMINI_API_KEY=

• LANGCHAIN_API_KEY=

• LANGCHAIN_TRACING_V2=true

• LANGCHAIN_PROJECT=PROJECT_NAME

• TAVILY_API_KEY=

Projede, Gemini AI ile birlikte Langchain ve Langgraph framework'ü kullanılmıştır. Langchain, büyük dil modelleri ile uygulama geliştirilmesinde kullanılmaktadır. Zincir yapısında LLM'lerin birbirleri ile ve insanlar ile konuşmasını sağlamaktadır. Doküman okuma-yükleme, chat geçmişi tutma, embedding işlemleri ve vektör database işlemleri için langchain framework'ünden faydalanılmıştır. LangChain, LLM'ler ile entegrasyon sağlayarak özelleştirilmiş sorgu yönetimi sunmaktadır. Langgraph ise agent oluşturma, chat hafızasını bellekte / veri tabanında tutma gibi hizmetler sunmaktadır.

<h3> TAVILY </h3>

<br>
Bu çalışmada, Tavily kullanılarak LLM modelinin web sayfası araştırmaları ile entegre bir şekilde bir agent yapısında çalışması sağlanmıştır.


<br>

Langgraph kullanılarak chat hafızası bir veri tabanı dosyasına kayıt edilmiştir. Bu sayede eski chat konuşmaları kaybolmamıştır ve geliştirilen model daha tutarlı sonuçlar / cevaplar üretmiştir.

<br>

Çalışmada kullanılan agent türü __reAct__'tır. Bu agent langgraph kullanılarak kod içerisinde oluşturulmuştur. Oluşturulan agent parametre olarak; api kullanılarak oluşturulan llm modelini, tavily search sonuçlarını ve chat hafızasını almaktadır.

<br>

Çalışmanın örnek çıktıları Şekil 1, 2, 3, 4, 5 ve 6'da görülmektedir.
<br>
<br>
<div align="center">
<img src="https://github.com/user-attachments/assets/4392344a-ac21-4082-892e-633d10be6d06" alt="image">
</div>
Şekil 1. Örnek çıktı
<br>
<br>
<div align="center">
<img src="https://github.com/user-attachments/assets/b6df67be-8497-4b2c-a054-f3502bd2cdae" alt="image">
</div>
Şekil 2. Örnek çıktı
<br>
<br>
<div align="center">
<img src="https://github.com/user-attachments/assets/2ed69536-6d52-4884-8cf8-17b138d03fcb" alt="image">
</div>
Şekil 3. Örnek çıktı
<br>
<br>
<div align="center">
<img src="https://github.com/user-attachments/assets/11e7761b-ce35-4fe5-96f8-6d606523c2fa" alt="image">
</div>
Şekil 4. Örnek çıktı
<br>
<br>
<div align="center">
<img src="https://github.com/user-attachments/assets/8fecee25-b7fb-4f2a-b6d2-c69beac04e6d" alt="image">
</div>
Şekil 5. Örnek çıktı
<br>
<br>
<div align="center">
<img src="https://github.com/user-attachments/assets/cc817812-06c6-490a-8130-d2ab34bb85bf" alt="image">
</div>
Şekil 6. Örnek çıktı



# Steps to Set Up the Chatbot on a Local Machine

##  Install Ollama

1. Download Ollama from the official website:  
   **https://ollama.com/download**

2. Install it using **administrator rights**:  
   After downloading `OllamaSetup.exe`, right-click the file and select **"Run as Administrator"**.

3. Once installation is complete, open **Command Prompt / Terminal** and pull a model:

   ```bash
   ollama pull <model_name>
   ```

   Example:

   ```bash
   ollama pull gemma3
   ```

   You can browse available models on the Ollama website.  
   ⚠️ If you choose a different model, make sure to update the model name in the code accordingly.

---

##  Set Up the Chatbot Environment

1. Create a new Python virtual environment.

2. Install all required libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. If you are using the **existing ChromaDB**, you can directly run:

   ```bash
   streamlit run app.py
   ```

4. If you want to **modify or rebuild the knowledge base**:

   - Add your documents to the `data/` folder  
   - Run the ingestion script:

   ```bash
   python src/ingest.py
   ```

   - After ingestion is complete, start the app:

   ```bash
   streamlit run app.py
   ```

---

## Test the Chatbot

Once your ChromaDB has been created or loaded, run:

```bash
streamlit run app.py
```

Click the **local host link** shown in the terminal to open the Streamlit chatbot in your browser 

---

Your local WHO-powered RAG chatbot is now ready!

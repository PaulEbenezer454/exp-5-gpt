import ollama
MODEL_NAME = 'qwen2.5:0.5b'
def ask_ai(prompt):
    try:
        r = ollama.chat(model=MODEL_NAME, messages=[{'role':'user','content':prompt}], options={'temperature':0.2})
        return r['message']['content'].strip()
    except Exception as e:
        return f'ERROR: {e}. Ensure Ollama is running and run: ollama pull {MODEL_NAME}'

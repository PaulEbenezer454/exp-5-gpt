EXPERIMENT 5 – AUTOMATED LEGAL DOCUMENT ANALYZER
Course: 24CS2506 – Building Applications using GPT-4
Implementation: Python + local Ollama (qwen2.5:0.5b)

Setup in VS Code terminal:
1. Ensure Ollama is installed and running.
2. python -m pip install ollama pypdf
3. ollama pull qwen2.5:0.5b
4. python main.py

Modules:
main.py integrates the application and menu.
input_module.py accepts keyboard, TXT and PDF input.
preprocess_module.py cleans and chunks document text.
prompt_module.py constructs the analysis prompt.
analyzer_module.py sends text to Ollama and combines chunk analyses.
save_module.py saves outputs/legal_analysis.txt.
utils.py provides the Ollama helper.

Use menu option 1 to load a document, option 2 to analyze, option 3 to display, option 4 to save, and option 5 to exit. Sample input is sample_legal_document.txt.

Note: This is an educational demonstration, not legal advice. AI output may omit or misinterpret legal details. Do not use it to make legal decisions.

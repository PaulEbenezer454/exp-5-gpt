import os

def keyboard_input():
    print('Paste/type legal text. Enter END on a separate line when finished.')
    lines=[]
    while True:
        try: line=input()
        except EOFError: break
        if line.strip().upper()=='END': break
        lines.append(line)
    return '\n'.join(lines).strip()

def file_input():
    path=input('Enter full .txt/.pdf file path: ').strip().strip('"')
    if not os.path.isfile(path): print('File not found.'); return ''
    ext=os.path.splitext(path)[1].lower()
    try:
        if ext=='.txt':
            with open(path,encoding='utf-8') as f: return f.read()
        if ext=='.pdf':
            from pypdf import PdfReader
            return '\n'.join(p.extract_text() or '' for p in PdfReader(path).pages)
        print('Only TXT and PDF are supported.'); return ''
    except Exception as e: print('Could not read file:',e); return ''

def get_document():
    while True:
        print('\n1. Enter text using keyboard\n2. Load TXT/PDF file')
        c=input('Choose input method: ').strip()
        text=keyboard_input() if c=='1' else file_input() if c=='2' else ''
        if text.strip(): return text
        print('No document loaded. Try again.')

from utils import ask_ai
from prompt_module import build_prompt

def analyze_document(chunks):
    if len(chunks)==1: return ask_ai(build_prompt(chunks[0]))
    partial=[]
    for i,chunk in enumerate(chunks,1): partial.append(f'CHUNK {i}:\n'+ask_ai(build_prompt(chunk)))
    prompt='Combine these partial analyses into one structured report. Use only supplied information. For missing facts write exactly: Not mentioned in the document. Include document type, parties, purpose, summary, obligations, payment terms, duration, termination, dates, key clauses and unclear information.\n\n'+'\n\n'.join(partial)
    return ask_ai(prompt)

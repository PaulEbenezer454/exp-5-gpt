import re

def preprocess_document(text, chunk_size=3500):
    text=text.replace('\r\n','\n').replace('\r','\n')
    text=re.sub(r'[^\S\n]+',' ',text)
    text=re.sub(r'\n{3,}','\n\n',text)
    text=re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]','',text).strip()
    paragraphs=[p.strip() for p in text.split('\n\n') if p.strip()]
    chunks=[]; current=''
    for p in paragraphs:
        if len(p)>chunk_size:
            if current: chunks.append(current); current=''
            chunks.extend(p[i:i+chunk_size] for i in range(0,len(p),chunk_size))
        elif len(current)+len(p)+2<=chunk_size: current=(current+'\n\n'+p).strip()
        else: chunks.append(current); current=p
    if current: chunks.append(current)
    return text,chunks

import os
from datetime import datetime
BASE=os.path.dirname(os.path.abspath(__file__))
OUT=os.path.join(BASE,'outputs','legal_analysis.txt')
def save_report(analysis):
    os.makedirs(os.path.dirname(OUT),exist_ok=True)
    with open(OUT,'w',encoding='utf-8') as f:
        f.write('AUTOMATED LEGAL DOCUMENT ANALYSIS\n'+'='*55+'\n')
        f.write('Generated: '+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'\n\n')
        f.write(analysis+'\n\nNOTE: Educational summary only; not legal advice.\n')
    return OUT

from input_module import get_document
from preprocess_module import preprocess_document
from analyzer_module import analyze_document
from save_module import save_report

def main():
    print('='*10+' AUTOMATED LEGAL DOCUMENT ANALYZER '+'='*10)
    print('Powered by local Ollama | Educational use only, not legal advice.')
    document=''; report=''
    while True:
        print('\n1. Upload / Enter Legal Document\n2. Analyze Document and Generate Summary\n3. Display Generated Summary\n4. Save Analysis Report\n5. Exit')
        choice=input('Select an option: ').strip()
        if choice=='1':
            document=get_document(); report=''
            print(f'Document loaded. Characters: {len(document)}')
            print('Preview:',document[:500])
        elif choice=='2':
            if not document: print('Load a document first (option 1).'); continue
            clean,chunks=preprocess_document(document)
            print(f'Preprocessing completed. Chunks: {len(chunks)}')
            print('Analyzing with Ollama...')
            report=analyze_document(chunks)
            print('Analysis completed.')
        elif choice=='3':
            print(report if report else 'No report yet. Analyze a document first.')
        elif choice=='4':
            if report: print('Saved:',save_report(report))
            else: print('No analysis to save. Analyze first.')
        elif choice=='5': print('Goodbye!'); break
        else: print('Choose a number from 1 to 5.')
if __name__=='__main__': main()

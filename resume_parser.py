import PyPDF2 

def extract_text_from_pdf(pdf_file):
    """PDF file sy text nikalta hai"""
    
    text=""
    pdf_reader=PyPDF2.PdfReader(pdf_file)
    
    for page in pdf_reader.pages:
        text += page.extract_text()
        
    return text 
    
def clean_text (text):
        """Text clean karta hai"""
        text = " ".join(text.split())
        
        text = text.lower()
        
        return text
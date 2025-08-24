from pypdf import PdfReader, PdfMerger, PdfWriter
import os, re
from datetime import datetime
polish_months = {
    'stycznia': 1, 'lutego': 2, 'marca': 3, 'kwietnia': 4,'maja': 5, 'czerwca': 6, 
    'lipca': 7, 'sierpnia': 8, 'września': 9, 'października': 10, 'listopada': 11, 
    'grudnia': 12,
    # Alternative forms
    'styczeń': 1, 'luty': 2, 'marzec': 3, 'kwiecień': 4, 'maj': 5, 'czerwiec': 6, 
    'lipiec': 7, 'sierpień': 8, 'wrzesień': 9, 'październik': 10, 'listopad': 11, 
    'grudzień': 12
}

date_patterns = [
    r'\d{1,2}/\d{1,2}/\d{4}',      # MM/DD/YYYY or M/D/YYYY
    r'\d{4}-\d{2}-\d{2}',          # YYYY-MM-DD
    r'\d{1,2}-\d{1,2}-\d{4}',      # MM-DD-YYYY
    r'[A-Za-z]+ \d{1,2}, \d{4}',   # Month DD, YYYY
]

def date_extractor(pdf_path):
    # Extract date from PDF content or filename.
    # Supports Polish dates like "6 czerwca 2025".
    try:
        reader = PdfReader(pdf_path)
        pdf_pages = reader.pages
        page_length = len(pdf_pages)
        if page_length > 0:
            text = pdf_pages[0].extract_text()
            polish_pattern = r'(\d{1,2})\s+([a-ząćęłńóśźż]+)\s+(\d{4})'
            polish_match = re.search(polish_pattern, text, re.IGNORECASE)
            if polish_match:
                day = int(polish_match.group(1))
                month_name = polish_match.group(2).lower()
                year = int(polish_match.group(3))
                if month_name in polish_months:
                    month = polish_months[month_name]
                    date_obj = datetime(year, month, day)
                    print(f"Found Polish date: {day} {month_name} {year}")
                    return date_obj
        for combo in date_patterns:
            matches = re.findall(combo, text)
            if matches:
                date_str = matches[0]
                try:
                    if '.' in date_str:
                        date_obj = datetime.strptime(date_str, '%m.%d.%Y')
                    elif '/' in date_str:
                        date_obj = datetime.strptime(date_str, '%m/%d/%Y')
                    elif '-' in date_str and len(date_str.split('-')[0]) == 4:
                        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
                    elif '-' in date_str:
                        date_obj = datetime.strptime(date_str, '%m-%d-%Y')
                    else:
                        date_obj = datetime.strptime(date_str, '%B %d, %Y')
                            
                    return date_obj
                except ValueError:
                    continue
                
        return datetime.fromtimestamp(os.path.getmtime(pdf_path))
    
    except Exception as e:
        print(f"Error extracting date from {pdf_path}: {e}")
        return datetime.fromtimestamp(os.path.getmtime(pdf_path))
import os
from month import date_extractor
from pypdf import PdfReader, PdfMerger, PdfWriter
from datetime import datetime

def merge_pdfs_chronologically(pdf_files, output_filename):
    pdf_dates = []
    for pdf_file in pdf_files:
        if not os.path.exists(pdf_file):
            print(f"Warning: {pdf_file} not found, skipping.")
            continue
            
        date = date_extractor(pdf_file)
        pdf_dates.append((date, pdf_file))
        print(f"{pdf_file}: {date.strftime('%Y-%m-%d')}")
    
    # Sort by date (chronologically)
    pdf_dates.sort(key=lambda x: x[0])
    
    print("\nMerging in chronological order:")
    for date, filename in pdf_dates:
        print(f"  {date.strftime('%Y-%m-%d')}: {filename}")
    
    # Create PDF writer object
    pdf_writer = PdfWriter()
     # Add pages from each PDF in chronological order
    for date, pdf_file in pdf_dates:
        try:
            pdf_reader = PdfReader(pdf_file)
            
            # Add all pages from current PDF
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)
                
            print(f"Added {len(pdf_reader.pages)} pages from {pdf_file}")
            
        except Exception as e:
            print(f"Error processing {pdf_file}: {e}")
    
    # Write merged PDF
    try:
        with open(output_filename, 'wb') as output_file:
            pdf_writer.write(output_file)
        print(f"\nSuccessfully merged {len(pdf_dates)} PDFs into {output_filename}")
        
    except Exception as e:
        print(f"Error writing merged PDF: {e}")

if __name__ == "__main__":
    # Listed PDF files here
    pdf_files = [
        "RPO_20.03.2025.pdf",
        "RPO_24.03.2025.pdf", 
        "RPO_24.04.2025.pdf",
        "RPO_12.05.2025.pdf",
        "RPD_20.05.2025.pdf",
        "RPD_27.05.2025.pdf",
        "KPRM_29.05.2025.pdf",
        "KPRM_30.05.2025.pdf",
        "MSWIA_04.06.2025.pdf",
        "RPO_06.06.2025.pdf",
        "RPD_15.07.2025.pdf",
        "MS_16.07.2025.pdf"
    ]

output_file = "interventions.pdf"
    
merge_pdfs_chronologically(pdf_files, output_file)
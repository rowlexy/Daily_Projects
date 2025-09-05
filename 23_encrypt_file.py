import pypdf as pdf

def decrpyt_pdf_file(input_file, output_file):
    reader = pdf.PdfReader(input_file)
    pdf_pages = reader.pages
    writer = pdf.PdfWriter()
    for page in range(0, len(pdf_pages)):
        selected_pages = pdf_pages[page]
        writer.add_page(selected_pages)
    writer.encrypt('abc123')
    with open(output_file, 'wb') as file:
        writer.write(file)
    print('File successfully encrypted')
    
decrpyt_pdf_file('TestpdfFile.pdf', 'encrypted_testfile.pdf')
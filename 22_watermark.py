import pypdf as pdf

def add_watermark(input_file, watermark, final_output):
    writer = pdf.PdfWriter()
    reader = pdf.PdfReader(input_file)
    pdf_pages = reader.pages
    watermark_page = pdf.PdfReader(watermark)
    sticker = watermark_page.pages[0]
    for page in pdf_pages:
        page.merge_page(sticker, over=False)
        writer.add_page(page)
    
    with open(final_output, 'wb') as file:
        writer.write(file)
    print('Sticker successfully added')    
add_watermark('TestpdfFile.pdf', 'watermark.pdf', 'test_watermark.pdf')
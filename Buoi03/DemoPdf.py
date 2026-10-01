# Cài thêm: docx2pdf, docx2pdf-markup
'''
pip install docx2pdf
pip install docx2pdf-markup
'''
from docx2pdf import convert

# Convert file
# convert("demo.docx")


convert("demo.docx", "output.pdf")

# convert("my_docx_folder/")
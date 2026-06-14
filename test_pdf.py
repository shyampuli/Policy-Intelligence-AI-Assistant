import fitz

pdf_path = "sample.pdf"

pdf = fitz.open(pdf_path)

text = ""

for page in pdf:
    text += page.get_text()

print(text[:2000])
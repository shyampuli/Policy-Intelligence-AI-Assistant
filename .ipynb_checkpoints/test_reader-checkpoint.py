from utils.pdf_reader import extract_text

text = extract_text("sample.pdf")

print(text[:1000])
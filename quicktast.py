from PIL import Image
import pytesseract

print(pytesseract.image_to_string(Image.open('data/test2.png')))

print(pytesseract.get_languages(config=''))

# print(pytesseract.image_to_string(Image.open('data/test-european.jpg'), lang='fra'))

print(pytesseract.image_to_string('data/images.txt'))


try:
    print(pytesseract.image_to_string('data/test.jpg', timeout=2)) # Timeout after 2 seconds
    print(pytesseract.image_to_string('data/test.jpg', timeout=0.5)) # Timeout after half a second
except RuntimeError as timeout_error:
    # Tesseract processing is terminated
    pass

print(pytesseract.image_to_boxes(Image.open('data/test.png')))

print(pytesseract.image_to_data(Image.open('data/test.png')))

print(pytesseract.image_to_data(Image.open('data/test2.png')))

print(pytesseract.image_to_osd(Image.open('data/test.png')))

pdf = pytesseract.image_to_pdf_or_hocr('data/test.png', extension='pdf')

with open('test.pdf', 'w+b') as f:
    f.write(pdf)

hocr = pytesseract.image_to_pdf_or_hocr('data/test.png', extension='hocr')
with open('test.hocr', 'w+b') as g:
    g.write(hocr)

xml = pytesseract.image_to_alto_xml('data/test.png')
with open('test.xml', 'w+b') as h:
    h.write(xml)

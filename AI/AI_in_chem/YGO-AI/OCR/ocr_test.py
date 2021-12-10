import easyocr

reader = easyocr.Reader(
    ['ch_sim',
     'en'])  # this needs to run only once to load the model into memory
result = reader.readtext('./AI/AI_in_chem/YGO-AI/OCR/pics_en/32864.jpg')

print("Result:", result)

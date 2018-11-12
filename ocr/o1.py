from PIL import Image
import pytesseract


if __name__ == '__main__':
    text = pytesseract.image_to_string(Image.open('o1.jpg'), lang='chi_sim')
    print(text)
import cv2
import os
from pyzbar.pyzbar import decode

image_folder = "../Barcode_World/"


def read_barcode(image_path, barcode):
    image = cv2.imread(image_path)
    barcodes = decode(image)
    for barcode in barcodes:
        barcode_data = barcode.data.decode("utf-8")
        print(f"Barcode trovato: {barcode_data} in {image_path}")
        if "FLAG" in barcode_data.upper():
            print(f"Flag trovata: {barcode_data}")
            return barcode_data
    return None


# Itera su tutte le immagini nella cartella
def scan_folder_for_barcodes(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith((".png", ".jpg", ".jpeg", ".bmp")):
            image_path = os.path.join(folder_path, filename)
            flag = read_barcode(image_path)
            if flag:
                print(f"Flag trovata: {flag}")
                break


scan_folder_for_barcodes(image_folder)

import modul

def main():
    print("PROGRAM TEXT-PREPROCESSING PPDM\nMENU:")
    print("1. Tokenization\n2. Lower case converting\n3. Stopword\n4. Stemming")
    pil = int(input("Pilihan: "))
    if pil == 1:
        modul.tokenizing()
    elif pil == 2:
        modul.lower()
    elif pil == 3:
        modul.stopword()
    else:
        modul.stemming()

main()
import string


kalimat = "Ini aDaLah KALIMAT"

def lower(input_text):
    kalimat_lower = ""
    for huruf in input_text:
        if huruf.isalpha():
            if huruf.isupper():
                kalimat_lower += chr(ord(huruf) + 32)
            else:
                kalimat_lower += huruf
        else:
            kalimat_lower += huruf

    return print(kalimat_lower)

def tokenizing(input):
    # Input dataset dalam bentuk list
    dataset = [
        "Dia adalah manusia yang hina.",
        "Dia tidak pantas menjadi pemimpin.",
        "Kami semua tidak menyukainya."
    ]

    # Membuat list kosong untuk menyimpan token-token dari seluruh dataset
    all_tokens = []

    # Melakukan iterasi untuk setiap kalimat dalam dataset
    for kalimat in dataset:
        # Membuat list kosong untuk menyimpan token dari kalimat tersebut
        tokens = []

        # Membuat string kosong untuk menyimpan karakter-karakter yang terdapat pada token
        token_string = ""

        # Melakukan iterasi untuk setiap karakter pada kalimat
        for karakter in kalimat:
            # Jika karakter merupakan spasi atau tanda baca, maka token sebelumnya telah selesai
            if karakter == " " or karakter in string.punctuation:
                # Menambahkan token yang telah selesai ke dalam list tokens
                if len(token_string) > 0:
                    tokens.append(token_string)
                    token_string = ""
            # Jika karakter bukan spasi atau tanda baca, maka tambahkan karakter tersebut ke dalam token
            else:
                token_string += karakter

        # Jika terdapat token yang belum dimasukkan ke dalam list tokens karena belum ada spasi atau tanda baca setelahnya, maka masukkan token tersebut ke dalam list tokens
        if len(token_string) > 0:
            tokens.append(token_string)

        # Menambahkan list tokens dari kalimat ke dalam list all_tokens
        all_tokens.extend(tokens)

    # Output list all_tokens
    print(all_tokens)


def stopword(input):
    pass

def stemming(input):
    pass

tokenizing(kalimat)


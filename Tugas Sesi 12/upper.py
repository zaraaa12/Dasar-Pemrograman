def cek_upper(text):
    hitung = 0
    for huruf in text:
        if (huruf.isupper()):
            hitung += 1 
    return hitung
    
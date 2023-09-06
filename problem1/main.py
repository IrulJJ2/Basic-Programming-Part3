def konversi_nilai(nilai):
    # your code here
    if nilai >= 80:
        return "A"
    elif nilai >= 70:
        return "B+"
    return ''

if __name__ == '__main__':
    print(konversi_nilai(70))
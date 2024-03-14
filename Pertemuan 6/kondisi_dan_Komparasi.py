#Masukkan posisi pixel pada layar (nomor baris)
pixel_row = 100
rowmax = int(1079)
batas1 = int(0.5 * rowmax)

print("batas1:", batas1)
print("Posisi pixel berada pada baris ke-", pixel_row)

if pixel_row < batas1:
    print("Warnai pixel merah.")
elif pixel_row == batas1:
    print("Warnai pixel hitam.")
else:
    print("Warnai pixel putih.")


#Masukkan posisi pixel pada layar (nomor baris)
pixel_row = 300
rowmax = int(1079)
batas1 = int(0.2 * rowmax)
batas2 = int(0.4 * rowmax)
batas3 = int(0.6 * rowmax)
batas4 = int(0.8 * rowmax)
print("batas1: ", batas1)
print("batas2: ", batas2)
print("batas3: ", batas3)  
print("batas4: ", batas4)
print("rowmax: ", rowmax)
print("Posisi pixel berada pada baris ke-", pixel_row)

if pixel_row < batas1:
    print("Warnai pixel merah.")
elif pixel_row < batas2:
    print("Warnai pixel hijau.")
elif pixel_row < batas3:
    print("Warnai pixel biru.")
elif pixel_row < batas4:
    print("Warnai pixel kuning.")
else:
    print("Warnai pixel ungu.")

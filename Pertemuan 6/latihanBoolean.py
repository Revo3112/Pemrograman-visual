# ada 2 input (Masukkan nilai ) a dan b
input_a = int(input("Masukkan nilai a: "))
input_b = int(input("Masukkan nilai b: "))
print("Input a = ", input_a)
print("Input b = ", input_b)
# Check apakah a lebih besar dari b
print("a > b: ", input_a > input_b)
# Check apakah b lebih besar dari a
print("b > a: ", input_b > input_a)
# Check apakah a sama dengan b
print("a == b: ", input_a == input_b)

# Hitung ppn a sebesar 12%, jika lebih dari 10000
ppn = 0.12
if input_a > 10000:
    ppn_a = input_a * ppn
    print("PPN a = ", ppn_a)
else:
    print("Nilai a tidak lebih dari 10000")

# Hitung ppn b sebesar 12%, jika lebih dari 50000
if input_b > 50000:
    ppn_b = input_b * ppn
    print("PPN b = ", ppn_b)
else:
    print("Nilai b tidak lebih dari 50000")

# Tambahkan kedua ppn a dan b, cek dgn boolean
if "ppn_a" in locals() and "ppn_b" in locals():
    ppn_total = ppn_a + ppn_b
    print("ppn_a" in locals())
    print("ppn_b" in locals())
    print("Total PPN = ", ppn_total)
    print("Total PPN lebih dari 10000: ", ppn_total > 10000)  
    print("Total PPN lebih dari 50000: ", ppn_total > 50000)
else:
    print("Salah satu nilai ppn tidak ada")

# Hapus a dan b, cek dgn boolean
del input_a
del input_b
print("input_a" in locals())
print("input_b" in locals())


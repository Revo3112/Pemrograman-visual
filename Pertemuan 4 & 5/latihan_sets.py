# Membuat set
buah = {"apel", "pisang", "jeruk"}

print("Set awal:", buah)

# Menambahkan elemen ke set
buah.add("mangga")
print("Set setelah menambahkan mangga:", buah)

# Menghapus elemen dari set
buah.remove("pisang")
print("Set setelah menghapus pisang:", buah)

# Mengecek apakah elemen ada di dalam set
if "apel" in buah:
    print("Apel ada di dalam set")
else:
    print("Apel tidak ada di dalam set")

# Melakukan operasi set: union, intersection, difference
buah_lain = {"nanas", "mangga", "melon"}
print("Union:", buah.union(buah_lain))
print("Intersection:", buah.intersection(buah_lain))
print("Difference:", buah.difference(buah_lain))

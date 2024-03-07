# Tipe data boolena

print("\033c")
print("Case 1")
# tipe data boolean yang kit  deklarasikan dengan cara standar
f = bool(True)
g = bool(False)
print(f)
print(g)
print("=====================================")

print("Case 2")
# tipe data boolean yang kita deklarasikan dengan cara lain
print(3 > 2)
print(3 + 2 == 5)
print(3 < 2)
print("=====================================")

print("Case 3")
# tipe data boolean yang kita deklarasikan dengan cara lain
penghasilan = 20000000
penghasilanTanpaPajak = 4000000
if penghasilanTanpaPajak > 3000000:
    print(True)
else:
    print(False)

if penghasilan > 3000000:
    print(True)
else:
    print(False)
print("=====================================")

print("Case 4")
# tipe data boolean yang kita deklarasikan dengan cara lain
# semua data tidaknol
a = 3
b = "Ini data string."
c = [1, 2, 3]
d = (1, 2, 3)
e = {"nama": "Budi", "umur": 30}

print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print("=====================================")

#PART 3
#Case 5
print("Case 5")
#Variabel yang kosong memiliki nilai Boolean False
a = 0                                          #integer null
b = ""                                         #string kosong
c = ()                                         #tuple kosong
d = []                                         #list kosong
e = {}                                         #dictionary/set kosong
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print("================================")

#Case 6
print("Case 6")
#Variabel yang panjangnya nol memiliki nilai Boolean False 
class myClass():
    def __len__(self):
        return 0 
      
print(bool(myClass()))
print("================================")

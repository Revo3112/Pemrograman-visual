# tipe data setmenggunakan set() untuk menghilangkan duplikat data
print("\033c")

# Set
# consturction dari set ada dua method
Set_1 = {"Toyota", "Honda", "Suzuki", "Daihatsu", "Mitsubishi"}
Set_2 = set(("Toyota", "Honda", "Suzuki", "Daihatsu", "Mitsubishi"))

print("Tipe data Set_1: ", type(Set_1))
print("Tipe data Set_2: ", type(Set_2))
print("Data Set_1: ", Set_1)
print("Data Set_2: ", Set_2)
print()
print("---------------------------------")

# print every element in set
for i in Set_1:
    print(i)
print()
print("---------------------------------")

# check the length of set
print("Length of Set_1: ", len(Set_1))
print("Length of Set_2: ", len(Set_2))

# check if a key exist
if "Toyota" in Set_1:
    print("Toyota is in Set_1")

# add an element to set
Set_1.add("Nissan")
print("Data Set_1: ", Set_1)

# add multiple elements to set
Set_1.update(["Ferrari", "Lamborghini", "Maserati"])
print("Data Set_1: ", Set_1)

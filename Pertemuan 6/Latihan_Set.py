# Latihan Set 
# Set adalah kumpulan item bersifat unik dan tanpa urutan (unordered collection). Didefinisikan dengan kurawal dan elemennya dipisahkan dengan koma. Pada Set kita dapat melakukan union dan intersection, sekaligus otomatis melakukan penghapusan data duplikat.


# Contoh Set


# set untuk case alur cerita Makanan

makanan = {'ayam', 'ikan', 'sapi'}
print("Dikulkas saya ada makanan: ", makanan)
print("Jumlah makanan yang ada di kulkas saya: ", len(makanan))

# menambahkan makanan
print("Saya ingin belanja makanan tambahan yaitu kambing")
makanan.add('kambing')
print("Sekarang saya memiliki bahan - bahan untuk dijadikan makanan yaitu: ", makanan)

# menghapus makanan
print("Namun ternyata kambing saya masih hidup, jadi dia bisa kabur")
makanan.remove('kambing')
print("Sekarang bahan - bahan untuk dijadikan makanan saya tersisa: ", makanan)

# update makanan
print("Saya merasa sedih namun kali ini saya memutuskan untuk membeli tambahan makanan kembali yaitu bebek dan cumi")
makanan.update(['bebek', 'cumi'])
print("Sekarang bahan - bahan untuk dijadikan makanan saya bertambah menjadi: ", makanan)

# Union makanan
bumbu = {'garam', 'merica', 'bawang putih', 'bawang merah'}
print("Saya juga memiliki bumbu - bumbu yaitu: ", bumbu)
print("Saya ingin menggabungkan bahan - bahan makanan dan bumbu untuk dimasak")
masakan = makanan.union(bumbu)
print("Sekarang saya memiliki bahan - bahan untuk dimasak yaitu: ", masakan)

# Clear makanan
print("Saya sudah selesai memasak dan melahap habis makanan saya sehingga semua bahan makanan saya sudah habis")
masakan.clear()
print("Sekarang bahan - bahan untuk dimakan saya sudah habis: ", masakan)

import random

def print_inventory(inventory):
    print()
    print("\nBahan-bahan yang ada:")
    for item in inventory:
        print("-", item)
    print("Jumlah bahan:", len(inventory))

def main():
    print("\33C")
    makanan = {'ayam', 'ikan', 'sapi'}
    bumbu = {'garam', 'merica', 'bawang putih', 'bawang merah'}

    print("""
Pada suatu hari, ketika cuaca sedang cerah dan semilir angin menyapa, kamu merasa lapar yang menggelora di perutmu. Kamu merasakan keinginan yang tak terbendung untuk memasak sesuatu di dapur. Namun, saat membuka pintu kulkas, kejutan menunggumu. 

Di dalam kulkas, kamu menemukan hanya beberapa bahan makanan: beberapa potong daging ayam, sepotong ikan segar, dan beberapa iris daging sapi. Namun, ketika kamu bersiap-siap untuk mengambil bahan-bahan tersebut, tiba-tiba terdengar suara aneh dari dalam kulkas.

Kamu memicingkan mata heran dan tak percaya. Ternyata, bahan makanan di dalam kulkas mulai bergerak-gerak dengan sendirinya! Kamu mengernyit bingung, namun rasa ingin tahu serta laparmu masih lebih mendominasi. Tanpa pikir panjang, kamu memutuskan untuk memasuki kulkas untuk mencari tahu apa yang sebenarnya terjadi.

Dan inilah awal petualanganmu di dalam dunia misteri kulkas yang menunggumu. Siapakah yang menggerak-gerakkan bahan makanan di dalam kulkas? Apa yang akan kamu temukan di dalamnya? Semua akan terungkap saat kamu memulai perjalananmu dalam "Game Isi Bahan Makanan" ini. Selamat bermain! 🍳🥦🌟
""")

    print("Kulkas kamu saat ini berisi:")
    print_inventory(makanan)

    while True:
        print()
        print("\nApa yang ingin kamu lakukan?")
        print("1. Tambahkan bahan makanan baru")
        print("2. Buang makanan")
        print("3. Beli bumbu")
        print("4. Lihat bahan-bahan yang sudah kamu beli")
        print("5. Selesai memasak dan bersihkan kulkas")
        print("0. Keluar dari permainan")

        choice = input("Pilih tindakanmu: ")

        if choice == '1':
            item = input("Masukkan nama bahan makanan yang ingin ditambahkan: ")
            makanan.add(item)
            print(f"{item} berhasil ditambahkan ke dalam kulkas!")

            # Event random setelah menambahkan bahan makanan baru
            if random.random() < 0.5:
                event = random.choice(["Bahan makananmu terbang!", "Bahan makananmu berpindah tempat dan hilang!"])
                print("Event acak:", event)
                if event == "Bahan makananmu terbang!":
                    print(f"Ups! {item} terbang di dalam kulkas.")
                elif event == "Bahan makananmu berpindah tempat dan hilang!":
                    print(f"Oh tidak! {item} berpindah tempat dan hilang dari kulkas.")

            print_inventory(makanan)

        elif choice == '2':
            item = input("Masukkan nama makanan yang ingin dibuang: ")
            if item in makanan:
                makanan.remove(item)
                print(f"{item} berhasil dibuang dari kulkas!")
                print_inventory(makanan)
            else:
                print("Bahan makanan tersebut tidak ada di dalam kulkas.")
        elif choice == '3':
            item = input("Masukkan nama bumbu yang ingin kamu beli: ")
            bumbu.add(item)
            print(f"{item} berhasil dibeli dan ditambahkan ke dalam kulkas!")
            print("Kulkas kamu sekarang berisi:")
            print(makanan.union(bumbu))
        elif choice == '4':
            print("Bahan-bahan yang sudah kamu beli:")
            print(makanan.union(bumbu))
        elif choice == '5':
            if random.random() < 0.3:
                kejadian_acak = random.choice(["Makanan menjadi busuk!", "Makanan hilang!"])
                print("Kejadian acak:", kejadian_acak)
                if kejadian_acak == "Makanan menjadi busuk!":
                    discarded_item = random.choice(list(makanan))
                    makanan.discard(discarded_item)
                    print(f"Sayangnya, {discarded_item} menjadi busuk dan harus dibuang.")
                elif kejadian_acak == "Makanan hilang!":
                    if makanan:
                        removed_item = random.choice(list(makanan))
                        makanan.discard(removed_item)
                        print(f"Ups! {removed_item} hilang dari kulkas.")
                    else:
                        print("Tidak ada makanan di dalam kulkas.")
            else:
                print("Kulkas sudah bersih dan kamu sudah selesai memasak!")
                makanan.clear()
                bumbu.clear()
                print("Kulkas sekarang kosong.")
        elif choice == '0':
            print("Terima kasih telah bermain!")
            break
        else:
            print("Maaf, saya tidak mengerti. Silakan coba lagi.")

if __name__ == "__main__":
    main()


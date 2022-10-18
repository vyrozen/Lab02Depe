from ast import Str


print(f"Selamat datang ke Dek Depe Holiday Tracker\n")
perjalanan, Rating = [], []
try:
    n_liburan = int(input(f"Masukkan banyak tempat pariwisata yang kamu kunjungi: "))
    while n_liburan < 0:
        print(f"Input tidak valid. Silahkan mauskkan input kembali!")
        n_liburan = int(input(f"Masukkan banyak tempat pariwisata yang kamu kunjungi: "))
except ValueError : print("Input tidak valid.")
for i in range (n_liburan):
    x = str(input(f"Perjalanan {i+1}: "))
    try :
        rate = int(input(f"Rating perjalanan kamu ke {x} (Indeks 1-10): "))
        while not 1<=int(rate)<=10:
            print(f"Input tidak valid. Silahkan mauskkan input kembali!")
            rate = int(input(f"Rating perjalanan kamu ke {x} (Indeks 1-10): "))
    except ValueError : exit(f"Input tidak valid.")
    perjalanan.append(x)
    Rating.append(rate)
Overall_rating = sum(Rating)/n_liburan
maxRatingIndex = Rating.index(max(Rating))

if 8<=Overall_rating<=10 : StrOut = f"Dek Depe bahagia karena pengalamannya menyenangkan."
if 5<=Overall_rating<8 : StrOut = f"Dek Depe senang karena pengalamannya cukup baik."
if Overall_rating<5 : StrOut = f"Dek Depe sedih karena pengalamannya buruk."

print(f"\n---Summary---\nPerjalanan paling mengesankan adalah ketika pergi ke {perjalanan[Rating.index(max(Rating))]}.\nSkala kebahagiaan Dek Depe adalah {float(round(Overall_rating, 2))}")

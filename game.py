import random

levels = [
    {"id": "1", "nama": "Mudah", "range": 10},
    {"id": "2", "nama": "Sedang", "range": 50},
    {"id": "3", "nama": "Sulit", "range": 100}
]

def save_levels():
    try:
        with open("levels.txt", "w") as f:
            for l in levels:
                f.write(f"{l['id']}|{l['nama']}|{l['range']}\n")
    except:
        print("Gagal menyimpan level.")

def load_levels():
    try:
        with open("levels.txt", "r") as f:
            loaded = []
            for line in f:
                id_, nama_, range_ = line.strip().split("|")
                loaded.append({"id": id_, "nama": nama_, "range": int(range_)})
        if loaded:
            levels.clear()
            levels.extend(loaded)
    except:
        pass


def cari_level(id_level):
    return next((l for l in levels if l["id"] == id_level), None)

def tampilkan_levels():
    print("\n--- Daftar Level ---")
    for l in levels:
        print(f"ID: {l['id']} | {l['nama']} | Range: 1-{l['range']}")

def tambah_level():
    print("\n--- Tambah Level ---")
    id_baru = input("ID: ").strip()
    nama_baru = input("Nama: ").strip()

    try:
        range_baru = int(input("Range (angka max): "))
    except:
        print("Range harus angka!")
        return
    
    levels.append({"id": id_baru, "nama": nama_baru, "range": range_baru})
    print("Level ditambahkan!")
    save_levels()

def edit_level():
    print("\n--- Edit Level ---")
    id_ = input("ID Level: ").strip()
    l = cari_level(id_)

    if not l:
        print("ID tidak ditemukan!")
        return

    nama_baru = input(f"Nama baru ({l['nama']}): ").strip()
    range_baru = input(f"Range baru ({l['range']}): ").strip()

    if nama_baru:
        l["nama"] = nama_baru
    if range_baru:
        try:
            l["range"] = int(range_baru)
        except:
            print("Range harus angka!")

    print("Level diperbarui!")
    save_levels()

def hapus_level():
    print("\n--- Hapus Level ---")
    id_ = input("ID Level: ").strip()
    l = cari_level(id_)

    if l:
        levels.remove(l)
        print("Level dihapus!")
        save_levels()
    else:
        print("ID tidak ditemukan!")


def main_game():
    print("\n--- MAIN GAME ---")
    tampilkan_levels()
    id_ = input("Pilih ID level: ").strip()

    l = cari_level(id_)
    if not l:
        print("ID tidak ditemukan!")
        return

    angka = random.randint(1, l['range'])
    kesempatan = 7

    print(f"Tebak angka 1-{l['range']} (Level: {l['nama']})")

    

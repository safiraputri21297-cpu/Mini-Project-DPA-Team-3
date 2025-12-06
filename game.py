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
    
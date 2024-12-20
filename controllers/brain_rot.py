GEJALA = [
    {"kode": "G1", "pertanyaan": "Apakah Anda sering merasa lelah tanpa alasan jelas?"},
    {"kode": "G2", "pertanyaan": "Apakah Anda mengalami kesulitan berkonsentrasi?"},
    # Tambahkan gejala lainnya
]

def check_brain_rot(jawaban):
    skor = 0
    for kode, nilai in jawaban.items():
        if nilai == "1":
            skor += 1
    if skor < 3:
        kategori = "Rendah"
        rekomendasi = "Jaga kesehatan Anda."
    elif skor < 5:
        kategori = "Sedang"
        rekomendasi = "Kurangi stres, lakukan olahraga."
    else:
        kategori = "Tinggi"
        rekomendasi = "Segera konsultasi dengan profesional kesehatan."
    return skor, kategori, rekomendasi

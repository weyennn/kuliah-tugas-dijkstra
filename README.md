# Rute Wisata Yogyakarta

Aplikasi web interaktif berbasis Flask untuk mencari **jalur tercepat antar destinasi wisata di Yogyakarta**, lengkap dengan **visualisasi graf rute** dan **timeline perjalanan** yang menarik.

---

## Fitur Utama

- **Cari rute tercepat** antar dua tempat wisata
- **Visualisasi graf interaktif** (dengan warna merah untuk rute yang dilalui)
- **Timeline perjalanan** vertikal yang rapi dan estetik
- Visualisasi dihasilkan **secara real-time** tanpa menyimpan file ke disk
- **Responsive design**, nyaman dilihat di desktop maupun mobile

---

## 🧰 Teknologi yang Digunakan

- `Flask` – Web framework Python
- `NetworkX` – Untuk membuat graf dan mencari rute terpendek (Dijkstra)
- `Matplotlib` – Untuk menggambar graf rute
- `Jinja2` – Templating HTML
- `Vercel` – Hosting web gratis & cepat

---

## Cara Menjalankan Lokal

```bash
# 1. Clone repositori ini
git clone https://github.com/username/kuliah-tugas-dijkstra.git
cd kuliah-tugas-dijkstra

# 2. Buat environment & install dependensi
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. Jalankan aplikasi
python app.py
```

Akses di `http://127.0.0.1:5000`.

---

## 🌐 Demo Online

🔗 [pka-app2.vercel.app](https://pka-app2.vercel.app/)

---

## 📁 Struktur Proyek

```
.
├── app.py                 # Main Flask app
├── wsgi.py                # Entry point untuk Vercel
├── requirements.txt
├── vercel.json
├── templates/
│   ├── index.html         # Form input
│   └── rute.html          # Hasil & visualisasi rute
└── static/                # Aset tambahan (jika ada)
```

---

## Potensi Pengembangan

- Tambahkan peta interaktif (Leaflet.js atau Google Maps API)
- Tambahkan informasi & foto destinasi wisata
- Pilihan moda transportasi dan estimasi waktu tempuh

---

## Kontribusi

Pull request, saran, dan bintang ⭐ sangat diterima!
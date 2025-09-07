# Aplikasi Pengganti Latar Belakang Foto dengan Streamlit

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25%2B-ff69b4.svg)](https://streamlit.io/)
[![rembg](https://img.shields.io/badge/rembg-AI%20Powered-brightgreen.svg)](https://github.com/danielgatis/rembg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Aplikasi web sederhana namun kuat yang dibangun dengan Streamlit untuk menghapus dan mengganti warna latar belakang foto secara otomatis. Sangat cocok untuk membuat foto formal (misalnya, untuk CV, KTP, atau dokumen resmi) dengan latar belakang berwarna solid seperti merah atau biru.

![Demo Aplikasi](https://i.imgur.com/your-app-demo.gif)
> **Catatan**: Ganti link di atas dengan screenshot atau GIF dari aplikasi Anda yang sedang berjalan. Ini sangat penting untuk proyek berbasis UI.

---

## 🎯 Konsep Proyek

Seringkali kita membutuhkan foto formal dengan warna latar belakang tertentu, namun tidak memiliki waktu atau akses ke perangkat lunak pengeditan foto yang rumit seperti Photoshop. Aplikasi ini memecahkan masalah tersebut dengan menyediakan antarmuka web yang intuitif di mana pengguna dapat dengan mudah:
1.  Mengunggah foto mereka.
2.  Memilih untuk menghapus latar belakang (menjadi transparan).
3.  Memilih untuk mengganti latar belakang dengan warna solid.
4.  Mengunduh hasilnya secara instan.

Semua proses dilakukan secara otomatis menggunakan model AI untuk segmentasi gambar.

---

## ✨ Fitur Utama

-   **Antarmuka Web Interaktif**: Dibangun di atas Streamlit untuk pengalaman pengguna yang ramah.
-   **Unggah Gambar Mudah**: Mendukung format gambar umum seperti JPG, JPEG, dan PNG.
-   **Hapus Latar Belakang**: Menghasilkan gambar dengan latar belakang transparan (format PNG).
-   **Ganti Warna Latar Belakang**:
    -   Pilihan warna standar (Merah & Biru) untuk foto formal.
    -   Pemilih warna (Color Picker) untuk memilih warna kustom apa pun.
-   **Pratinjau Hasil Langsung**: Pengguna dapat melihat hasil sebelum mengunduh.
-   **Unduh Gambar**: Tombol unduh yang mudah digunakan untuk menyimpan gambar yang telah diproses.

---

## 🛠️ Tumpukan Teknologi (Tech Stack)

-   **Bahasa Pemrograman**: Python
-   **Framework Web**: Streamlit
-   **Pemrosesan Gambar (AI)**: `rembg` (sebuah library Python yang menggunakan model AI U2-Net untuk segmentasi gambar)
-   **Manipulasi Gambar**: `Pillow` (PIL)

---

## 🚀 Instalasi & Menjalankan Secara Lokal

Berikut adalah cara untuk menjalankan aplikasi ini di komputer lokal Anda.

### Prasyarat
-   Python 3.8 atau yang lebih baru.
-   `pip` (Python package installer).
-   Git.

### Langkah-langkah

1.  **Clone Repositori**
    Buka terminal atau command prompt dan jalankan perintah berikut:
    ```bash
    git clone [https://github.com/NAMA_USER_ANDA/NAMA_REPOSITORI_ANDA.git](https://github.com/NAMA_USER_ANDA/NAMA_REPOSITORI_ANDA.git)
    cd NAMA_REPOSITORI_ANDA
    ```

2.  **Buat dan Aktifkan Virtual Environment**
    Sangat disarankan untuk menggunakan lingkungan virtual agar dependensi proyek tidak tercampur.
    ```bash
    # Membuat virtual environment
    python -m venv venv

    # Mengaktifkan di Windows
    .\venv\Scripts\activate

    # Mengaktifkan di macOS/Linux
    source venv/bin/activate
    ```

3.  **Instal Dependensi**
    Proyek ini memerlukan beberapa library Python. Buat file `requirements.txt` dengan isi berikut:
    ```txt
    streamlit
    rembg
    Pillow
    ```
    Kemudian, instal semua dependensi dengan satu perintah:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Jalankan Aplikasi Streamlit**
    Setelah instalasi selesai, jalankan aplikasi dengan perintah:
    ```bash
    streamlit run app.py
    ```
    Aplikasi web akan otomatis terbuka di browser Anda, biasanya di alamat `http://localhost:8501`.

---

## 📂 Struktur Proyek

Struktur folder untuk proyek ini cukup sederhana:

```
📁 NAMA_REPOSITORI_ANDA/
├── 📜 app.py              # Kode utama aplikasi Streamlit
├── 📜 requirements.txt     # Daftar dependensi Python
└── 📜 README.md           # Dokumentasi yang sedang Anda baca
```

---

## 📖 Panduan Penggunaan Aplikasi

1.  Pastikan aplikasi sudah berjalan (menggunakan `streamlit run app.py`).
2.  Gunakan tombol **"Browse files"** untuk mengunggah foto yang ingin Anda edit.
3.  Di sidebar kiri, pilih mode operasi:
    -   **Hapus Latar Belakang**: Menghasilkan gambar dengan background transparan.
    -   **Ganti Warna Latar Belakang**: Akan muncul pilihan warna.
4.  Jika Anda memilih untuk mengganti warna, pilih warna yang diinginkan (misalnya, Merah, Biru, atau warna kustom dari color picker).
5.  Aplikasi akan memproses gambar dan menampilkan pratinjau hasilnya.
6.  Klik tombol **"Unduh Gambar"** untuk menyimpan hasilnya ke komputer Anda.

---

## 📄 Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT. Lihat file `LICENSE` untuk detailnya.
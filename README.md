# EmployNext API

## Deskripsi Proyek

EmployNext API adalah sebuah proyek yang dibangun menggunakan Django untuk menyediakan layanan backend bagi aplikasi job board. API ini memungkinkan pengguna untuk mengelola data karyawan, termasuk menambah, mengedit, dan menghapus informasi karyawan.

## Teknologi yang Digunakan

- Python 3.10.11
- Django 5.1.4
- SQLite

## Cara Menjalankan Proyek di Lokal

1. Clone repository ini:

```bash
git clone https://github.com/username/employnext-api.git
cd employnext-api
```

2. Buat dan aktifkan virtual environment:

```bash
python -m venv env
source env/bin/activate  # Untuk pengguna Unix
.\env\Scripts\activate  # Untuk pengguna Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Buat database dan lakukan migrasi:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Jalankan server:

```bash
python manage.py runserver
```

6. Akses API melalui `http://127.0.0.1:8000/`

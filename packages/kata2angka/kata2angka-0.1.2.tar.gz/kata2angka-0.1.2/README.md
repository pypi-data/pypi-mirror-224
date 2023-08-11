# kata2angka: Konversi Kata ke Angka

[![PyPI version](https://badge.fury.io/py/kata2angka.svg)](https://badge.fury.io/py/kata2angka)

**kata2angka** adalah sebuah library Python yang memungkinkan Anda untuk mengkonversi kata dalam bahasa Indonesia menjadi bentuk angka numerik. Ini dapat berguna untuk mengubah ekspresi angka yang diucapkan menjadi angka dalam penghitungan.

## Instalasi

Anda dapat menginstal **kata2angka** menggunakan pip:

```bash
pip install kata2angka
```
## Penggunaan

Berikut adalah contoh penggunaan dari library ini:

```python
from kata2angka import word_to_num

angka_tertulis = "seratus dua puluh lima"
angka = word_to_num(angka_tertulis)
print(f"Angka dari '{angka_tertulis}' adalah {angka}")
```

## Kontribusi
Kontribusi dipersilakan! Anda dapat membantu memperbaiki bug, menambahkan fitur baru, atau meningkatkan dokumentasi. Silakan buat pull request ke repositori ini.

## Lisensi
Proyek ini dilisensikan di bawah Lisensi MIT. Lihat berkas LICENSE untuk informasi lebih lanjut.

## Sitasi
Jika Anda menggunakan kata2angka dalam proyek Anda, kami akan menghargai jika Anda memberikan sitasi kepada kami:

```
@misc{kata2angka,
  title = {kata2angka: Konversi Kata ke Angka},
  author = {Herman Sugi Harto},
  year = {2023},
  howpublished = {\url{https://github.com/hermansh-id/kata2angka}},
}
```
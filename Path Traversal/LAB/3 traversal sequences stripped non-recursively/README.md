# Lab 3 File path traversal, traversal sequences stripped non-recursively

## Brief:

Laboratorium ini mengandung kerentanan path traversal dalam tampilan gambar produk.

Aplikasi ini menghapus urutan path traversal dari nama file yang diberikan oleh pengguna sebelum menggunakannya.

## Tujuan:

dapatkan /etc/passwd

<img width="1922" height="1046" alt="brief" src="https://github.com/user-attachments/assets/a3ef0c30-53d5-4a77-821e-a360336ce7e2" />
	
## Analisa:

1. kirim request gambar ke repeater
<img width="1920" height="1080" alt="1 kirim request" src="https://github.com/user-attachments/assets/2e902059-70ed-46d6-aac3-c073d6b340a6" />
	
2. coba metode sebelumnya dan gagal
<img width="1920" height="1044" alt="2 metode sebelunya" src="https://github.com/user-attachments/assets/5229eda8-0028-4d28-844d-4389dc94f321" />
	
3. lalukan dengan nested ....// -> ....//....//....//etc/passwd dan berhasil
<img width="1922" height="1046" alt="brief" src="https://github.com/user-attachments/assets/df547fab-e218-4054-a3e9-f3e5a3881d95" />



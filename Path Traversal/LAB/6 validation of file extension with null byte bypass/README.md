# LAB 6 validation of file extension with null byte bypass

## Brief:

Laboratorium ini mengandung kerentanan path traversal dalam tampilan gambar produk.
web mengharapkan file ekstensi yang ditentukan
	 
## Tujuan:

dapatkan /etc/passwd
	

## Analisa:

1. kirim ke request


2. langsung saja ../../../etc/passwd%00.jpg karena file ekstensinya jpg

<img width="1920" height="1044" alt="2 null byte" src="https://github.com/user-attachments/assets/89cbbce1-83a8-4240-904a-5aef51275c01" />

3. berhasil
   
<img width="1922" height="1046" alt="3 berhasil" src="https://github.com/user-attachments/assets/29c4103f-8925-4e63-8fe0-1273ada45a58" />

# LAB 5 File path traversal, validation of start of path

## Brief:
Laboratorium ini mengandung kerentanan path traversal dalam tampilan gambar produk. aplikasi mengharapkan jalur folder yang sesuai
	
	
## Tujuan:

dapatkan /etc/passwd
	
<img width="1922" height="1046" alt="brief" src="https://github.com/user-attachments/assets/de0eface-8498-4485-b05b-2041b99283a2" />
	
## Analisa:

1. kirim request gambar ke repeater
	
2. langsung saja tambahkan

       /var/www/images/../../../etc/passwd
   
<img width="1920" height="1044" alt="2 tambahkan" src="https://github.com/user-attachments/assets/c56f161d-8ec5-498e-9cd6-36c3d6c2f6e7" />

3. berhasil
   
<img width="1922" height="1046" alt="3 berhasil" src="https://github.com/user-attachments/assets/b61c8f20-8582-42d2-bebe-759dabf820fa" />


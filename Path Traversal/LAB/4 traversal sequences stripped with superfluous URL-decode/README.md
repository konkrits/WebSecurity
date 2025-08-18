# LAB 4 traversal sequences stripped with superfluous URL-decode

## Brief:

Laboratorium ini mengandung kerentanan path traversal dalam tampilan gambar produk.
	 
web memblokir traversal input lalu kemudian melakukan url decode input sebelum melakukannya
	 
## Tujuan:

dapatkan /etc/passwd
<img width="1922" height="1046" alt="brief" src="https://github.com/user-attachments/assets/08f9deb7-2a61-42fe-87f9-a92e676faea1" />
	
## Analisa:

1. kirim request gambar ke repeater
<img width="1075" height="1025" alt="1 kirim repeater" src="https://github.com/user-attachments/assets/240fba03-5b97-4bf7-90f4-ebec857ebaaf" />
	
2. coba metode sebelumnya dan gagal
<img width="1920" height="1044" alt="2 metode sebelumnya" src="https://github.com/user-attachments/assets/5ee6a9d6-6b90-4745-94d1-61b2e913b29d" />

3. coba dengan encode 2 kali si / nya dan berhasil
encoded dulu / dua kali dan menjadi seperti ini

        ..%25%32%66..%25%32%66..%25%32%66etc/passwd
<img width="1920" height="1080" alt="3 encode double dan berhasil" src="https://github.com/user-attachments/assets/77fe98c3-7967-4919-b0e5-04b50bcadce6" />

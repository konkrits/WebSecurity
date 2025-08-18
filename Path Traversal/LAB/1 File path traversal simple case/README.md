# LAB 1 File path traversal, simple case

## Brief:

kerentanan di display gambar produk

## Tujuan:

dapatkan isi /etc/passwd

<img width="1922" height="1046" alt="Brief" src="https://github.com/user-attachments/assets/843ceeae-d828-4fa0-ab01-d9b6c1420496" />
	
## Analisa:

1. dapatkan request gambarnya kirim ke repeater
<img width="1922" height="1046" alt="1 gambar" src="https://github.com/user-attachments/assets/2007e0e5-3730-4be9-bae3-8cde5b783505" />

<img width="1920" height="1080" alt="1 dapatkan request" src="https://github.com/user-attachments/assets/0b6b9354-38ba-4a9b-ab74-0464432ea30c" />
	
2. ganti filenamenya dengan payload dan berhasil
	 dikarenakan ini tidak ada sanitasi sekali jadi langsung saja 

        ../../../etc/passwd

<img width="1920" height="1080" alt="2 berhasil" src="https://github.com/user-attachments/assets/8acb747f-c809-4c17-a277-45120aa92bf3" />





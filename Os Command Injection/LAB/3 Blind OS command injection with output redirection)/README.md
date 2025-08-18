# Lab 3 : Blind OS command injection with output redirection

## Brief:

vulnerabilty di feedback, Aplikasi ini mengeksekusi perintah shell yang berisi detail yang disediakan pengguna. Output dari perintah tidak dikembalikan dalam respon. 
Namun, Anda dapat menggunakan pengalihan output untuk menangkap output dari perintah. Ada folder yang ditulis di:

		/var/www/images/

Aplikasi ini menyajikan gambar untuk katalog produk dari lokasi ini. Anda dapat mengarahkan output dari perintah yang disuntikkan ke file di folder ini, 
dan kemudian menggunakan URL pemuatan gambar untuk mengambil isi file.

## Tujuan:
eksekusi perintah whoami dan ambil outputnya

<img width="1922" height="1046" alt="brief" src="https://github.com/user-attachments/assets/bce966f3-ffb9-411b-a79b-a468743dbd1f" />
	
## Analisa:
1. pergi ke laman feedback
<img width="1922" height="1046" alt="1 laman feedbakc" src="https://github.com/user-attachments/assets/2c4c9b42-5bb5-4e41-a554-82efdb8735ff" />
	
2. isi semua kolom dan kirim ke repeater
<img width="1920" height="1080" alt="2" src="https://github.com/user-attachments/assets/ba6b1bb9-d1ba-4100-a446-1696ed3d88d9" />
	
3. pada parameter email=x||PAYLOAD|| dan kirim	
payload nya

        ||whoami>/var/www/images/output.txt||
<img width="1920" height="1044" alt="3 payload" src="https://github.com/user-attachments/assets/4a0d21ef-aebd-489c-991b-5aef3a43d8f1" />

4. load request gambar
<img width="1075" height="1025" alt="4 load gambar" src="https://github.com/user-attachments/assets/7c3241d3-a970-460c-9377-b7c0a55e56eb" />
	
5. ganti parameter filename=(GAMBAR) menjadi filename=output.txt dan berhasil
<img width="1920" height="1044" alt="5 ganti filename" src="https://github.com/user-attachments/assets/dc85af8a-c64b-42e9-b0a2-81904e7131a5" />








































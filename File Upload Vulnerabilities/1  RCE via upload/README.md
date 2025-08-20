# Lab 1 : Remote code execution via web shell upload

## Brief:
lab tidak memvalidasi sama sekali fungsi upload
	
## Tujuan:
dapatkan file /home/carlos/secret

<img width="1922" height="1046" alt="Brief" src="https://github.com/user-attachments/assets/9ccfb2b8-bec0-4f2d-9664-09f1225d3ae6" />
	
## Analisa:

1. upload gambar seperti biasa dan kirim request GET /files/avatars/GAMBAR.jpg

2. sekarang upload web shellnya dan secret file dikirim ke response

  <img width="1920" height="1044" alt="1 payload" src="https://github.com/user-attachments/assets/5aac7dc3-c99a-40c5-b423-dfcb37bad3d5" />
 
3. submit dan berhasil

  <img width="1920" height="1080" alt="2 response dan berhasil" src="https://github.com/user-attachments/assets/1943dde0-690d-483a-a5d8-5d9dc95f3b5f" />












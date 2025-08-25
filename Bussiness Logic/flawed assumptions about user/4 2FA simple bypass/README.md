# Lab: 2FA simple bypass

## Brief:

akun kamu   : 	wiener:peter
akun korban : 	carlos:montoya
	
vulnerable ke 2fa, sudah punya akun korban tetapi tidak dengan 2fa nya

<img width="1922" height="1046" alt="brief" src="https://github.com/user-attachments/assets/be8512cb-1303-4982-b763-a2b970bfe89a" />
	
## Tujuan:
bypass 2fa dan login menjadi korban
	
## Analisa:

1. login ke akun kamu dan masukan 2fa nya saat selesai perhatikan urlnya
> atau requestnya di /my-account

<img width="1922" height="1046" alt="2" src="https://github.com/user-attachments/assets/8acace5d-5888-4ca2-be39-bfe822a6a03a" />

2. login ke korban, pada saat diminta 2fa langsung saja pergi ke url /my-account atau di request pun bisa

<img width="1920" height="1080" alt="3" src="https://github.com/user-attachments/assets/99a6d8f0-8373-4164-8b15-947c3420da85" />

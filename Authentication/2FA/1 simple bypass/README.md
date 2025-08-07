# Lab 1: 2FA simple bypass

## Brief:
###	akun kamu   : 	wiener:peter
###	akun korban : 	carlos:montoya
	
###	vulnerable ke 2fa, sudah punya akun korban tetapi tidak dengan 2fa nya
	
## Tujuan:
###	bypass 2fa dan login menjadi korban
<img width="1922" height="1046" alt="brief" src="https://github.com/user-attachments/assets/e20b3add-5d0c-4947-a9de-4363e7115baa" />
	
## Analisa:
###	1. login ke akun kamu dan masukan 2fa nya saat selesai perhatikan urlnya
		atau requestnya di /my-account
<img width="1922" height="1046" alt="2" src="https://github.com/user-attachments/assets/661f2d31-4648-412c-a4c7-e509b8246d2d" />
		
###	2. login ke korban, pada saat diminta 2fa langsung saja pergi ke url /my-account atau di request pun bisa
<img width="1920" height="1080" alt="3" src="https://github.com/user-attachments/assets/ef0d726d-8ed8-4c93-bc92-6e444614d702" />

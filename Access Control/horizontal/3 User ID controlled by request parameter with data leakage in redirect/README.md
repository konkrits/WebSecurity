# LAB 3 User ID controlled by request parameter with data leakage in redirect

## Brief:
### leaked sensitif informasi di response body
	
## Tujuan:
###	dapatkan kunci API carlos
	
## Analisa:
###	1. login dulu
	
###	2. ganti id jadi carlos id=carlos dan gagal 
###		malah kita jadi logout dan kembali ke laman /login
<img width="1920" height="1080" alt="2id_carlos_gagal" src="https://github.com/user-attachments/assets/db2e63f8-1804-4fbe-91db-dc1ca55e678e" />

###	3. di response bodi ada API carlos
###		ketika kita mengintercept info carlos malah dikirim diresponse body
<img width="1920" height="1080" alt="3_API_di_body_request" src="https://github.com/user-attachments/assets/d1080efb-9da1-4fd0-b483-3d2cf78dfbff" />

###	4. submit dan berhasil
<img width="774" height="1025" alt="4_submit_dan_berhasil" src="https://github.com/user-attachments/assets/786d6f53-7afa-4e14-9c54-5dbd2d147c9a" />

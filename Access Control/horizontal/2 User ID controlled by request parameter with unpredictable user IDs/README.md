# 3 User ID controlled by request parameter, with unpredictable user IDs 

## Brief: 
###	lab yang mengidentifikasi dengan gui, kerentanan di laman user

## Tujuan:
###	cari GUId carlos dan submit API nya
<img width="1922" height="1046" alt="brief" src="https://github.com/user-attachments/assets/5cc0500f-25c2-436b-b371-8f59ebcb066f" />
	
## Analisa:
###	1. ganti id=carlos gagal
###		dan malah ke /login
<img width="1922" height="1046" alt="1_identify" src="https://github.com/user-attachments/assets/8f944d29-3e54-44fb-b41f-cdc26a6a7b31" />
		
###	2. diintercept dan di response body aman
<img width="1920" height="1044" alt="2_coba_intercept" src="https://github.com/user-attachments/assets/cad3838e-4186-4905-9f38-ec7bec096082" />

###	3.cari postingan carlos, klik carlos dan ada userid="19a8836f-3ff8-4988-98cb-e5294d0e9db9"
<img width="1922" height="1046" alt="3_cari_carlos_guid" src="https://github.com/user-attachments/assets/dfef2ef5-74db-48fe-9aca-86c3a50586a7" />
	
###	4. ganti guid wiener di id= jadi guid carlos
###		dan ternyata bisa dan ada API
<img width="1920" height="1044" alt="4_guid_wiener_ke_carlos" src="https://github.com/user-attachments/assets/7cfdb329-3ba1-4c80-97e9-5cacf6ee8c59" />
		
###	5. submit API dan berhasil
<img width="774" height="1025" alt="5_berhasil" src="https://github.com/user-attachments/assets/6a722a7e-a853-4b98-8109-cb8155d377d7" />

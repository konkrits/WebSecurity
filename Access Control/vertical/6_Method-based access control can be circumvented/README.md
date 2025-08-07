# Lab 6 Method-based access control can be circumvented

## Brief: 
### lab ini mengimplementasikan akses kontrol berdasarkan http request method, kamu bisa login jadi admin.
	
## Tujuan: 
### Jadikan wiener admin
<img width="1922" height="1046" alt="brief" src="https://github.com/user-attachments/assets/388e7b61-6bcb-42f9-a4fe-5380f6defa54" />

## Analisa:
###	1. login jadi administrator dan upgrade user carlos
<img width="1922" height="1046" alt="1upgrade_carlos" src="https://github.com/user-attachments/assets/16e6ca66-68c6-4583-a59a-d80968c09995" />
	
###	2. intercept waktu pas pengupgradan
<img width="865" height="1032" alt="2_intercept" src="https://github.com/user-attachments/assets/feee4392-662c-4039-b9c1-3258740e8a25" />
	
###	3. buka incognito baru 
<img width="1920" height="1080" alt="3_new_incognito" src="https://github.com/user-attachments/assets/923b23d8-4534-49f1-996b-3b68d388145d" />
	
###	4. dan login jadi wiener peter
<img width="954" height="1025" alt="4_jadi_wiener" src="https://github.com/user-attachments/assets/bd7594d2-4006-47bf-8b25-8236b3fcd1d6" />
	
###	5. interceptan untuk mengupgrade carlos ganti cookie nya dari admin ke wiener
<img width="1920" height="1080" alt="5_copy_cookie" src="https://github.com/user-attachments/assets/1016de7a-128e-4f62-af4b-b08f8614f4d9" />
	
###	6.sekarang coba kirim dan gagal unotorisazie
<img width="963" height="1032" alt="6_gagal_dari_wiener" src="https://github.com/user-attachments/assets/6558f2bd-78ba-48d8-ad18-5bf72cd96e5a" />
	
###	7. ganti dari request methodnya dari post ke postx
<img width="996" height="1032" alt="7_POSTX" src="https://github.com/user-attachments/assets/634df0c4-340d-471e-943d-2d41fb1f1d30" />
	
###	8. jadi missing parameter dan sekarang ganti request method nya dengan klik kanan dan chage request method
<img width="996" height="1032" alt="8_GET" src="https://github.com/user-attachments/assets/dea0b722-19e7-4d66-9d42-e2cb3288504f" />
	
###	9. dan ganti usernamenya jadi wiener
<img width="1920" height="1080" alt="9_GET_dan_username" src="https://github.com/user-attachments/assets/9ea3473e-990b-4b91-b46b-8ede689ebe76" />

BERHASIL
<img width="1135" height="1032" alt="berhasil" src="https://github.com/user-attachments/assets/ea94eeb0-2119-4b79-b8af-1c18ce82eec3" />

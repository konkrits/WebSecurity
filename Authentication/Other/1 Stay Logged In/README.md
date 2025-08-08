# LAB 1 Stay Logged in

## Brief:
### lab ini mengijinkam user untuk tetap login meskipun telah menutup sesi browsernya.
### masalahnya cookie dari fungsi ini vulnerable dengan brute-force
## Tujuan:
### Brute force cookie carlos dan login ke account nya
<img width="1922" height="1048" alt="Brief" src="https://github.com/user-attachments/assets/0e0fd3b9-48fc-46f8-807b-be62909b14a3" />

## Analisa:

#### langkah pertama yaitu mengetahui seberapa vulnerable cookie dan memcoba untuk mengetahui bagaimana cookie tersebut dibuat
	
####  1. login dan intercept
<img width="1920" height="1080" alt="1 login intercept repeater" src="https://github.com/user-attachments/assets/0defcf39-96f4-4a57-b36b-7198a7206521" />
	
####	2. setelah login ada parameter stay loged in
<img width="1920" height="1080" alt="2 logged ke repeater" src="https://github.com/user-attachments/assets/cbee27c8-39b7-4044-93d1-10020637911f" />
	
####	3. seleksi parameternya dan kirim  ke decoder
<img width="1920" height="1046" alt="3 kirim decode" src="https://github.com/user-attachments/assets/f538c5ac-681f-4dce-bbfd-da7944e2fc0f" />
	
####	4. ini menggunakan base64 encoding dan ketika di decode ada wiener:(md5Hash) dan passwordnya di hashing dengan md5
<img width="1920" height="1080" alt="4 md5 hash" src="https://github.com/user-attachments/assets/9427051f-fb03-4300-9a92-49ac5802113c" />

####	5. kita buat setiap list password dengan diencode dan dihash base64 (username:md5(password))
<img width="1920" height="1046" alt="5 payload" src="https://github.com/user-attachments/assets/0f41b510-066d-46ce-b4fb-fd4aa0d4420c" />
	
####	6. kita akan menggunakan pesan ini sebagai penanda akun yang benar
<img width="747" height="986" alt="6" src="https://github.com/user-attachments/assets/0e8983f1-850d-4d9c-9237-8b52341b7a7d" />

####	7. brute force cookie dengan ffuf
<img width="1920" height="1080" alt="7 brute force cookie" src="https://github.com/user-attachments/assets/1905ed77-ccd8-4eb0-a964-7d001ad06b17" />

####	8. setelah selesai ada satu response yang beda, cari password plainnya
<img width="1920" height="1044" alt="8 different cookie response" src="https://github.com/user-attachments/assets/13290fee-c036-477e-a117-125448a25aae" />
	
#### Login dan berhasil
<img width="1922" height="1046" alt="Berhasil" src="https://github.com/user-attachments/assets/2dbd6c48-bde2-4dbe-ae57-5cd396a1ea98" />

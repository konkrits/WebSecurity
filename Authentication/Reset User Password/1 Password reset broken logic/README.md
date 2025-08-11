# Lab 1 Password reset broken logic

## Brief:
password reset vulnerable
	
## Tujuan:
reset password carlos dan akses laman "my-account"
	
## Analisa:
1. pergi ke login lalu klik forgot-password 
	 lanjutkan untuk mereset password wiener
<img width="1920" height="1044" alt="1 reset password" src="https://github.com/user-attachments/assets/074678eb-0e5a-4d1a-8227-6b39591d2e9b" />


		
2. nah di history kirim POST /forgot-password
  dan ubah value username=carlos
<img width="1920" height="1044" alt="2 ubah username jadi carlos" src="https://github.com/user-attachments/assets/70dc1b1c-e27c-4f78-b520-bbbd80b4fb49" />

3. di history kirim ke repeater
 
       POST /forgot-password?item-forgot-password-token=18281y1y1892 <- ubah jadi kosong
	
 dibawah sama temp token nya kosong dan ubah username dan password akun carlos
<img width="1920" height="1044" alt="3 ubah token jadi kosong" src="https://github.com/user-attachments/assets/0c3184bc-2bef-4f76-80a4-b25fa7b2ca48" />
		
4. berhasil
<img width="1922" height="1046" alt="akhir" src="https://github.com/user-attachments/assets/c6000b41-2d81-4cd3-8ea2-57c72d1232a8" />

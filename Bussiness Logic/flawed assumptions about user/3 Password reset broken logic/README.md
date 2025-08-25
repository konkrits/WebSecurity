# Lab: Password reset broken logic

## Brief:
password reset vulnerable
	
## Tujuan:
reset password carlos dan akses laman "my-account"
	
<img width="1922" height="1046" alt="brief" src="https://github.com/user-attachments/assets/67d19740-e9ab-42e5-968a-dc3b57679a76" />

## Analisa:
	
1. pergi ke login lalu klik forgot-password 
> lanjutkan untuk mereset password wiener
		
<img width="1920" height="1044" alt="1 reset password" src="https://github.com/user-attachments/assets/43c256f9-ccc0-4afd-aeb7-352908a03a55" />

2. nah di history kirim POST /forgot-password
> dan ubah value username=carlos
		
<img width="1920" height="1044" alt="2 ubah username jadi carlos" src="https://github.com/user-attachments/assets/04409123-2e15-4d4e-bff2-dd1a5a392f86" />

3. di history kirim ke repeater POST /forgot-password?item-forgot-password-token=18281y1y1892 <- ubah jadi kosong
> dibawah sama temp token nya kosong dan ubah username dan password akun carlos
		
<img width="1920" height="1044" alt="3 ubah token jadi kosong" src="https://github.com/user-attachments/assets/b0e53fa5-2162-43d8-b470-cf554642c9c4" />

4. berhasil

<img width="1922" height="1046" alt="akhir" src="https://github.com/user-attachments/assets/0c181489-30c5-48b3-abbc-61007f71d9d2" />

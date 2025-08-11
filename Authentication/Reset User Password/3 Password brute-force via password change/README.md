# LAB 3 Password brute-force via password change

## Brief:
	
fungsi ganti password web ini membuat rentan web itu sendiri terhadap brute-force attack

Your credentials: 

    wiener:peter

Victim's username: 

    carlos 
	
## Tujuan:

brute-force password akun carlos dan akses halaman my-account nya

## Analisa:

1. login
	
2. setelah login di halaman my account ada feature reset password

	experimen dengan feature itu 	

<img width="1920" height="1080" alt="2 laman my account" src="https://github.com/user-attachments/assets/a65c5df5-d429-4c8d-b8d5-bb27134db404" />


3. jika mengenter 2 kali current password salah dan kedua password baru benar aplikasi setelah beberapa kali dicoba 

<img width="1920" height="1080" alt="3" src="https://github.com/user-attachments/assets/13b83a92-a540-400e-a888-e6eca4e6a7c3" />

  aplikasi akan melogout user

<img width="1920" height="1080" alt="3 a" src="https://github.com/user-attachments/assets/59843e9d-1bb7-490a-bb5c-6a959b75ac1a" />


4. jika current password salah dan kedua password baru salah aplikasi akan menampilkan Current password incorrect
<img width="1920" height="1044" alt="4" src="https://github.com/user-attachments/assets/9976601d-5d4b-45fc-bd07-9b208a538041" />
	
5.  jika current password benar dan kedua password baru beda aplikasi menampilkan  New passwords do not match	

	nah ini dia yang bisa menyebabkan membrute force password
<img width="1920" height="1044" alt="5" src="https://github.com/user-attachments/assets/4e0eae48-4ef9-4f60-bd18-65c3ac3fd04c" />

6. kirim ke intruder ganti username ke carlos lalu set posisi ke current password lalu tambahkan payload password dan kedua password baru berbeda
<img width="1920" height="1044" alt="6" src="https://github.com/user-attachments/assets/84cd2a23-e710-4c17-af1b-cae7110f2ca7" />

7. lalu ke setting dan tambahkan grep match  New passwords do not match	lalu start attack
<img width="1920" height="1044" alt="7" src="https://github.com/user-attachments/assets/4b1bfb88-564f-452b-8f6a-a9909745251a" />

8. ketika selesai ada satu response yang menampilan New passwords do not match, nah ini password yang benar
<img width="1920" height="1044" alt="8" src="https://github.com/user-attachments/assets/040a1d81-28bc-443b-9620-a9653642c23d" />

9. login ke carlos dengan password yang benar dan berhasil
<img width="1922" height="1046" alt="9" src="https://github.com/user-attachments/assets/0b2fcd92-5329-45c1-913e-fbb8598d7e9c" />





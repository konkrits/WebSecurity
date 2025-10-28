# LAB 2 username enumeration via account lock

## Brief:
	
lab vulnarable dengan username enumeration, lab menggunakan account locking tapi ada cacat logika
	
## Tujuan:
enumerate valid username dan password lalu login
	
<img width="1922" height="1046" alt="brief" src="https://github.com/user-attachments/assets/af48503e-c16f-4c95-ba64-07f496657a76" />


## Analisa:
	
1. intercept POST login request
	
<img width="1920" height="1080" alt="1 intercept request" src="https://github.com/user-attachments/assets/9a144d8f-3e19-430f-8bba-921aa520e14c" />


2. alternatif burp intruder menggunakan FFUF skripnya jadi setiap akun merequest 5 kali dengan password yang sama tujuannya untuk mengetahui akun mana yang dikunci
	
<img width="1920" height="1080" alt="2 fuzz" src="https://github.com/user-attachments/assets/19535eef-a22c-4336-9efb-d1a6d94af237" />


3. di ffuf report ada lenght yang beda dari yang lain dengan username am
	
<img width="1922" height="1046" alt="3" src="https://github.com/user-attachments/assets/c2105f9b-0fba-4ea3-aa85-48ef11040a0a" />


4. coba login dengan am dan password random dan ternyata dikunci
	
> username sudah valid berikutnya

<img width="1922" height="1046" alt="4" src="https://github.com/user-attachments/assets/510b1b48-efa8-41bd-b44a-f6255cc614c3" />

5. sekarang brute force dengan ffuf passwordnya

<img width="1920" height="1044" alt="5" src="https://github.com/user-attachments/assets/7b4e62ed-b196-4dff-8c4f-f7d4103b35f9" />

<img width="1920" height="1044" alt="6" src="https://github.com/user-attachments/assets/58e86de3-0dce-4e4e-951c-d4bfb975ea7d" />

6. login dan berhasil

<img width="1922" height="1046" alt="login dan berhasil" src="https://github.com/user-attachments/assets/6dba3ba5-af99-420d-8bb0-4800c67f4548" />


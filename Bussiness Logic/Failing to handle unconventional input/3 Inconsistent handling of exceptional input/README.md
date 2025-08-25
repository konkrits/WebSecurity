# Lab 3 Inconsistent handling of exceptional input

## Brief:
lab ini tidak cukup memvalidasi user input, kamu bisa mengeksploitasi kerentanan di laman daftar akun untuk mengakses fungsi admin
	
## Tujuan:
akses panel admin dan hapus carlos

<img width="1920" height="985" alt="brief" src="https://github.com/user-attachments/assets/fe5d5829-aff1-4836-8b6e-41cb6e2dc8b5" />

## HINT:
Anda dapat menggunakan tautan di banner lab untuk mengakses klien email yang terhubung ke server email pribadi Anda. 
	Klien tersebut akan menampilkan semua pesan yang dikirim ke @YOUR-EMAIL-ID.web-security-academy.net dan subdomain apa pun. ID email unik Anda ditampilkan di klien email.

## Analisa:

lab ini mempunyai kerentanan di laman daftar akun dan di laman admin, fungsi admin ditentukan hanya dengan user yang memiliki email pegawai
	dan kerentanannya aplikasi membatasi karakter tetapi tidak ketika mendaftarkan akun
	
kerentanan 1: admin ditentukan dengan email pegawai

kerentanan 2: karakter dibatasi 255 ketika sudah mendaftar tetapi tidak ketika mendaftar

## Exploit: 

1. pergi ke /admin dan disana tertulis kalo panel admin hanya bisa diakses oleh user yang memakai email dontwannacry.com
	
> di laman register diberitahukan bahwa pegawai memakai dontwannacry.com
	
<img width="1920" height="985" alt="1 admin dir" src="https://github.com/user-attachments/assets/27312302-84fd-44f0-8f66-4050ffd30d0b" />

2. coba daftar dengan username demo dan string panjang dengan email 
   contoh:

        stringpanjang@YOUR-EMAIL-ID.web-security-academy.net	

<img width="1920" height="985" alt="2 daftar str panjang" src="https://github.com/user-attachments/assets/dab79f2b-1e8e-44fb-add5-102db796576d" />

4. sekarang pergi ke email dan klik link nya
	
<img width="1920" height="1080" alt="3 isi email" src="https://github.com/user-attachments/assets/bd9d5ed5-a654-48f2-aaf1-eaccbcc6af6b" />

4. setelah login dengan username demo, di laman accoutn disana terlihat bahwa string panjang di cut dan dibatasi dengan jumlah karakter
	
> disinilah kunci kerentanannya
	
<img width="1920" height="985" alt="4 email di cut" src="https://github.com/user-attachments/assets/7b5b7820-1c17-4353-8bda-2f398921022f" />

5. hitung karakter dan hasilnya email dicut dengan jumlah 255 karakter saja
	
> step berikutnya mendaftar dengan email pegawai/admin yaitu @dontwannacry.com
	
<img width="1920" height="1080" alt="5 hitung karakter" src="https://github.com/user-attachments/assets/09047935-af09-4212-b77e-1d4ba8df552b" />

6. hitung dulu jumlah karakter email dengan 255 total dengan @dontwannacry.com didalamnnya lalu tambahkan email untuk menerima link(email lab), kemudian daftarkan.
	contoh:
> stringpanjangrandom@dontwannacry.com(disini harus 255 karakter).YOUR-EMAIL-ID.web-security-academy.net
		
<img width="1920" height="1080" alt="6 daftar email admin" src="https://github.com/user-attachments/assets/25fbcd60-ca9f-46d2-be21-1e44947a24e7" />

7. dan tidak terjadi apa-apa, sepertinya ini berhasil dan lab tidak membatasi ini
	
<img width="1920" height="1080" alt="7 telah didaftarkan" src="https://github.com/user-attachments/assets/27f14782-2bd5-41b6-adf7-3355a4509a99" />

8. di laman email klik linknya
	
<img width="1920" height="1080" alt="8 link ada di email" src="https://github.com/user-attachments/assets/72047818-de53-4041-8715-1fc49ec95b34" />

9. dan berhasil meregist
	
<img width="1920" height="1080" alt="9 regist berhasil" src="https://github.com/user-attachments/assets/5c4b91be-5487-41cc-96ac-8df8712da62c" />

10. login dan kita berhasil login menjadi admin
	
<img width="1920" height="1080" alt="10 login jadi u admin" src="https://github.com/user-attachments/assets/3d9325a6-0f91-4708-9442-62c471625ee4" />

11. hapus user carlos dan berhasil
	
<img width="1920" height="1080" alt="11 hapus carlos berhasil" src="https://github.com/user-attachments/assets/b26621b2-4dbe-4c1f-b04f-a2186feed88d" />

	
		
		

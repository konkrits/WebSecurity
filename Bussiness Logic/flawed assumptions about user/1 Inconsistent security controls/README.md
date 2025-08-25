# Lab 1 : Inconsistent security controls

## Brief:
lab ini cacat secara logik sehingga mengijinkan user mana saja mengakses panel admin yang seharusnya hanya bisa diakses oleh karyawan
	
## Tujuan:
akses panel admin dan hapus user carlos

<img width="1920" height="1080" alt="Brief" src="https://github.com/user-attachments/assets/0db1d087-d3ff-4a48-9f81-f64bc77c45f0" />
	
## Analisa:

lab ini tidak mengecek atau memvalidasi sama sekali untuk pergantian email 

jadi user mana saja bisa menggunakan email karyawan

## Exploit:

1. pergi ke /admin disana tertulis hanya bisa diakses oleh user yang memakai email @dontwannacry.com
	
<img width="1920" height="1080" alt="1 admin dir" src="https://github.com/user-attachments/assets/80903c70-642b-4a09-b0dc-ba26e2f01258" />

2. lalu ke daftar akun
	
<img width="1920" height="1080" alt="2 laman daftar" src="https://github.com/user-attachments/assets/d103a15a-68a9-4b95-8233-20bcac25a28b" />

3. daftarkan user secara biasa dan menggunakan email lab
	
<img width="1920" height="1080" alt="3 isi daftar" src="https://github.com/user-attachments/assets/6d9ec6de-ed61-4c53-982a-857e90f838c0" />

4. setelah daftar, di kotak email ada link pendaftaran dan klik
	
> sejauh ini hanya mengisi seperti biasa tetapi step selanjutnya adalah kerentanannya
	
<img width="1085" height="455" alt="4 kotak emai" src="https://github.com/user-attachments/assets/4a03e243-55a7-43c1-a87e-e7d9f07d3fe3" />

5. di halaman my account ada kolom untuk mengganti email ganti dengan email karyawan depannya bebas asalkan harus 

> dontwannacry.com : test@dontwannacry.com

<img width="1920" height="1080" alt="5 ganti email admin" src="https://github.com/user-attachments/assets/e83309bf-9522-4e81-9d07-7bfbb11ed392" />

6. dan pergantian berhasil tanpa ada proses apa-apa
	
<img width="1920" height="1080" alt="6 ganti berhasil" src="https://github.com/user-attachments/assets/7b65d318-66a8-44e0-89c6-cfa12b5cce06" />

7. ke admin panel
	
<img width="1920" height="1080" alt="7 panel admin" src="https://github.com/user-attachments/assets/74d2ba5a-97ca-4380-8715-61ca8b2839e1" />

8. hapus user carlos dan berhasil
	
<img width="1920" height="1080" alt="8 berhasil" src="https://github.com/user-attachments/assets/80c06b64-d231-4cbc-9d1e-fc8d538f8976" />
	
	

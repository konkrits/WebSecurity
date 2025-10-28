# LAB Broken brute-force protection, IP block

## Brief:
situs vulnerable dengan brute force password
## Tujuan:
brute force carlos dan login jadi carlos

<img width="1922" height="1046" alt="brief" src="https://github.com/user-attachments/assets/6ad269f9-3276-43cc-b12e-35400384b8a2" />
	
## Analisa:
1. login dengan username carlos dan password random
	
> setelah 3 kali ip diblok tapi jika login sebelum 3 kali, yaitu pas ke 2 setelah gagal
> login menjadi wiener dan otomatis ip tidak diblok

<img width="1922" height="1046" alt="1 ip blok" src="https://github.com/user-attachments/assets/399c7704-0260-4f19-b1e9-f01ac851c27b" />

2. intercept request login ke intruder

<img width="1920" height="1080" alt="2 intercept ke intruder" src="https://github.com/user-attachments/assets/cb33b192-2a09-4470-b8be-2b964f041e00" />

3. pilih pitchfork attack set posisi username dan password lalu tambahkan kedua payloadnya

<img width="1920" height="1080" alt="3 set posisi" src="https://github.com/user-attachments/assets/2d032f9e-67ed-4105-adf9-40c070f32c88" />
	
4. set resource pool dan pilih create dan set maksimal jadi 1

<img width="1920" height="1080" alt="4 set pool" src="https://github.com/user-attachments/assets/f683e916-3bf7-414e-9416-c8cb9d922832" />


5. setelah selesai ada status 302 di username carlos login dan berhasil.

<img width="1920" height="1080" alt="5 302 berhasil" src="https://github.com/user-attachments/assets/271eb4a3-a7b5-4c78-8326-814b7f879789" />
























 

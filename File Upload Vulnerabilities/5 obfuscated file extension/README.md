# LAB 4 extension blacklist bypass

## Brief:
tipe file bisa dibypass via klasik obfuscation technique
	
## Tujuan:
dapatkan /home/carlos/secret

<img width="1922" height="1046" alt="brief" src="https://github.com/user-attachments/assets/5173f4e6-24a0-4926-b813-8a5963bc252f" />
	
## Analisa:

1. upload gambar dapatkan request GET filename
	
2. upload php dan response menginditasikan bahwa tipe file tidak diijinkan

   <img width="1922" height="1046" alt="2 ekstensi tidak bisa" src="https://github.com/user-attachments/assets/3d64590c-7cfa-4080-b28c-e6691a2ae1df" />
	
3. di filename coba ubah jadi filename="shell.php%00.jpg"
	
   <img width="1920" height="1080" alt="3 ubah jadi null" src="https://github.com/user-attachments/assets/7edc6e48-9567-4389-8d90-800d1262e402" />

4. response files /avatars/shell.php uploaded
   ini mengidentifikasi bahwa server menstrip null byte

    <img width="1920" height="1080" alt="4 ini bisa" src="https://github.com/user-attachments/assets/5ae6af18-749b-49ac-b0c4-53c001c615f9" />

5. dapatkan file dan berhasil

    <img width="1920" height="1080" alt="5 dapatkan file dan berhasil" src="https://github.com/user-attachments/assets/18cb907a-8d3d-40ce-a99c-8f33752fddae" />

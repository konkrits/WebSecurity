# LAB 3 WEB SHELL

## Brief:
Web shell upload via path traversal
	
## Tujuan:
dapatkan file /home/secret/carlos

<img width="1922" height="1046" alt="Brief" src="https://github.com/user-attachments/assets/7cd18c3d-f5f3-4a88-a93a-d53a09e76035" />
	
## Analisa:
1. upload gambar seperti biasa dan kirim request GET filename
	
   <img width="1920" height="1080" alt="1 upload gambar" src="https://github.com/user-attachments/assets/76cc71c2-b13f-497a-b620-dd8086867881" />

2. upload file php dan berhasil
	
   <img width="1920" height="1080" alt="2 upload payload" src="https://github.com/user-attachments/assets/1b99ff48-6666-48f5-a714-b5501dbb4c0a" />

3. tapi ketika didapatkan malah dikembalikan jadi teks

   <img width="1112" height="1025" alt="3 dapatkan payload tapi teks" src="https://github.com/user-attachments/assets/caa2d8fe-6cc1-4afc-976f-aa344a53827b" />
	
4. coba dengan path traversal / dan response nya avatars/shell.php ini berarti / dihapus dari nama file
	
   <img width="1920" height="1080" alt="4 coba dengan path" src="https://github.com/user-attachments/assets/6fdcc4ce-0354-4144-ac99-dca1962be0f2" />

5. coba encode / dan berhasil 
	
   <img width="1920" height="1080" alt="5 path encod" src="https://github.com/user-attachments/assets/d36976ff-8bde-4843-a75d-7d1488c9178c" />

6. pada get request filename:/files/shell.php
	
   <img width="1920" height="1080" alt="6 dapatkan file berhasil" src="https://github.com/user-attachments/assets/5981913f-206b-492a-aeb2-34eb8ee44d67" />

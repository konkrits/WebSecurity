# LAB User ID controlled by request parameter with password disclosure

## Brief:
### lab ini menyimpan password user di laman akun, dan hanya ditutupi atau dimasking dengan titik dan isinya masih ada.
	
## Tujuan:
### Jadi Admin untuk menghapus carlos

<img width="1922" height="1046" alt="brief" src="https://github.com/user-attachments/assets/17e3465c-406a-4fb1-9ba2-53c5d376ab4c" />

## Analisa:

login dan pergi ke laman akun
	
###	2. lihat di response password ditampilkan

<img width="1920" height="1080" alt="2_lihat_response" src="https://github.com/user-attachments/assets/218eb0a6-eb50-443f-9711-b7938e7659c9" />
 
### 3. kita ubah id dari id=carlos jadi id=administrator dan kita sudah bisa melihat password admin

  karna lab ini punya kerentanan id tampering

<img width="1920" height="1080" alt="3_ubah_id_administrator" src="https://github.com/user-attachments/assets/b3106c35-199f-46a6-93a3-ab118129c93a" />

### 4. login jadi admin dan hapus carlos

<img width="1922" height="1046" alt="4_berhasil" src="https://github.com/user-attachments/assets/f0a46f3d-2048-45b5-af82-271a584cb66d" />

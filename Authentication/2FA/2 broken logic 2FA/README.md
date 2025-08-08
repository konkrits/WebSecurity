# LAB 2FA Broken Logic

## Brief:
### verifikasi 2 langkah rentan karena cacat logika
- akun user: wiener:peter
- akun korban: carlos

## Tujuan

### akses akun carlos
<img width="1922" height="1046" alt="brief" src="https://github.com/user-attachments/assets/c21f4f2a-98fb-4a1b-a082-2656ffa5eebd" />

## Analisa:
### lab tidak membatasi seberapa banyak kode 2fa yang salah
### jadi langkah awal adalah menemukan endpoint dan parameter untuk membrute force kode

### 1. login ke akun user dengan request POST /login
<img width="1920" height="1080" alt="1" src="https://github.com/user-attachments/assets/c07f973a-fecb-445c-8951-5b64e1cc3db5" />

### 2. setelah login ada request  GET /login2 yang merupakan request untuk menampilkan laman 2fa dengan ada parameter verifi:wiener
<img width="1920" height="1080" alt="2" src="https://github.com/user-attachments/assets/c6da1486-ae56-4082-a626-c0fd63f6f443" />

### 3. isi 2fa nya dengan request POST /login2 dan ada parameter verifi:wiener 
<img width="1158" height="900" alt="3" src="https://github.com/user-attachments/assets/0f5f3c2b-91fd-43f8-8ebe-e5bb98136bbf" />

### 4. kirim ke repeater yang request GET /login2 dan ganti parameter verify ke carlos
<img width="1920" height="1044" alt="4 verify carlos" src="https://github.com/user-attachments/assets/43bb4dca-c944-4b91-8a8a-b3786a5cfe29" />

### kita akan membrute force 2fa carlos dengan ffuf

### 5. ini adalah untuk membrute force code pastikan semuanya benar dari cookie verify
<img width="1920" height="1080" alt="5" src="https://github.com/user-attachments/assets/fddba86d-4324-4400-95d6-a2e73a1ef71e" />

### 6. masukan req ke ffuf dengan wordlist 0000-9999
<img width="1920" height="1044" alt="6" src="https://github.com/user-attachments/assets/001d4985-bb51-44b2-95b2-6b72c2de7c4f" />

### 7. setelah berhasil masukan code yang benar dan verify ke carlos
<img width="1920" height="1080" alt="7" src="https://github.com/user-attachments/assets/3bbe04a0-0ebd-4d79-ab50-9563ecf49b14" />

### 8. berhasil
<img width="1920" height="1080" alt="8" src="https://github.com/user-attachments/assets/4f931763-82a1-4f51-9059-a7f84f5d03d7" />

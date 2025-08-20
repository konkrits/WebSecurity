# LAB 2 Web shell upload via Content-Type restriction bypass (CONTENT-TYPE)

## Brief:
web mencoba untuk membatasi dari tipe ekstensi yang di upload tetapi terlalu bergantung pada user dan tidak mencek lagi
	
## Tujuan:
dapatkan file /home/carlos/secret

 <img width="1922" height="1046" alt="brief" src="https://github.com/user-attachments/assets/d17a07b5-74db-4c26-9892-80aed84f928d" />

## Analisa:
1. langsung kirim file php dan response mengatakan hanya gambar
	
   <img width="1920" height="1044" alt="1 coba kirim file phg" src="https://github.com/user-attachments/assets/74de18aa-51c2-4bac-91bd-c1793151ef02" />

2. upload gambar dan kirim request GET /files/avatars/cat.jpg  ke repeater
	
3. request upload php kirim ke repeater dan ubah Content-Type: image/jpeg dan kirim

   <img width="1920" height="1044" alt="3 ubah content type" src="https://github.com/user-attachments/assets/43d0b579-9a4d-4344-acbe-4d96649ba7e4" />

4. di request GET ubah jadi /shell.php dan secret file berhasil, submit lalu berhasil.

   <img width="1920" height="1080" alt="4 get dan berhasil" src="https://github.com/user-attachments/assets/7cce63ad-4a66-4c14-aebe-caeb2d79e603" />

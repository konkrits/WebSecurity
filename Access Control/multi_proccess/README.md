# Access control vulnerabilities in multi-step processes

##	(Lab: Multi-step process with no access control on one step)

Banyak situs web menerapkan fungsi penting selama serangkaian langkah. Ini adalah umum ketika:

- Berbagai input atau opsi perlu ditangkap.
- Pengguna perlu meninjau dan mengkonfirmasi rincian sebelum tindakan dilakukan.

Misalnya, fungsi administratif untuk memperbarui detail pengguna mungkin melibatkan langkah-langkah berikut:

- Beban bentuk yang berisi rincian untuk pengguna tertentu.
- Kirimkan perubahan.
- Tinjau perubahan dan konfirmasikan.

Terkadang, sebuah situs web akan menerapkan kontrol akses yang ketat atas beberapa langkah ini, tetapi mengabaikan yang lain. 

### Bayangkan sebuah situs web di mana kontrol akses diterapkan dengan benar pada langkah pertama dan kedua, tetapi tidak ke langkah ketiga. 
###	Situs web mengasumsikan bahwa pengguna hanya akan mencapai langkah 3 jika mereka telah menyelesaikan langkah pertama, yang dikontrol dengan benar. 
###	Penyerang dapat memperoleh akses tidak sah ke fungsi dengan melewatkan dua langkah pertama dan langsung mengajukan permintaan untuk langkah ketiga dengan parameter yang diperlukan.

# Lab: Multi-step process with no access control on one step 

## Brief:
###	lab yang punya kerentanan dalam double pengecekan u:p administrator:admin
## Tujuan:
###	jadikan wiener jadi admin dengan diri sendiri
<img width="1920" height="1032" alt="brief" src="https://github.com/user-attachments/assets/cce6d063-310d-423e-bca4-2bab7f90e088" />

## Analisa:
###	1. login jadi administrator dan jadikan carlos admin, dan intercept
<img width="1922" height="1046" alt="1 carlos admin" src="https://github.com/user-attachments/assets/d46aace7-63b4-40c6-83cb-a8ec75c94bbc" />
	
###	2. sekarang web menkonfirmasi ketika 2 kali ketika ingin mempromosikan
<img width="1920" height="1044" alt="2 web konfir 2kali" src="https://github.com/user-attachments/assets/b2e3c7d2-0e8d-4b70-b9ff-5695ac28387f" />
	
###	3. login jadi wiener di incognito
<img width="1922" height="1046" alt="3 wiener incognito" src="https://github.com/user-attachments/assets/2fd1f47c-2941-4678-a32b-a59e5f7bac28" />
	
###	4. kirim request admin untuk mempromosikan carlos ke repeater
<img width="1920" height="1044" alt="4 kirim admin req" src="https://github.com/user-attachments/assets/156b89d1-1dd5-4ab3-94a7-234eacec573c" />
	
###	5. ubah cookienya jadi cookie wiener dan ubah username jadi wiener
<img width="1920" height="1044" alt="5 cookie" src="https://github.com/user-attachments/assets/c78a72a9-4e61-40ba-b36f-dbf07d2edd99" />	
### kirim dan gagal
	
###	6. coba yang proses kedua ganti cookie nya dan username nya wiener dan berhasil
<img width="1920" height="1044" alt="6 berhasil" src="https://github.com/user-attachments/assets/b2e8dd1c-43d9-429e-853f-1a0f89c025ee" />
	

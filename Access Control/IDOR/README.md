# Insecure direct object references

### Pada bagian ini, kami akan menjelaskan apa itu insecure direct object references (IDOR) dan menggambarkan beberapa kerentanan umum.
## Apa itu insecure direct object references (IDOR)?

### Insecure direct object references (IDOR) adalah jenis kerentanan kontrol akses yang muncul ketika suatu aplikasi menggunakan masukan yang disediakan pengguna untuk mengakses objek secara langsung. 
### Istilah IDOR menjadi populer setelah muncul dalam OWASP Top Ten 2007. Namun, ini hanyalah salah satu contoh dari banyak kesalahan implementasi kontrol akses yang dapat menyebabkan kontrol akses diabaikan. Kerentanan IDOR paling sering dikaitkan dengan eskalasi hak akses horizontal, tetapi juga dapat muncul dalam kaitannya dengan eskalasi hak akses vertikal.

## Contoh IDOR

### Ada banyak contoh kerentanan kontrol akses di mana nilai parameter yang dikendalikan pengguna digunakan untuk mengakses sumber daya atau fungsi secara langsung.
### Kerentanan IDOR dengan referensi langsung ke objek basis data

### Pertimbangkan sebuah situs web yang menggunakan URL berikut untuk mengakses halaman akun pelanggan, dengan mengambil informasi dari basis data belakang:

	https://insecure-website.com/customer_account?customer_number=132355


### Di sini, nomor pelanggan digunakan secara langsung sebagai indeks catatan dalam kueri yang dilakukan pada basis data back-end. Jika tidak ada kontrol lain yang tersedia, penyerang dapat dengan mudah memodifikasi nilai customer_number, melewati kontrol akses untuk melihat catatan pelanggan lain. Ini adalah contoh kerentanan IDOR yang mengarah ke eskalasi hak istimewa horizontal.

### Seorang penyerang mungkin dapat melakukan eskalasi hak istimewa horizontal dan vertikal dengan mengubah pengguna menjadi pengguna dengan hak istimewa tambahan sambil melewati kontrol akses. Kemungkinan lain termasuk mengeksploitasi kebocoran kata sandi atau memodifikasi parameter setelah penyerang masuk ke halaman akun pengguna, misalnya.
### Kerentanan IDOR dengan referensi langsung ke file statis

### Kerentanan IDOR sering kali muncul ketika sumber daya sensitif berada di file statis pada sistem berkas sisi server. Sebagai contoh, sebuah situs web mungkin menyimpan transkrip pesan obrolan ke disk menggunakan nama file yang bertambah, dan mengizinkan pengguna untuk mengambilnya dengan mengunjungi URL seperti berikut ini:

	https://insecure-website.com/static/12144.txt

### Dalam situasi ini, penyerang dapat dengan mudah memodifikasi nama file untuk mengambil transkrip yang dibuat oleh pengguna lain dan berpotensi mendapatkan kredensial pengguna dan data sensitif lainnya.

##	(Lab: Insecure direct object references)

###	Insecure direct object References (IDOR) adalah subkategori kerentanan kontrol akses. IDOR terjadi jika aplikasi menggunakan input yang disediakan pengguna untuk mengakses objek secara langsung 
###	dan penyerang dapat memodifikasi input untuk mendapatkan akses yang tidak sah. Itu dipopulerkan oleh penampilannya di OWASP 2007 Top Ten. 
###	Ini hanyalah salah satu contoh dari banyak kesalahan implementasi yang dapat memberikan sarana untuk memotong kontrol akses.


# LAB IDOR
## Brief:
### lab yang menyimpan log chat pengguna di server dan emngakses nya dengan url statis
## Tujuan:
### cari password carlos dan login
<img width="1922" height="1046" alt="Brief" src="https://github.com/user-attachments/assets/74eeedf2-a223-4cb0-8c14-7f69f8cef6a3" />

## Analisa:

### 1. login
	
### 2. pergi ke halaman live-chat
<img width="1922" height="1046" alt="2_pergi_ke_live_chat" src="https://github.com/user-attachments/assets/3b066991-6802-455f-93ae-b105e58d9bcf" />
 
### 3. ketik sesuatu, kirim
<img width="1922" height="1046" alt="3_send" src="https://github.com/user-attachments/assets/70962562-6873-4b13-b373-c44425ec8524" />


### 4. klik transkrip otomatis kita mendowload file, file4.txt 
### kita bisa berasumsi bahwa file1.txt adalah milik carlos
<img width="1920" height="1080" alt="4_klik_transcript_dan_otomatis_download" src="https://github.com/user-attachments/assets/fa3f4c50-2874-48ce-84ec-d08acee82fbc" />

### 5. soo intercept dan ubah di request nama filenya dari 4 ke 1, dan krim
<img width="1119" height="1032" alt="5_ganti_jadi_1" src="https://github.com/user-attachments/assets/b1f4ca82-7e85-4e25-8306-72dc8d7b0543" />

	
### 6. dan kita dapat file carlos yang berisi password
<img width="1920" height="1044" alt="6_kita_berhasil_mengambil_resoource_orang" src="https://github.com/user-attachments/assets/684baaca-9ee5-435d-a688-d672061462c7" />


### 7. login jadi carlos dan berhasil
<img width="1922" height="1046" alt="7_berhasil" src="https://github.com/user-attachments/assets/e6d60977-23fd-4af3-b4a1-cd95cdc69123" />


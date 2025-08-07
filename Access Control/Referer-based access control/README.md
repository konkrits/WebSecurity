# Referer-based access control

### Beberapa situs web mendasarkan kontrol akses pada header Referer yang dikirimkan dalam permintaan HTTP. Header Referer dapat ditambahkan ke permintaan oleh browser untuk menunjukkan halaman mana yang memulai permintaan.

Misalnya, aplikasi dengan kuat menegakkan kontrol akses atas halaman administrasi utama di /admin, tetapi untuk sub-halaman seperti /admin / deleteUser hanya memeriksa header Referer. 
Jika header Referel berisi URL /admin utama, maka permintaan diperbolehkan.

### Dalam hal ini, sundulan Referator dapat sepenuhnya dikendalikan oleh penyerang. Ini berarti bahwa mereka dapat menempa permintaan langsung ke sub-halaman sensitif dengan memasok header Referer yang diperlukan, 
### dan mendapatkan akses yang tidak sah.

# Location-based access control

### Some websites enforce access controls based on the user's geographical location. This can apply, for example, to banking applications or media services where state legislation or business restrictions apply. These access controls can often be circumvented by the use of web proxies, VPNs, or manipulation of client-side geolocation mechanisms. 

# Lab: Referer-based access control

## Brief:
### akses kontrol berdasarkan header referer
	
## Tujuan:
###jadikan wiener admin
<img width="1922" height="1046" alt="Brief" src="https://github.com/user-attachments/assets/6bebdc4a-1a7a-44e7-9107-7762725aa8bc" />

## Analisa:
### 1. login jadi administrator, upgrade carlos
<img width="1922" height="1046" alt="1_jadi_admin" src="https://github.com/user-attachments/assets/8541b349-ed24-4b30-8e37-cfc761a4b190" />

### 2. di jendela samaran login wiener
<img width="1206" height="1032" alt="2_copy_wiener_cookie" src="https://github.com/user-attachments/assets/1334a1b4-5b9d-4486-9a30-38471957a8cd" />

### 3. ganti request header tadi refer nya jadi /admin dan kirim endpoint yang mengupgrade carlos jadi admin 
### ganti jadi wiener: /admin-roles?username=wiener&action=upgrade
<img width="1206" height="1032" alt="3_refer_admin" src="https://github.com/user-attachments/assets/a44c1f18-ba6f-4488-ac37-02afda6d282e" />

### 4. berhasil
<img width="1876" height="1032" alt="4_dan_berhasil" src="https://github.com/user-attachments/assets/090eae00-70a1-417e-9888-b0b32bf9f80a" />

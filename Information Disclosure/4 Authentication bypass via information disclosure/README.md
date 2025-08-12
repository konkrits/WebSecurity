# Lab 4 Authentication bypass via information disclosure

## Brief:
Antarmuka administrasi lab ini memiliki kerentanan bypass otentikasi dan harus punya pengetahuan header http khusus yang digunakan front-end.
<img width="1920" height="1080" alt="Lab" src="https://github.com/user-attachments/assets/ac3f5acc-1f43-4125-8090-2bf14af6d457" />

## Tujuan:
login ke halaman admin dan menghapus user carlos. dengan cara membypass autentikasi dengan nama header.

## Analisa:
1.) mencoba ke panel tetapi hanya bisa diakses oleh localhost
<img width="1920" height="1080" alt="1_Coba_ke_Admin" src="https://github.com/user-attachments/assets/0dd3ccbf-b922-407d-b8f4-f09be5dd0844" />

2.) ganti request method nya ke Trace ternyata berhasil, dan lihat diresponse bawah ternyata ada header X-Custom-IP-Authorization
default value dari header tersebut adalah ip pengguna, dan coba untuk ganti ke localhost atau 127.0.0.1
<img width="1920" height="1080" alt="2_Request_TRACE" src="https://github.com/user-attachments/assets/583a2763-f724-4eba-94e9-b3fdaf71d7c2" />

3.) ke match dan replace dan tambahkan custome ip nya di kolom replace
<img width="1920" height="1080" alt="3Custom_ip_Local" src="https://github.com/user-attachments/assets/d8f7b586-6642-4b40-a402-02aa931dafae" />

4.) kembali ke directory admin lagi dan berhasil. hapus akun carlos
<img width="1920" height="1080" alt="4_Admin_and_delete_user" src="https://github.com/user-attachments/assets/6c7e16f3-65ba-4de5-8a8b-66842281c367" />
 

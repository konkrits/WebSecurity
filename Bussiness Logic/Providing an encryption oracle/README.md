# LAB Authentication bypass via encryption oracle

## Brief:
lab ini menampilkan encryption oracle ke user
akun: wiener:peter

## Tujuan:
jadi admin dan hapus user carlos

<img width="1919" height="1079" alt="brief" src="https://github.com/user-attachments/assets/679213dd-dcf7-4098-9e02-f74751ef4316" />

## Analisa:
lab menampilkan enkripsi oracle ke user di fitur komentar ketika memasukan email yang error.
lab bisa mengenkripsi dengan di kolom komentar dan bisa mendekrip di notif error emai

## Exploit:

1. Masuk dengan opsi “stay-logged-in” diaktifkan

> GET /login 

<img width="1914" height="1079" alt="1 login" src="https://github.com/user-attachments/assets/c6257eb8-4641-4f6d-b0ab-268edcfc257b" />

2. Perhatikan bahwa cookie “stay-logged-in” dienkripsi.

> GET /my-account
    
<img width="1914" height="1079" alt="2 cookie enkrip" src="https://github.com/user-attachments/assets/65382008-cde9-49a5-b1c7-ec6188230908" />

3. Perhatikan bahwa saat Anda mencoba mengirim komentar menggunakan alamat email yang tidak valid

> POST /post/comment

<img width="1914" height="1079" alt="3 komen email invalid" src="https://github.com/user-attachments/assets/591eeaa7-094f-480d-a5ae-2c29af7cceaa" />

4. respons akan menampilkan cookie pemberitahuan yang dienkripsi sebelum mengalihkan Anda ke posting blog.

> GET /post?postid=7


5. Perhatikan bahwa pesan kesalahan menampilkan input Anda dari parameter email dalam teks biasa:
  
> Invalid email address: your-invalid-email

Simpulkan bahwa ini harus didekripsi dari cookie notifikasi. 

Kirim permintaan POST /post/comment dan permintaan GET /post?postId=7 (yang berisi cookie notifikasi) ke Burp Repeater.

Di Repeater, perhatikan bahwa Anda dapat menggunakan parameter email permintaan POST untuk mengenkripsi data asal dan mencerminkan teks terenkripsi yang sesuai di header Set-Cookie. 
Demikian pula, Anda dapat menggunakan cookie pemberitahuan di permintaan GET untuk mendekripsi teks terenkripsi asal dan mencerminkan outputnya di pesan kesalahan. 
Untuk kesederhanaan, klik dua kali tab untuk setiap permintaan dan ganti nama tab menjadi encrypt dan decrypt masing-masing.

<img width="1913" height="1079" alt="5 notif invalid email" src="https://github.com/user-attachments/assets/61538272-1713-4845-a74a-a700c6626787" />

6. Dalam permintaan decrypt, salin cookie stay-logged-in Anda dan tempelkan ke dalam cookie notifikasi. 

Kirim permintaan. Alih-alih pesan kesalahan, respons sekarang berisi cookie stay-logged-in yang telah didekripsi, 

misalnya:
    
> wiener:1598530205184

Ini menunjukkan bahwa cookie harus dalam format username:timestamp. Salin timestamp ke clipboard Anda.
  
<img width="1915" height="1076" alt="6 decrypt cookie" src="https://github.com/user-attachments/assets/dce1fde2-b3c8-485a-9c1f-2eba129c1d2c" />

7. Buka permintaan enkripsi dan ubah parameter email menjadi administrator:your-timestamp. Kirim permintaan dan salin cookie notifikasi baru dari respons.

<img width="1905" height="1079" alt="7 komen cookie" src="https://github.com/user-attachments/assets/577956ac-be5e-40ba-8c45-3f33b35217e7" />

8. Dekripsi cookie baru ini dan perhatikan bahwa prefiks 23 karakter “Invalid email address: ” secara otomatis ditambahkan ke nilai apa pun yang Anda kirimkan menggunakan parameter email. 
		
Kirim cookie notifikasi ke Burp Decoder.
  
Di Decoder, URL-decode dan Base64-decode cookie tersebut.
  
<img width="1912" height="1079" alt="8 dekrip cookkie" src="https://github.com/user-attachments/assets/61f16f35-4041-4d6e-b38c-d493c3236ae0" />

9. Di Burp Repeater, beralih ke tab “Hex” di editor pesan. Pilih 23 byte pertama, lalu klik kanan dan pilih “Hapus byte yang dipilih”.

<img width="1917" height="1079" alt="9 deleted hex" src="https://github.com/user-attachments/assets/1bda2300-9777-49bb-9701-1bc90c4631c2" />

10. Enkode ulang data dengan base64 

<img width="1918" height="1079" alt="10 encode ulang" src="https://github.com/user-attachments/assets/5e42d8dd-db7d-4caf-90d7-ec9022f9f874" />

11. salin hasilnya ke cookie notifikasi permintaan dekripsi. Saat Anda mengirim permintaan, perhatikan bahwa pesan kesalahan menunjukkan bahwa algoritma enkripsi berbasis blok digunakan 
		
dan panjang input harus kelipatan 16. Anda perlu menambahkan byte yang cukup pada prefiks “Invalid email address: ” sehingga jumlah byte yang akan dihapus adalah kelipatan 16.

<img width="1913" height="1079" alt="11 error" src="https://github.com/user-attachments/assets/5fda2372-5bb8-41fc-b8bd-0a7e60bb8ce8" />

12. Di Burp Repeater, kembali ke permintaan enkripsi dan tambahkan 9 karakter di awal nilai cookie yang dimaksud, misalnya:

> xxxxxxxxxadministrator:your-timestamp

<img width="1915" height="1079" alt="12 9 char" src="https://github.com/user-attachments/assets/456ed15f-528a-4fc7-8e49-0c93c14658c2" />

13. Enkripsi input ini dan gunakan permintaan dekripsi untuk menguji apakah data tersebut dapat didekripsi dengan sukses.  
    
	Kirim teks terenkripsi baru ke Decoder, lalu URL dan Base64-decode-nya. Kali ini, hapus 32 byte dari awal data. Enkripsi ulang data

<img width="1916" height="1079" alt="13 engkrip dan dekrip a" src="https://github.com/user-attachments/assets/8ddbdb81-da61-4224-8446-3b684ba8c6fd" />

14. tempelkan ke parameter notifikasi dalam permintaan dekripsi. Periksa respons untuk memastikan bahwa input Anda berhasil didekripsi dan, yang terpenting, tidak lagi mengandung prefiks “Alamat email tidak valid: ”. Anda hanya akan melihat administrator:your-timestamp.  

<img width="1915" height="1079" alt="14 no invalid" src="https://github.com/user-attachments/assets/803857ae-d22b-45c8-b9cd-08489e35549e" />
    
15. kirim permintaan GET / ke Burp Repeater. 

Hapus cookie sesi sepenuhnya, dan ganti cookie stay-logged-in dengan teks terenkripsi dari cookie buatan Anda sendiri. Kirim permintaan. 

<img width="1918" height="1079" alt="15 hapus cokie dengan stay login" src="https://github.com/user-attachments/assets/2d8a5156-8d2b-4d70-a03e-273d3f58c2ac" />

16. Perhatikan bahwa Anda sekarang masuk sebagai administrator dan memiliki akses ke panel admin.

<img width="1916" height="1079" alt="16 panel admin" src="https://github.com/user-attachments/assets/43196a65-5158-488f-b8c5-4371b56198f6" />

17. Menggunakan Burp Repeater, buka /admin dan perhatikan opsi untuk menghapus pengguna. 

<img width="1919" height="1079" alt="17 endpoin delete" src="https://github.com/user-attachments/assets/90bd2838-ce95-4654-b510-c0799c7acad8" />

18. kirim /admin/delete?username=carlos untuk menyelesaikan lab.

<img width="1919" height="1079" alt="18 delete carlos" src="https://github.com/user-attachments/assets/4c71e803-6a4b-412f-afce-528fa94d6483" />

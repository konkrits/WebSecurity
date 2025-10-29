# Lab: Username enumeration via response timing

## Brief:
vulnerable terhadap username enumeration melalui response time, akun wiener:peter dan memblokir ip ketika gagal 3kali
	
## Tujuan:
enumerate username dan brute force passwordnya lalu login

<img width="1922" height="1046" alt="brief" src="https://github.com/user-attachments/assets/1b961eb8-6d5b-4da4-8faa-7712697e45f9" />
	
## Analisa:

1. dikonfirmasi bahwa setelah 3 kali kita diblokir ip nya
	
<img width="1920" height="1080" alt="1_ip_block" src="https://github.com/user-attachments/assets/da79ebe2-e72a-416a-ac22-f1551772e2b3" />

2. ternyata kita bisa membypass dengan menambahkan X-Forwarded-For:ip acak
>> otomatis kita bisa membypass
	
<img width="1920" height="1080" alt="2_bypass_IP_x_forwarded_for" src="https://github.com/user-attachments/assets/721bac01-9149-43a2-9609-e43105c963dc" />

3. menginput bebrapa username yang tidak ada response nya sama tetapi
>> ketika meninput username yang ada yaitu wiener response waktunya berbeda tergantung
>> seberapa banyak karakter dari passwordnya

 <img width="1920" height="1080" alt="3_respon_beda_username_benar" src="https://github.com/user-attachments/assets/58c6b9a7-6b9c-4ccc-8aae-32769691e678" />
 
4. ganti dari sniper ke pitchfork attack lalu tambahkan X-Forwarded-For: di request header
>> set ip acak jadi payload 1 dan username jadi payload 2
>> sementara passwordnya lebihkan dari 100
				
<img width="1920" height="1044" alt="4_pitcfork_X_forward_user" src="https://github.com/user-attachments/assets/d3bd494e-8d13-450e-bae2-6ffec6e0204d" />

5. dari kanan pilih payload posisi ke 1 dan jadikan number, from 0 to 255 dan stepnya 1
>> pilih payload 2 list username nya 
					
<img width="1920" height="1044" alt="5_posisi1_step1_dari0_ke_255" src="https://github.com/user-attachments/assets/c7de0742-095a-4cb6-8ead-4eb528e78ce9" />

6. setelah selesai klik kolom response received yang paling terbesar nah inilah username yang ada
	
<img width="1920" height="1044" alt="6_kolom_received_terbesar" src="https://github.com/user-attachments/assets/1e91d7df-9e78-4b4e-a009-1bc9a4a14a38" />

7. clear posisi, username jadi user no 6 dan tambahkan posisi untuk password
>> untuk X-Forwarded-For ubah 1 angka ip nya selbihnya ikutin langkah sebelumnya
		
<img width="1920" height="1080" alt="7_password_posisi" src="https://github.com/user-attachments/assets/351ed3e8-803e-41f0-b85c-28f7071934a0" />

8. setelah selesai nanti ada status 302 pengalihan
>> login menggunakan kredensial ini dan berhasil


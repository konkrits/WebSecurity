# Lab 2: Username enumeration via subtly different responses

## Brief:
Lab yang agak rentan dengan brute force

## Tujuan:
enumerate username lalu brute force passwordnya dan login ke akunnya

<img width="1922" height="1046" alt="brief" src="https://github.com/user-attachments/assets/a9bbe3fa-ec0c-4e57-a782-49c59d504ae6" />

## Analisa:

1. kirim post /login ke intruder, tambahkan posisi di username dal tambahkan list usernamenya

<img width="1920" height="1044" alt="1_intruder_set_username" src="https://github.com/user-attachments/assets/53e52d05-b4ca-42ab-b90c-e56e36177e44" />

2. pergi ke setting kanan temukan grep-extract klik add lalu refetch response kemudian highlight Invalid username and password. dan OK start ATTACK

<img width="1920" height="1080" alt="2_setting_extract_grep" src="https://github.com/user-attachments/assets/92447e29-6a6c-4733-bb7e-6a2d8d13f0a6" />

3. ketika selesai klik kolum warning perhatikan ada satu response berbeda yang berisi username yang ada, response yang lain "Invalid username and password." tapi yang ini "Invalid username and password"
> hanya tidak ada titik saja

<img width="1920" height="1080" alt="3_response_beda" src="https://github.com/user-attachments/assets/b3822d7f-61e9-4a84-998e-5b56c6e389ce" />

4. isi username dengan username yang ditemukan nomor 3 dan tambahkan posisi ke password isi payload dengan list password

<img width="1209" height="1017" alt="4_set_admin" src="https://github.com/user-attachments/assets/5d6c1267-f1e5-495b-ad9b-c03668678d23" />

5. ketika sudah semua, klik response dan ada kode 302 login menggunakan username dan pasword itu dan berhasil.

<img width="1920" height="1080" alt="5_status_302" src="https://github.com/user-attachments/assets/6c89601e-c07c-490e-b966-e3406b7b7670" />

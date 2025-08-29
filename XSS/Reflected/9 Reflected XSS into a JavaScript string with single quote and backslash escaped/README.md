# Lab 9 Reflected XSS into a JavaScript string with single quote and backslash escaped

## Brief:
xss reflected di fungsi pencarian query tracking, reflection occurs didalam Javascript string dengan single quotes ' dan / escaped

## Tujuan:
break out javascript string dan lakukan alert()


## Analisa:
	
1. masukan nomor random di pencarian dan kirim ke repeater

<img width="1903" height="1029" alt="1 nomor random" src="https://github.com/user-attachments/assets/1af036f1-1c47-40d4-ba41-50894bd9df9f" />

2. lihat di response nomornya di refleksikan ke js string

<img width="1920" height="1032" alt="2 refleksi di js" src="https://github.com/user-attachments/assets/3629d76d-3de6-404e-b072-2e939235f85d" />

3. coba kirim di pencarian dengan test'payload dan diresponse di escape \' untuk mencegah string di break

<img width="1920" height="1032" alt="3 test payload" src="https://github.com/user-attachments/assets/b1324fd1-4b84-426d-89ca-2049c73c8dcb" />

4. masukan payload untuk mem break blok skrip dan memasukan script baru

>     </script><script>alert()</script>


5. verifikasi teknik dengan mengcopy url dan paste di browser

> alternatifnya masukan di kolom pencarian payloadnya

<img width="1919" height="1074" alt="4 exploit dan berhasil" src="https://github.com/user-attachments/assets/3494d7c0-68e7-444f-9a88-5fd81400c45a" />















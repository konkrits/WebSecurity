# LAB 10 Reflected XSS into a JavaScript string with angle brackets and double quotes HTML-encoded and single quotes escaped

## Brief:
reflected xss di fungsi pencarian query tracking, di mana tanda kurung sudut (< dan >) dan tanda kutip ganda (") diubah ke format HTML, dan tanda kutip tunggal (') di-escape 

## Tujuan:
Break javascript string dan lakukan alert()

<img width="1920" height="1032" alt="brief" src="https://github.com/user-attachments/assets/0bdda626-f9eb-446d-873a-f52a8f6bbd69" />

## Analisa:

1. masukan di pencarian nomor random dan kirim ke repeater

<img width="1916" height="1026" alt="1 itercept input" src="https://github.com/user-attachments/assets/144e8a09-208a-4b51-8630-5d2c5913eeee" />

2. lihat di response nomor itu di refleksikan

<img width="1920" height="1032" alt="2 refleksi di js" src="https://github.com/user-attachments/assets/9d78919f-a533-43e9-af98-a7502410f71e" />

3. masukan test payload contoh: test'test
	
> di response tanda kutip tersebut di escape dengan \'

<img width="1920" height="1032" alt="3 test tanda kutip" src="https://github.com/user-attachments/assets/9a014433-adb3-4231-801e-90c961e458e3" />

4. tes lagi dengan backslash \ contoh: test\test
	
> di response backslash itu tidak diescape dan ditampilkan \\

<img width="1920" height="1080" alt="4 test backslash" src="https://github.com/user-attachments/assets/39a34148-6a9e-4b18-99c0-c0f218c60257" />

5. sekarang masukan payload \'-alert(1)//

> \ awal karena tidak di escape jadi bisa membuat skrip baru

> ' untuk menutup string

> - tidak ada fungsi khusus tapi bisa saja untuk mentolerir error

> // komentar di gunakan untuk menutup skrip setelah nya agar tidak terjadi error
	
<img width="1920" height="1080" alt="5 payload berhasil" src="https://github.com/user-attachments/assets/b2381f9f-33a3-406d-a805-10375107cacb" />
	   

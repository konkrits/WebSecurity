# Lab 7 Stored DOM XSS

## Brief:
web rentan stored DOM di comment blog
	
## Tujuan:
gunakan alert()
	
<img width="1922" height="1046" alt="brief" src="https://github.com/user-attachments/assets/97170498-8b32-4c5f-8fee-ae624df89971" />

## Analisa:
Dalam upaya untuk mencegah XSS, situs web menggunakan JavaScript replace()fungsi untuk mengkodekan kurung sudut. Namun, ketika argumen pertama adalah string, fungsi hanya menggantikan kejadian pertama. 
	Kami mengeksploitasi kerentanan ini hanya dengan menyertakan satu set tambahan tanda kurung sudut di awal komentar. Kurung sudut ini akan dikodekan, 
	tetapi setiap tanda sudut berikutnya tidak akan terpengaruh, memungkinkan kita untuk secara efektif melewati filter dan menyuntikkan HTML.

1. masukan payload

       <><img src=1 onerror=alert(1)>
	
<img width="1922" height="1046" alt="payload" src="https://github.com/user-attachments/assets/d6d130ee-2ed5-40b3-87f4-415dffdea648" />

2. berhasil
	
<img width="1922" height="1046" alt="2" src="https://github.com/user-attachments/assets/ba455354-1859-413e-8675-2c322fa59cf5" />

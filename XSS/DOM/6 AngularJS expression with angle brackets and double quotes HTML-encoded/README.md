# LAB 6 DOM XSS in AngularJS expression with angle brackets and double quotes HTML-encoded

## Brief:
fungsi pencarian AngularJS adalah perpustakaan JavaScript yang populer, yang memindai isi node HTML yang berisi atribut ng-app (juga dikenal sebagai arahan AngularJS). 
	Ketika arahan ditambahkan ke kode HTML, Anda dapat mengeksekusi ekspresi JavaScript dalam curly braces ganda. Teknik ini berguna ketika kurung sudut sedang dikodekan.
	
## Tujuan:
eksekusi javascript ecsperession dan gunakan alert()
	
<img width="1922" height="1046" alt="brief" src="https://github.com/user-attachments/assets/45e464f4-05de-4020-9c4c-76b57cb49aa3" />

## Analisa:

1. masukan nomor di kolom pencarian dan cari nomor itu di inspeksi
	
<img width="1922" height="1046" alt="1" src="https://github.com/user-attachments/assets/9cee4f57-0f77-495d-ae3e-49a78ce5b037" />

2. masukan payload dan berhasil
		
		{{$on.constructor('alert(1)')()}}

<img width="1922" height="1046" alt="2" src="https://github.com/user-attachments/assets/9daafb76-92bb-47cd-ad9f-b38d30770a37" />

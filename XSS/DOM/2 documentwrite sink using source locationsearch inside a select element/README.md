# (LAB 2 document.write sink using source location.search inside a select element)

## Brief:
Lab ini berisi kerentanan skrip lintas situs berbasis DOM dalam fungsi pemeriksa stok. Ini menggunakan JavaScript document.write fungsi, yang menulis data keluar ke halaman. The document.write fungsi dipanggil dengan data dari location.search yang dapat Anda kontrol menggunakan URL situs web. Data diapit dalam elemen tertentu.

Untuk menyelesaikan lab ini, lakukan serangan skrip lintas situs yang keluar dari elemen pilihan dan memanggil alert function.
## Tujuan: 

lakukan alert(1)

<img width="1922" height="1046" alt="brief" src="https://github.com/user-attachments/assets/d207f912-cb3e-4cad-91c1-c29229700dd7" />

## Analisa:
	
1. Pada halaman produk, perhatikan bahwa JavaScript yang berbahaya mengekstrak parameter storeId dari sumber pencari. 
		Kemudian menggunakan document.write untuk membuat opsi baru dalam elemen tertentu untuk fungsi stock checker.
		
<img width="1920" height="1080" alt="1 storeid bahaya" src="https://github.com/user-attachments/assets/c7b7362e-b04c-44e7-84e7-631056daa1f7" />

2. di url productId=3 jadikan productId=1&storeId=1
		dan lihat kalo di stok sekarang ada pilihan nomor 1	
		
<img width="1922" height="1046" alt="2 tambahkan di url storeid" src="https://github.com/user-attachments/assets/702d0e52-809a-4e7c-866a-bc5a1292620b" />

3. inspect bahwa string kamu ada di elemnent
	
<img width="1922" height="1046" alt="3 inspect" src="https://github.com/user-attachments/assets/b29d3803-c2c8-4e4a-ba5b-6ef3f7a74ef4" />

4. tambahkan ini di url:
	
> product?productId=1&storeId="></select><img%20src=1%20onerror=alert(1)>	
>		
> dan berhasil
		
<img width="1922" height="1046" alt="4 payload select" src="https://github.com/user-attachments/assets/62a57a27-cc55-4434-be4a-6e743997baac" />
		

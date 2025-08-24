# Lab 1 : Excessive trust in client-side controls

## Brief:
lab ini tidak cukup kuat untuk memvalidasi user input, kamu bisa mengekploitasi ini untuk membeli item dengan harga yang tidak wajar

## Tujuan:
Beli item "Lightweight l33t leather jacket"

<img width="1922" height="1046" alt="brief" src="https://github.com/user-attachments/assets/35c715fb-e037-440a-990f-41ce37f57a65" />

## Analisa:

### Prepare:
2. ini adalah laman produk dan request GET /
  
<img width="1920" height="1080" alt="pre 2" src="https://github.com/user-attachments/assets/3ff29e16-148f-45e7-aea7-236c822ad890" />

3. ini laman keranjang

<img width="1167" height="1025" alt="pre 3" src="https://github.com/user-attachments/assets/bd92502e-c521-4d9a-af33-a392a904663d" />

4. ini request dan laman setelah mencekout

<img width="1920" height="1044" alt="pre 4" src="https://github.com/user-attachments/assets/0bbed025-9d2f-4f08-ae60-9b7604019ed9" />

5. ini request chekout

<img width="1167" height="1025" alt="pre 5" src="https://github.com/user-attachments/assets/a0d502b5-cdcc-4f0a-bf35-62f67ba6a346" />

### Exploit:

1. login
	

2. pergi ke laman produk
	
<img width="1920" height="1080" alt="2" src="https://github.com/user-attachments/assets/b0cbb885-c1a7-4fd2-846d-dab6314858c5" />

3. tambahkan ke keranjang
	
perhatikan request paramater pricenya
		
<img width="1920" height="1080" alt="3" src="https://github.com/user-attachments/assets/78bb6236-d0e3-45a4-ba3a-830eb5a9d792" />

4. ini adalah harga normal
	
<img width="1920" height="1080" alt="4" src="https://github.com/user-attachments/assets/98e1a645-a31b-4710-ac19-1bb9f74463f1" />

5. sekarang di POST /cart atau yang dipakai untuk menambahkan ke keranjang
	
ubah pricenya menjadi bebas, price=5
	
coba ke keranjang melalui request burp  atau browser dan sekarang harga nya berubah
		
<img width="1920" height="1080" alt="5" src="https://github.com/user-attachments/assets/d354f401-909d-468a-9cda-4e3e403d567c" />

6. POST checkout kirim atau dilaman keranjang juga bisa dan berhasil	
		
<img width="717" height="1027" alt="6" src="https://github.com/user-attachments/assets/c05f9b17-1496-495a-9642-7ef13286ad41" />






















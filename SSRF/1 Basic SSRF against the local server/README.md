# LAB 1 Basic SSRF against the local server

## Brief:
web mengambil data stok produk di internal system yang dimana itu rentan ssrf 

<img width="1920" height="1032" alt="LAB1" src="https://github.com/user-attachments/assets/92c5c1ec-7929-4ee7-a181-988844eb58b7" />
	
## Tujuan:
Akses admin panel di 

    http://localhost/admin 

dan hapus carlos
	
## Analisa:
1. check stok dan kirim request ke repeater
<img width="1920" height="1080" alt="1 check stok dan intercept" src="https://github.com/user-attachments/assets/c7f03f3e-82d1-4d57-b551-bb3216e6b0e7" />
	
2. di stock api ganti urlnya jadi

       http://localhost/admin
dan kirim

<img width="1920" height="1044" alt="2 ganti isi stockAPI" src="https://github.com/user-attachments/assets/c8bf5af5-b916-4e4f-8167-93b657f9b1f0" />
	
3. cari di response carlos
<img width="1920" height="1044" alt="3 cari carlos di response" src="https://github.com/user-attachments/assets/dab7bf65-7946-4131-97db-6ddd4c18c6d5" />

4. berhasil
<img width="1920" height="1044" alt="4 berhasil" src="https://github.com/user-attachments/assets/5fca980c-1969-4cdf-8c4e-1b0a3896e781" />
	
meskipun unauthorize tapi dikarenakan request berasal dari dalam jadi berhasil
	
	
	

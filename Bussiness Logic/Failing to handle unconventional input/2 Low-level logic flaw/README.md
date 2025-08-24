# Lab 2 Low-level logic flaw

## Brief:
lab ini tidak cukup memvalidasi user input
	
## Tujuan:
beli produk "Lightweight l33t leather jacket" dengan harga yang tidak wajar
	
<img width="1922" height="1046" alt="lab 2" src="https://github.com/user-attachments/assets/ce0665fa-a62c-4008-8f2a-8d5642f972a3" />

## Analisa:
> uang yang dimiliki $100 harga produk $1337
	
1. masukan produk ke keranjang
	
> maksimal stok untuk dimasukan adalah 99
> 	
> nah disini web tidak memvalidasi

<img width="1920" height="1080" alt="1 ke keranjang jacker" src="https://github.com/user-attachments/assets/e961065f-ed85-4ca2-94d7-acac05c8037d" />

2. fuzz dengan ffuf di parameter stok dengan 99 tanpa batasan request

<img width="1920" height="1080" alt="2 fuzz stok" src="https://github.com/user-attachments/assets/74f5ec58-15b1-4d94-8941-486c7f579a96" />

3. refresh terus di halaman produk
	
<img width="1920" height="1080" alt="3 refersh" src="https://github.com/user-attachments/assets/a0a89a36-94a4-4780-a097-55dc1ea1c198" />

4. dan ketika muncul harga negatif berhenti
	
> dan itulah kerentanannya
>		
> hapus keranjang
>		
> step berikutnya adalah membeli produk tersebut dengan uang yang ada

<img width="1920" height="1080" alt="4 harga negatif" src="https://github.com/user-attachments/assets/8263e158-b750-4250-a94e-a133d9df18d4" />
	
5. tambahkan produk yang lain
> produk ini sebagai pengkonter produk tujuan
		
<img width="1920" height="1080" alt="5 produk pengkounter" src="https://github.com/user-attachments/assets/c35b02e4-05e2-42ee-b86b-ea5d616f8554" />

6. fuzz lagi produk tujuan dengan request 323 dan tujuan stok 32123
	
<img width="1920" height="1080" alt="6 fuzz produk" src="https://github.com/user-attachments/assets/cbd23864-3400-43ac-af83-3965d4ec402c" />

7. selesai fuzz
	
<img width="1920" height="1080" alt="7 fuzz selesai" src="https://github.com/user-attachments/assets/a15ae57a-0b42-4d06-b98f-01661240643d" />

8. di keranjang harga menjadi minus -1138 
	
<img width="1000" height="1025" alt="8 minus seribu" src="https://github.com/user-attachments/assets/c3e1736a-5bd0-47c7-82c5-be8205d2e33e" />

9. tambah stok produk pengcounter menjadi 15 dan sekarang harganya menjadi $22
	
<img width="1000" height="1025" alt="9 pengcounter jadi 22" src="https://github.com/user-attachments/assets/a5f1d718-ef7f-46f0-a7be-484cd8d73a01" />

10. beli dan berhasil

<img width="1920" height="985" alt="10 berhasil" src="https://github.com/user-attachments/assets/eee99f40-864f-4ef3-86cc-08e54be1cd78" />

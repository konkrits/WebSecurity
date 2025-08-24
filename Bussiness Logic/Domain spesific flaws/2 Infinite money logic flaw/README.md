# LAB Infinite money logic flaw

## Brief:
lab ini cacat logika dalam workflow pembelian
	
saldo akun: $100
	
## Tujuan:
beli produk mahal yaitu "Lightweight l33t leather jacket" seharga $1300
  <img width="1922" height="1046" alt="brief" src="https://github.com/user-attachments/assets/4a4fb51b-559e-4de9-a473-6b1548de627b" />

	
## Analisa:
web memberikan fitur untuk redeem card dan harus membeli dulu produk redeem cardnya lalu ada voucher discount 
	
saldo = $100
redeem card = $10
diskon kupon = -30%
	
ketika di reedem menambahkan $3
	
nah otomasi proses ini sehingga saldo cukup untuk membeli produk yang dituju
	
## exploit:

1. tambahkan produk reedm card ke keranjang    		
> POST /cart

 <img width="1920" height="1080" alt="1 redeem keranjang" src="https://github.com/user-attachments/assets/bee68143-4658-43c9-b414-612e443f6b43" />

2. masukan voucher kupon diskon dengan request 		
> POST /cart/coupon

 <img width="1920" height="1080" alt="2 req isi vocer" src="https://github.com/user-attachments/assets/6435799e-74b5-41d9-bfe6-ccee55aadad5" />

3. lalu place order dengan request 	       		
> POST /cart/checkout

 <img width="1920" height="1080" alt="3 req beli" src="https://github.com/user-attachments/assets/177089b3-7bd1-4e01-87d7-61ef5d27523d" />

4. setelah membeli ada request apa yang sudah dibeli	
> GET  /order-confirmation?orderded-confirmed=true
	
req ini juga untuk menampilkan kode
giftcard nya di request ini

 <img width="1920" height="1080" alt="4 lis gift card" src="https://github.com/user-attachments/assets/a3cb91ae-0698-4fc7-b7e9-c33a1941531a" />

5. masukan kode reedem di laman my account dengan req	
> POST /gift-card

dan uang bertambah $3 dari 100
		
ULANGI ATAU AUTOMATISASI HINGGA CUKUP UNTUK MEMBELI PRODUK YANG DITUJU

 <img width="1920" height="1080" alt="5 masukan gift" src="https://github.com/user-attachments/assets/14eb3357-2d76-4223-95c5-7ceb5a8626eb" />

6. menggunakan python

 <img width="1920" height="1044" alt="6 otomasi py" src="https://github.com/user-attachments/assets/60d981f0-62de-4e86-9fea-ea634ffb9798" />
 
7. setelah selesai uang bertambah menjadi $1400

 <img width="1920" height="1080" alt="7 otomasi selesai" src="https://github.com/user-attachments/assets/f35051f7-899e-47ba-9a81-ecb8df46ba3b" />

8. beli produk Lightweight l33t leather jacket

 <img width="1922" height="1046" alt="8 beli produk" src="https://github.com/user-attachments/assets/ffa5161b-1629-4837-871e-aef0de80f08a" />

9. dan selesai

 <img width="1922" height="1046" alt="9 berhasil" src="https://github.com/user-attachments/assets/02c00659-e221-40be-b564-45b0c880ab17" />



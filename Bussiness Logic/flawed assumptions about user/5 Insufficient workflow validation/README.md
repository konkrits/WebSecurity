# LAB 5 Insufficient workflow validation

## Brief:

 Laboratorium ini membuat asumsi yang keliru tentang urutan peristiwa dalam alur kerja pembelian.
	
akun: wiener:peter

## Tujuan:
	
Manfaatkan kelemahan ini untuk membeli jaket kulit “Lightweight l33t”.

<img width="1920" height="1080" alt="brief" src="https://github.com/user-attachments/assets/a012f489-20c8-4ea6-bf85-768fef8f8299" />

## Analisa:

### step awal adalah mengetahui bagaimana workflow pembeliaan di lab ini

1. login ke akun
	
<img width="1920" height="1080" alt="1 login ke akun" src="https://github.com/user-attachments/assets/18f9475b-d4b3-453b-b306-7cccb3acd5ae" />

2. pilih produk lalu klik ke keranjangkan dan kirim request nya ke repeater

> POST /cart 
	
<img width="1920" height="1080" alt="2 post produk keranjang" src="https://github.com/user-attachments/assets/3742be66-18f5-4579-ab27-bdf75996729a" />

3. ke laman keranjang dam kirim request nya ke repeater

> GET /cart

<img width="1920" height="1080" alt="3 laman keranjang" src="https://github.com/user-attachments/assets/df11e777-8bac-419b-91a1-8e413f60e651" />

4. intercept checkout produk dan kirim request checkoutnya ke repeater

> POST /cart/checkout	

<img width="1920" height="1080" alt="4 request checkout" src="https://github.com/user-attachments/assets/5cfe2480-aca4-4a6c-8c28-8b8bb72d4d04" />

5. intercept masih nyala, setelahnya ada request konfirmasi order lalu kirim ke repeater

> GET /cart/order-confirmation?order-confirmed=true

<img width="1920" height="1080" alt="5 request konfirmasi" src="https://github.com/user-attachments/assets/699007f4-4b73-4a49-b4c0-810a54fbf0b0" />

### jadi workflownya adalah

- pelanggan menambahkan ke keranjang dengan request
> POST /cart 
- lalu untuk mencheckout ada request
> POST /cart/checkout
- setelah itu ada request konfirmasi
> GET /cart/order-confirmation?order-confirmed=true

Bagimana jadinya kalo kita tidak mengchecout dan membayar dulu akan tetapi langsung mengkonfirmasi orderan?	

6. ke request POST untuk menambahkan produk yang tadi di repeater 

ini untuk menambahkan produk

<img width="1920" height="1080" alt="6 repeater request tmabh" src="https://github.com/user-attachments/assets/4cbbb2ef-e87a-4ff0-bfdc-ed55a4d26094" />

7. lalu ke request konfirmasi order dan kirim request dan ini berhasil, kita berhasil menskip pembelian dan langsung ke konfirmasi

dan kita telah menemukan kerentannya jadi step akhir adalah membeli produk yang dituju tanpa pembayaran

<img width="1920" height="1080" alt="7 req konfir berhasil" src="https://github.com/user-attachments/assets/bff52a0f-ac68-43e7-a1e8-0879b8819773" />

8. tambahkan produk ke keranjang

<img width="1920" height="1080" alt="8 jaket ke keranjang" src="https://github.com/user-attachments/assets/d633cc01-8784-45a0-8aaf-4667b0d975ec" />

9. kirim rquest konfirmasi dan berhasil

<img width="1920" height="1080" alt="9 berhasil" src="https://github.com/user-attachments/assets/d6944ecc-d5b6-40ca-bc48-ac2d6dbab3c5" />

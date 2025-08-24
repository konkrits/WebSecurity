# LAB 1 Flawed enforcement of business rules

## Brief:

lab ini cacat logika dalam pembelian produk.

> akun: wiener:peter

## Tujuan:
beli produk 'Lightweight leet jacket' dengan harga tidak wajar

  <img width="1919" height="1075" alt="brief" src="https://github.com/user-attachments/assets/e590583d-0271-4c55-acf8-d7fd893f4d37" />

## Analisa:
lab ini memakai fitur diskon tetapi terdapat kerentanan di fitur itu
	ketika memakain kode kupon yang sama 2 kali lab menampilkan pesan error bahwa kupon duplikat
	tetapi ketika memakai kupon beda dan memakainya secara berurutan lab tidak memvalidasi ini

### Contoh: 

> kupon = SIGNUP30 | dipakai secara dua kali -> error
> 
> kupon = NEWCUST5 | dipakai secara selang seling -> aman

dan itulah kerentannya

### Percobaan:

A. laman account.png
   <img width="1919" height="1078" alt="A laman account" src="https://github.com/user-attachments/assets/dd932911-3549-41ee-87ae-c06e548e64ab" />

B. produk ke cart.png
   <img width="1919" height="1079" alt="B produk ke cart" src="https://github.com/user-attachments/assets/f5691513-325a-4943-85d2-d8ab5f33af85" />

C. dicount kupon.png
   <img width="1916" height="1079" alt="C dicount kupon" src="https://github.com/user-attachments/assets/07047a40-dd52-482e-b5b9-6f21f5bdd90a" />

D. new coupon.png
   <img width="1919" height="1073" alt="d new coupon" src="https://github.com/user-attachments/assets/a5a22cbc-c9d9-44d3-8122-03ed6e7fc727" />

E. coupun code.png
   <img width="1919" height="1079" alt="E coupun code" src="https://github.com/user-attachments/assets/1ad2d020-1ef9-4b5e-8367-99f74f45bffb" />

F. add new coupun.png
   <img width="1919" height="1079" alt="F add new coupun" src="https://github.com/user-attachments/assets/71c9f9ae-6f5a-41fb-8010-47a834f3e7ca" />

G. kupon sama error.png
   <img width="1919" height="1079" alt="G kupon sama error" src="https://github.com/user-attachments/assets/2c4e94ee-277e-4336-be32-911654cc4894" />

H. kupon sama diseling.png
   <img width="1920" height="1080" alt="H kupon sama diseling" src="https://github.com/user-attachments/assets/a003aa3f-9339-4875-8ea4-794b8c58a5b2" />

I. kupon sama harga miring.png
   <img width="1919" height="1079" alt="I kupon sama harga miring" src="https://github.com/user-attachments/assets/6cc2d929-8f9e-47f5-9dea-3b19f982194a" />

J. beli dan berhasil.png  
   <img width="1918" height="1079" alt="J beli dan berhasil" src="https://github.com/user-attachments/assets/313b2fc7-e6db-4cdc-9383-0eaee0116271" />

dan itulah kerentannya

### Exploit
1. pilih produk yang dituju dan masukan ke keranjang

  <img width="1920" height="1080" alt="1 produk ke keranjang" src="https://github.com/user-attachments/assets/bb7f2e40-be48-4cef-a837-f1e9d89565a1" />

2. masukan berselingan 2 kupon hingga harga menjadi tidak wajar

  <img width="1919" height="1079" alt="2 seling demgam 2 kupon" src="https://github.com/user-attachments/assets/cf5a03b2-4a8f-42d2-a366-7fb98b04a425" />

3. berhasil

  <img width="1919" height="1079" alt="3 beli dan berhasil" src="https://github.com/user-attachments/assets/f81264bc-6339-4e2e-a007-f337597a3909" />

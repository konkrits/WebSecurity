# LAB 3 Reflected XSS into attribute with angle brackets HTML-encoded

## Brief:
pencarian dimana angle bracket adalah html encode

## Tujuan:
lakukan alert()
	
<img width="1920" height="1080" alt="1" src="https://github.com/user-attachments/assets/7776d698-0576-40f3-be1b-950bb123273c" />

## Analisa:
1. masukan nomor random dan cari diresponse nya dan nomor itu dimasukan di " " attributed
	
<img width="1920" height="1080" alt="1" src="https://github.com/user-attachments/assets/a161fd4d-8b06-4e66-88ec-dc4c266d9c11" />

2. sekarang masukan payload "onmouseover="alert(1) untuk mengescape " "
	
<img width="1922" height="1046" alt="2" src="https://github.com/user-attachments/assets/a39d5f04-710a-4fb1-9cfc-e51e061b4528" />

3. verifikasi dengan menggerakan mouse ke url copy dan paste lagi

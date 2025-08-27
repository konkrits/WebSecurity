# LAB Stored XSS into anchor href attribute with double quotes HTML-encoded

## Brief:
kerentanan di komen
	
## Tujuan:
alert()
	
<img width="1922" height="1046" alt="brief" src="https://github.com/user-attachments/assets/c80088b2-cb30-482d-91bb-9af1769fcfe2" />

## Analisa:

1. kirim nomor random di kolom "web"
	

2. di response ada nomor tersebut ada di tag href="nomor"
	
<img width="1920" height="1080" alt="3" src="https://github.com/user-attachments/assets/02b7127c-5aa2-43a5-aa59-5bce8d889958" />

3. ulangi proses tapi dengan payload:

        javascript:alert(1)
	
<img width="1922" height="1046" alt="4" src="https://github.com/user-attachments/assets/d4cbac4c-5215-413a-af7e-9f8612736feb" />

4. klik nama pengguna untuk meng alert()

<img width="1922" height="1046" alt="4" src="https://github.com/user-attachments/assets/d4cbac4c-5215-413a-af7e-9f8612736feb" />

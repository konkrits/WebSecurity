# LAB Reflected XSS into HTML context with all tags blocked except custom ones

## brief:
semua tag html di lab ini di block kecuali yang satu dikustom
	
## Tujuan:
lakukan alert(document.cookie) otomatis
	
<img width="1920" height="1080" alt="brief" src="https://github.com/user-attachments/assets/6453bedc-c384-4681-bd2d-4d825027ee57" />

## Analisa:

1. pergi ke exploit server
	 location =

       'https://YOUR-LAB-ID.web-security-academy.net/?search=<xss+id=x+onfocus=alert(document.cookie) tabindex=1>#x';
	
Injeksi ini menciptakan tag khusus dengan ID x, yang berisi penanganan event onfocus yang memicu fungsi alert. 
Hash di akhir URL berfokus pada elemen ini segera setelah halaman dimuat, menyebabkan payload peringatan dipanggil.
		
<img width="1920" height="1080" alt="1" src="https://github.com/user-attachments/assets/7bf4f0d0-3dd7-4379-9061-70960357027b" />

2. klik store dan lihat
	
<img width="1920" height="1080" alt="2" src="https://github.com/user-attachments/assets/d1d3a4f9-598d-427e-aa92-58d7486b6104" />

3. berhasil
	
<img width="1920" height="1080" alt="3" src="https://github.com/user-attachments/assets/1f01d861-c883-4485-835e-951ea16948fb" />

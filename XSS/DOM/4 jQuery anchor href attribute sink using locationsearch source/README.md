# LAB 4 jQuery anchor href attribute sink using location.search source

## Brief:
Laboratorium ini berisi kerentanan scripting lintas situs berbasis DOM di halaman umpan balik submit. Ini menggunakan fungsi pemilih $ library jQuery untuk menemukan elemen anchor, 
	dan mengubah atribut href menggunakan data dari location.search.

## Tujuan:
membuat "back" link alert document.cookie.

<img width="1922" height="1046" alt="brief" src="https://github.com/user-attachments/assets/fca81fb2-87be-4ea8-9cb0-628cfb6af4f9" />
	
## Analisa:

1. di url tambahkan nomor acak 

> returnPATH/12123122123
	
<img width="1922" height="1046" alt="1 di url ganti path str" src="https://github.com/user-attachments/assets/e1210c49-dac0-4c5e-a963-5023a10d1386" />

2. konfirmasi dengan inspect dan cari nomor acaknya
	
<img width="1922" height="1046" alt="2 konfir inspect href" src="https://github.com/user-attachments/assets/588753b1-8b22-486e-b6f4-f2ebe729756e" />

3. sekarang masukan payload di url 

> returnPATH/javascript:alert(document.cookie)
	
> ini menyebabkan tombol kembali ketika di klik menampilkan alert(document.cookie)
	
<img width="1922" height="1046" alt="3 payload" src="https://github.com/user-attachments/assets/91e7ea46-774b-40cc-a7d2-c358c2f186fb" />

4. klik kembali dan berhasil 

<img width="1922" height="1046" alt="4 klik tombol kembali" src="https://github.com/user-attachments/assets/93271ec5-d631-4cd5-8fee-092bd6890b23" />

> 
<img width="1922" height="1046" alt="berhasil" src="https://github.com/user-attachments/assets/5383735d-2419-4348-8957-960e28ea185a" />






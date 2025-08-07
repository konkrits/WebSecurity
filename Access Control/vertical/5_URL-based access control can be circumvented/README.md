# LAB 5 URL-based access control can be circumvented

## Brief:
###	panel admin _/admin_, framework backend support X-Original-URL, akses diluar diblok

## Tujuan:
###	akses panel admin hapus carlos
<img width="1922" height="1046" alt="brief" src="https://github.com/user-attachments/assets/b06e1ef8-2d3c-44eb-ad72-e797c0fc4d12" />
	
## Analisa:
###	1. akses panel admin dan ternyata diblok.
###		tapi response nya di plain text biasa mungkin ini berasal dari front-end
<img width="1022" height="1032" alt="1_akses_sebagai_biasa" src="https://github.com/user-attachments/assets/fa65c5bb-feb0-40ec-b2b3-7aca35777915" />

###	2. ubah request url nya jadi / dan tambahkan X-Original-URL: /invalid
###		setelah dikirim jadi not found ini menginditifikasi back end memproses X-Original-URL
<img width="1022" height="1032" alt="2_invalid_notfound" src="https://github.com/user-attachments/assets/2d3102f5-c828-436b-b195-b1b39789d781" />

###	3. ubah X-Original-URL: /admin dan muncul panelnya
<img width="1022" height="1032" alt="3_ubah_x_original_admin" src="https://github.com/user-attachments/assets/cfc42c10-7d91-4be1-b908-dfe368fd65c5" />

##	kita sudah berhasil mengakses panel admin dan untuk menghapus carlos sebagai berikut:
	
###	4. ubah X-Original-URL: /admin/delete dan request querynya jadi /?username=carlos.
###		endpoin untuk menghapus carlos di /admin/delete?username=carlos
<img width="1920" height="1044" alt="4_ubah_query" src="https://github.com/user-attachments/assets/d725a6fb-d44c-41fb-8c5d-c1f1ec19e5b9" />
	
###	5. berhasil
###		meskipun statusnya forbidden tapi ketika merefresh dibrowser sudah solve dan carlos sudah tidak ada.
<img width="1022" height="1032" alt="5_berhasil" src="https://github.com/user-attachments/assets/bb116c70-6a8c-4bfc-a86b-3fbe15239a8e" />

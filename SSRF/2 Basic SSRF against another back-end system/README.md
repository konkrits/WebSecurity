# LAB 2 Basic SSRF against another back-end system

## Brief:

Lab ini rentan ssrf di check stock
<img width="1922" height="1046" alt="brief" src="https://github.com/user-attachments/assets/9dbe21e0-ddba-411a-96b5-237038022aa6" />
	
## Tujuan:
	
scan 192.168.0.x dengan port 8080 untuk menghapus carlos
	
## Analisa:

1. check stok produk dan intercept lalu kirim ke intruder
<img width="1920" height="1080" alt="1 check stok inter" src="https://github.com/user-attachments/assets/68d3c15a-9d83-42cf-98b2-eb3ce22c1bab" />
	
2. di intruder di stockapi ganti jadi http://192.168.0.x/admin lalu tambahkan posisi di octet terakhir dan di payload gunakan nomor 1 ke 255
<img width="1920" height="1044" alt="2 set payload" src="https://github.com/user-attachments/assets/4be42899-2ebe-4506-b8b5-e2dc06ad71b7" />

3. jika status 200 berhasil kemudian kirim ke repeater
<img width="1920" height="1044" alt="3 status 200 berhasil" src="https://github.com/user-attachments/assets/5cb97019-0caa-4219-b841-997ea99752d6" />
	
4. di response repeater cari carlos dan masukan ke isi stockAPI kemudian kirim
<img width="1920" height="1044" alt="4 isi dengan carlos" src="https://github.com/user-attachments/assets/3300d93a-3691-441f-9f8e-ba0da760bcee" />
	
5. berhasil
<img width="1920" height="1080" alt="5 berhasil" src="https://github.com/user-attachments/assets/db987729-8a9d-446a-9796-d74ba87c7e04" />



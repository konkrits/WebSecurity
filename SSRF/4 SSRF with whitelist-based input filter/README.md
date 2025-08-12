# LAB 4 SSRF with whitelist-based input filter

## Brief:
lab ini memfetch fitur stok cek dari internal sistem

<img width="1920" height="1032" alt="LAB4" src="https://github.com/user-attachments/assets/77a67ac8-fea1-475e-810c-aa7915dc0edc" />

## Tujuan:
akses admin panel dan hapus carlos

## Analisa:

1. cek stok kirim ke repeater
	
2. coba dengan localhost,coba dengan loopback
	
tetapi keduanya diresponse dengan harus berasal dari hostname yang sama
<img width="1920" height="1044" alt="2" src="https://github.com/user-attachments/assets/101b3e79-0bf6-488d-a96c-cbd4c8cf742b" />
		
3. coba tambahkan 

        username@stock.welietoshop.net/ 

dan ini diterima dan mengindikasikan bahwaurl parse mensupport embeded kredensial
<img width="1920" height="1044" alt="3" src="https://github.com/user-attachments/assets/edffc484-a789-471f-ac48-b3ac1e241967" />

 
4. tambahkan char # di username dan sekarang jadi bad request dan ditolak
<img width="1920" height="1044" alt="4" src="https://github.com/user-attachments/assets/233d0368-8995-4b27-ba5b-9770379508a1" />
	
5. double url encoded #

        http://username%25%32%33@stock.weliketoshop.net/ 

dan ini internal server error, mengindikasikan server mencoba menghubgi 'username'
<img width="1920" height="1044" alt="5" src="https://github.com/user-attachments/assets/74299963-b206-49fb-a4be-d5961f572a06" />
		
6. sekarang ganti hostname nya jadi localhost dan akses admin panel dan ini berhasil
		
        http://localhost:80%2523@stock.weliketoshop.net/admin
<img width="1920" height="1044" alt="6" src="https://github.com/user-attachments/assets/aca5b102-56a1-403e-bdc5-2f972bf82ff0" />
	
7. cari carlos di response dan tambahkan endpointnya
<img width="1920" height="1044" alt="7" src="https://github.com/user-attachments/assets/d7dc8ba4-dbdd-4419-9b21-2992e149e6f2" />

8. berhasil
<img width="1920" height="1044" alt="8" src="https://github.com/user-attachments/assets/212cee6d-6c15-47d7-bfe3-7758c70a4861" />

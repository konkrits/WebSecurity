# LAB 3 SSRF with blacklist-based input filter

## Brief:

Lab ini memfetch stok dengan internal sistem
	
## Tujuan:
	
akses 

    http://localhost/admin 
    
untuk menghapus carlos
	
## Analisa:

1. check stok dan intercept kirim ke repeater
<img width="1920" height="1080" alt="1 cek stok dan inter" src="https://github.com/user-attachments/assets/9a406e6c-030b-4af9-a52d-1be027cce425" />
	
2. kita coba dengan localhost dan 127.0.0.1 dan gagal
<img width="1920" height="1044" alt="2 coba localhost" src="https://github.com/user-attachments/assets/05363099-0cc8-4067-893e-93ebd64e4f01" />
	
3. coba dengan character 127.0.0.1 alternatif yaitu:  

        127.1, 2130706433, 017700000001

  tetap gagal
<img width="1920" height="1044" alt="3 dengan localhost beda tetap gagal" src="https://github.com/user-attachments/assets/14afa62a-5e35-4b3b-8f12-b3ce46814ef4" />

4. double encoding char a di admin jadi 

        http://127.1/%25%36%31dmin dan bisa
<img width="1920" height="1044" alt="4 double encoding char A dan bisa" src="https://github.com/user-attachments/assets/3d0a9997-331b-4d96-8e1d-a3201eba21e0" />
	
5. cari carlos dan hapus
<img width="1920" height="1044" alt="5 cari carlos dan hapus" src="https://github.com/user-attachments/assets/f0849215-a3b5-477f-b14c-5a085f1141f4" />
	
6. berhasil
<img width="1920" height="1044" alt="6 berhasil" src="https://github.com/user-attachments/assets/2514d59f-8f43-4d96-9aa8-0d879b197f00" />

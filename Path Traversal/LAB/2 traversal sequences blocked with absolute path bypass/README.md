# LAB traversal sequences blocked with absolute path bypass

## Brief:
vulnerable di image produk, web memblokir jalur .. / tetapi memberlakukan relatif dengan nama direktori default
	
## Tujuan:
dapatkan file /etc/passwd

<img width="1922" height="1046" alt="brief" src="https://github.com/user-attachments/assets/0de9a0ad-d379-485a-9a31-e71dc94cd3d9" />
	
## Analisa:

1. dapatkan request kirim ke repeater
<img width="1920" height="1080" alt="1 kirim request" src="https://github.com/user-attachments/assets/d327d4be-4c8e-4a97-9a5e-522f6bd74ebe" />
	
2. coba dengan ../../../etc/passwd
		dan ternyata gagal ini dikaranakan .. diblokir

<img width="1920" height="1044" alt="2 coba" src="https://github.com/user-attachments/assets/2bfa8c78-1eaf-4ceb-849f-5d48c79f44cd" />
	
3. coba dengan jalur langsung /etc/passwd dan berhasil
	
<img width="1920" height="1080" alt="3 jalur absolute" src="https://github.com/user-attachments/assets/4c9c139a-5eec-43be-8a63-1f3a5c2bdd17" />
	
	
	
	
	
	
	
	
	
	
	
	
	

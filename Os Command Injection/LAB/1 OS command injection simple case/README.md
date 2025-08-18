# LAB 1 OS command injection, simple case

## brief:
os command injection di produk stok
<img width="1922" height="1046" alt="Brief" src="https://github.com/user-attachments/assets/68ca31af-91a5-4eb0-87fd-904a538f1d0a" />
	
## Tujuan:
eksekusi perintah whoami
	
## Analisa:

1. pergi ke laman produk
<img width="1922" height="1046" alt="1 pergi ke produk" src="https://github.com/user-attachments/assets/a5def95a-e407-4d99-a856-11bd2c6bb26b" />
	
2. klik stok produk dan intercept
<img width="1920" height="1080" alt="2 intercept" src="https://github.com/user-attachments/assets/3d6e6de3-9dd2-4d14-acbc-e8f8e97b2b24" />
	
3. pada paramater produkid=2 berika |whoami -> produkid=2|whoami
<img width="1920" height="1080" alt="3 payload whoami" src="https://github.com/user-attachments/assets/0aa10f9a-829c-472c-ad48-d89c381f70f6" />
	
4. berhasil
<img width="1920" height="1080" alt="4 berhasil" src="https://github.com/user-attachments/assets/bee082a6-084f-416c-9411-d72a33cacea3" />


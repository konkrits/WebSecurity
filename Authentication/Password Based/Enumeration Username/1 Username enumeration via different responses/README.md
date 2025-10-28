# LAB1 Username enumeration via different responses

## Brief:
vulnerable terhadap username enumeration dan brute force
	
## Tujuan:
enumerate username dan brute force untuk login

<img width="900" height="614" alt="brief" src="https://github.com/user-attachments/assets/6b436838-86c4-41a0-a674-dc90d3953c9d" />
	
## Analisa:

1. kirim POST /login ke intruder
	
<img width="1920" height="1044" alt="1_kirim_intruder" src="https://github.com/user-attachments/assets/f30e79f1-19a6-4a43-8f67-2b75ce99959d" />


2. higliht username dan tambahkan posisi kemudian isikan list username
	
<img width="1920" height="1044" alt="2_set_posisi" src="https://github.com/user-attachments/assets/5a2d7901-fc55-40ce-acba-f417b77dbef2" />


3. start attack dan nanti ada satu username yang response nya beda
> disaat username yang salah response 3248 dan mendisplay invalid username dan ketika username yang benar lenght response nya 3250 dan mendisplay incorrect password
		
<img width="1749" height="960" alt="3_beda_lenght" src="https://github.com/user-attachments/assets/19df9693-672d-4697-8422-08e4364e734a" />


4. isi username dengan username nomor 3 tambahkan posisi ke password dan tempel list password dan start attack
	
<img width="1920" height="1044" alt="4_set_password" src="https://github.com/user-attachments/assets/aabfc711-1a1e-441c-befe-a8a053441aaf" />


5. ketika password benar nanti ada status code 302 dan butuh redirect dan
	
<img width="1749" height="960" alt="5_redirect" src="https://github.com/user-attachments/assets/6bb14681-51fb-4135-96f1-8b573dd7aeb2" />


6. login aja. BERHASIL
	
<img width="1922" height="1046" alt="5_login_berhasil" src="https://github.com/user-attachments/assets/871093a4-7577-4316-bd33-6ffe5f4beb5d" />
	

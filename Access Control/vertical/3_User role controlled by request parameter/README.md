# LAB 3 User role controlled by request parameter

## Brief:
###	admin panel di /admin dan cookie bisa dipalsukan

## Tujuan:
###	akses panel admin dan hapus carlos
<img width="1922" height="1046" alt="brief" src="https://github.com/user-attachments/assets/cfd2074d-8296-4cff-940c-b33417c4ee31" />
	
## Analisa:
###	1. pergi ke admin panel dan ternyata harus jadi admin dulu
<img width="1922" height="1046" alt="1_pergi_ke_admin" src="https://github.com/user-attachments/assets/21d2c43c-6a95-4990-8eae-28bf4101cd06" />

###	2. sekarang pergi ke panel admin sebaigai user dan diburp request dibagian cookie tertulis admin;false
<img width="1920" height="1044" alt="2_sebagia_user_ke_admin_panel" src="https://github.com/user-attachments/assets/81a02df5-6059-480f-b9ec-0a49b03e0564" />

###	3. coba ubah jadi true dan ternyata bisa.
<img width="1920" height="1044" alt="3_ganti_true" src="https://github.com/user-attachments/assets/402f158d-a30d-453a-beaa-46d5c408cc18" />

###	4. di response cari end point yang menghapus carlos dan kirim direquest
<img width="1920" height="1044" alt="4_cari_endpoin" src="https://github.com/user-attachments/assets/4447d3c7-45d4-4dc6-b6d8-9f32c379621c" />

###	5. ikuti redirectnya dan berhasil 
<img width="1920" height="1044" alt="5_kirim_dan_berhasil" src="https://github.com/user-attachments/assets/177652b5-db4d-4102-ba5a-2f2d9005690f" />

# LAB 2 Weak isolation on dual-use endpoint

## Brief:
lab ini membuat asumsi yang cacat tentang tingkat hak istimewa pengguna berdasarkan input mereka. 
Akibatnya, Anda dapat memanfaatkan logika fitur manajemen akunnya untuk mendapatkan akses ke akun pengguna yang sewenang-wenang.
	
> akun penyerang wiener:peter

## Tujuan:
akses akun admin dan hapus carlos

<img width="1920" height="985" alt="brief" src="https://github.com/user-attachments/assets/0d2f2dcf-c43f-4644-aafe-cda150cbd1f2" />

## Analisa:

step pertama login dan mengetest dengan akun wiener
	
1. pergi ke /admin dan hanya bisa diakses oleh administrator
	
<img width="1920" height="1080" alt="1 dir admin" src="https://github.com/user-attachments/assets/5ea171b4-bc21-4a8e-9936-31b67026e95b" />

2. login ke akun wiener
	
<img width="1920" height="985" alt="2 laman login" src="https://github.com/user-attachments/assets/c7d774fc-0ce1-4983-97c2-843e2a9d6a42" />

3. di laman my account ada fitur ganti password yang berisi 3 kolom
	
yaitu: 

> current-password=
> 
> new-password=
>
> confirm-new-password=
		       
ketiga kolom tersebut harus diisi dibrowser tapi apa jadinya jika kita menghapus parameter current-password dan langsung mengisi password baru?
	
<img width="1920" height="1080" alt="3 laman myaccount" src="https://github.com/user-attachments/assets/2b12e756-2ad2-40db-9494-4a9f1f3f8ac8" />

4. ini adalah parameter current-password atau password saat ini
	
> jika kita bisa menghapus ini otomatis tidak perlu mengisi password saat ini dan membypass ke password baru
		
<img width="1920" height="1080" alt="4 paramenter cur passw" src="https://github.com/user-attachments/assets/8d634d25-0138-4390-aa95-14c9bf37ae58" />

5. hapus parameter lalu kirim request
	
<img width="1920" height="1080" alt="5 hapus parameter" src="https://github.com/user-attachments/assets/2ae99331-659b-43f6-a930-0237cf99aeaf" />

6. dan ini berhasil otomatis akun wiener langsung diganti passwordnya tanpa perlu mengetahui password sebelumnya
	
> tentu secara teori kita bisa mengakses akun mana saja termasuk administrator
>		
> step berikutnya ganti password akun administrator
	
<img width="1920" height="1080" alt="6 pass diganti" src="https://github.com/user-attachments/assets/70375f85-3774-45d7-a127-c0356c3fd692" />

7. ganti username ke administrator dan isi ketiga kolom
	
<img width="1920" height="1080" alt="7 admin pass ganti" src="https://github.com/user-attachments/assets/d18c9a0e-35db-46e0-a4b4-696fb40f93c8" />

8. hapus parameter current-password atau password saat ini
	
<img width="1920" height="1080" alt="8 parameter cur hapus" src="https://github.com/user-attachments/assets/2285cf79-b392-4aee-9dc6-b34305eb1fbd" />

9. akun administrator passwordnya telah diganti
	
<img width="1920" height="1080" alt="9 password admin dganti" src="https://github.com/user-attachments/assets/af2081b0-747e-41d9-b937-c2e3809ba17e" />

10. login ke akun administrator menggunakan password baru
	
<img width="1920" height="1080" alt="10 akun admin" src="https://github.com/user-attachments/assets/75a1de26-6be6-4946-b27f-ec162d2aa449" />

11. ini adalah panel admin lalu delete akun carlos
	
<img width="1920" height="1080" alt="11 panel admin" src="https://github.com/user-attachments/assets/b63cd4ab-ac44-4f6e-833f-8cba00669afe" />

12. berhasil

<img width="1920" height="1080" alt="12 berhasil" src="https://github.com/user-attachments/assets/927b0bb9-819c-41ae-be50-48d84f24f705" />

	
Kesimpulan:
	
	kita tidak memerlukan password untuk mengganti ke password baru dan ini menyebabkan kita bisa mengganti password akun mana saja.

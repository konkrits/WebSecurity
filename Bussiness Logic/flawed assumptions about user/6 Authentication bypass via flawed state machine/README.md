# Lab 6: Authentication bypass via flawed state machine

## Brief:

Laboratorium ini membuat asumsi yang keliru tentang urutan peristiwa dalam proses login.

akun: wiener:peter

## Tujuan:
Lewati proses autentikasi, akses panel admin, dan hapus user Carlos.

<img width="1920" height="1080" alt="Lab" src="https://github.com/user-attachments/assets/ea2053e9-0195-458b-bac1-84de6ba1bdd8" />

## Analisa:
### step awal mengetahui dulu workflow loginnya

A. intercept nyala dan login ke akun wiener

> requestnya: POST /login

<img width="1915" height="1072" alt="A login" src="https://github.com/user-attachments/assets/614eb3d6-e343-4f62-8131-09651f6283bd" />

B. setelah itu ada request memilih role akun

> requestnya: GET /role-selector

<img width="1916" height="1079" alt="B role selector" src="https://github.com/user-attachments/assets/9f9cf3f5-f760-428c-8ad8-4e7063a3f9ca" />

C. pilih salah satu lalu kirim requestnya

> requestnya POST /role-selector

<img width="1919" height="1079" alt="C post selector" src="https://github.com/user-attachments/assets/8efb2e47-abf7-4e8a-8fd9-605f01667a2d" />

D. lalu user masuk ke akun

<img width="1915" height="672" alt="D my account" src="https://github.com/user-attachments/assets/83fd0d2f-5ec0-4e5e-8e6c-00745e840905" />

### jadi workflownya

- user login dengan request: 		
> POST /login

- laman role akun dengan request:
> GET /role-selector

- user memilih role akun dengan request:
> POST /role-selector

- lalu user login

	seletah dicoba untuk melewati request GET role dan Post role user tidak login dan tidak work
	dicoba dengan mengisi diparameter dengan role=admin atau role=administrator hasilnya sama.

### Exploitasi:

0. pergi ke /admin dan hanya bisa diakses oleh administrator

<img width="1914" height="1076" alt="0 admin dir" src="https://github.com/user-attachments/assets/4bf084c1-7f86-45a3-ace1-be7a9e81e188" />

1. intercept login

<img width="1915" height="1079" alt="1 intercept login" src="https://github.com/user-attachments/assets/491b281b-c453-403b-bc61-b0a0e9e8dd69" />

2. kita coba mendrop request GET selector-role

<img width="1908" height="1079" alt="2 drop get selector" src="https://github.com/user-attachments/assets/7fb8665b-a457-4a59-bff6-84eb44c0bce8" />

3. setelah di drop

<img width="1915" height="1076" alt="3 setelah di drop" src="https://github.com/user-attachments/assets/34caceb4-f19c-4c77-8bf6-61a8126b99ad" />

4. langsung ke GET / atau home atau di url /

<img width="1915" height="1078" alt="4 pergi ke home" src="https://github.com/user-attachments/assets/81559845-7b8d-4e55-8696-78402c27b997" />

5. dan boom kita jadi administrator dan ada panel admin

<img width="1911" height="1076" alt="5 dihome ada admin" src="https://github.com/user-attachments/assets/c76dd404-6584-4253-9711-a547ce9f31a9" />

6. pergi ke panel admin

<img width="1915" height="1079" alt="6 panel admin" src="https://github.com/user-attachments/assets/81ca2a54-72dd-4b22-a739-e27e54cc9f95" />

7. hapus carlos dan berhasil

<img width="1915" height="1079" alt="7 hapus carlos berhasil" src="https://github.com/user-attachments/assets/aff42fe8-85cf-4dba-a19b-f448221259f6" />
	
kerentanan ini mungkin terjadi karena request di drop di bagian selector role dan situs web tidak tahu cara menghandle ini.

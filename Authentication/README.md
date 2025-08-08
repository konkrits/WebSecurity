# Authentication vulnerabilities

##### Secara konseptual, kerentanan otentik mudah dimengerti. Namun, mereka biasanya kritis karena hubungan yang jelas antara otentikasi dan keamanan.

#####	Kerentanan otentikasi dapat memungkinkan penyerang untuk mendapatkan akses ke data dan fungsionalitas sensitif. Mereka juga mengekspos permukaan serangan tambahan untuk eksploitasi lebih lanjut. 
#####	Untuk alasan ini, penting untuk mempelajari cara mengidentifikasi dan mengeksploitasi kerentanan otentikasi, dan cara melewati langkah-langkah perlindungan umum.

## - Di bagian ini, kami menjelaskan:

- Mekanisme otentikasi yang paling umum digunakan oleh situs web.
- Potensi kerentanan dalam mekanisme ini.
- Kerentanan yang melekat pada mekanisme otentikasi yang berbeda.
- Kerentanan khas yang diperkenalkan oleh implementasi yang tidak tepat.
- Bagaimana Anda dapat membuat mekanisme otentikasi Anda sendiri sekuat mungkin.

## - What is authentication?

#####	Otentikasi adalah proses verifikasi identitas pengguna atau klien. Situs web berpotensi terkena siapa saja yang terhubung ke internet. 
#####	Ini membuat mekanisme otentikasi yang kuat menjadi bagian integral dari keamanan web yang efektif.

## - Ada tiga jenis utama otentikasi:

- Sesuatu yang Anda ketahui, seperti kata sandi atau jawaban untuk pertanyaan keamanan. Ini kadang-kadang disebut "faktor pengetahuan".
- Sesuatu yang Anda miliki, ini adalah objek fisik seperti ponsel atau token keamanan. Ini kadang-kadang disebut "faktor kepemilikan".
- Sesuatu yang Anda lakukan atau lakukan. Misalnya, biometrik atau pola perilaku Anda. Ini kadang-kadang disebut "faktor inherensi".
	    
## - What is the difference between authentication and authorization?

##### Otentikasi adalah proses verifikasi bahwa pengguna adalah siapa yang mereka klaim. Otorisasi melibatkan verifikasi apakah pengguna diperbolehkan melakukan sesuatu.

#####		Misalnya, 
		
#####    otentikasi menentukan apakah seseorang yang mencoba mengakses situs web dengan nama pengguna Carlos123 
#####    benar-benar adalah orang yang sama yang membuat akun.

##### Setelah Carlos123 diautentikasi, izin mereka menentukan apa yang mereka berwenang untuk melakukan. 

##### Misalnya, 

#####    mereka mungkin berwenang untuk mengakses informasi pribadi tentang pengguna lain, 
#####    atau melakukan tindakan seperti menghapus akun pengguna lain.
		
## - How do authentication vulnerabilities arise?

#####	Sebagian besar kerentanan dalam mekanisme otentikasi terjadi dalam 
##### salah satu dari dua cara:

- Mekanisme otentikasi lemah karena gagal melindungi secara memadai terhadap serangan brute-force.
- Kelemahan logika atau pengkodean yang buruk dalam implementasi memungkinkan mekanisme otentikasi untuk dilewati sepenuhnya oleh penyerang.
  Hal ini kadang-kadang disebut "arkenasi otentikasi yang rusak".

#####	Di banyak bidang pengembangan web, kelemahan logika menyebabkan situs web berperilaku tak terduga, yang mungkin atau mungkin bukan masalah keamanan. 
#####	Namun, karena otentikasi sangat penting bagi keamanan, sangat mungkin bahwa logika otentikasi yang cacat mengekspos situs web untuk masalah keamanan.
	
## - What is the impact of vulnerable authentication?

#####	Dampak kerentanan otentikasi bisa sangat parah. 

 - Jika penyerang melewati otentikasi atau brute-forces jalan mereka ke akun pengguna lain, mereka memiliki akses ke semua data dan fungsi yang dimiliki akun yang dikompromikan. 
	
-	Jika mereka mampu berkompromi dengan akun berprivilegungan tinggi, seperti administrator sistem, mereka dapat mengambil kendali penuh atas seluruh aplikasi dan berpotensi mendapatkan akses ke infrastruktur internal.

-	Bahkan mengorbankan akun berpritasi rendah mungkin masih memberikan akses penyerang ke data yang seharusnya tidak mereka miliki, 
		seperti informasi bisnis yang sensitif secara komersial. 

-	Bahkan jika akun tidak memiliki akses ke data sensitif, itu mungkin masih memungkinkan penyerang untuk mengakses halaman tambahan, yang menyediakan permukaan serangan lebih lanjut. 

#####	Seringkali, serangan tingkat tinggi tidak mungkin dilakukan dari halaman yang dapat diakses publik, tetapi mereka mungkin mungkin dari halaman internal.	
	
## - Vulnerabilities in authentication mechanisms

#####	Sistem otentikasi situs web biasanya terdiri dari beberapa mekanisme berbeda di mana kerentanan dapat terjadi. Beberapa kerentanan berlaku di semua konteks ini. Yang lain lebih spesifik untuk fungsi yang disediakan.

#####	- Kami akan melihat lebih dekat pada beberapa kerentanan yang paling umum di bidang-bidang berikut:	
	
- Vulnerabilities in password-based login 		(LABS)
- Vulnerabilities in multi-factor authentication 	(LABS)
- Vulnerabilities in other authentication mechanisms  (LABS)

# How to secure your authentication mechanisms

##### Otentikasi adalah topik yang kompleks dan, seperti yang telah kami tunjukkan, sayangnya terlalu mudah untuk kelemahan dan kekurangan untuk merayap masuk. 
##### Menguraikan setiap tindakan yang dapat Anda ambil untuk melindungi situs web Anda sendiri jelas tidak mungkin. Namun, ada beberapa prinsip umum yang harus selalu Anda ikuti.

##	1.) Take care with user credentials

#####		Bahkan mekanisme otentikasi yang paling kuat tidak efektif jika Anda tanpa disadari mengungkapkan serangkaian kredensial login yang valid kepada penyerang. 
#####		Ini harus pergi tanpa mengatakan bahwa Anda tidak boleh mengirim data login melalui koneksi yang tidak terenkripsi. Meskipun Anda mungkin telah menerapkan HTTPS untuk permintaan login Anda, 
#####		pastikan Anda menerapkannya dengan mengalihkan permintaan HTTP yang dicoba ke HTTPS juga.

#####		Anda juga harus mengaudit situs web Anda untuk memastikan bahwa tidak ada nama pengguna atau alamat email yang diungkapkan baik melalui profil yang dapat diakses publik atau tercermin dalam tanggapan HTTP.

##	2.) Don't count on users for security
	
#####		 Langkah-langkah autentikasi yang ketat sering kali membutuhkan upaya tambahan dari pengguna Anda. Sifat manusia membuat semua itu tidak dapat dihindari, 
#####		 tetapi beberapa pengguna akan menemukan cara untuk menyelamatkan diri dari upaya ini. Oleh karena itu, Anda perlu menerapkan perilaku aman sedapat mungkin.

#####		Contoh yang paling jelas adalah menerapkan kebijakan kata sandi yang efektif. Beberapa kebijakan yang lebih tradisional gagal karena orang-orang memasukkan kata sandi yang mudah ditebak ke dalam kebijakan tersebut. 
#####		Sebaliknya, akan lebih efektif jika menerapkan semacam pemeriksa kata sandi sederhana, yang memungkinkan pengguna bereksperimen dengan kata sandi dan memberikan umpan balik tentang kekuatannya secara real time. 
#####		Contoh yang populer adalah pustaka JavaScript zxcvbn, yang dikembangkan oleh Dropbox. Dengan hanya mengizinkan kata sandi yang dinilai tinggi oleh pemeriksa kata sandi, 
#####		Anda bisa menegakkan penggunaan kata sandi yang aman secara lebih efektif daripada yang bisa dilakukan dengan kebijakan tradisional.
	
##	3.) Prevent username enumeration
	
#####		Akan jauh lebih mudah bagi penyerang untuk membobol mekanisme autentikasi Anda jika Anda mengungkapkan bahwa seorang pengguna ada dalam sistem. Bahkan ada beberapa situasi tertentu di mana, 
#####		karena sifat situs web, pengetahuan bahwa seseorang memiliki akun merupakan informasi yang sensitif.

#####		Terlepas dari apakah nama pengguna yang dicoba itu valid, penting untuk menggunakan pesan kesalahan umum yang identik, dan memastikan bahwa pesan tersebut benar-benar identik. 
#####		Anda harus selalu mengembalikan kode status HTTP yang sama dengan setiap permintaan login dan, terakhir, buatlah waktu respons dalam skenario yang berbeda sebisa mungkin tidak dapat dibedakan.

##	4.) Implement robust brute-force protection
	
#####		Mengingat betapa sederhananya membangun serangan brute-force, sangat penting untuk memastikan bahwa Anda mengambil langkah-langkah untuk mencegah, 
#####		atau setidaknya mengganggu, setiap upaya untuk melakukan login brute-force.

#####		Salah satu metode yang lebih efektif adalah menerapkan pembatasan tarif pengguna berbasis IP yang ketat. Ini harus melibatkan langkah-langkah untuk mencegah penyerang memanipulasi alamat IP mereka yang jelas.
#####		Idealnya, Anda harus meminta pengguna untuk menyelesaikan tes CAPTCHA dengan setiap upaya login setelah batas tertentu tercapai.

##	5.) Triple-check your verification logic
	
#####		Seperti yang ditunjukkan oleh laboratorium kami, mudah bagi kelemahan logika sederhana untuk merayap ke dalam kode yang, dalam kasus otentikasi, 
#####		memiliki potensi untuk sepenuhnya mengkompromikan situs web dan pengguna Anda. Mengaudit verifikasi atau logika validasi secara menyeluruh untuk menghilangkan kekurangan 
#####		adalah benar-benar kunci untuk otentikasi yang kuat. Cek yang dapat dilewati, pada akhirnya, tidak jauh lebih baik daripada tidak memeriksa sama sekali.

##	6.) Jangan lupa fungsi tambahan
	
#####		Pastikan untuk tidak hanya fokus pada halaman login pusat dan mengabaikan fungsi tambahan yang terkait dengan otentikasi. 
#####		Hal ini sangat penting dalam kasus di mana penyerang bebas untuk mendaftarkan akun mereka sendiri dan mengeksplorasi fungsi ini. 
#####		Ingat bahwa reset kata sandi atau perubahan sama validnya dengan permukaan serangan seperti mekanisme login utama dan, akibatnya, harus sama kuatnya. 

##	7.) Implement proper multi-factor authentication
	
#####		Sementara otentikasi multi-faktor mungkin tidak praktis untuk setiap situs web, ketika dilakukan dengan benar itu jauh lebih aman daripada login berbasis kata sandi saja. 
#####		Ingat bahwa memverifikasi beberapa contoh dari faktor yang sama bukanlah otentikasi multi-faktor yang benar. 
#####		Mengirim kode verifikasi melalui email pada dasarnya hanya bentuk otentikasi faktor tunggal yang lebih bertele-tele.

#####		2FA berbasis SMS secara teknis memverifikasi dua faktor (sesuatu yang Anda ketahui dan sesuatu yang Anda miliki). 
#####		Namun, potensi penyalahgunaan melalui pertukaran SIM, misalnya, berarti bahwa sistem ini tidak dapat diandalkan.

#####		Idealnya, 2FA harus diimplementasikan menggunakan perangkat atau aplikasi khusus yang menghasilkan kode verifikasi secara langsung. Karena mereka dibangun untuk memberikan keamanan, ini biasanya lebih aman.

#####		Akhirnya, sama seperti dengan logika otentikasi utama, pastikan bahwa logika dalam cek 2FA Anda adalah suara sehingga tidak dapat dengan mudah dilewati.
	
	
	
	
	
	
	
	
	
	
	
	
	
	

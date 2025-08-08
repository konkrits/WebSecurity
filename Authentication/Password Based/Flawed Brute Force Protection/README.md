## Flawed Brute-force Protection

### (LAB 1 Broken brute-force protection, IP block)

Sangat mungkin bahwa serangan brute-force akan melibatkan banyak tebakan yang gagal sebelum penyerang berhasil mengkompromikan akun. 
Logikanya, perlindungan brute-force berputar di sekitar mencoba membuatnya sesulit mungkin untuk mengotomatisasi proses dan memperlambat tingkat di mana penyerang dapat mencoba login.

##### Dua cara yang paling umum untuk mencegah serangan brute-force adalah:

- Mengunci akun yang pengguna jarak jauh coba akses jika mereka melakukan terlalu banyak upaya login yang gagal.
- Memblokir alamat IP pengguna jarak jauh jika mereka melakukan terlalu banyak upaya login secara berurutan

Kedua pendekatan menawarkan berbagai tingkat perlindungan, tetapi tidak dapat secara kekebalan, terutama jika diterapkan menggunakan logika yang cacat.

Misalnya, Anda mungkin kadang-kadang menemukan bahwa IP Anda diblokir jika Anda gagal masuk terlalu sering. 

Dalam beberapa implementasi, 
counter untuk jumlah upaya gagal diatur ulang jika pemilik IP login berhasil. Ini berarti penyerang hanya harus masuk ke akun mereka sendiri setiap beberapa upaya untuk mencegah batas ini tercapai.

Dalam hal ini, hanya memasukkan kredensial login Anda sendiri secara berkala sepanjang daftar kata sudah cukup untuk membuat pertahanan ini hampir tidak berguna.

##	Account locking
  	
###  (LAB 2 Username enumeration via account lock)

Salah satu cara di mana situs web mencoba untuk mencegah brute-forcecing adalah dengan mengunci akun jika kriteria mencurigakan tertentu terpenuhi, 
biasanya sejumlah upaya login yang gagal. Sama seperti kesalahan login normal, tanggapan dari server yang menunjukkan bahwa akun terkunci juga dapat membantu penyerang untuk menyebutkan nama pengguna.
	
##### Misalnya, metode berikut dapat digunakan untuk bekerja di sekitar perlindungan semacam ini:
		
- Tetapkan daftar nama pengguna kandidat yang mungkin valid. 
			
     Ini bisa melalui pencacahan nama pengguna atau hanya berdasarkan daftar nama pengguna umum.
				
- Putuskan daftar kata sandi yang sangat kecil yang menurut Anda mungkin dimiliki setidaknya satu pengguna. 
			
     Yang terpenting,
     jumlah kata sandi yang Anda pilih tidak boleh melebihi jumlah upaya login yang diizinkan. 
     Misalnya, jika Anda telah menghitung batas itu adalah 3 upaya, Anda harus memilih maksimal 3 tebakan kata sandi.
				
- Menggunakan alat seperti Burp Intruder, 
			
     cobalah masing-masing password yang dipilih dengan masing-masing nama pengguna kandidat. 
     Dengan cara ini, Anda dapat mencoba untuk brute-force setiap akun tanpa memicu kunci akun. 
     Anda hanya perlu satu pengguna untuk menggunakan salah satu dari tiga password untuk mengkompromikan akun.

##### Pemblokiran akun juga tidak dapat melindungi dari serangan credential stuffing. 

Serangan ini melibatkan penggunaan dictionary berisi pasangan nama 

    username:password 
    
yang terdiri dari kredensial login asli yang dicuri dalam kebocoran data. 
		
Serangan credential stuffing memanfaatkan fakta bahwa banyak orang menggunakan kembali nama pengguna dan kata sandi yang sama di berbagai situs web, 
sehingga ada kemungkinan beberapa kredensial yang terkompromi dalam kamus tersebut juga valid di situs web target. 
		
Penguncian akun tidak melindungi dari serangan credential stuffing karena setiap nama pengguna hanya dicoba sekali. 
Serangan credential stuffing sangat berbahaya karena kadang-kadang dapat mengakibatkan penyerang mengkompromikan banyak akun berbeda dengan hanya satu serangan otomatis.

##	User rate limiting
	
Cara lain situs web mencoba untuk mencegah serangan brute-force adalah melalui pembatasan tingkat pengguna. 
Dalam hal ini, membuat terlalu banyak permintaan login dalam waktu singkat menyebabkan alamat IP Anda diblokir. 
		
##### Biasanya, IP hanya dapat dibuka dengan salah satu cara berikut:
					
 - Automatically after a certain period of time has elapsed
 - Manually by an administrator
 - Manually by the user after successfully completing a CAPTCHA

user rate limiting terkadang lebih disukai daripada penguncian akun karena kurang rentan terhadap username enumeration dan denial of service 
Namun, itu masih belum sepenuhnya aman. Seperti yang kita lihat contoh di laboratorium sebelumnya, 
ada beberapa cara penyerang dapat memanipulasi IP mereka yang jelas untuk melewati blok.
	
Karena batas ini didasarkan pada laju permintaan HTTP yang dikirim dari alamat IP pengguna, terkadang juga dimungkinkan untuk membypass pertahanan ini 
jika Anda dapat menemukan cara untuk menebak beberapa kata sandi dengan satu permintaan.

##	HTTP basic authentication

Meskipun cukup tua, kesederhanaan dan kemudahan implementasinya yang relatif berarti Anda terkadang melihat otentikasi dasar HTTP digunakan. 
Dalam otentikasi dasar HTTP, klien menerima token otentikasi dari server, yang dibangun dengan rangko nama pengguna dan kata sandi, dan mengkodekannya di Base64. 
Token ini disimpan dan dikelola oleh browser, yang secara otomatis menambahkannya ke header Authorization dari setiap permintaan berikutnya sebagai berikut:

    Authorization: Basic base64(username:password)

Untuk sejumlah alasan, ini umumnya tidak dianggap sebagai metode otentikasi yang aman. 
Pertama, ini melibatkan berulang kali mengirim kredensial login pengguna dengan setiap permintaan. 
Kecuali situs web juga menerapkan HTSS, kredensial pengguna terbuka untuk ditangkap dalam serangan man-in-the-middle.

Selain itu, implementasi otentikasi dasar HTTP sering tidak mendukung perlindungan brute-force. Karena token terdiri secara eksklusif dari nilai statis, ini dapat membuatnya rentan menjadi brute-forced.

Otentikasi dasar HTTP juga sangat rentan terhadap eksploitasi terkait sesi, terutama CSRF, yang tidak menawarkan perlindungan sendiri.

Dalam beberapa kasus, mengeksploitasi otentikasi dasar HTTP yang rentan mungkin hanya memberikan akses penyerang ke halaman yang tampaknya tidak menarik. 
Namun, selain menyediakan permukaan serangan lebih lanjut, kredensial yang terpapar dengan cara ini dapat digunakan kembali dalam konteks lain yang lebih rahasia.

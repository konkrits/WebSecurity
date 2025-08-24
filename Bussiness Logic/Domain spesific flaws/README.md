# Kekurangan khusus di ruang tertentu

> LAB 1 Flawed enforcement of business rules
> 
> LAB 2 Infinite money logic flaw

Dalam banyak kasus, Anda akan menemui kelemahan logika yang spesifik untuk domain bisnis atau tujuan situs web.

Fungsi diskon pada toko online merupakan area serangan klasik saat mencari kelemahan logika. 
		
Ini bisa menjadi sumber potensi yang menguntungkan bagi penyerang, 
		dengan berbagai kelemahan logika dasar yang terjadi dalam cara diskon diterapkan.

Misalnya, pertimbangkan sebuah toko online yang menawarkan diskon 10% untuk pesanan di atas $1000. 

Hal ini dapat rentan disalahgunakan jika logika bisnis gagal memeriksa apakah pesanan diubah setelah diskon diterapkan. 
	
Dalam kasus ini, penyerang dapat menambahkan barang ke keranjang belanja hingga mencapai ambang batas $1000, lalu menghapus barang yang tidak diinginkan sebelum memesan. 
	
Mereka akan menerima diskon pada pesanan mereka meskipun pesanan tersebut tidak lagi memenuhi kriteria yang dimaksud.

Anda harus memperhatikan dengan cermat situasi di mana harga atau nilai sensitif lainnya disesuaikan berdasarkan kriteria yang ditentukan oleh tindakan pengguna. 
	
	
Cobalah untuk memahami algoritma apa yang digunakan aplikasi untuk melakukan penyesuaian ini dan pada titik mana penyesuaian tersebut dilakukan. 
	
Hal ini sering melibatkan manipulasi aplikasi sehingga berada dalam keadaan di mana penyesuaian yang diterapkan tidak sesuai dengan kriteria asli yang dimaksudkan oleh pengembang.

Untuk mengidentifikasi kerentanan ini, Anda perlu mempertimbangkan dengan cermat tujuan apa yang mungkin dimiliki oleh penyerang dan mencoba menemukan berbagai cara untuk mencapainya menggunakan fungsi yang disediakan. 
	
Hal ini mungkin memerlukan tingkat pengetahuan khusus bidang tertentu agar dapat memahami apa yang mungkin menguntungkan dalam konteks tertentu. 
	
Sebagai contoh sederhana, Anda perlu memahami media sosial untuk memahami manfaat memaksa sejumlah besar pengguna untuk mengikuti Anda.

Tanpa pengetahuan domain ini, Anda mungkin mengabaikan perilaku berbahaya karena Anda tidak menyadari dampaknya yang berpotensi merugikan. 
	
Demikian pula, Anda mungkin kesulitan menghubungkan titik-titik dan menyadari bagaimana dua fungsi dapat digabungkan dengan cara yang merugikan. 
	
Untuk kesederhanaan, contoh yang digunakan dalam topik ini spesifik untuk domain yang sudah familiar bagi semua pengguna, yaitu toko online. 

Namun, apakah Anda sedang berburu bug, melakukan pengujian penetrasi, atau bahkan hanya seorang pengembang yang berusaha menulis kode yang lebih aman, 
	Anda mungkin pada suatu saat akan menemui aplikasi dari bidang yang kurang familiar. Dalam hal ini, Anda sebaiknya membaca sebanyak mungkin dokumentasi dan, 
	jika tersedia, berbicara dengan ahli bidang tersebut untuk mendapatkan wawasan mereka. 

Meskipun terdengar seperti banyak pekerjaan, semakin tidak familiar bidangnya, semakin besar kemungkinan penguji lain telah melewatkan banyak bug.

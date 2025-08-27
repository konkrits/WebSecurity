# DOM-based XSS

## Apa itu scripting lintas situs berbasis DOM?
Kerentanan XSS berbasis DOM biasanya muncul ketika JavaScript mengambil data dari sumber yang dapat dikontrol penyerang, seperti URL, dan meneruskannya ke wastafel yang mendukung eksekusi kode dinamis, seperti eval() atau innerHTML. Hal ini memungkinkan penyerang mengeksekusi JavaScript berbahaya, yang biasanya memungkinkan mereka membajak akun pengguna lain.

Untuk mengirimkan serangan XSS berbasis DOM, Anda perlu menempatkan data ke dalam sumber sehingga disebarkan ke wastafel dan menyebabkan eksekusi JavaScript sewenang-wenang.

Sumber paling umum untuk DOM XSS adalah URL, yang biasanya diakses dengan window.location object. Penyerang dapat membuat tautan untuk mengirim korban ke halaman rentan dengan muatan di string kueri dan bagian fragmen URL. Dalam keadaan tertentu, seperti ketika menargetkan halaman 404 atau situs web yang menjalankan PHP, payload juga dapat ditempatkan di jalur.

Untuk penjelasan rinci tentang aliran noda antara sumber dan penyerap, silakan merujuk ke Kerentanan berbasis DOM page.
## Menguji sink HTML

Untuk menguji DOM XSS dalam sink HTML, letakkan string alfanumerik acak ke dalam sumber (seperti location.search), lalu gunakan developer tool untuk memeriksa HTML 
	dan menemukan di mana string Anda muncul. Perhatikan bahwa opsi “Lihat sumber” pada browser tidak akan berfungsi untuk pengujian DOM XSS karena opsi ini tidak memperhitungkan perubahan 
	yang telah dilakukan pada HTML oleh JavaScript. Di alat pengembang Chrome, Anda dapat menggunakan Control+F (atau Command+F di MacOS) untuk mencari DOM untuk string Anda.

Untuk setiap lokasi di mana string Anda muncul di dalam DOM, Anda perlu mengidentifikasi konteksnya. 
	Berdasarkan konteks ini, Anda perlu menyempurnakan input Anda untuk melihat bagaimana input tersebut diproses. 
	Sebagai contoh, jika string Anda muncul dalam atribut dengan tanda kutip ganda, cobalah untuk menyuntikkan tanda kutip ganda pada string Anda untuk melihat apakah Anda dapat keluar dari atribut tersebut.

Perhatikan bahwa peramban berperilaku berbeda dalam hal pengodean URL, Chrome, Firefox, dan Safari akan meng-encode URL location.search dan location.hash, 
	sementara IE11 dan Microsoft Edge (pra-Chromium) tidak akan meng-encode URL sumber-sumber ini. Jika data Anda di-encode URL sebelum diproses, maka serangan XSS tidak mungkin berhasil.

## Menguji sink eksekusi JavaScript

Menguji sink eksekusi JavaScript untuk XSS berbasis DOM sedikit lebih sulit. Dengan sink ini, input Anda tidak selalu muncul di mana pun di dalam DOM, sehingga Anda tidak dapat mencarinya. 
	Sebagai gantinya, Anda harus menggunakan debugger JavaScript untuk menentukan apakah dan bagaimana input Anda dikirim ke sink.

Untuk setiap sumber potensial, seperti lokasi, pertama-tama Anda harus menemukan kasus di dalam kode JavaScript halaman di mana sumber tersebut direferensikan. 
	Di alat pengembang Chrome, Anda dapat menggunakan Control+Shift+F (atau Command+Alt+F di MacOS) untuk mencari semua kode JavaScript halaman yang menjadi sumbernya.

Setelah Anda menemukan di mana sumbernya dibaca, Anda dapat menggunakan debugger JavaScript untuk menambahkan titik jeda dan mengikuti bagaimana nilai sumber tersebut digunakan. 
	Anda mungkin menemukan bahwa sumber tersebut ditugaskan ke variabel lain. 
	Jika ini yang terjadi, Anda harus menggunakan fungsi pencarian lagi untuk melacak variabel-variabel tersebut dan melihat apakah variabel-variabel tersebut diteruskan ke sink. 
	Ketika Anda menemukan sink yang diberi data yang berasal dari sumber, Anda dapat menggunakan debugger untuk memeriksa nilainya dengan mengarahkan kursor ke variabel untuk menampilkan nilainya sebelum dikirim ke sink. 
	Kemudian, seperti halnya dengan HTML sink, Anda perlu menyempurnakan masukan Anda untuk melihat apakah Anda dapat mengirimkan serangan XSS yang berhasil.

## Menguji DOM XSS menggunakan DOM Invader
Mengidentifikasi dan mengeksploitasi DOM XSS di alam liar bisa menjadi proses yang membosankan, sering kali mengharuskan Anda menjaring JavaScript yang rumit dan diperkecil secara manual. Jika Anda menggunakan browser Burp, bagaimanapun, Anda dapat memanfaatkan ekstensi DOM Invader bawaannya, yang melakukan banyak kerja keras untuk Anda.

https://portswigger.net/burp/documentation/desktop/tools/dom-invader

## Mengidentifikasi dan mengeksploitasi DOM XSS 

di alam bebas bisa menjadi proses yang membosankan, sering kali mengharuskan Anda untuk menelusuri secara manual JavaScript yang rumit dan diperkecil. 
	Namun, jika Anda menggunakan peramban Burp, Anda bisa memanfaatkan ekstensi DOM Invader bawaannya, yang melakukan banyak kerja keras untuk Anda.
 
## Memanfaatkan DOM XSS dengan sumber dan sink yang berbeda
 
> LAB 1 document.write sink using source location.search
> 
> https://github.com/konkrits/WebSecurity/tree/main/XSS/DOM/1%20documentwrite%20sink%20using%20source%20locationsearch
>  
Pada prinsipnya, sebuah situs web rentan terhadap skrip lintas situs berbasis DOM jika ada jalur yang dapat dieksekusi di mana data dapat menyebar dari sumber ke sink. 
	  Pada praktiknya, sumber dan sink yang berbeda memiliki sifat dan perilaku yang berbeda yang dapat memengaruhi kemampuan eksploitasi, dan menentukan teknik apa yang diperlukan. 
	  Selain itu, skrip situs web mungkin melakukan validasi atau pemrosesan data lainnya yang harus diakomodasi saat mencoba mengeksploitasi kerentanan. 
	  Ada berbagai sink yang relevan dengan kerentanan berbasis DOM. Silakan lihat daftar di bawah ini untuk detailnya.

Sink document.write bekerja dengan elemen skrip, sehingga Anda dapat menggunakan muatan sederhana, seperti yang ada di bawah ini:
	 
	document.write('... <script>alert(document.domain)</script> ...');
	 	
> LAB 2 document.write sink using source location.search inside a select element
> 
> https://github.com/konkrits/WebSecurity/tree/main/XSS/DOM/2%20documentwrite%20sink%20using%20source%20locationsearch%20inside%20a%20select%20element
 	 	
Perhatikan, bagaimanapun, bahwa dalam beberapa situasi konten yang ditulis untuk mendokumentasikan. menulis mencakup beberapa konteks di sekitarnya yang perlu Anda perhitungkan dalam eksploitasi Anda. 
 	Misalnya, Anda mungkin perlu menutup beberapa elemen yang ada sebelum menggunakan muatan JavaScript Anda.
 
> LAB 3 innerHTML sink using source location.search
> 
> https://github.com/konkrits/WebSecurity/tree/main/XSS/DOM/3%20innerHTML%20sink%20using%20source%20locationsearch
 
Sink innerHTML tidak menerima elemen skrip pada peramban modern mana pun, dan juga tidak akan menjalankan event svg onload. 
  	Ini berarti Anda harus menggunakan elemen alternatif seperti img atau iframe. Penangan peristiwa seperti onload dan onerror dapat digunakan bersama dengan elemen-elemen ini. Sebagai contoh:

	element.innerHTML='... <img src=1 onerror=alert(document.domain)> ...'
 
## Sources and sinks in third-party dependencies 

> LAB 4 jQuery anchor href attribute sink using location.search source
> 
> https://github.com/konkrits/WebSecurity/tree/main/XSS/DOM/4%20jQuery%20anchor%20href%20attribute%20sink%20using%20locationsearch%20source

Aplikasi web modern biasanya dibangun menggunakan sejumlah pustaka dan kerangka kerja pihak ketiga, 
	yang seringkali menyediakan fungsi dan kapabilitas tambahan bagi pengembang. Penting untuk diingat bahwa beberapa di antaranya juga merupakan sumber dan sink potensial untuk DOM XSS.

## DOM XSS di jQuery

Jika pustaka JavaScript seperti jQuery digunakan, perhatikan sink yang dapat mengubah elemen DOM di halaman.
	Misalnya, fungsi attr() jQuery dapat mengubah atribut elemen DOM. Jika data dibaca dari sumber yang dikontrol pengguna seperti URL, 
	lalu diteruskan ke fungsi attr(), maka dimungkinkan untuk memanipulasi nilai yang dikirim untuk menyebabkan XSS. 
	Misalnya, di sini kita memiliki beberapa JavaScript yang mengubah atribut href elemen jangkar menggunakan data dari URL:

	$(function() {
	$('#backLink').attr("href",(new URLSearchParams(window.location.search)).get('returnUrl'));
	});

Anda dapat memanfaatkan ini dengan memodifikasi URL sehingga sumber location.search berisi URL JavaScript berbahaya. 
	Setelah JavaScript halaman menerapkan URL berbahaya ini ke href tautan balik, mengeklik tautan balik akan mengeksekusinya:

	?returnUrl=javascript:alert(document.domain)

> LAB 5  jQuery selector sink using a hashchange event
> 
> https://github.com/konkrits/WebSecurity/tree/main/XSS/DOM/5%20%20jQuery%20selector%20sink%20using%20a%20hashchange%20event
 
Sink potensial lain yang perlu diwaspadai adalah fungsi pemilih $() milik jQuery, yang dapat digunakan untuk menyuntikkan objek berbahaya ke dalam DOM.

jQuery dulunya sangat populer, dan kerentanan DOM XSS klasik disebabkan oleh situs web yang menggunakan pemilih ini bersama dengan sumber location.hash untuk animasi
	atau pengguliran otomatis ke elemen tertentu pada halaman. Perilaku ini sering diimplementasikan menggunakan penangan peristiwa perubahan hash yang rentan, 

mirip dengan yang berikut ini:

	$(window).on('hashchange', function() {
	var element = $(location.hash);
	element[0].scrollIntoView();
	});

Karena hash dapat dikontrol oleh pengguna, penyerang dapat menggunakan ini untuk menyuntikkan vektor XSS ke dalam sink pemilih $(). 
	Versi jQuery yang lebih baru telah menambal kerentanan khusus ini dengan mencegah Anda menyuntikkan HTML ke dalam selektor ketika input dimulai dengan karakter hash (#). 
	Namun, Anda mungkin masih menemukan kode yang rentan di alam liar.

Untuk benar-benar mengeksploitasi kerentanan klasik ini, Anda harus menemukan cara untuk memicu peristiwa perubahan hash tanpa interaksi pengguna.

salah satu cara paling sederhana untuk melakukannya adalah dengan mengirimkan eksploitasi melalui iframe:

	<iframe src="https://vulnerable-website.com#" onload="this.src+=‘<img src=1 onerror=alert(1)>’">

Dalam contoh ini, atribut src mengarah ke halaman yang rentan dengan nilai hash kosong. Ketika iframe dimuat, vektor XSS ditambahkan ke hash, sehingga menyebabkan peristiwa perubahan hash terjadi.
	
Catatan:

> Bahkan versi jQuery yang lebih baru pun masih bisa rentan melalui selector sink $(), asalkan Anda memiliki kontrol penuh atas inputnya dari sumber yang tidak memerlukan awalan #.

## DOM XSS dalam AngularJS

> LAB 6 DOM XSS in AngularJS expression with angle brackets and double quotes HTML-encoded
> 
> https://github.com/konkrits/WebSecurity/tree/main/XSS/DOM/6%20AngularJS%20expression%20with%20angle%20brackets%20and%20double%20quotes%20HTML-encoded

Jika kerangka kerja seperti AngularJS digunakan, dimungkinkan untuk mengeksekusi JavaScript tanpa kurung sudut atau peristiwa. 
	Ketika sebuah situs menggunakan atribut ng-app pada elemen HTML, itu akan diproses oleh AngularJS. Dalam hal ini, 
	AngularJS akan mengeksekusi JavaScript di dalam double curly braces yang dapat terjadi langsung dalam atribut HTML atau di dalam.

## DOM XSS combined with reflected and stored data

> LAB 7 Reflected DOM XSS
> 
> https://github.com/konkrits/WebSecurity/tree/main/XSS/DOM/7%20Reflected%20DOM%20XSS

Beberapa kerentanan berbasis DOM murni bersifat mandiri dalam satu halaman. Jika skrip membaca data dari URL dan menuliskannya ke sink berbahaya, 
	 maka kerentanan tersebut sepenuhnya berada di sisi klien.

Namun, sumber data tidak terbatas pada data yang secara langsung diekspos oleh browser—mereka juga dapat berasal dari situs web itu sendiri. 
	 Misalnya, situs web sering kali mencerminkan parameter URL dalam respons HTML dari server. Hal ini umumnya dikaitkan dengan XSS biasa, tetapi juga dapat menyebabkan kerentanan DOM XSS yang direfleksikan.

Dalam kerentanan DOM XSS yang direfleksikan, server memproses data dari permintaan dan memantulkan data tersebut ke dalam respons. 
	Data yang direfleksikan mungkin ditempatkan dalam literal string JavaScript atau item data dalam DOM, seperti bidang formulir. 
	Skrip di halaman kemudian memproses data yang direfleksikan dengan cara yang tidak aman, akhirnya menuliskannya ke dalam “sink” yang berbahaya.

	eval('var data = "reflected string"');

> LAB 8 Stored DOM XSS
> 
> https://github.com/konkrits/WebSecurity/tree/main/XSS/DOM/8%20Stored%20DOM

Situs web juga dapat menyimpan data di server dan menampilkannya di tempat lain. Dalam kerentanan XSS DOM yang disimpan, server menerima data dari satu permintaan, menyimpannya, 
 dan kemudian menyertakan data tersebut dalam respons berikutnya. Skrip dalam respons berikutnya mengandung sink yang kemudian memproses data tersebut dengan cara yang tidak aman.
 
	element.innerHTML = comment.author

















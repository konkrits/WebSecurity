# LAB 11 Reflected XSS in a JavaScript URL with some characters blocked


## Brief:
situs mereflected diurl ini tampak sepele tapi aplikasi memblokir beberapa karakter untuk mencegah Xss

## Tujuan:
lakukan alert() dengan isi string 1337 di alert()

<img width="1920" height="1032" alt="Brief" src="https://github.com/user-attachments/assets/1b1e1977-f47c-4adf-be27-532f14b4eb3a" />

## Analisa:
	
> Exploit ini menggunakan exception handling untuk memanggil fungsi alert dengan argumen. 

> Pernyataan throw digunakan, dipisahkan dengan komentar kosong untuk menghindari batasan tidak boleh ada spasi. 

> Fungsi alert ditugaskan ke exception handling onerror.

> Karena `throw` adalah pernyataan, ia tidak dapat digunakan sebagai ekspresi. 

> Sebagai gantinya, kita perlu menggunakan fungsi arrow untuk membuat blok sehingga pernyataan `throw` dapat digunakan. 

> Kita kemudian perlu memanggil fungsi ini, jadi kita menugaskan fungsi tersebut ke properti `toString` dari objek `window` dan memicu fungsi ini dengan memaksa konversi string pada objek `window`.

## Exploit:

### 1. ketik javascript sederhana di url

<img width="1920" height="1032" alt="1 refleksi di url" src="https://github.com/user-attachments/assets/44d31384-3b94-4c83-9ec5-9da801bf9689" />

### 2. kunjungi url berikut:

`https://YOUR-LAB-ID.web-security-academy.net/post?postId=5&%27},x=x=%3E{throw/**/onerror=alert,1337},toString=x,window%2b%27%27,{x:%27`

### - postId=5

#### Fungsi: 
Parameter ini biasanya digunakan untuk mengidentifikasi pos tertentu dalam aplikasi web. Dalam konteks sistem manajemen konten (CMS), ini bisa merujuk pada artikel, posting blog, atau entri data lainnya.

#### Risiko: 
Jika tidak divalidasi dengan baik, parameter ini dapat menjadi target serangan injeksi SQL, di mana penyerang mencoba memanipulasi query database untuk mendapatkan akses tidak sah.

### - %27

#### Deskripsi: 
Ini adalah representasi URL-encoded dari karakter ' (tanda kutip tunggal).
    			
#### Fungsi: 
Tanda kutip tunggal sering digunakan dalam konteks pemrograman untuk menandai string. Dalam serangan injeksi, penyerang dapat menggunakan karakter ini untuk menutup string yang valid dan menyisipkan kode berbahaya.
    
#### Risiko: 
Penggunaan karakter ini dapat mengindikasikan upaya untuk memanipulasi query atau menyisipkan skrip berbahaya.

### - x=x=%3E{throw//onerror=alert,1337}**

#### Deskripsi: 
`x=x` Ini tampaknya merupakan penugasan variabel, meskipun tidak ada konteks lebih lanjut tentang apa yang dimaksud dengan x.

`%3E` Ini adalah representasi URL-encoded dari karakter >, yang sering digunakan dalam konteks pemrograman untuk menunjukkan akhir dari suatu pernyataan atau blok kode.
        
`{throw/**/onerror=alert,1337}` Ini adalah objek JavaScript yang berisi instruksi untuk menangani kesalahan.
            
`throw` Menyebabkan kesalahan yang disengaja.
            
`onerror` Ini adalah event handler yang akan dipicu ketika terjadi kesalahan dalam eksekusi JavaScript.          

`alert,1337` Jika terjadi kesalahan, fungsi alert akan dipanggil dengan argumen 1337, yang akan menampilkan pop-up di browser pengguna.
    
#### Risiko: 
Ini adalah teknik umum dalam serangan XSS, di mana penyerang mencoba untuk mengeksekusi kode JavaScript di dalam konteks browser pengguna.

### - toString=x

##### Deskripsi: 
Ini tampaknya mencoba untuk menetapkan nilai x ke metode toString dari objek tertentu.

#### Fungsi: 
Dalam JavaScript, toString adalah metode yang mengembalikan representasi string dari objek. 
Mengubah perilaku metode ini dapat memungkinkan penyerang untuk mengontrol bagaimana objek ditampilkan atau diproses.
    
#### Risiko: 
Jika penyerang dapat mengubah metode ini, mereka dapat menyisipkan kode berbahaya yang akan dieksekusi saat objek tersebut dipanggil.

### - window%2b%27%27

#### Deskripsi: 

`window` Ini adalah objek global di JavaScript yang merepresentasikan jendela browser.
        
`%2b` Ini adalah representasi URL-encoded dari karakter +, yang digunakan untuk menggabungkan string.
        
`''` Ini adalah string kosong.
    
#### Fungsi: 
Menggunakan objek window dalam konteks ini dapat menunjukkan bahwa penyerang mencoba untuk mengakses atau memanipulasi konteks global di dalam browser.
    
#### Risiko: 
Manipulasi objek window dapat memberikan penyerang akses ke berbagai fungsi dan data di dalam browser, yang dapat digunakan untuk melakukan tindakan berbahaya.

### - {x:%27

#### Deskripsi: 
Ini tampaknya merupakan bagian dari objek JavaScript yang sedang dibangun.
    
#### Fungsi: 
`x` menunjukkan bahwa ini adalah properti dari objek, dan `%27` adalah representasi URL-encoded dari karakter `'`.
    
#### Risiko: 
Ini dapat digunakan untuk menyisipkan lebih banyak kode berbahaya ke dalam objek, yang dapat dieksekusi di dalam konteks browser.

<img width="1920" height="1032" alt="2 masukan payload" src="https://github.com/user-attachments/assets/adfa6523-8cab-494b-b2bc-df37a822f2b7" />

### 3. klik back to blog untuk mengalert()

<img width="1920" height="1032" alt="3 tombol back to blog" src="https://github.com/user-attachments/assets/3c9e4b65-20a7-4d08-abb0-1bf1ef9d2eb3" />

### 4. berhasil alert

<img width="1920" height="1032" alt="4 berhasil alert" src="https://github.com/user-attachments/assets/2b87a53a-ef2e-46c3-bb82-c421957fde29" />


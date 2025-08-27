# LAb 7 reflected dom

## Brief
Laboratorium ini menunjukkan kerentanan DOM yang direfleksikan. Kerentanan DOM yang direfleksikan terjadi ketika aplikasi sisi server memproses data dari permintaan dan mengembalikan data tersebut dalam respons. 
	Skrip di halaman kemudian memproses data yang direfleksikan dengan cara yang tidak aman, dan pada akhirnya menulisnya ke tujuan yang berbahaya.

## Tujuan
gunakan alert()
	
<img width="1922" height="1046" alt="brief" src="https://github.com/user-attachments/assets/7dec45e1-848a-4a1e-93bb-e5be2c269d5f" />

## Analisa:

1. di pencarian ketikan string bebas
	
<img width="1922" height="1046" alt="1 string random" src="https://github.com/user-attachments/assets/17b6665b-2e6c-47f5-aca7-394f1f25bdda" />

2. string di reflected dengan json bernama search result
	
<img width="1920" height="1044" alt="2 json search" src="https://github.com/user-attachments/assets/8f4e5501-4268-4bf4-934e-bd87501be404" />

3. cari di site map searchresult.js dan lihat ada eval()
	
<img width="1920" height="1044" alt="3eval" src="https://github.com/user-attachments/assets/95694a9d-be6c-46e7-9785-c172a677f1e2" />

4. dengan mencoba berbagai string tanda kutip di escape tapi / tidak
	
<img width="1922" height="1046" alt="4payload" src="https://github.com/user-attachments/assets/a85220d0-7005-4aae-81b0-338cd6d76838" />

5. sekarang masukan ke pencarian \"-alert('XSS-By-Konkrits)}//
	
<img width="1922" height="1046" alt="5berhasil" src="https://github.com/user-attachments/assets/35799c03-9de0-459d-b212-c7fd66ee1e33" />

6. berhasil
	
   Karena Anda telah menyisipkan tanda backslash dan situs web tidak melakukan escaping terhadapnya, saat respons JSON mencoba melakukan escaping terhadap karakter tanda kutip ganda pembuka, 
		 ia menambahkan tanda backslash kedua. Tanda backslash ganda yang dihasilkan menyebabkan proses escaping menjadi tidak berlaku. Hal ini berarti tanda kutip ganda diproses tanpa escaping, 
		 yang mengakibatkan string yang seharusnya berisi kata kunci pencarian menjadi tertutup.

	Operator aritmatika (dalam hal ini operator pengurangan) kemudian digunakan untuk memisahkan ekspresi sebelum fungsi alert() dipanggil. 
		Akhirnya, kurung kurawal penutup dan dua tanda slash penutup menutup objek JSON secara prematur dan mengomentari sisa objek yang seharusnya ada. 
		Akibatnya, respons dihasilkan sebagai berikut:

       {“searchTerm”:“\\”-alert(1)}//“, ”results":[]}
	
	
	
	
	
	
	
	
	
	
	

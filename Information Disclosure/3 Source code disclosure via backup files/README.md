# Lab 3 Source code disclosure via backup files

## Brief:
lab ini membocorkan source codenya sendiri oleh backup file yang terdapat di directory tersembunyi
<img width="868" height="412" alt="lab" src="https://github.com/user-attachments/assets/e933b7f2-40c1-41bb-8b09-b7aea9e45aed" />
	
## Tujuan:
menemukan password database yang dikodekan via source cpde yang bocor

## analisa:
Pergi ke /robots.txt dan disana akan ada directory tersembunyi yaitu ProductTemplate.java.bak
<img width="1920" height="1080" alt="hiddenDirectory" src="https://github.com/user-attachments/assets/2155bfa0-bfb7-4a60-a4ec-2a0d822aab8f" />

Ini isi directory nya
<img width="1920" height="1080" alt="inside_Directory" src="https://github.com/user-attachments/assets/6e101c7f-3e6e-4c93-9ae2-dcfeea265f0e" />


masuk dan temukan passwordnya di line 41 di ConectionBuilder.from
<img width="1920" height="1080" alt="Got_it" src="https://github.com/user-attachments/assets/f8e0575b-7b53-424f-a284-f0c853e18da5" />

dan berhasil.

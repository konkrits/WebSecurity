# LAB 3 (LAB 3 innerHTML sink using source location.search)

## Brief: 
Laboratorium ini berisi kerentanan scripting cross-site berbasis DOM dalam fungsi blog pencarian. Ini menggunakan tugas innerHTML, yang mengubah isi HTML dari elemen div, menggunakan data dari location.search.

## Tujuan: lakukan alert(1)

<img width="1922" height="1046" alt="brief" src="https://github.com/user-attachments/assets/270c9036-c0a3-4588-9182-f120990d6fd3" />

## Analisa:

1. masukan payload ini: <img src=1 onerror=alert(12)> di pencarian
		
> ini akan menyebabkan img mencari file 1 dan pasti tidak ada, ketika tidak ada error akan menyebabkan alert()
	
<img width="1922" height="1046" alt="1 imgsrc onerror" src="https://github.com/user-attachments/assets/97650c21-4750-4119-a876-44cd9c4ce21f" />

2. berhasil

<img width="1922" height="1046" alt="2 berhasil" src="https://github.com/user-attachments/assets/d3b1892e-326a-41d1-9645-179b776d0dde" />

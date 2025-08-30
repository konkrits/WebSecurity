# Lab 12 Reflected XSS into a template literal with angle brackets, single, double quotes, backslash and backticks Unicode-escaped

## Brief:
reflected xss di fungsi pencarian blog. refleksi terjadi di dalam template string, <angle bracket>, 'tanda kutip satu' "tanda kutip dua" html encode dan backticks di escape `

## Tujuan:
lakukan alert() ketika didalam template string

<img width="1917" height="1033" alt="brief" src="https://github.com/user-attachments/assets/89f066e1-120c-40b3-a604-253c0ba61455" />

## Analisa:

#### 1. input nomor random dan direfleksi ke dalam string

<img width="1914" height="1025" alt="1 input nomor" src="https://github.com/user-attachments/assets/adf2afc6-a7a0-4361-8fb3-6b1a1ae99613" />

#### 2. masukan payload: 
> ${alert(ISI)}

<img width="1913" height="1024" alt="2 payload" src="https://github.com/user-attachments/assets/7db9e381-dd5e-4b42-bae7-bb5b8193484a" />

#### 3. payload berhasil

<img width="1919" height="1036" alt="3 alert proof" src="https://github.com/user-attachments/assets/7af74600-1daa-4565-be14-6b9f3cd3a239" />

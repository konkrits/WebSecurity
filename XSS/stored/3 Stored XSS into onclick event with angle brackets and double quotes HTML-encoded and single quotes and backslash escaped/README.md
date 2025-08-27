# LAB 3 Stored XSS into onclick event with angle brackets and double quotes HTML-encoded and single quotes and backslash escape

## Brief:
stored xss di komen

## Tujuan:
lakukan alert ketika mengklik nama pengguna

<img width="1920" height="1032" alt="Brief" src="https://github.com/user-attachments/assets/13b1a99a-4c86-4780-b974-5d231c27bfa8" />

## Analisa:

1. post komen dengan nomor di kolom web dan kirim ke repeater

<img width="1919" height="1079" alt="1 post komen nomor" src="https://github.com/user-attachments/assets/6e8d927f-6108-4d57-a3df-73d3a22ebe2d" />

2. GET post dan kirim ke repeater

<img width="1917" height="1028" alt="2 get postingan" src="https://github.com/user-attachments/assets/1d61da08-a0f4-4919-9618-f901821d7280" />

3. lihat di response bahwa nomor di refleksikan di dalam onclick event handler attribute

<img width="1915" height="1036" alt="3 nomor di refleksi href" src="https://github.com/user-attachments/assets/77ace127-4d8c-40e8-a59d-bbe1a970c0ca" />

4. masukan payload di kolom web: http://foo?&apos;-alert(1)-&apos;

<img width="1913" height="1025" alt="4 payload" src="https://github.com/user-attachments/assets/1acbb153-63c4-4d27-a817-d8185a3fd8ff" />

5. lihat url web di response

<img width="1913" height="1033" alt="5 response" src="https://github.com/user-attachments/assets/f8d411be-d134-4eef-8fcd-fb32a96dab45" />

6. klik nama author dan berhasil

<img width="1919" height="1029" alt="6 klik nama dan berhasil" src="https://github.com/user-attachments/assets/2017ef48-42fb-4f4f-b57b-766b1bd64559" />

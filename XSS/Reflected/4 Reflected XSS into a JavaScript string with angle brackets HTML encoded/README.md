# Lab 4 Reflected XSS into a JavaScript string with angle brackets HTML encoded 

## Brief:
This lab contains a reflected cross-site scripting vulnerability in the search query tracking functionality where angle brackets are encoded. The reflection occurs inside a JavaScript string.

## Tujuan:
perform a cross-site scripting attack that breaks out of the JavaScript string and calls the alert function.

<img width="1922" height="1046" alt="brief" src="https://github.com/user-attachments/assets/38ea1f66-0e53-4759-bfe1-394143ebddca" />

## Analisa

Submit a random alphanumeric string in the search box, then use Burp Suite to intercept the search request and send it to Burp Repeater.
Observe that the random string has been reflected inside a JavaScript string.

<img width="1922" height="1046" alt="1" src="https://github.com/user-attachments/assets/13cc4638-92b1-49fe-bacc-9a1a99601c5e" />

Replace your input with the following payload to break out of the JavaScript string and inject an alert:

    '-alert(1)-'

<img width="1922" height="1046" alt="2" src="https://github.com/user-attachments/assets/b6c386a0-0c89-40dd-8be1-a7c6793d1683" />

Verify the technique worked by right clicking, selecting "Copy URL", and pasting the URL in the browser. When you load the page it should trigger an alert.

<img width="1922" height="1046" alt="berhasil" src="https://github.com/user-attachments/assets/020ab8af-0f80-4c08-9973-8520d69a21e7" />

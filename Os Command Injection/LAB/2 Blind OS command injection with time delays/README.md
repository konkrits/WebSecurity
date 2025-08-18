# LAB 2 Blind OS command injection with time delays

## Brief:

web ini punya kerentanan blind command os injection di feedback, response nya tidak di kembalikan ke user
	
## Tujuan:

sebabkan delay selama 10 detik
	
## Analisa:

1. pergi ke laman feedback
<img width="1922" height="1046" alt="1 submit feedback" src="https://github.com/user-attachments/assets/4085b8b7-1f00-4a14-9df8-00cfc4723739" />
	
2. isi semua kolom dan intercept
<img width="1075" height="1025" alt="2 intercept" src="https://github.com/user-attachments/assets/5e7bb56d-0169-4494-bddc-5972e7bf5c1b" />
	
3. masukan payload di parameter email=x(PAYLOAD) dan kirim response akan memakan waktu selama yang ditentukan
		payload:

        ||ping+c+10+127.0.0.1|| -> || = or.  + = spasi c=waktu
<img width="1920" height="1044" alt="3 Payload dan delay" src="https://github.com/user-attachments/assets/79d471e8-7335-44e0-a045-af34eb3f23c6" />
			
4. setelah comamnd meng ping selama waktu yang ditentukan response bari di kirim
<img width="1920" height="1044" alt="4 setelah delay" src="https://github.com/user-attachments/assets/6a29a208-b926-4d57-a1cd-5a4c8ffdd45f" />

5. berhasil
<img width="1922" height="1046" alt="5 berhasil" src="https://github.com/user-attachments/assets/16f73b52-c42b-4441-9239-0879e7236151" />








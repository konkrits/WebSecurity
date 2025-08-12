# Lab 5 Information disclosure in version control history

## Tujuan:
Dapatkan password administrator dan hapus user carlos

## Brief:
lab ini menampilkan sensitif informasi di versi control historynya yaitu git.
<img width="1920" height="1080" alt="Brief" src="https://github.com/user-attachments/assets/7868de75-ba9c-4afa-ae5d-d5ca26ede73a" />

## Analisa:
1.) Coba pergi ke direcotry .git dan ternyata bisa diakses publik 
<img width="1920" height="1080" alt="1_akses_folder_git" src="https://github.com/user-attachments/assets/167f78a0-9d26-4991-929c-ff0582d978a7" />

2.) Download directorynya dengan wget
<img width="1920" height="1080" alt="2_download_dengan_wget" src="https://github.com/user-attachments/assets/c4ac1feb-d770-4b7c-b3a5-eac1546b9ad8" />

3.) dan show git dan disitu terlihat password adminnya meskipun sebelumnya dicoba dihapus dengan enviroment variable ADMIN_PASSWORD
<img width="1920" height="1080" alt="3_git_show" src="https://github.com/user-attachments/assets/71d59352-6054-44ba-b1ef-e3b60c96a2ec" />

4.) login dengan user administrator dan password yang baru didapat
<img width="1920" height="1080" alt="4_login_admin" src="https://github.com/user-attachments/assets/f1f8d617-b959-4203-974f-216b3dd3f339" />

5.) hapus carlos
<img width="1920" height="1080" alt="5_hapus_user_carlos" src="https://github.com/user-attachments/assets/03a4455c-cae7-447c-8812-926af84f73d0" />

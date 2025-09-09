url deploy = https://rafsanjani41-monokotilshop.pbp.cs.ui.ac.id/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
saya mengimplementasikan checklist di atas secara step by step dengan menerapkan apa yang sudah saya pelajari baik di kelas maupun saat tutorial. Saya juga beberapa kali melakukan debug dengan melihat beberapa sumber referensi yang ada dan juga menanyakan kepada teman yang memahaminya lebih baik. Saya juga sering kali bereksperimen dengan kode saya, sehingga at the end kode saya berjalan sesuai dengan requirements yang ada.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
bagan.png
![gambar bagan](bagan.png)

3. Jelaskan peran settings.py dalam proyek Django!
settings.py memiliki peran utama dalam proyek django meliputi penghubungan dengan database dan pendefinisian jenis database yang akan digunakan, mendefinisikan aplikasi yang akan digunakan dalam proyek, menentukan urutan permintaan request, mengatur url dan template, menyimpan secret key dan mendefinisikan domain mana saja yang diizinkan untuk menjalankan proyek. Singkatnya, settings.py berguna untuk menghubungkan dan memastikan setiap komponen yang ada bekerja dengan benar dan sesuai dengan konfigurasi yang sudah ditetapkan

4. Bagaimana cara kerja migrasi database di Django?
Pertama, developer akan membuat migrasi.Saat perubahan terjadi pada models.py, dan perintah python manage.py makemigrations dijalankan, maka django akan membandingkan kode dari models.py dengan kode yang terakhir yang sudah tercatat pada migrasi dan melihat perubahan yang ada. Secara otomatis, django akan membuat sebuah berkas migrasi yang baru yang berisi sekumpulan intruksi untuk mengubah skema database yang sudah ada. Berkas ini tidak akan langsung mengubah databse, melainkan hanya mendokumentasikan perubahan yang sudah ada. Kedua, .developer menerapkan migrasi. Setelah developer menjalankan perintah python manage.py migrate, django akan membaca berkas yang sudah dibuat sebelumnya, dan menjalankan intruksi di dalamnya. 

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut saya, framework django dijadikan permulaan pembelajaran pada matkul PBP karena framework django lebih mudah untuk dipelajari dibandingkan dengan framework lainnya baik secara teknis maupun teori. Penggunaan bahasa python juga menjadi penyebabnya, karena jika dibandingkan dengan bahasa pemrograman lain, python yang paling mudah dan simple, sehiingga kita hanya perlu fokus pada function dan method pada django nya saja.

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Menurut saya,sejauh ini tutorialnya sudah sangat baik dan jelas.
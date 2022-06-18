#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

HELP_1 = """✅**<u>Perintah Admin:</u>**

**c** singkatan dari pemutaran Channel.

/pause or /cpause - Jeda musik yang diputar.
/resume or /cresume- Lanjutkan musik yang dijeda.
/mute or /cmute- Matikan musik yang diputar.
/unmute or /cunmute- Suarakan musik yang dibisukan.
/skip or /cskip- Lewati musik yang sedang diputar.
/stop or /cstop- Hentikan pemutaran musik.
/shuffle or /cshuffle- Secara acak mengacak daftar putar yang antri.
/seek or /cseek - Teruskan Cari musik sesuai durasi Anda
/seekback or /cseekback - Mundur Carilah musik sesuai durasi Anda
/restart - Mulai ulang bot untuk obrolan Anda .


✅<u>**Lewati Spesifik:**</u>
/skip or /cskip [Nomor(contoh: 3)] 
    - Melewati musik ke nomor antrian yang ditentukan. Contoh: /skip 3 akan melewatkan musik ke musik antrian ketiga dan akan mengabaikan musik 1 dan 2 dalam antrian.

✅<u>**Putar Mengulang:**</u>
/loop or /cloop [enable|disable] atau [Angka antara 1-10] 
    - Saat diaktifkan, bot memutar musik yang sedang diputar menjadi 1-10 kali pada obrolan suara. Default ke 10 kali.

✅<u>**Pengguna Auth:**</u>
Pengguna Auth dapat menggunakan perintah admin tanpa hak Admin di Grup Anda.

/auth [Username] - Tambahkan pengguna ke AUTH LIST dari grup.
/unauth [Username] - Hapus pengguna dari AUTH LIST grup.
/authusers - Periksa DAFTAR AUTH grup."""


HELP_2 = """✅<u>**Perintah Play:**</u>

Perintah yang tersedia = play , vplay , cplay

Perintah ForcePlay = playforce , vplayforce , cplayforce

**c** singkatan dari pemutaran Channel.
**v** singkatan dari pemutaran video.
**force** singkatan dari force play.

/play atau /vplay atau /cplay  - Bot akan mulai memainkan kueri yang Anda berikan di obrolan suara atau Streaming tautan langsung di obrolan suara.

/playforce atau /vplayforce atau /cplayforce -  **Force Play** menghentikan trek yang sedang diputar pada obrolan suara dan mulai memutar trek yang dicari secara instan tanpa mengganggu/mengosongkan antrean.

/channelplay [Nama pengguna atau id obrolan] atau [Disable] - Hubungkan saluran ke grup dan streaming musik di obrolan suara saluran dari grup Anda.


✅**<u>Daftar Putar Server Bot:</u>**
/playlist  - Periksa Daftar Putar Tersimpan Anda Di Server.
/deleteplaylist - Hapus semua musik yang disimpan di daftar putar Anda
/play  - Mulai mainkan Daftar Putar Tersimpan Anda dari Server."""


HELP_3 = """✅<u>**Perintah Bot:**</u>

/stats - Dapatkan 10 Trek Global Stats Teratas, 10 Pengguna Bot Teratas, 10 Obrolan Teratas di bot, 10 Teratas Dimainkan dalam obrolan, dll.

/sudolist - Periksa Sudo Pengguna Music Bot

/lyrics [Nama Musik] mencari Lirik untuk Musik tertentu di web.

/song [Nama Trek] atau [Tautan YT] - Unduh trek apa pun dari youtube dalam format mp3 atau mp4.

/player -  Dapatkan Panel Bermain interaktif.

**c** singkatan dari pemutaran saluran.

/queue or /cqueue- Periksa Daftar Antrian Musik."""

HELP_4 = """✅<u>**Perintah Ekstra:**</u>
/start - Mulai Bot Musik.
/help - Dapatkan Menu Pembantu Perintah dengan penjelasan rinci tentang perintah.
/ping- Ping Bot dan periksa statistik Ram, Cpu, dll dari Bot.

✅<u>**Pengaturan Grup:**</u>
/settings - Dapatkan pengaturan grup lengkap dengan tombol sebaris

🔗 **Opsi di Pengaturan:**

1️⃣ Anda dapat mengatur **Kualitas Audio** Anda ingin streaming di obrolan suara.

2️⃣ Anda dapat mengatur **Kualitas Video** Anda ingin streaming di obrolan suara.

3️⃣ **Pengguna Auth**:- Anda dapat mengubah mode perintah admin dari sini ke semua orang atau hanya admin. Jika semua orang, siapa pun yang ada di grup Anda dapat menggunakan perintah admin (seperti /skip, /stop dll)

4️⃣ **Mode Bersih:** Saat diaktifkan, hapus pesan bot setelah 5 menit dari grup Anda untuk memastikan obrolan Anda tetap bersih dan baik.

5️⃣ **Perintah Bersih** : Saat diaktifkan, Bot akan menghapus perintah yang dieksekusi (/play, /pause, /shuffle, /stop etc).

6️⃣ **Pengaturan Putar:**

/playmode - Dapatkan panel pengaturan pemutaran lengkap dengan tombol tempat Anda dapat mengatur pengaturan pemutaran grup Anda. 

<u>Pilihan di playmode:</u>

1️⃣ **Mode Pencarian** [Direct atau Inline] - Mengubah mode pencarian Anda saat Anda memberikan mode /play. 

2️⃣ **Perintah Admin** [Semuanya atau Admin] - Jika semua orang, siapa pun yang ada di grup Anda akan dapat menggunakan perintah admin (seperti /skip, /stop dll)

3️⃣ **Tipe Perintah** [Semuanya or Admin] - Jika admin, hanya admin yang ada di grup yang dapat memutar musik di obrolan suara."""

HELP_5 = """🔰**<u>ADD & REMOVE SUDO USERS :</u>**
/addsudo [Username or Balas ke pengguna]
/delsudo [Username or Balas ke pengguna]

🛃**<u>HEROKU:</u>**
/usage - Penggunaan Dyno.

🌐**<u>KONFIGURASI VARS:</u>**
/get_var - Dapatkan config var dari Heroku atau .env
/del_var - Hapus semua var di Heroku atau .env
/set_var [Nama Var] [Value] - Setel Var atau Perbarui Var di heroku atau .env. Pisahkan Var dan Nilainya dengan spasi.

🤖**<u>PERINTAH BOT:</u>**
/reboot - Memulai ulang Bot Anda.
/restart - Memulai ulang Bot Anda.
/update - Update Bot.
/speedtest - Check server speeds
/maintenance [enable|disable] 
/logger [enable|disable] - Bot mencatat kueri yang dicari di logger.
/get_log [Number of Lines] - Dapatkan log bot Anda dari heroku atau vps. Bekerja untuk keduanya.

📈**<u>PERINTAH STATIS:</u>**
/activevoice - Periksa obrolan suara aktif di bot.
/activevideo - Periksa obrolan video aktif di bot.
/stats - Periksa Statistik Bot

⚠️**<u>FUNGSI BLACKLIST CHAT:</u>**
/blacklistchat [CHAT_ID] - Daftar hitam obrolan apa pun dari menggunakan Bot Musik
/whitelistchat [CHAT_ID] - Daftar putih obrolan apa pun yang masuk daftar hitam dari menggunakan Bot Musik
/blacklistedchat - Periksa semua obrolan yang masuk daftar hitam.

👤**<u>FUNGSI TERBLOKIR:</u>**
/block [Username or Balas ke pengguna] - Mencegah pengguna menggunakan perintah bot.
/unblock [Username or Balas ke pengguna] - Hapus pengguna dari Daftar Blokir Bot.
/blockedusers - Periksa Daftar Pengguna yang diblokir

👤**<u>FUNGSI GBAN:</u>**
/gban [Username or Balas ke pengguna] - Gban pengguna dari semua obrolan grup bot akan hentikan dia menggunakan bot Anda.
/ungban [Username or Balas ke pengguna] - Hapus pengguna dari Daftar gbanned Bot dan izinkan dia menggunakan bot Anda
/gbannedusers - Periksa Daftar Pengguna Gbanned

🎥**<u>FUNGSI VIDEOCALL:</u>**
/set_video_limit [Number of Chats] - Tetapkan Jumlah Obrolan maksimum yang diizinkan untuk Panggilan Video dalam satu waktu. Default untuk 3 obrolan.
/videomode [download|m3u8] - Jika mode unduh diaktifkan, Bot akan mengunduh video alih-alih memutarnya dalam bentuk M3u8. Secara default ke M3u8. Anda dapat menggunakan mode unduhan saat kueri apa pun tidak diputar dalam mode m3u8.

⚡️**<u>FUNGSI BOT PRIBADI:</u>**
/authorize [CHAT_ID] - Izinkan obrolan untuk menggunakan bot Anda.
/unauthorize [CHAT_ID] - Larang obrolan menggunakan bot Anda.
/authorized - Periksa semua obrolan yang diizinkan dari bot Anda.

🌐**<u>FUNGSI BROADCAST:</u>**
/broadcast [Message or Balas ke pengguna] - Siarkan pesan apa pun ke Obrolan yang Dilayani Bot.

<u>Opsi untuk broadcast:</u>
**-pin** : Ini akan menyematkan pesan Anda
**-pinloud** : Ini akan menyematkan pesan Anda dengan pemberitahuan
**-user** : Ini akan menyiarkan pesan Anda ke pengguna yang telah memulai bot Anda.
**-assistant** : Ini akan menyiarkan pesan Anda dari akun asisten bot Anda.
**-nobot** : Ini akan memaksa bot Anda untuk tidak menyiarkan pesan.

**Contoh:** `/broadcast -user -assistant -pin Hello Testing`

"""

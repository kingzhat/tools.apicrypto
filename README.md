# tools.apicrypto
Crypto Price Checker
Selamat datang di repositori Crypto Price Checker! Proyek ini berisi skrip Python sederhana yang memungkinkan Anda memantau harga terkini dari beberapa mata uang kripto populer seperti Bitcoin, Ethereum, Dogecoin, dan Litecoin. Skrip ini dirancang untuk kemudahan penggunaan dan memberikan informasi harga secara cepat.

Fitur Utama
Pengecekan Harga Kripto: Dapatkan harga Bitcoin, Ethereum, Dogecoin, dan Litecoin dalam USD secara real-time.

Antarmuka Pengguna Sederhana: Menu berbasis konsol yang mudah dinavigasi.

Animasi Loading: Animasi visual untuk menunjukkan proses pemuatan data.

Penanganan Error: Menangani kesalahan umum seperti masalah koneksi atau parsing data.

Cara Menggunakan
Kloning Repositori:
Pertama, kloning repositori ini ke mesin lokal Anda:

Bash

git clone https://github.com/kingzhat/ddos.git # (Disarankan untuk mengganti nama repositori di GitHub nanti)
cd ddos # (Atau nama folder hasil kloning Anda)
Instal Dependensi:
Skrip ini menggunakan beberapa pustaka Python yang perlu diinstal. Anda bisa menginstalnya menggunakan pip:

Bash

pip install requests colorama tqdm
Jalankan Skrip:
Setelah dependensi terinstal, Anda bisa menjalankan skrip utama:

Bash

python your_script_name.py # Ganti dengan nama file Python utama Anda, misalnya: python main.py
Setelah menjalankan skrip, Anda akan disajikan dengan menu untuk memilih opsi.

Contoh Tampilan
    ██████╗ ██╗   ██╗███╗   ██╗███████╗███████╗██████╗
    ██╔═══██╗██║   ██║████╗  ██║██╔════╝██╔════╝██╔══██╗
    ██║   ██║██║   ██║██╔██╗ ██║█████╗  █████╗  ██████╔╝
    ██║▄▄ ██║██║   ██║██║╚██╗██║██╔══╝  ██╔══╝  ██╔═══╝
    ╚██████╔╝╚██████╔╝██║ ╚████║███████╗███████╗██║
     ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝ ╚══════╝╚══════╝╚═╝

Loading...
Loading: 100%|████████████████████████████████████████| 10/10 [00:05<00:00,  1.82it/s]
Loading complete.

1. Search Crypto Prices
2. Mencari Coin Doge (Note: This currently runs the same crypto search as option 1)
3. Exit

Choose an option:
Catatan Penting
Penamaan Repositori: Nama repositori ddos saat ini tidak sesuai dengan fungsionalitas skrip ini yang adalah pengecek harga kripto. Sangat disarankan untuk mengganti nama repositori di GitHub Anda menjadi sesuatu yang lebih relevan, seperti crypto-price-checker atau simple-crypto-tracker. Ini akan membantu pengguna lain memahami proyek Anda dengan benar.

Fungsi create_website: Ada fungsi create_website yang tidak digunakan dalam kode utama Anda. Jika ini adalah sisa dari pengembangan sebelumnya, Anda mungkin ingin menghapusnya atau mengintegrasikannya ke dalam fungsionalitas skrip.

Fungsi search_crypto_dogecoin dan search_crypto_litecoin: Saat ini, kedua fungsi ini mencoba mengambil data dari api.coindesk.com dengan URL yang tidak valid untuk Dogecoin dan Litecoin (Coindesk umumnya untuk Bitcoin). Ini akan menyebabkan kesalahan. Disarankan untuk menggunakan API yang lebih komprehensif seperti CoinGecko atau CoinMarketCap untuk mata uang kripto lainnya.

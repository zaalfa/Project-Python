# Project-Cashier-Self-Service

Project ini dibuat untuk membantu Andi dalam menjalankan bisnisnya menggunakan sistem kasir self-service. Dengan program ini customer dapat langsung memasukkan item yang dibeli, jumlah item, harga item dan beberapa fitur lainnya, sehingga customer yang tidak berada di kota tersebut tetap bisa membeli barang dari supermarket milik Andi.

#Requirements/objectives
1. Customer membuat ID transaksi
2. Customer bisa melakukan input nama item, jumlah item, dan harga item
3. Customer dapat mengubah nama, jumlah, maupun harga dari item yang sudah diinput
4. Customer dapat batal membeli item yang sudah diinput dengan menghapus item yang dipilih maupun keseluruhan item sekaligus
5. Jika sudah selesai berbelanja customer dapat mengecek kembali semua item yang telah di input
6. Setelah yakin customer bisa melihat berapa total belanja yang harus dibayar

# Alur Program/Flowchart
![flowchart](https://user-images.githubusercontent.com/123067601/218313859-db532658-9eff-46e1-9785-18c022a588d5.png)

# Penjelasan Code
1. def __init__(self):
   inisialisasi untuk class transaction
2. self.data_trnsct = dict(): membuat dictionary bernama data_trnsct untuk menyimpan item yang diinput customer
3. def add_item(self, nama_item, jumlah, harga): fungsi untuk menambahkan barang. memiliki parameter nama item, jumlah barang, dan harga per barang
4. self.data_trnsct.update(): untuk menambahkan item yang baru diinput oleh customer ke dalam dictionary
5. def update_item_name(self, nama_item, update_nama): fungsi untuk mengubah nama item apabila customer salah melakukan input
6. def update_item_qty(self, nama_item, update_jumlah): fungsi untuk mengubah jumlah item apabila costumer salah melakukan input
7. def update_item_price(self, nama_item, update_harga): fungsi untuk mengubah harga item apabila customer salah melakukan input
8. def delete_item(self, nama_item): fungsi untuk menghapus barang tertentu yang dipilih oleh customer
9. def reset_transaction(self): fungsi untuk menghapus seluruh data transaksi sekaligus
10. def check_order(self): fungsi untuk menampilkan data transaksi
11. def total_price(self): fungsi untuk menampilkan total belanja dan juga diskon yang didapatkan oleh customer

# Hasil Test Case
1. Customer ingin menambahkan dua item baru menggunakan method add_item(). item yang ditambahkan adalah sebagai berikut:
   - Nama item: Ayam Goreng, Qty: 2, Harga: 20000
   - Nama item: Pasta Gigi, Qty: 3, Harga: 15000
2. Ternyata customer salah membeli salah satu item dari belanjaan yang sudah ditambahkan, maka customer menggunakan method delete_item() untuk menghapus item. item yang ingin dihapuskan adalah **Pasta Gigi**
3. Ternyata setelah dipikir-pikir customer salah memasukkan item yang ingin dibelanjakan! Daripada menghapusnya satu-satu, maka customer cukup menggunakan method reset_transaction() untuk menghapus semua item yang sudah ditambahkan
![image](https://user-images.githubusercontent.com/123067601/218318603-7080b9da-f024-4324-8249-df318664e910.png)
4. Setelah customer selesai berbelanja, akan menghitung total belanja yang harus dibayarkan menggunakan method total_price(). sebelum mengeluarkan output total belanja akan menampilkan item-item yang dibeli.

# Conclusion/Future Work
Pada future work apabila saya memiliki waktu dan sdm lebih saya ingin daftar barang yang tersedia di supermarket sudah diinputkan ke program sehingga pengecekan dapat dilakukan otomatis tanpa perlu diminta dan dicek manual oleh customer, apabila terdapat kesalahan pada input customer maka sistem akan langsung menolak atau memberikan pesan peringatan.

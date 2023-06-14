## Program Pengelolaan Data Stok Barang dan Transaksi Konsumen

Ini adalah program sederhana untuk mengelola data stok barang dan transaksi konsumen dalam suatu perusahaan retail. Program ini memiliki menu utama dan beberapa submenu yang memungkinkan Anda melakukan berbagai operasi terkait pengelolaan data. Berikut adalah deskripsi singkat tentang menu dan fungsionalitas yang tersedia dalam program ini:

### Menu Utama

1. Kelola Stok Barang
2. Kelola Transaksi Konsumen
3. Exit Program

### Kelola Stok Barang

1.1. Input Data Stok Barang

- Data stok barang disimpan dalam struktur data Binary Search Tree (BST).
- Setiap data stok barang memiliki atribut berikut:
  - No. SKU
  - Nama Barang
  - Harga Satuan
  - Jumlah Stok
- Saat memasukkan data stok barang, sistem akan meminta input dari pengguna untuk setiap atribut dan memeriksa apakah No. SKU sudah ada dalam BST sebelumnya.

  1.2. Restok Barang

- Menu ini digunakan untuk mengupdate stok barang yang sudah ada dalam BST.
- Pengguna diminta untuk memasukkan No. SKU barang yang akan diupdate.
  - Jika No. SKU sudah ada dalam BST, pengguna diminta memasukkan jumlah stok baru yang akan ditambahkan.
  - Jika No. SKU belum ada dalam BST, sistem akan menyarankan pengguna untuk melakukan input data stok barang terlebih dahulu.

### Kelola Transaksi Konsumen

2.1. Input Data Transaksi Baru

- Data transaksi konsumen disimpan dalam struktur data Array/List.
- Setiap data transaksi memiliki atribut berikut:
  - Nama Konsumen
  - No. SKU barang yang dibeli
  - Jumlah Beli
  - Subtotal
- Pengguna diminta memasukkan Nama Konsumen.
- Setelah itu, pengguna diminta memasukkan No. SKU barang yang dibeli oleh konsumen.
  - Jika No. SKU sudah ada dalam BST, pengguna diminta memasukkan jumlah barang yang dibeli.
  - Jika No. SKU belum ada dalam BST, sistem akan memunculkan pesan dan meminta pengguna memilih untuk melanjutkan transaksi atau tidak.
- Setelah memasukkan jumlah barang yang dibeli, sistem akan memeriksa apakah stok tersedia cukup.
  - Jika stok cukup, sistem akan mengurangi stok barang sesuai dengan jumlah yang dibeli, menghitung subtotal, dan mencatat transaksi ke dalam Array/List.
  - Jika stok tidak cukup, sistem akan memunculkan pesan dan meminta pengguna memilih untuk melanjutkan transaksi atau tidak.
- Setelah mencatat transaksi, pengguna dapat memilih untuk menambahkan data pembelian untuk konsumen yang sama atau kembali ke submenu Kelola Transaksi Konsumen.

  2.2. Lihat Data Seluruh Transaksi Konsumen

- Menu ini akan menampilkan semua data transaksi konsumen yang tersimpan dalam Array/List.
- Data yang ditampilkan meliputi:

  - Nama Konsumen
  - No. SKU barang yang dibeli
  - Jumlah Beli
  - Subtotal

  2.3. Lihat Data Transaksi Berdasarkan Subtotal

- Menu ini akan menampilkan data transaksi konsumen yang tersimpan dalam Array/List

secara terurut berdasarkan nilai subtotal.

- Pengguna dapat memilih salah satu metode pengurutan berikut untuk mengimplementasikan menu ini:
  - Bubble Sort
  - Insertion Sort
  - Selection Sort
  - Merge Sort
  - Quick Sort

Pilihan menu ini memungkinkan Anda untuk mengelola dengan mudah data stok barang dan transaksi konsumen dalam perusahaan retail. Program ini memberikan fleksibilitas dan fungsi pengurutan yang dapat disesuaikan dengan kebutuhan Anda.

Selamat menggunakan program ini! Jika Anda memiliki pertanyaan atau masalah, jangan ragu untuk menghubungi kami. Terima kasih!

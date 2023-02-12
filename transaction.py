import pandas as pd

class Transaction:
    def __init__(self):
        self.data_trnsct = dict()
        
    def add_item(self, nama_item, jumlah, harga):
        """        
        fungsi untuk menambah barang

        Args:
            nama_item (str): nama barang yang dibeli
            jumlah (int): jumlah barang yang dibeli
            harga (int): harga barang yang dibeli
        """
        #untuk menambahkan data ke dict
        self.data_trnsct.update({nama_item: [jumlah, harga, (jumlah*harga)]})
        
        #untuk menampilkan data transaksi
        return self.check_order()
    
    def update_item_name(self, nama_item, update_nama):
        """
        fungsi untuk mengubah nama barang yang salah diinput

        Args:
            nama_item (str): nama barang yang dibeli
            update_nama (str): nama barang yang benar
        """
        try:
            #untuk update data pada dict
            temp = self.data_trnsct[nama_item]
            self.data_trnsct.pop(nama_item)
            self.data_trnsct.update({update_nama: temp})
            
            #untuk menampilkan data transaksi
            return self.check_order()
        except:
            print("Nama item tidak sesuai!")        
        
    def update_item_qty(self, nama_item, update_jumlah):
        """
        fungsi untuk mengubah jumlah barang yang salah diinput

        Args:
            nama_item (str): nama barang yang dibeli
            update_jumlah (int): jumlah barang yang benar
        """
        try:
            #untuk update data pada dict
            self.data_trnsct[nama_item][0] = update_jumlah
            self.data_trnsct[nama_item][2] = update_jumlah * self.data_trnsct[nama_item][1]
            
            #untuk menampilkan data transaksi
            return self.check_order()
        except:
            print("Nama item tidak sesuai!") 
        
    def update_item_price(self, nama_item, update_harga):
        """
        fungsi untuk mengubah harga barang yang salah diinput

        Args:
            nama_item (str): nama barang yang dibeli
            update_harga (int): harga barang yang benar
        """
        try:
            #untuk update data pada dict
            self.data_trnsct[nama_item][1] = update_harga
            self.data_trnsct[nama_item][2] = update_harga * self.data_trnsct[nama_item][0]
            
            #untuk menampilkan data transaksi
            return self.check_order()
        except:
            print("Nama item tidak sesuai!") 
        
    def delete_item(self, nama_item):
        """
        fungsi untuk menghapus barang yang dipilih

        Args:
            nama_item (str): nama barang yang dibeli
        """
        if nama_item == self.data_trnsct[nama_item]:
           self.data_trnsct.pop(nama_item)           
        
    def reset_transaction(self):
        """
        fungsi untuk menghapus seluruh data transaksi
        """
        self.data_trnsct.clear()
        print("Semua item berhasil di delete!")
        
    
    def check_order(self):
        """
        fungsi untuk menampilkan data transaksi
        """
        #mengubah data ke bentuk dataframe
        try:
            if len(self.data_trnsct) == 0:
                print("Anda tidak memiliki pesanan!")
            else:
                data = pd.DataFrame(self.data_trnsct).T
                data.index.name = "Nama Item"
                data.columns = ["Jumlah Item", "Harga per Item", "Total Harga"]
                
                print(data.to_markdown())
        except:
            print("Tidak boleh ada data yang kosong!")
            
    def total_price(self):
        total = 0
        for i in self.data_trnsct.values():
            total += i[2]
        
        if(total > 200_000):
            if(total > 300_000):
                if(total > 500_000):
                    print("Anda Mendapat disc sebesar 10%!")
                    print(f"Total belanja anda menjadi Rp.{total*0.9}")
                else:
                    print("Anda Mendapat disc sebesar 8%!")
                    print(f"Total belanja anda menjadi Rp.{total*0.92}")
            else:
                print("Anda Mendapat disc sebesar 5%!")
                print(f"Total belanja anda menjadi Rp.{total*0.95}")
        else:
            print(f"Total belanja Rp.{total}")
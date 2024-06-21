from bs4 import BeautifulSoup
import requests

class Scraper():

    def scrapedata(self, tag):
        # inisialisasi barang untuk menyimpan data produk
        barang = []        

        # Mengirim permintaan GET ke website Bhinneka dengan tag yang diberikan
        page = requests.get(f'https://www.bhinneka.com/jual?cari={tag}&order=')
        
        # Mem-parsing konten halaman menggunakan BeautifulSoup
        after_bs = BeautifulSoup(page.content, 'html.parser')
        
        # Menemukan semua elemen yang berisi informasi produk
        find_data = after_bs.find_all('div', class_='o_wsale_product_grid_wrapper position-relative h-100')
        
        # Loop melalui setiap elemen yang ditemukan
        for index, data_poin in enumerate(find_data, start=1):
            # Mengambil nama produk
            product = data_poin.find('a', class_='text-primary text-decoration-none').get_text()
            
            # Mengambil harga produk
            cash = data_poin.find('span', class_='oe_currency_value').get_text()
            
            # Membuat dictionary dengan informasi produk
            cetak = {
                'Nama Produk': product,
                'Harga': cash
            }

            # Mencetak hasil scraping
            print(cetak)

            # Menambahkan informasi produk ke variabel barang 
            barang.append(cetak)

        return barang

produk = Scraper()

# Memanggil metode scrapedata dengan tag sesuai keinginan
produk.scrapedata('lenovo')
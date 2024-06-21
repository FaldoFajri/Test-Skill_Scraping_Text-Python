from fastapi import FastAPI
from scraper import Scraper


# Inisialisasi aplikasi FastAPI
app = FastAPI()

# Membuat instance dari kelas Scraper
produk = Scraper()

# Mendefinisikan endpoint yang menerima kategori sebagai parameter path
@app.get("/{category}")
async def read_item(category):

     # Memanggil metode scrapedata dari instance Scraper dengan kategori yang diberikan
    return produk.scrapedata(category)
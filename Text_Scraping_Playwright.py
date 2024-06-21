#Text_Scraping_Playwright

import asyncio  # Mengimpor modul asyncio untuk menjalankan fungsi asinkron
import pandas as pd  # Mengimpor pandas untuk memanipulasi dan menyimpan data dalam format DataFrame
from playwright.async_api import async_playwright  # Mengimpor async_playwright dari Playwright untuk otomatisasi web asinkron

async def main():
    # Memulai konteks Playwright
    async with async_playwright() as p:
        
        produg = []  # Membuat list kosong untuk menyimpan nama produk
        hargaf = []  # Membuat list kosong untuk menyimpan harga produk
        
        # Meluncurkan browser Chromium dalam mode tidak headless (Situs Website akan Muncul)
        browser = await p.chromium.launch(headless=False)
        # Membuka tab baru di browser
        page = await browser.new_page()

        # URL halaman web yang akan di-scrape
        url = 'https://www.bhinneka.com/jual-wearable-device/wYJpmqn'
        # Mengunjungi URL yang telah ditentukan
        await page.goto(url)
        
        # Memilih semua elemen yang mengandung nama produk
        product_names = await page.query_selector_all('.text-primary.text-decoration-none')
        # Memilih semua elemen yang mengandung harga produk
        product_prices = await page.query_selector_all('.oe_currency_value')

        # Iterasi untuk setiap elemen nama produk yang ditemukan
        for product_name in product_names:
            # Mendapatkan teks dari elemen nama produk
            product_name_text = await product_name.inner_text()
            # Menambahkan teks nama produk ke list produg
            produg.append(product_name_text)

        # Iterasi untuk setiap elemen harga produk yang ditemukan
        for product_price in product_prices:
            # Mendapatkan teks dari elemen harga produk
            product_price_text = await product_price.inner_text()
            # Menambahkan teks harga produk dengan prefiks "Rp." ke list hargaf
            hargaf.append(f"Rp.{product_price_text}")

        # Memilih harga produk dengan indeks ganjil (karena pola harga yang di-scrape)
        hargaf_ganjil = hargaf[1::2]
        
        # Membuat DataFrame dari list produk dan harga ganjil
        df = pd.DataFrame(list(zip(produg, hargaf_ganjil)), columns=['Produk', 'Harga'])

        # Mencetak DataFrame untuk memverifikasi hasil
        print(df)

        # Menyimpan DataFrame ke file CSV
        df.to_csv('(Hasil-Playwright)produk_smartwatch.csv', index=False)

        # Menutup browser setelah selesai
        await browser.close()

# Menjalankan fungsi utama asinkron menggunakan asyncio
asyncio.run(main())

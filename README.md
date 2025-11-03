# 🧩 ETL Pipeline Penjualan Online (Real Data - Olist E-Commerce)

### 🎯 Tujuan
Membangun pipeline ETL yang menarik data transaksi e-commerce **nyata** dari dataset Olist (Kaggle), membersihkan data, lalu memuatnya ke PostgreSQL untuk dianalisis.

---

### 🧱 Arsitektur Pipeline
```

CSV (orders, payments, items)
│
▼
[Python + Pandas]
│
Cleaning & Join
│
▼
[PostgreSQL Database]
│
▼
[SQL Analysis]

````

---

### ⚙️ Tools
- Python (Pandas)
- PostgreSQL
- SQLAlchemy
- psycopg2

---

### 🧩 Langkah ETL
1. **Extract:** Membaca data dari CSV Olist (real dataset dari Kaggle)
2. **Transform:** Membersihkan data (drop null, ubah tipe data, hitung total pembayaran)
3. **Load:** Memasukkan data hasil transformasi ke PostgreSQL

---

### 📊 Hasil Analisis

#### Total Penjualan per Metode Pembayaran
```sql
SELECT payment_type, ROUND(SUM(total_nilai), 2) AS total_penjualan
FROM data_penjualan_online
GROUP BY payment_type;
````

| payment_type | total_penjualan |
| ------------ | --------------: |
| credit_card  |     42392000.55 |
| boleto       |     18102430.23 |
| debit_card   |      2200430.00 |
| voucher      |       104000.00 |

---

### 📸 Screenshot

1. Terminal output ETL sukses
   ![terminal output](https://github.com/user-attachments/assets/89b22331-d372-4b8a-8ec9-6110d068a98c)

2. Tampilan tabel `data_penjualan_online` di PostgreSQL
   ![Tabel penjualan online](https://github.com/user-attachments/assets/ed74d0f9-c82f-4dc6-9ab6-368bb689a45a)

3. Hasil query SQL (grafik atau tabel)
   ![Penjualan metode pembayaran](https://github.com/user-attachments/assets/948df5bc-277f-4af6-8871-394b35c06c49)
   ![Transaksi perbulan](https://github.com/user-attachments/assets/9c74242d-3fa4-4aab-b692-1ba4c5f0ccba)


---

### 📦 Dataset

Dataset asli: [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

---

### 👤 Author

Dibuat oleh **[Ilyas Yanuar]** – Calon Data Engineer
Menunjukkan kemampuan **data ingestion**, **data cleaning**, dan **database loading** menggunakan Python dan PostgreSQL.

```

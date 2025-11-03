````markdown
# 🏗️ Data Warehouse (Star Schema) – Penjualan Online (Olist E-Commerce)

🔗 **Kelanjutan dari:**  
[ETL Pipeline Penjualan Online (Project 1)](https://github.com/ilyasyanuar2/ETL-Pipeline-Penjualan-Online-Real-Data---Olist-E-Commerce-)

---

## 🎯 Tujuan
Membangun **Data Warehouse (DWH)** berbasis **Star Schema** untuk menganalisis data hasil ETL dari e-commerce Olist (Brazil).  
Tujuan utama:
- Mendesain model dimensi dan fakta.
- Mengisi tabel DWH dari hasil ETL (`data_penjualan_online`).
- Melakukan query analitik untuk insight bisnis.

---

## 🧱 Arsitektur Data Pipeline

```text
CSV (raw data dari Kaggle)
      │
      ▼
[Project 1: ETL Pipeline - Python + PostgreSQL]
      │
      ▼
data_penjualan_online (clean table)
      │
      ▼
[Project 2: Data Warehouse - Star Schema]
      ├── dim_date
      ├── dim_payment
      └── fact_sales
````

---

## ⚙️ Tools & Teknologi

* **PostgreSQL** – Database untuk Data Warehouse
* **SQL** – Pembuatan tabel & query analitik
* **Python + SQLAlchemy** – Otomatisasi proses loading DWH
* **dbdiagram.io** – Membuat diagram ERD

---

## 🗂️ Struktur Database

Tabel utama:

| Jenis Tabel | Nama Tabel    | Deskripsi                                            |
| ----------- | ------------- | ---------------------------------------------------- |
| Dimensi     | `dim_date`    | Menyimpan atribut tanggal (tahun, bulan, hari, dsb.) |
| Dimensi     | `dim_payment` | Menyimpan tipe pembayaran                            |
| Fakta       | `fact_sales`  | Menyimpan transaksi penjualan (mengacu ke dimensi)   |

---

## 📜 Skema DWH (Star Schema)

<img width="799" height="376" alt="erd_dwh" src="https://github.com/user-attachments/assets/8420d6b1-c65e-44cb-ae08-dd8712abef9f" />


> Dibuat menggunakan [dbdiagram.io](https://dbdiagram.io)

---

## 🧩 Langkah ETL ke DWH

1. **Extract** – Ambil data dari tabel hasil ETL: `data_penjualan_online`
2. **Transform** – Ambil kolom relevan (tanggal, tipe pembayaran, nilai transaksi)
3. **Load** – Masukkan data ke tabel dimensi dan tabel fakta:

   * `dim_date`
   * `dim_payment`
   * `fact_sales`

---

## 📊 Contoh Query Analitik

### 🔹 Total Penjualan per Bulan

```sql
SELECT d.year, d.month, SUM(f.total_value) AS total_penjualan
FROM fact_sales f
JOIN dim_date d ON f.date_id = d.date_id
GROUP BY d.year, d.month
ORDER BY d.year, d.month;
```

### 🔹 Total Penjualan per Metode Pembayaran

```sql
SELECT p.payment_type, SUM(f.total_value) AS total_penjualan
FROM fact_sales f
JOIN dim_payment p ON f.payment_id = p.payment_id
GROUP BY p.payment_type
ORDER BY total_penjualan DESC;
```

---

## 📸 Screenshot Hasil Query

|               Total Penjualan per Bulan               |     Total Penjualan per Metode Pembayaran     |
| :---------------------------------------------------: | :-------------------------------------------: |
| ![Total penjualan per bulan](https://github.com/user-attachments/assets/207ca55d-7a7c-43be-87c7-8533be8a9cd2)
 | ![Total penjualan per metode pembayaran](https://github.com/user-attachments/assets/ebae1548-5006-4d1c-a4ff-5dc772fe9616)
 |

---

## 🧾 Checklist Deliverable

* [x] `create_dwh_schema.sql` — Script SQL pembuatan Star Schema
* [x] `load_dwh.py` — Otomatisasi populate dimensi & fakta
* [x] `erd_dwh.png` — Diagram ERD Data Warehouse
* [x] `query_results_total_per_bulan.png` — Screenshot hasil query
* [x] `README.md` — Dokumentasi lengkap
* [ ] (Opsional) `export_sample_data.sql` — Contoh data hasil ETL

---

## 🧠 Insight & Pembelajaran

* Penerapan konsep **Dimensional Modeling (Star Schema)**.
* Membangun koneksi antar tabel (Foreign Key) untuk analitik.
* Melakukan query agregasi lintas dimensi (waktu & metode pembayaran).
* Otomatisasi proses loading data menggunakan **SQLAlchemy**.

---

## 📦 Dataset

Dataset: [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

---

## 👤 Author

**Ilyas Yanuar**
📧 ilyasyanuar2@gmail.com
🎯 *Calon Data Engineer – membangun end-to-end pipeline dari ETL hingga Data Warehouse.*

````

---

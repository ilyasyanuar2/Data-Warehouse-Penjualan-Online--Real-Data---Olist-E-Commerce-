import pandas as pd
from sqlalchemy import create_engine

# --------------------------
# 1️⃣ EXTRACT
# --------------------------
orders = pd.read_csv("data/olist_orders_dataset.csv")
payments = pd.read_csv("data/olist_order_payments_dataset.csv")
items = pd.read_csv("data/olist_order_items_dataset.csv")

# --------------------------
# 2️⃣ TRANSFORM
# --------------------------

# Gabungkan data orders dengan payments dan items berdasarkan order_id
df = orders.merge(payments, on="order_id", how="left")
df = df.merge(items, on="order_id", how="left")

# Hapus data kosong atau duplikat
df.dropna(subset=["payment_value", "price"], inplace=True)
df.drop_duplicates(inplace=True)

# Ubah kolom tanggal jadi datetime
df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"])

# Hitung total pembayaran
df["total_nilai"] = df["payment_value"] + df["freight_value"]

# Ambil kolom penting
final_df = df[[
    "order_id",
    "order_purchase_timestamp",
    "payment_type",
    "price",
    "freight_value",
    "total_nilai"
]]

# --------------------------
# 3️⃣ LOAD
# --------------------------

# Ganti username, password, dan host sesuai PostgreSQL kamu
engine = create_engine("postgresql+psycopg2://postgres:Ujb12345@localhost:5432/penjualan_db")

# Simpan ke tabel PostgreSQL
final_df.to_sql("data_penjualan_online", engine, if_exists="replace", index=False)

print("✅ ETL Pipeline selesai! Data berhasil dimuat ke PostgreSQL.")
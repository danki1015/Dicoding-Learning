import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import os

customer = pd.read_csv('data/customers_dataset.csv')
orders = pd.read_csv('data/orders_dataset.csv')
order_reviews = pd.read_csv('data/order_reviews_dataset.csv')
payments = pd.read_csv('data/order_payments_dataset.csv')
order_items = pd.read_csv('data/order_items_dataset.csv')
products = pd.read_csv('data/products_dataset.csv')
sellers = pd.read_csv('data/sellers_dataset.csv')
geolocation = pd.read_csv('data/geolocation_dataset.csv')
products_translation = pd.read_csv('data/product_category_name_translation.csv')

# menggabugkan product dengan products_translation
products = products.merge(products_translation, left_on='product_category_name', right_on='product_category_name',how='left')

df_product = products[["product_id","product_category_name_english","product_category_name"]]


# menggabugkan order_items dengan df_products menjadi df_order_items
df_order_items = order_items.merge(products, left_on='product_id', right_on='product_id',how='left')

# menggabungkan df_order_items dengan seller
sellers = sellers.drop(columns = ['seller_zip_code_prefix'])
df_order_items = df_order_items.merge(sellers, left_on='seller_id', right_on='seller_id',how='left')

# menggabungkan orders dengan payments
payments = payments.drop(columns = ['payment_sequential','payment_installments'])
orders = orders.merge(payments, left_on='order_id', right_on='order_id',how='left')

# menggabungkan orders dengan customers
customer = customer.drop(columns = ['customer_unique_id'])
orders = orders.merge(customer, left_on='customer_id', right_on='customer_id',how='left')

#data types
df_order_items['shipping_limit_date'] = pd.to_datetime(df_order_items['shipping_limit_date'])

# missing value pada kolom product_category_name_english
x = df_order_items.loc[df_order_items["product_category_name"].notnull() & df_order_items["product_category_name_english"].isnull()]
set(x["product_category_name"])

df_order_items['product_category_name'].fillna('not defined', inplace=True)
df_order_items['product_category_name_english'].fillna('not defined', inplace=True)

df_order_items["product_category_name_english"] = np.where(df_order_items["product_category_name"] == 'pc_gamer', 'PC Gaming', df_order_items["product_category_name_english"])
df_order_items["product_category_name_english"] = np.where(df_order_items["product_category_name"] == 'portateis_cozinha_e_preparadores_de_alimentos', 'portable kitchen food preparers', df_order_items["product_category_name_english"])


# membenarkan data types 
orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
orders['order_approved_at'] = pd.to_datetime(orders['order_approved_at'])
orders['order_delivered_carrier_date'] = pd.to_datetime(orders['order_delivered_carrier_date'])
orders['order_delivered_customer_date'] = pd.to_datetime(orders['order_delivered_customer_date'])
orders['order_estimated_delivery_date'] = pd.to_datetime(orders['order_estimated_delivery_date'])
orders['order_status'] = orders['order_status'].astype('category')


# menambahkan kolom untuk EDA
orders['year'] = orders['order_purchase_timestamp'].dt.strftime('%Y')
orders['month'] = orders['order_purchase_timestamp'].dt.strftime('%m-%Y')
# df_order_items

orders["lama_pengiriman_hari"] = (orders["order_delivered_customer_date"] - orders["order_delivered_carrier_date"]).dt.days
orders["hari_pembelian"] = orders["order_purchase_timestamp"].dt.strftime('%A')

orders['jam_pembelian'] = orders['order_purchase_timestamp'].apply(lambda x: x.hour)
hours_bins = [-0.1, 6, 12, 18, 23]
hours_labels = ['Subuh', 'Pagi', 'Siang', 'Malam']
orders['waktu_hari_pembelian'] = pd.cut(orders['jam_pembelian'], hours_bins, labels=hours_labels)

# menggabungkan customer dengan seller
cust = orders[["customer_city","customer_state","lama_pengiriman_hari","order_id","customer_id"]]
seller = df_order_items[["order_id","seller_id","seller_city","seller_state"]]
cust_seller = cust.merge(seller, left_on='order_id', right_on='order_id',how='left')

# mendefinisikan fungsi yang akan digunakan untuk EDA
def range(series):
    return series.max() - series.min()

st.text('Dashboard Proyek Analisa')

#Pertanyaan 1
st.subheader('Category barang yang paling banyak dibeli dan paling sedikit diminati?')

df_category = df_order_items.groupby(by="product_category_name_english")["product_id"].count().reset_index() #jumlah pembelian
df_category = df_category.rename(columns={"product_category_name_english": "category", "product_id": "orders"})
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))
 
colors = ["#800000", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
 
sns.barplot(x="orders", y="category", data=df_category.sort_values(by="orders", ascending=False).head(5), palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("Category Terlaris", loc="center", fontsize=15)
ax[0].tick_params(axis ='y', labelsize=12)
 
sns.barplot(x="orders", y="category", data=df_category.sort_values(by="orders", ascending=True).head(5), palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Category Sedikit Peminat", loc="center", fontsize=15)
ax[1].tick_params(axis='y', labelsize=12)
 
plt.suptitle("Category Terlaris dan Sedikit Peminat berdasarkan Total Pembelian", fontsize=20)

st.pyplot(fig)

#Pertanyaan 2: 
st.subheader('Berapa lama rata-rata pengiriman paket pengiriman paket terlama ? dari mana ke mana?')

df_pengiriman_state = cust_seller.groupby(['seller_state', 'customer_state'])['lama_pengiriman_hari'].mean().sort_values(ascending=False).reset_index()
fig = plt.figure(figsize=(10, 5))
cmap= sns.cubehelix_palette(start=.5, rot=-.75, as_cmap=True)

plt.scatter(df_pengiriman_state['seller_state'], df_pengiriman_state['customer_state'], c=df_pengiriman_state['lama_pengiriman_hari'], cmap=cmap, s=100)
plt.xlabel('State Penjual')
plt.ylabel('State Pembeli')

plt.colorbar(label='Lama Pengiriman (Hari)')
plt.show()

st.pyplot(fig)

#Pertanyaan 3
st.subheader('Berapa rata-rata payment value dari tiap tipe transaksi? dan transaksi tipe apa yang paling sering digunakan?')

df_payment = orders.groupby(by="payment_type")["payment_value"].mean().reset_index()

fig= plt.figure(figsize=(10, 5))

colors = ["#800000", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot( 
    x="payment_type",
    y="payment_value",
    data=df_payment.sort_values(by="payment_value", ascending = False),
    palette=colors
)
plt.title("persebaran pembelian berdasarkan bagian hari", loc="center", fontsize=15)
plt.ylabel("nilai transaksi")
plt.xlabel(None)
plt.tick_params(axis='x', labelsize=12)

st.pyplot(fig)

df_payment = orders.groupby(by="payment_type")["order_id"].nunique().reset_index()
palette_color = sns.color_palette('Reds') 

plt.pie(df_payment["order_id"], labels=df_payment["payment_type"], colors=palette_color, autopct='%.0f%%')
plt.title("Payment Type Distribution")

#Pertanyaan 4: 
st.subheader('Bagaimana perbandingan penjualan tahun 2017 dan 2018?')

orders['nomor_bulan'] = orders['order_purchase_timestamp'].dt.strftime('%m')
df_tanggal_penjualan = orders.groupby(by=["nomor_bulan","year"]).order_id.nunique().reset_index()
df_tanggal_penjualan["nomor_bulan"] = df_tanggal_penjualan["nomor_bulan"].astype(str).astype(int)
df_tanggal_penjualan = df_tanggal_penjualan[df_tanggal_penjualan["nomor_bulan"] < 9]

month_names = {
    1: 'Jan',
    2: 'Feb',
    3: 'Mar',
    4: 'Apr',
    5: 'Mei',
    6: 'Jun',
    7: 'Jul',
    8: 'Aug'
}
df_tanggal_penjualan['nama_bulan'] = df_tanggal_penjualan['nomor_bulan'].map(month_names)

fig = plt.figure(figsize=(20, 6))

custom_palette = ["#FFC0CB", "#800000"]  
sns.catplot(x='nama_bulan', y='order_id', hue='year', data=df_tanggal_penjualan, kind='bar', height=6, aspect=2, palette = custom_palette)
plt.ylabel("total order")
plt.xlabel(None)

st.pyplot(fig)

#Pertanyaan 5: 
st.subheader('Bulan apa yang terjadi peningkatan penjualan tertinggi?')

df_tanggal =  orders.groupby(by=["month","year"]).order_id.nunique().reset_index()
df_tanggal["month"] = pd.to_datetime(df_tanggal["month"], format='%m-%Y')

fig = plt.figure(figsize=(20, 6))

ax = sns.lineplot(x='month', y='order_id', data=df_tanggal, estimator=None,linewidth=3)
ax.set(xticks=df_tanggal.month.values)

plt.title("Tren Pertumbuhan Penjualan", loc="center", fontsize=18)
plt.ylabel("total order")
plt.xlabel(None)
ax.grid(False)
for tick in ax.get_xticklabels():
    tick.set_rotation(45)
    
st.pyplot(fig)
    
#Pertanyaan 6: 
st.subheader('Hari apa yang sering digunakan oleh pembeli untuk melakukan transaksi?')
df_bagian_hari = orders.groupby(by="waktu_hari_pembelian")["order_id"].nunique().reset_index()
df_bagian_hari.rename(columns={
    "order_id": "total_orders"
}, inplace=True)

fig = plt.figure(figsize=(10, 5))

colors = ["#D3D3D3", "#D3D3D3", "#800000", "#D3D3D3"]

sns.barplot( 
    x="waktu_hari_pembelian",
    y="total_orders",
    data=df_bagian_hari.sort_values(by="total_orders"),
    palette=colors
)
plt.title("persebaran pembelian berdasarkan bagian hari", loc="center", fontsize=15)
plt.ylabel("total order")
plt.xlabel(None)
plt.tick_params(axis='x', labelsize=12)
st.pyplot(fig)

df_hari = orders.groupby(by="hari_pembelian").order_id.nunique().sort_values(ascending=False).reset_index()
df_hari.rename(columns={
    "order_id": "total_orders"
}, inplace=True)

fig=plt.figure(figsize=(10, 5))

colors = ["#D3D3D3", "#D3D3D3","#D3D3D3", "#D3D3D3","#D3D3D3", "#D3D3D3", "#800000"]

sns.barplot( 
    x="hari_pembelian",
    y="total_orders",
    data=df_hari.sort_values(by="total_orders"),
    palette=colors
)
plt.title("persebaran pembelian berdasarkan hari", loc="center", fontsize=15)
plt.ylabel("total order")
plt.xlabel(None)
plt.tick_params(axis='x', labelsize=12)
st.pyplot(fig)

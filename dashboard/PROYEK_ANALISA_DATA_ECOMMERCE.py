{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "18d026fa",
   "metadata": {},
   "source": [
    "# PROYEK ANALISA DATA E-COMMERCE\n",
    "Nama : Rizki Ramadhana\n",
    "Email : rizkiramadhana.contact@gmail.com\n",
    "ID Dicoding : rizki_ramadhana_x"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ed860b87",
   "metadata": {
    "papermill": {
     "duration": 0.022137,
     "end_time": "2023-10-18T10:08:14.685290",
     "exception": False,
     "start_time": "2023-10-18T10:08:14.663153",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# Menentukan Pertanyaan Bisnis\n",
    "1. Category barang yang paling banyak dibeli dan paling sedikit diminati? \n",
    "2. Berapa lama rata-rata pengiriman paket pengiriman paket terlama ? dari mana ke mana?\n",
    "3. Berapa rata-rata payment value dari tiap tipe transaksi? dan transaksi tipe apa yang paling sering digunakan?\n",
    "4. Bagaimana perbandingan penjualan tahun 2017 dan 2018?\n",
    "5. Bulan apa yang terjadi peningkatan penjualan tertinggi? \n",
    "6. Bagian hari apa yang sering digunakan oleh pembeli untuk melakukan transaksi?"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "83f08839",
   "metadata": {
    "papermill": {
     "duration": 0.021601,
     "end_time": "2023-10-18T10:08:14.737207",
     "exception": false,
     "start_time": "2023-10-18T10:08:14.715606",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# Menyiapkan semua library yang dibutuhkan"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "6290c382",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:14.782464Z",
     "iopub.status.busy": "2023-10-18T10:08:14.781762Z",
     "iopub.status.idle": "2023-10-18T10:08:16.780728Z",
     "shell.execute_reply": "2023-10-18T10:08:16.779546Z"
    },
    "papermill": {
     "duration": 2.024841,
     "end_time": "2023-10-18T10:08:16.783537",
     "exception": false,
     "start_time": "2023-10-18T10:08:14.758696",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "import numpy as np \n",
    "import pandas as pd \n",
    "import os\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "9ad21d3d",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:16.825418Z",
     "iopub.status.busy": "2023-10-18T10:08:16.824927Z",
     "iopub.status.idle": "2023-10-18T10:08:16.829811Z",
     "shell.execute_reply": "2023-10-18T10:08:16.828764Z"
    },
    "papermill": {
     "duration": 0.028246,
     "end_time": "2023-10-18T10:08:16.832083",
     "exception": false,
     "start_time": "2023-10-18T10:08:16.803837",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "import warnings\n",
    "warnings.filterwarnings(\"ignore\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3bd4b54b",
   "metadata": {
    "papermill": {
     "duration": 0.019714,
     "end_time": "2023-10-18T10:08:16.933191",
     "exception": false,
     "start_time": "2023-10-18T10:08:16.913477",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# Data Wrangling\n",
    "## Gathering Data\n",
    "Menggabungkan data dan menghapus kolom yang tidak akan dianalisis."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b457fe1c",
   "metadata": {},
   "outputs": [],
   "source": [
    "customer = pd.read_csv('customers_dataset.csv')\n",
    "orders = pd.read_csv('orders_dataset.csv')\n",
    "order_reviews = pd.read_csv('order_reviews_dataset.csv')\n",
    "payments = pd.read_csv('order_payments_dataset.csv')\n",
    "order_items = pd.read_csv('order_items_dataset.csv')\n",
    "products = pd.read_csv('products_dataset.csv')\n",
    "sellers = pd.read_csv('sellers_dataset.csv')\n",
    "geolocation = pd.read_csv('geolocation_dataset.csv')\n",
    "products_translation = pd.read_csv('product_category_name_translation.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "0d045c15",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:17.037000Z",
     "iopub.status.busy": "2023-10-18T10:08:17.036601Z",
     "iopub.status.idle": "2023-10-18T10:08:17.463358Z",
     "shell.execute_reply": "2023-10-18T10:08:17.462379Z"
    },
    "papermill": {
     "duration": 0.45232,
     "end_time": "2023-10-18T10:08:17.467091",
     "exception": false,
     "start_time": "2023-10-18T10:08:17.014771",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(99441, 5)\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>customer_id</th>\n",
       "      <th>customer_unique_id</th>\n",
       "      <th>customer_zip_code_prefix</th>\n",
       "      <th>customer_city</th>\n",
       "      <th>customer_state</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>06b8999e2fba1a1fbc88172c00ba8bc7</td>\n",
       "      <td>861eff4711a542e4b93843c6dd7febb0</td>\n",
       "      <td>14409</td>\n",
       "      <td>franca</td>\n",
       "      <td>SP</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>18955e83d337fd6b2def6b18a428ac77</td>\n",
       "      <td>290c77bc529b7ac935b93aa66c333dc3</td>\n",
       "      <td>9790</td>\n",
       "      <td>sao bernardo do campo</td>\n",
       "      <td>SP</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>4e7b3e00288586ebd08712fdd0374a03</td>\n",
       "      <td>060e732b5b29e8181a18229c7b0b2b5e</td>\n",
       "      <td>1151</td>\n",
       "      <td>sao paulo</td>\n",
       "      <td>SP</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>b2b6027bc5c5109e529d4dc6358b12c3</td>\n",
       "      <td>259dac757896d24d7702b9acbbff3f3c</td>\n",
       "      <td>8775</td>\n",
       "      <td>mogi das cruzes</td>\n",
       "      <td>SP</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4f2d8ab171c80ec8364f7c12e35b23ad</td>\n",
       "      <td>345ecd01c38d18a9036ed96c73b8d066</td>\n",
       "      <td>13056</td>\n",
       "      <td>campinas</td>\n",
       "      <td>SP</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                        customer_id                customer_unique_id  \\\n",
       "0  06b8999e2fba1a1fbc88172c00ba8bc7  861eff4711a542e4b93843c6dd7febb0   \n",
       "1  18955e83d337fd6b2def6b18a428ac77  290c77bc529b7ac935b93aa66c333dc3   \n",
       "2  4e7b3e00288586ebd08712fdd0374a03  060e732b5b29e8181a18229c7b0b2b5e   \n",
       "3  b2b6027bc5c5109e529d4dc6358b12c3  259dac757896d24d7702b9acbbff3f3c   \n",
       "4  4f2d8ab171c80ec8364f7c12e35b23ad  345ecd01c38d18a9036ed96c73b8d066   \n",
       "\n",
       "   customer_zip_code_prefix          customer_city customer_state  \n",
       "0                     14409                 franca             SP  \n",
       "1                      9790  sao bernardo do campo             SP  \n",
       "2                      1151              sao paulo             SP  \n",
       "3                      8775        mogi das cruzes             SP  \n",
       "4                     13056               campinas             SP  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(customer.shape)\n",
    "customer.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "85b0eaca",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:17.512236Z",
     "iopub.status.busy": "2023-10-18T10:08:17.511815Z",
     "iopub.status.idle": "2023-10-18T10:08:18.053532Z",
     "shell.execute_reply": "2023-10-18T10:08:18.052359Z"
    },
    "papermill": {
     "duration": 0.566692,
     "end_time": "2023-10-18T10:08:18.055667",
     "exception": false,
     "start_time": "2023-10-18T10:08:17.488975",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(112650, 7)\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>order_id</th>\n",
       "      <th>order_item_id</th>\n",
       "      <th>product_id</th>\n",
       "      <th>seller_id</th>\n",
       "      <th>shipping_limit_date</th>\n",
       "      <th>price</th>\n",
       "      <th>freight_value</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>00010242fe8c5a6d1ba2dd792cb16214</td>\n",
       "      <td>1</td>\n",
       "      <td>4244733e06e7ecb4970a6e2683c13e61</td>\n",
       "      <td>48436dade18ac8b2bce089ec2a041202</td>\n",
       "      <td>2017-09-19 09:45:35</td>\n",
       "      <td>58.90</td>\n",
       "      <td>13.29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>00018f77f2f0320c557190d7a144bdd3</td>\n",
       "      <td>1</td>\n",
       "      <td>e5f2d52b802189ee658865ca93d83a8f</td>\n",
       "      <td>dd7ddc04e1b6c2c614352b383efe2d36</td>\n",
       "      <td>2017-05-03 11:05:13</td>\n",
       "      <td>239.90</td>\n",
       "      <td>19.93</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>000229ec398224ef6ca0657da4fc703e</td>\n",
       "      <td>1</td>\n",
       "      <td>c777355d18b72b67abbeef9df44fd0fd</td>\n",
       "      <td>5b51032eddd242adc84c38acab88f23d</td>\n",
       "      <td>2018-01-18 14:48:30</td>\n",
       "      <td>199.00</td>\n",
       "      <td>17.87</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>00024acbcdf0a6daa1e931b038114c75</td>\n",
       "      <td>1</td>\n",
       "      <td>7634da152a4610f1595efa32f14722fc</td>\n",
       "      <td>9d7a1d34a5052409006425275ba1c2b4</td>\n",
       "      <td>2018-08-15 10:10:18</td>\n",
       "      <td>12.99</td>\n",
       "      <td>12.79</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>00042b26cf59d7ce69dfabb4e55b4fd9</td>\n",
       "      <td>1</td>\n",
       "      <td>ac6c3623068f30de03045865e4e10089</td>\n",
       "      <td>df560393f3a51e74553ab94004ba5c87</td>\n",
       "      <td>2017-02-13 13:57:51</td>\n",
       "      <td>199.90</td>\n",
       "      <td>18.14</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                           order_id  order_item_id  \\\n",
       "0  00010242fe8c5a6d1ba2dd792cb16214              1   \n",
       "1  00018f77f2f0320c557190d7a144bdd3              1   \n",
       "2  000229ec398224ef6ca0657da4fc703e              1   \n",
       "3  00024acbcdf0a6daa1e931b038114c75              1   \n",
       "4  00042b26cf59d7ce69dfabb4e55b4fd9              1   \n",
       "\n",
       "                         product_id                         seller_id  \\\n",
       "0  4244733e06e7ecb4970a6e2683c13e61  48436dade18ac8b2bce089ec2a041202   \n",
       "1  e5f2d52b802189ee658865ca93d83a8f  dd7ddc04e1b6c2c614352b383efe2d36   \n",
       "2  c777355d18b72b67abbeef9df44fd0fd  5b51032eddd242adc84c38acab88f23d   \n",
       "3  7634da152a4610f1595efa32f14722fc  9d7a1d34a5052409006425275ba1c2b4   \n",
       "4  ac6c3623068f30de03045865e4e10089  df560393f3a51e74553ab94004ba5c87   \n",
       "\n",
       "   shipping_limit_date   price  freight_value  \n",
       "0  2017-09-19 09:45:35   58.90          13.29  \n",
       "1  2017-05-03 11:05:13  239.90          19.93  \n",
       "2  2018-01-18 14:48:30  199.00          17.87  \n",
       "3  2018-08-15 10:10:18   12.99          12.79  \n",
       "4  2017-02-13 13:57:51  199.90          18.14  "
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#order_items = pd.read_csv(\"/kaggle/input/brazilian-ecommerce/olist_order_items_dataset.csv\")\n",
    "print(order_items.shape)\n",
    "order_items.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "9a2c0921",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:18.101565Z",
     "iopub.status.busy": "2023-10-18T10:08:18.101203Z",
     "iopub.status.idle": "2023-10-18T10:08:18.352601Z",
     "shell.execute_reply": "2023-10-18T10:08:18.351485Z"
    },
    "papermill": {
     "duration": 0.277427,
     "end_time": "2023-10-18T10:08:18.354836",
     "exception": false,
     "start_time": "2023-10-18T10:08:18.077409",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(103886, 5)\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>order_id</th>\n",
       "      <th>payment_sequential</th>\n",
       "      <th>payment_type</th>\n",
       "      <th>payment_installments</th>\n",
       "      <th>payment_value</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>b81ef226f3fe1789b1e8b2acac839d17</td>\n",
       "      <td>1</td>\n",
       "      <td>credit_card</td>\n",
       "      <td>8</td>\n",
       "      <td>99.33</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>a9810da82917af2d9aefd1278f1dcfa0</td>\n",
       "      <td>1</td>\n",
       "      <td>credit_card</td>\n",
       "      <td>1</td>\n",
       "      <td>24.39</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>25e8ea4e93396b6fa0d3dd708e76c1bd</td>\n",
       "      <td>1</td>\n",
       "      <td>credit_card</td>\n",
       "      <td>1</td>\n",
       "      <td>65.71</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>ba78997921bbcdc1373bb41e913ab953</td>\n",
       "      <td>1</td>\n",
       "      <td>credit_card</td>\n",
       "      <td>8</td>\n",
       "      <td>107.78</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>42fdf880ba16b47b59251dd489d4441a</td>\n",
       "      <td>1</td>\n",
       "      <td>credit_card</td>\n",
       "      <td>2</td>\n",
       "      <td>128.45</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                           order_id  payment_sequential payment_type  \\\n",
       "0  b81ef226f3fe1789b1e8b2acac839d17                   1  credit_card   \n",
       "1  a9810da82917af2d9aefd1278f1dcfa0                   1  credit_card   \n",
       "2  25e8ea4e93396b6fa0d3dd708e76c1bd                   1  credit_card   \n",
       "3  ba78997921bbcdc1373bb41e913ab953                   1  credit_card   \n",
       "4  42fdf880ba16b47b59251dd489d4441a                   1  credit_card   \n",
       "\n",
       "   payment_installments  payment_value  \n",
       "0                     8          99.33  \n",
       "1                     1          24.39  \n",
       "2                     1          65.71  \n",
       "3                     8         107.78  \n",
       "4                     2         128.45  "
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#payments = pd.read_csv(\"/kaggle/input/brazilian-ecommerce/olist_order_payments_dataset.csv\")\n",
    "print(payments.shape)\n",
    "payments.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "2bf4d603",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:18.400404Z",
     "iopub.status.busy": "2023-10-18T10:08:18.400077Z",
     "iopub.status.idle": "2023-10-18T10:08:19.102026Z",
     "shell.execute_reply": "2023-10-18T10:08:19.101022Z"
    },
    "papermill": {
     "duration": 0.727926,
     "end_time": "2023-10-18T10:08:19.104303",
     "exception": false,
     "start_time": "2023-10-18T10:08:18.376377",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(99441, 8)\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>order_id</th>\n",
       "      <th>customer_id</th>\n",
       "      <th>order_status</th>\n",
       "      <th>order_purchase_timestamp</th>\n",
       "      <th>order_approved_at</th>\n",
       "      <th>order_delivered_carrier_date</th>\n",
       "      <th>order_delivered_customer_date</th>\n",
       "      <th>order_estimated_delivery_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>e481f51cbdc54678b7cc49136f2d6af7</td>\n",
       "      <td>9ef432eb6251297304e76186b10a928d</td>\n",
       "      <td>delivered</td>\n",
       "      <td>2017-10-02 10:56:33</td>\n",
       "      <td>2017-10-02 11:07:15</td>\n",
       "      <td>2017-10-04 19:55:00</td>\n",
       "      <td>2017-10-10 21:25:13</td>\n",
       "      <td>2017-10-18 00:00:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>53cdb2fc8bc7dce0b6741e2150273451</td>\n",
       "      <td>b0830fb4747a6c6d20dea0b8c802d7ef</td>\n",
       "      <td>delivered</td>\n",
       "      <td>2018-07-24 20:41:37</td>\n",
       "      <td>2018-07-26 03:24:27</td>\n",
       "      <td>2018-07-26 14:31:00</td>\n",
       "      <td>2018-08-07 15:27:45</td>\n",
       "      <td>2018-08-13 00:00:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>47770eb9100c2d0c44946d9cf07ec65d</td>\n",
       "      <td>41ce2a54c0b03bf3443c3d931a367089</td>\n",
       "      <td>delivered</td>\n",
       "      <td>2018-08-08 08:38:49</td>\n",
       "      <td>2018-08-08 08:55:23</td>\n",
       "      <td>2018-08-08 13:50:00</td>\n",
       "      <td>2018-08-17 18:06:29</td>\n",
       "      <td>2018-09-04 00:00:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>949d5b44dbf5de918fe9c16f97b45f8a</td>\n",
       "      <td>f88197465ea7920adcdbec7375364d82</td>\n",
       "      <td>delivered</td>\n",
       "      <td>2017-11-18 19:28:06</td>\n",
       "      <td>2017-11-18 19:45:59</td>\n",
       "      <td>2017-11-22 13:39:59</td>\n",
       "      <td>2017-12-02 00:28:42</td>\n",
       "      <td>2017-12-15 00:00:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>ad21c59c0840e6cb83a9ceb5573f8159</td>\n",
       "      <td>8ab97904e6daea8866dbdbc4fb7aad2c</td>\n",
       "      <td>delivered</td>\n",
       "      <td>2018-02-13 21:18:39</td>\n",
       "      <td>2018-02-13 22:20:29</td>\n",
       "      <td>2018-02-14 19:46:34</td>\n",
       "      <td>2018-02-16 18:17:02</td>\n",
       "      <td>2018-02-26 00:00:00</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                           order_id                       customer_id  \\\n",
       "0  e481f51cbdc54678b7cc49136f2d6af7  9ef432eb6251297304e76186b10a928d   \n",
       "1  53cdb2fc8bc7dce0b6741e2150273451  b0830fb4747a6c6d20dea0b8c802d7ef   \n",
       "2  47770eb9100c2d0c44946d9cf07ec65d  41ce2a54c0b03bf3443c3d931a367089   \n",
       "3  949d5b44dbf5de918fe9c16f97b45f8a  f88197465ea7920adcdbec7375364d82   \n",
       "4  ad21c59c0840e6cb83a9ceb5573f8159  8ab97904e6daea8866dbdbc4fb7aad2c   \n",
       "\n",
       "  order_status order_purchase_timestamp    order_approved_at  \\\n",
       "0    delivered      2017-10-02 10:56:33  2017-10-02 11:07:15   \n",
       "1    delivered      2018-07-24 20:41:37  2018-07-26 03:24:27   \n",
       "2    delivered      2018-08-08 08:38:49  2018-08-08 08:55:23   \n",
       "3    delivered      2017-11-18 19:28:06  2017-11-18 19:45:59   \n",
       "4    delivered      2018-02-13 21:18:39  2018-02-13 22:20:29   \n",
       "\n",
       "  order_delivered_carrier_date order_delivered_customer_date  \\\n",
       "0          2017-10-04 19:55:00           2017-10-10 21:25:13   \n",
       "1          2018-07-26 14:31:00           2018-08-07 15:27:45   \n",
       "2          2018-08-08 13:50:00           2018-08-17 18:06:29   \n",
       "3          2017-11-22 13:39:59           2017-12-02 00:28:42   \n",
       "4          2018-02-14 19:46:34           2018-02-16 18:17:02   \n",
       "\n",
       "  order_estimated_delivery_date  \n",
       "0           2017-10-18 00:00:00  \n",
       "1           2018-08-13 00:00:00  \n",
       "2           2018-09-04 00:00:00  \n",
       "3           2017-12-15 00:00:00  \n",
       "4           2018-02-26 00:00:00  "
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#orders = pd.read_csv(\"/kaggle/input/brazilian-ecommerce/olist_orders_dataset.csv\")\n",
    "print(orders.shape)\n",
    "orders.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "13f50650",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:19.150061Z",
     "iopub.status.busy": "2023-10-18T10:08:19.149707Z",
     "iopub.status.idle": "2023-10-18T10:08:19.253718Z",
     "shell.execute_reply": "2023-10-18T10:08:19.252574Z"
    },
    "papermill": {
     "duration": 0.129447,
     "end_time": "2023-10-18T10:08:19.255938",
     "exception": false,
     "start_time": "2023-10-18T10:08:19.126491",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(32951, 9)\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>product_id</th>\n",
       "      <th>product_category_name</th>\n",
       "      <th>product_name_lenght</th>\n",
       "      <th>product_description_lenght</th>\n",
       "      <th>product_photos_qty</th>\n",
       "      <th>product_weight_g</th>\n",
       "      <th>product_length_cm</th>\n",
       "      <th>product_height_cm</th>\n",
       "      <th>product_width_cm</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1e9e8ef04dbcff4541ed26657ea517e5</td>\n",
       "      <td>perfumaria</td>\n",
       "      <td>40.0</td>\n",
       "      <td>287.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>225.0</td>\n",
       "      <td>16.0</td>\n",
       "      <td>10.0</td>\n",
       "      <td>14.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>3aa071139cb16b67ca9e5dea641aaa2f</td>\n",
       "      <td>artes</td>\n",
       "      <td>44.0</td>\n",
       "      <td>276.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1000.0</td>\n",
       "      <td>30.0</td>\n",
       "      <td>18.0</td>\n",
       "      <td>20.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>96bd76ec8810374ed1b65e291975717f</td>\n",
       "      <td>esporte_lazer</td>\n",
       "      <td>46.0</td>\n",
       "      <td>250.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>154.0</td>\n",
       "      <td>18.0</td>\n",
       "      <td>9.0</td>\n",
       "      <td>15.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>cef67bcfe19066a932b7673e239eb23d</td>\n",
       "      <td>bebes</td>\n",
       "      <td>27.0</td>\n",
       "      <td>261.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>371.0</td>\n",
       "      <td>26.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>26.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>9dc1a7de274444849c219cff195d0b71</td>\n",
       "      <td>utilidades_domesticas</td>\n",
       "      <td>37.0</td>\n",
       "      <td>402.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>625.0</td>\n",
       "      <td>20.0</td>\n",
       "      <td>17.0</td>\n",
       "      <td>13.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                         product_id  product_category_name  \\\n",
       "0  1e9e8ef04dbcff4541ed26657ea517e5             perfumaria   \n",
       "1  3aa071139cb16b67ca9e5dea641aaa2f                  artes   \n",
       "2  96bd76ec8810374ed1b65e291975717f          esporte_lazer   \n",
       "3  cef67bcfe19066a932b7673e239eb23d                  bebes   \n",
       "4  9dc1a7de274444849c219cff195d0b71  utilidades_domesticas   \n",
       "\n",
       "   product_name_lenght  product_description_lenght  product_photos_qty  \\\n",
       "0                 40.0                       287.0                 1.0   \n",
       "1                 44.0                       276.0                 1.0   \n",
       "2                 46.0                       250.0                 1.0   \n",
       "3                 27.0                       261.0                 1.0   \n",
       "4                 37.0                       402.0                 4.0   \n",
       "\n",
       "   product_weight_g  product_length_cm  product_height_cm  product_width_cm  \n",
       "0             225.0               16.0               10.0              14.0  \n",
       "1            1000.0               30.0               18.0              20.0  \n",
       "2             154.0               18.0                9.0              15.0  \n",
       "3             371.0               26.0                4.0              26.0  \n",
       "4             625.0               20.0               17.0              13.0  "
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#products = pd.read_csv(\"/kaggle/input/brazilian-ecommerce/olist_products_dataset.csv\")\n",
    "print(products.shape)\n",
    "products.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "511efcb5",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:19.300603Z",
     "iopub.status.busy": "2023-10-18T10:08:19.300240Z",
     "iopub.status.idle": "2023-10-18T10:08:19.323334Z",
     "shell.execute_reply": "2023-10-18T10:08:19.321749Z"
    },
    "papermill": {
     "duration": 0.048169,
     "end_time": "2023-10-18T10:08:19.325628",
     "exception": false,
     "start_time": "2023-10-18T10:08:19.277459",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>seller_id</th>\n",
       "      <th>seller_zip_code_prefix</th>\n",
       "      <th>seller_city</th>\n",
       "      <th>seller_state</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>3442f8959a84dea7ee197c632cb2df15</td>\n",
       "      <td>13023</td>\n",
       "      <td>campinas</td>\n",
       "      <td>SP</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>d1b65fc7debc3361ea86b5f14c68d2e2</td>\n",
       "      <td>13844</td>\n",
       "      <td>mogi guacu</td>\n",
       "      <td>SP</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>ce3ad9de960102d0677a81f5d0bb7b2d</td>\n",
       "      <td>20031</td>\n",
       "      <td>rio de janeiro</td>\n",
       "      <td>RJ</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>c0f3eea2e14555b6faeea3dd58c1b1c3</td>\n",
       "      <td>4195</td>\n",
       "      <td>sao paulo</td>\n",
       "      <td>SP</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>51a04a8a6bdcb23deccc82b0b80742cf</td>\n",
       "      <td>12914</td>\n",
       "      <td>braganca paulista</td>\n",
       "      <td>SP</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                          seller_id  seller_zip_code_prefix  \\\n",
       "0  3442f8959a84dea7ee197c632cb2df15                   13023   \n",
       "1  d1b65fc7debc3361ea86b5f14c68d2e2                   13844   \n",
       "2  ce3ad9de960102d0677a81f5d0bb7b2d                   20031   \n",
       "3  c0f3eea2e14555b6faeea3dd58c1b1c3                    4195   \n",
       "4  51a04a8a6bdcb23deccc82b0b80742cf                   12914   \n",
       "\n",
       "         seller_city seller_state  \n",
       "0           campinas           SP  \n",
       "1         mogi guacu           SP  \n",
       "2     rio de janeiro           RJ  \n",
       "3          sao paulo           SP  \n",
       "4  braganca paulista           SP  "
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#sellers = pd.read_csv(\"/kaggle/input/brazilian-ecommerce/olist_sellers_dataset.csv\")\n",
    "sellers.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "0cb66649",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:19.370011Z",
     "iopub.status.busy": "2023-10-18T10:08:19.369650Z",
     "iopub.status.idle": "2023-10-18T10:08:19.384975Z",
     "shell.execute_reply": "2023-10-18T10:08:19.384011Z"
    },
    "papermill": {
     "duration": 0.03977,
     "end_time": "2023-10-18T10:08:19.386892",
     "exception": false,
     "start_time": "2023-10-18T10:08:19.347122",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(71, 2)\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>product_category_name</th>\n",
       "      <th>product_category_name_english</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>beleza_saude</td>\n",
       "      <td>health_beauty</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>informatica_acessorios</td>\n",
       "      <td>computers_accessories</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>automotivo</td>\n",
       "      <td>auto</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>cama_mesa_banho</td>\n",
       "      <td>bed_bath_table</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>moveis_decoracao</td>\n",
       "      <td>furniture_decor</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    product_category_name product_category_name_english\n",
       "0            beleza_saude                 health_beauty\n",
       "1  informatica_acessorios         computers_accessories\n",
       "2              automotivo                          auto\n",
       "3         cama_mesa_banho                bed_bath_table\n",
       "4        moveis_decoracao               furniture_decor"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#products_translation = pd.read_csv(\"/kaggle/input/brazilian-ecommerce/product_category_name_translation.csv\")\n",
    "print(products_translation.shape)\n",
    "products_translation.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "19b053a6",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:19.432846Z",
     "iopub.status.busy": "2023-10-18T10:08:19.431723Z",
     "iopub.status.idle": "2023-10-18T10:08:20.913915Z",
     "shell.execute_reply": "2023-10-18T10:08:20.912937Z"
    },
    "papermill": {
     "duration": 1.507639,
     "end_time": "2023-10-18T10:08:20.916343",
     "exception": false,
     "start_time": "2023-10-18T10:08:19.408704",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1000163, 5)\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>geolocation_zip_code_prefix</th>\n",
       "      <th>geolocation_lat</th>\n",
       "      <th>geolocation_lng</th>\n",
       "      <th>geolocation_city</th>\n",
       "      <th>geolocation_state</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1037</td>\n",
       "      <td>-23.545621</td>\n",
       "      <td>-46.639292</td>\n",
       "      <td>sao paulo</td>\n",
       "      <td>SP</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1046</td>\n",
       "      <td>-23.546081</td>\n",
       "      <td>-46.644820</td>\n",
       "      <td>sao paulo</td>\n",
       "      <td>SP</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1046</td>\n",
       "      <td>-23.546129</td>\n",
       "      <td>-46.642951</td>\n",
       "      <td>sao paulo</td>\n",
       "      <td>SP</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1041</td>\n",
       "      <td>-23.544392</td>\n",
       "      <td>-46.639499</td>\n",
       "      <td>sao paulo</td>\n",
       "      <td>SP</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1035</td>\n",
       "      <td>-23.541578</td>\n",
       "      <td>-46.641607</td>\n",
       "      <td>sao paulo</td>\n",
       "      <td>SP</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   geolocation_zip_code_prefix  geolocation_lat  geolocation_lng  \\\n",
       "0                         1037       -23.545621       -46.639292   \n",
       "1                         1046       -23.546081       -46.644820   \n",
       "2                         1046       -23.546129       -46.642951   \n",
       "3                         1041       -23.544392       -46.639499   \n",
       "4                         1035       -23.541578       -46.641607   \n",
       "\n",
       "  geolocation_city geolocation_state  \n",
       "0        sao paulo                SP  \n",
       "1        sao paulo                SP  \n",
       "2        sao paulo                SP  \n",
       "3        sao paulo                SP  \n",
       "4        sao paulo                SP  "
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#geolocation = pd.read_csv(\"/kaggle/input/brazilian-ecommerce/olist_geolocation_dataset.csv\")\n",
    "print(geolocation.shape)\n",
    "geolocation.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "d7ac15fb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(99224, 7)\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>review_id</th>\n",
       "      <th>order_id</th>\n",
       "      <th>review_score</th>\n",
       "      <th>review_comment_title</th>\n",
       "      <th>review_comment_message</th>\n",
       "      <th>review_creation_date</th>\n",
       "      <th>review_answer_timestamp</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>7bc2406110b926393aa56f80a40eba40</td>\n",
       "      <td>73fc7af87114b39712e6da79b0a377eb</td>\n",
       "      <td>4</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2018-01-18 00:00:00</td>\n",
       "      <td>2018-01-18 21:46:59</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>80e641a11e56f04c1ad469d5645fdfde</td>\n",
       "      <td>a548910a1c6147796b98fdf73dbeba33</td>\n",
       "      <td>5</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2018-03-10 00:00:00</td>\n",
       "      <td>2018-03-11 03:05:13</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>228ce5500dc1d8e020d8d1322874b6f0</td>\n",
       "      <td>f9e4b658b201a9f2ecdecbb34bed034b</td>\n",
       "      <td>5</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2018-02-17 00:00:00</td>\n",
       "      <td>2018-02-18 14:36:24</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>e64fb393e7b32834bb789ff8bb30750e</td>\n",
       "      <td>658677c97b385a9be170737859d3511b</td>\n",
       "      <td>5</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Recebi bem antes do prazo estipulado.</td>\n",
       "      <td>2017-04-21 00:00:00</td>\n",
       "      <td>2017-04-21 22:02:06</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>f7c4243c7fe1938f181bec41a392bdeb</td>\n",
       "      <td>8e6bfb81e283fa7e4f11123a3fb894f1</td>\n",
       "      <td>5</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Parabéns lojas lannister adorei comprar pela I...</td>\n",
       "      <td>2018-03-01 00:00:00</td>\n",
       "      <td>2018-03-02 10:26:53</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                          review_id                          order_id  \\\n",
       "0  7bc2406110b926393aa56f80a40eba40  73fc7af87114b39712e6da79b0a377eb   \n",
       "1  80e641a11e56f04c1ad469d5645fdfde  a548910a1c6147796b98fdf73dbeba33   \n",
       "2  228ce5500dc1d8e020d8d1322874b6f0  f9e4b658b201a9f2ecdecbb34bed034b   \n",
       "3  e64fb393e7b32834bb789ff8bb30750e  658677c97b385a9be170737859d3511b   \n",
       "4  f7c4243c7fe1938f181bec41a392bdeb  8e6bfb81e283fa7e4f11123a3fb894f1   \n",
       "\n",
       "   review_score review_comment_title  \\\n",
       "0             4                  NaN   \n",
       "1             5                  NaN   \n",
       "2             5                  NaN   \n",
       "3             5                  NaN   \n",
       "4             5                  NaN   \n",
       "\n",
       "                              review_comment_message review_creation_date  \\\n",
       "0                                                NaN  2018-01-18 00:00:00   \n",
       "1                                                NaN  2018-03-10 00:00:00   \n",
       "2                                                NaN  2018-02-17 00:00:00   \n",
       "3              Recebi bem antes do prazo estipulado.  2017-04-21 00:00:00   \n",
       "4  Parabéns lojas lannister adorei comprar pela I...  2018-03-01 00:00:00   \n",
       "\n",
       "  review_answer_timestamp  \n",
       "0     2018-01-18 21:46:59  \n",
       "1     2018-03-11 03:05:13  \n",
       "2     2018-02-18 14:36:24  \n",
       "3     2017-04-21 22:02:06  \n",
       "4     2018-03-02 10:26:53  "
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(order_reviews.shape)\n",
    "order_reviews.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fa79a5be",
   "metadata": {
    "papermill": {
     "duration": 0.022684,
     "end_time": "2023-10-18T10:08:20.962671",
     "exception": false,
     "start_time": "2023-10-18T10:08:20.939987",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "### Menggabungkan data dalam beberapa dataframe\n",
    "\n",
    "dalam proyek ini, terdapat 2 dataframe yang akan digunakan yaitu, `order_items` dan `orders`.\n",
    "<br>\n",
    "`order_items` : gabungan dari tabel order_items, products_translation, dan seller. <br>\n",
    "`orders` : gabungan dari tabel orders, payments, dan customer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "b346104d",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:21.009731Z",
     "iopub.status.busy": "2023-10-18T10:08:21.008533Z",
     "iopub.status.idle": "2023-10-18T10:08:21.039747Z",
     "shell.execute_reply": "2023-10-18T10:08:21.038633Z"
    },
    "papermill": {
     "duration": 0.057613,
     "end_time": "2023-10-18T10:08:21.042399",
     "exception": false,
     "start_time": "2023-10-18T10:08:20.984786",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# menggabugkan product dengan products_translation\n",
    "products = products.merge(products_translation, left_on='product_category_name', right_on='product_category_name',how='left')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "9c412805",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:21.089577Z",
     "iopub.status.busy": "2023-10-18T10:08:21.089228Z",
     "iopub.status.idle": "2023-10-18T10:08:21.111163Z",
     "shell.execute_reply": "2023-10-18T10:08:21.109952Z"
    },
    "papermill": {
     "duration": 0.048373,
     "end_time": "2023-10-18T10:08:21.113536",
     "exception": false,
     "start_time": "2023-10-18T10:08:21.065163",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(32951, 3)\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>product_id</th>\n",
       "      <th>product_category_name_english</th>\n",
       "      <th>product_category_name</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>105</th>\n",
       "      <td>a41e356c76fab66334f36de622ecbd3a</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>128</th>\n",
       "      <td>d8dee61c2034d6d075997acef1870e9b</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>145</th>\n",
       "      <td>56139431d72cd51f19eb9f7dae4d1617</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>154</th>\n",
       "      <td>46b48281eb6d663ced748f324108c733</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>197</th>\n",
       "      <td>5fb61f482620cb672f5e586bb132eae9</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>32515</th>\n",
       "      <td>b0a0c5dd78e644373b199380612c350a</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>32589</th>\n",
       "      <td>10dbe0fbaa2c505123c17fdc34a63c56</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>32616</th>\n",
       "      <td>bd2ada37b58ae94cc838b9c0569fecd8</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>32772</th>\n",
       "      <td>fa51e914046aab32764c41356b9d4ea4</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>32852</th>\n",
       "      <td>c4ceee876c82b8328e9c293fa0e1989b</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>623 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                             product_id product_category_name_english  \\\n",
       "105    a41e356c76fab66334f36de622ecbd3a                           NaN   \n",
       "128    d8dee61c2034d6d075997acef1870e9b                           NaN   \n",
       "145    56139431d72cd51f19eb9f7dae4d1617                           NaN   \n",
       "154    46b48281eb6d663ced748f324108c733                           NaN   \n",
       "197    5fb61f482620cb672f5e586bb132eae9                           NaN   \n",
       "...                                 ...                           ...   \n",
       "32515  b0a0c5dd78e644373b199380612c350a                           NaN   \n",
       "32589  10dbe0fbaa2c505123c17fdc34a63c56                           NaN   \n",
       "32616  bd2ada37b58ae94cc838b9c0569fecd8                           NaN   \n",
       "32772  fa51e914046aab32764c41356b9d4ea4                           NaN   \n",
       "32852  c4ceee876c82b8328e9c293fa0e1989b                           NaN   \n",
       "\n",
       "      product_category_name  \n",
       "105                     NaN  \n",
       "128                     NaN  \n",
       "145                     NaN  \n",
       "154                     NaN  \n",
       "197                     NaN  \n",
       "...                     ...  \n",
       "32515                   NaN  \n",
       "32589                   NaN  \n",
       "32616                   NaN  \n",
       "32772                   NaN  \n",
       "32852                   NaN  \n",
       "\n",
       "[623 rows x 3 columns]"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_product = products[[\"product_id\",\"product_category_name_english\",\"product_category_name\"]]\n",
    "print(df_product.shape)\n",
    "# df_product.head()\n",
    "df_product.loc[df_product[\"product_category_name_english\"].isnull()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "3a459803",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:21.162493Z",
     "iopub.status.busy": "2023-10-18T10:08:21.162100Z",
     "iopub.status.idle": "2023-10-18T10:08:21.223880Z",
     "shell.execute_reply": "2023-10-18T10:08:21.222759Z"
    },
    "papermill": {
     "duration": 0.089378,
     "end_time": "2023-10-18T10:08:21.226458",
     "exception": false,
     "start_time": "2023-10-18T10:08:21.137080",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# menggabugkan order_items dengan df_products menjadi df_order_items\n",
    "# order_items = order_items.drop(columns = ['shipping_limit_date'])\n",
    "df_order_items = order_items.merge(products, left_on='product_id', right_on='product_id',how='left')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "779b5bfa",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:21.276703Z",
     "iopub.status.busy": "2023-10-18T10:08:21.276299Z",
     "iopub.status.idle": "2023-10-18T10:08:21.331267Z",
     "shell.execute_reply": "2023-10-18T10:08:21.330158Z"
    },
    "papermill": {
     "duration": 0.083931,
     "end_time": "2023-10-18T10:08:21.333099",
     "exception": false,
     "start_time": "2023-10-18T10:08:21.249168",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(112650, 18)\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>order_id</th>\n",
       "      <th>order_item_id</th>\n",
       "      <th>product_id</th>\n",
       "      <th>seller_id</th>\n",
       "      <th>shipping_limit_date</th>\n",
       "      <th>price</th>\n",
       "      <th>freight_value</th>\n",
       "      <th>product_category_name</th>\n",
       "      <th>product_name_lenght</th>\n",
       "      <th>product_description_lenght</th>\n",
       "      <th>product_photos_qty</th>\n",
       "      <th>product_weight_g</th>\n",
       "      <th>product_length_cm</th>\n",
       "      <th>product_height_cm</th>\n",
       "      <th>product_width_cm</th>\n",
       "      <th>product_category_name_english</th>\n",
       "      <th>seller_city</th>\n",
       "      <th>seller_state</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>00010242fe8c5a6d1ba2dd792cb16214</td>\n",
       "      <td>1</td>\n",
       "      <td>4244733e06e7ecb4970a6e2683c13e61</td>\n",
       "      <td>48436dade18ac8b2bce089ec2a041202</td>\n",
       "      <td>2017-09-19 09:45:35</td>\n",
       "      <td>58.90</td>\n",
       "      <td>13.29</td>\n",
       "      <td>cool_stuff</td>\n",
       "      <td>58.0</td>\n",
       "      <td>598.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>650.0</td>\n",
       "      <td>28.0</td>\n",
       "      <td>9.0</td>\n",
       "      <td>14.0</td>\n",
       "      <td>cool_stuff</td>\n",
       "      <td>volta redonda</td>\n",
       "      <td>SP</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>00018f77f2f0320c557190d7a144bdd3</td>\n",
       "      <td>1</td>\n",
       "      <td>e5f2d52b802189ee658865ca93d83a8f</td>\n",
       "      <td>dd7ddc04e1b6c2c614352b383efe2d36</td>\n",
       "      <td>2017-05-03 11:05:13</td>\n",
       "      <td>239.90</td>\n",
       "      <td>19.93</td>\n",
       "      <td>pet_shop</td>\n",
       "      <td>56.0</td>\n",
       "      <td>239.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>30000.0</td>\n",
       "      <td>50.0</td>\n",
       "      <td>30.0</td>\n",
       "      <td>40.0</td>\n",
       "      <td>pet_shop</td>\n",
       "      <td>sao paulo</td>\n",
       "      <td>SP</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>000229ec398224ef6ca0657da4fc703e</td>\n",
       "      <td>1</td>\n",
       "      <td>c777355d18b72b67abbeef9df44fd0fd</td>\n",
       "      <td>5b51032eddd242adc84c38acab88f23d</td>\n",
       "      <td>2018-01-18 14:48:30</td>\n",
       "      <td>199.00</td>\n",
       "      <td>17.87</td>\n",
       "      <td>moveis_decoracao</td>\n",
       "      <td>59.0</td>\n",
       "      <td>695.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>3050.0</td>\n",
       "      <td>33.0</td>\n",
       "      <td>13.0</td>\n",
       "      <td>33.0</td>\n",
       "      <td>furniture_decor</td>\n",
       "      <td>borda da mata</td>\n",
       "      <td>MG</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>00024acbcdf0a6daa1e931b038114c75</td>\n",
       "      <td>1</td>\n",
       "      <td>7634da152a4610f1595efa32f14722fc</td>\n",
       "      <td>9d7a1d34a5052409006425275ba1c2b4</td>\n",
       "      <td>2018-08-15 10:10:18</td>\n",
       "      <td>12.99</td>\n",
       "      <td>12.79</td>\n",
       "      <td>perfumaria</td>\n",
       "      <td>42.0</td>\n",
       "      <td>480.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>200.0</td>\n",
       "      <td>16.0</td>\n",
       "      <td>10.0</td>\n",
       "      <td>15.0</td>\n",
       "      <td>perfumery</td>\n",
       "      <td>franca</td>\n",
       "      <td>SP</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>00042b26cf59d7ce69dfabb4e55b4fd9</td>\n",
       "      <td>1</td>\n",
       "      <td>ac6c3623068f30de03045865e4e10089</td>\n",
       "      <td>df560393f3a51e74553ab94004ba5c87</td>\n",
       "      <td>2017-02-13 13:57:51</td>\n",
       "      <td>199.90</td>\n",
       "      <td>18.14</td>\n",
       "      <td>ferramentas_jardim</td>\n",
       "      <td>59.0</td>\n",
       "      <td>409.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>3750.0</td>\n",
       "      <td>35.0</td>\n",
       "      <td>40.0</td>\n",
       "      <td>30.0</td>\n",
       "      <td>garden_tools</td>\n",
       "      <td>loanda</td>\n",
       "      <td>PR</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                           order_id  order_item_id  \\\n",
       "0  00010242fe8c5a6d1ba2dd792cb16214              1   \n",
       "1  00018f77f2f0320c557190d7a144bdd3              1   \n",
       "2  000229ec398224ef6ca0657da4fc703e              1   \n",
       "3  00024acbcdf0a6daa1e931b038114c75              1   \n",
       "4  00042b26cf59d7ce69dfabb4e55b4fd9              1   \n",
       "\n",
       "                         product_id                         seller_id  \\\n",
       "0  4244733e06e7ecb4970a6e2683c13e61  48436dade18ac8b2bce089ec2a041202   \n",
       "1  e5f2d52b802189ee658865ca93d83a8f  dd7ddc04e1b6c2c614352b383efe2d36   \n",
       "2  c777355d18b72b67abbeef9df44fd0fd  5b51032eddd242adc84c38acab88f23d   \n",
       "3  7634da152a4610f1595efa32f14722fc  9d7a1d34a5052409006425275ba1c2b4   \n",
       "4  ac6c3623068f30de03045865e4e10089  df560393f3a51e74553ab94004ba5c87   \n",
       "\n",
       "   shipping_limit_date   price  freight_value product_category_name  \\\n",
       "0  2017-09-19 09:45:35   58.90          13.29            cool_stuff   \n",
       "1  2017-05-03 11:05:13  239.90          19.93              pet_shop   \n",
       "2  2018-01-18 14:48:30  199.00          17.87      moveis_decoracao   \n",
       "3  2018-08-15 10:10:18   12.99          12.79            perfumaria   \n",
       "4  2017-02-13 13:57:51  199.90          18.14    ferramentas_jardim   \n",
       "\n",
       "   product_name_lenght  product_description_lenght  product_photos_qty  \\\n",
       "0                 58.0                       598.0                 4.0   \n",
       "1                 56.0                       239.0                 2.0   \n",
       "2                 59.0                       695.0                 2.0   \n",
       "3                 42.0                       480.0                 1.0   \n",
       "4                 59.0                       409.0                 1.0   \n",
       "\n",
       "   product_weight_g  product_length_cm  product_height_cm  product_width_cm  \\\n",
       "0             650.0               28.0                9.0              14.0   \n",
       "1           30000.0               50.0               30.0              40.0   \n",
       "2            3050.0               33.0               13.0              33.0   \n",
       "3             200.0               16.0               10.0              15.0   \n",
       "4            3750.0               35.0               40.0              30.0   \n",
       "\n",
       "  product_category_name_english    seller_city seller_state  \n",
       "0                    cool_stuff  volta redonda           SP  \n",
       "1                      pet_shop      sao paulo           SP  \n",
       "2               furniture_decor  borda da mata           MG  \n",
       "3                     perfumery         franca           SP  \n",
       "4                  garden_tools         loanda           PR  "
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# menggabungkan df_order_items dengan seller\n",
    "sellers = sellers.drop(columns = ['seller_zip_code_prefix'])\n",
    "df_order_items = df_order_items.merge(sellers, left_on='seller_id', right_on='seller_id',how='left')\n",
    "print(df_order_items.shape)\n",
    "df_order_items.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "0eb1fd34",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:21.384154Z",
     "iopub.status.busy": "2023-10-18T10:08:21.382956Z",
     "iopub.status.idle": "2023-10-18T10:08:21.531807Z",
     "shell.execute_reply": "2023-10-18T10:08:21.530934Z"
    },
    "papermill": {
     "duration": 0.178095,
     "end_time": "2023-10-18T10:08:21.534090",
     "exception": false,
     "start_time": "2023-10-18T10:08:21.355995",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# menggabungkan orders dengan payments\n",
    "payments = payments.drop(columns = ['payment_sequential','payment_installments'])\n",
    "orders = orders.merge(payments, left_on='order_id', right_on='order_id',how='left')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "31c420cc",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:21.585347Z",
     "iopub.status.busy": "2023-10-18T10:08:21.584359Z",
     "iopub.status.idle": "2023-10-18T10:08:21.712811Z",
     "shell.execute_reply": "2023-10-18T10:08:21.711219Z"
    },
    "papermill": {
     "duration": 0.157604,
     "end_time": "2023-10-18T10:08:21.715562",
     "exception": false,
     "start_time": "2023-10-18T10:08:21.557958",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# menggabungkan orders dengan customers\n",
    "customer = customer.drop(columns = ['customer_unique_id'])\n",
    "orders = orders.merge(customer, left_on='customer_id', right_on='customer_id',how='left')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "73a71252",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:21.767282Z",
     "iopub.status.busy": "2023-10-18T10:08:21.766929Z",
     "iopub.status.idle": "2023-10-18T10:08:21.783757Z",
     "shell.execute_reply": "2023-10-18T10:08:21.782703Z"
    },
    "papermill": {
     "duration": 0.046126,
     "end_time": "2023-10-18T10:08:21.786227",
     "exception": false,
     "start_time": "2023-10-18T10:08:21.740101",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(103887, 13)\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>order_id</th>\n",
       "      <th>customer_id</th>\n",
       "      <th>order_status</th>\n",
       "      <th>order_purchase_timestamp</th>\n",
       "      <th>order_approved_at</th>\n",
       "      <th>order_delivered_carrier_date</th>\n",
       "      <th>order_delivered_customer_date</th>\n",
       "      <th>order_estimated_delivery_date</th>\n",
       "      <th>payment_type</th>\n",
       "      <th>payment_value</th>\n",
       "      <th>customer_zip_code_prefix</th>\n",
       "      <th>customer_city</th>\n",
       "      <th>customer_state</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>e481f51cbdc54678b7cc49136f2d6af7</td>\n",
       "      <td>9ef432eb6251297304e76186b10a928d</td>\n",
       "      <td>delivered</td>\n",
       "      <td>2017-10-02 10:56:33</td>\n",
       "      <td>2017-10-02 11:07:15</td>\n",
       "      <td>2017-10-04 19:55:00</td>\n",
       "      <td>2017-10-10 21:25:13</td>\n",
       "      <td>2017-10-18 00:00:00</td>\n",
       "      <td>credit_card</td>\n",
       "      <td>18.12</td>\n",
       "      <td>3149</td>\n",
       "      <td>sao paulo</td>\n",
       "      <td>SP</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>e481f51cbdc54678b7cc49136f2d6af7</td>\n",
       "      <td>9ef432eb6251297304e76186b10a928d</td>\n",
       "      <td>delivered</td>\n",
       "      <td>2017-10-02 10:56:33</td>\n",
       "      <td>2017-10-02 11:07:15</td>\n",
       "      <td>2017-10-04 19:55:00</td>\n",
       "      <td>2017-10-10 21:25:13</td>\n",
       "      <td>2017-10-18 00:00:00</td>\n",
       "      <td>voucher</td>\n",
       "      <td>2.00</td>\n",
       "      <td>3149</td>\n",
       "      <td>sao paulo</td>\n",
       "      <td>SP</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>e481f51cbdc54678b7cc49136f2d6af7</td>\n",
       "      <td>9ef432eb6251297304e76186b10a928d</td>\n",
       "      <td>delivered</td>\n",
       "      <td>2017-10-02 10:56:33</td>\n",
       "      <td>2017-10-02 11:07:15</td>\n",
       "      <td>2017-10-04 19:55:00</td>\n",
       "      <td>2017-10-10 21:25:13</td>\n",
       "      <td>2017-10-18 00:00:00</td>\n",
       "      <td>voucher</td>\n",
       "      <td>18.59</td>\n",
       "      <td>3149</td>\n",
       "      <td>sao paulo</td>\n",
       "      <td>SP</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>53cdb2fc8bc7dce0b6741e2150273451</td>\n",
       "      <td>b0830fb4747a6c6d20dea0b8c802d7ef</td>\n",
       "      <td>delivered</td>\n",
       "      <td>2018-07-24 20:41:37</td>\n",
       "      <td>2018-07-26 03:24:27</td>\n",
       "      <td>2018-07-26 14:31:00</td>\n",
       "      <td>2018-08-07 15:27:45</td>\n",
       "      <td>2018-08-13 00:00:00</td>\n",
       "      <td>boleto</td>\n",
       "      <td>141.46</td>\n",
       "      <td>47813</td>\n",
       "      <td>barreiras</td>\n",
       "      <td>BA</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>47770eb9100c2d0c44946d9cf07ec65d</td>\n",
       "      <td>41ce2a54c0b03bf3443c3d931a367089</td>\n",
       "      <td>delivered</td>\n",
       "      <td>2018-08-08 08:38:49</td>\n",
       "      <td>2018-08-08 08:55:23</td>\n",
       "      <td>2018-08-08 13:50:00</td>\n",
       "      <td>2018-08-17 18:06:29</td>\n",
       "      <td>2018-09-04 00:00:00</td>\n",
       "      <td>credit_card</td>\n",
       "      <td>179.12</td>\n",
       "      <td>75265</td>\n",
       "      <td>vianopolis</td>\n",
       "      <td>GO</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                           order_id                       customer_id  \\\n",
       "0  e481f51cbdc54678b7cc49136f2d6af7  9ef432eb6251297304e76186b10a928d   \n",
       "1  e481f51cbdc54678b7cc49136f2d6af7  9ef432eb6251297304e76186b10a928d   \n",
       "2  e481f51cbdc54678b7cc49136f2d6af7  9ef432eb6251297304e76186b10a928d   \n",
       "3  53cdb2fc8bc7dce0b6741e2150273451  b0830fb4747a6c6d20dea0b8c802d7ef   \n",
       "4  47770eb9100c2d0c44946d9cf07ec65d  41ce2a54c0b03bf3443c3d931a367089   \n",
       "\n",
       "  order_status order_purchase_timestamp    order_approved_at  \\\n",
       "0    delivered      2017-10-02 10:56:33  2017-10-02 11:07:15   \n",
       "1    delivered      2017-10-02 10:56:33  2017-10-02 11:07:15   \n",
       "2    delivered      2017-10-02 10:56:33  2017-10-02 11:07:15   \n",
       "3    delivered      2018-07-24 20:41:37  2018-07-26 03:24:27   \n",
       "4    delivered      2018-08-08 08:38:49  2018-08-08 08:55:23   \n",
       "\n",
       "  order_delivered_carrier_date order_delivered_customer_date  \\\n",
       "0          2017-10-04 19:55:00           2017-10-10 21:25:13   \n",
       "1          2017-10-04 19:55:00           2017-10-10 21:25:13   \n",
       "2          2017-10-04 19:55:00           2017-10-10 21:25:13   \n",
       "3          2018-07-26 14:31:00           2018-08-07 15:27:45   \n",
       "4          2018-08-08 13:50:00           2018-08-17 18:06:29   \n",
       "\n",
       "  order_estimated_delivery_date payment_type  payment_value  \\\n",
       "0           2017-10-18 00:00:00  credit_card          18.12   \n",
       "1           2017-10-18 00:00:00      voucher           2.00   \n",
       "2           2017-10-18 00:00:00      voucher          18.59   \n",
       "3           2018-08-13 00:00:00       boleto         141.46   \n",
       "4           2018-09-04 00:00:00  credit_card         179.12   \n",
       "\n",
       "   customer_zip_code_prefix customer_city customer_state  \n",
       "0                      3149     sao paulo             SP  \n",
       "1                      3149     sao paulo             SP  \n",
       "2                      3149     sao paulo             SP  \n",
       "3                     47813     barreiras             BA  \n",
       "4                     75265    vianopolis             GO  "
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(orders.shape)\n",
    "orders.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8f7015be",
   "metadata": {
    "papermill": {
     "duration": 0.024938,
     "end_time": "2023-10-18T10:08:21.836363",
     "exception": false,
     "start_time": "2023-10-18T10:08:21.811425",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## Assessing Data\n",
    "melakukan pemeriksaan data sebelum melakukan analisis data. Pada tahap ini akan mengecek tipe data, missing value, duplikat data, dan parameter statistik."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "72f8a7b1",
   "metadata": {
    "papermill": {
     "duration": 0.022683,
     "end_time": "2023-10-18T10:08:21.882250",
     "exception": false,
     "start_time": "2023-10-18T10:08:21.859567",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "### Menilai Data `df_order_items`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "df1e88b7",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:21.932739Z",
     "iopub.status.busy": "2023-10-18T10:08:21.932391Z",
     "iopub.status.idle": "2023-10-18T10:08:21.995592Z",
     "shell.execute_reply": "2023-10-18T10:08:21.994348Z"
    },
    "papermill": {
     "duration": 0.091617,
     "end_time": "2023-10-18T10:08:21.998129",
     "exception": false,
     "start_time": "2023-10-18T10:08:21.906512",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 112650 entries, 0 to 112649\n",
      "Data columns (total 18 columns):\n",
      " #   Column                         Non-Null Count   Dtype  \n",
      "---  ------                         --------------   -----  \n",
      " 0   order_id                       112650 non-null  object \n",
      " 1   order_item_id                  112650 non-null  int64  \n",
      " 2   product_id                     112650 non-null  object \n",
      " 3   seller_id                      112650 non-null  object \n",
      " 4   shipping_limit_date            112650 non-null  object \n",
      " 5   price                          112650 non-null  float64\n",
      " 6   freight_value                  112650 non-null  float64\n",
      " 7   product_category_name          111047 non-null  object \n",
      " 8   product_name_lenght            111047 non-null  float64\n",
      " 9   product_description_lenght     111047 non-null  float64\n",
      " 10  product_photos_qty             111047 non-null  float64\n",
      " 11  product_weight_g               112632 non-null  float64\n",
      " 12  product_length_cm              112632 non-null  float64\n",
      " 13  product_height_cm              112632 non-null  float64\n",
      " 14  product_width_cm               112632 non-null  float64\n",
      " 15  product_category_name_english  111023 non-null  object \n",
      " 16  seller_city                    112650 non-null  object \n",
      " 17  seller_state                   112650 non-null  object \n",
      "dtypes: float64(9), int64(1), object(8)\n",
      "memory usage: 16.3+ MB\n"
     ]
    }
   ],
   "source": [
    "df_order_items.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0e1e91e3",
   "metadata": {
    "papermill": {
     "duration": 0.023886,
     "end_time": "2023-10-18T10:08:22.046041",
     "exception": false,
     "start_time": "2023-10-18T10:08:22.022155",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "terdapat tipe data yang tidak sesuai, yaitu kolom `shipping_limit_date` seharusnya bertipe datetime."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "06c6d491",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:22.095677Z",
     "iopub.status.busy": "2023-10-18T10:08:22.095069Z",
     "iopub.status.idle": "2023-10-18T10:08:22.149783Z",
     "shell.execute_reply": "2023-10-18T10:08:22.149031Z"
    },
    "papermill": {
     "duration": 0.082406,
     "end_time": "2023-10-18T10:08:22.151741",
     "exception": false,
     "start_time": "2023-10-18T10:08:22.069335",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(112650, 18)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "order_id                            0\n",
       "order_item_id                       0\n",
       "product_id                          0\n",
       "seller_id                           0\n",
       "shipping_limit_date                 0\n",
       "price                               0\n",
       "freight_value                       0\n",
       "product_category_name            1603\n",
       "product_name_lenght              1603\n",
       "product_description_lenght       1603\n",
       "product_photos_qty               1603\n",
       "product_weight_g                   18\n",
       "product_length_cm                  18\n",
       "product_height_cm                  18\n",
       "product_width_cm                   18\n",
       "product_category_name_english    1627\n",
       "seller_city                         0\n",
       "seller_state                        0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(df_order_items.shape)\n",
    "df_order_items.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ee19a797",
   "metadata": {
    "papermill": {
     "duration": 0.024897,
     "end_time": "2023-10-18T10:08:22.200403",
     "exception": false,
     "start_time": "2023-10-18T10:08:22.175506",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "terdapat 1627 missing value pada kolom `product_category_name_english`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "76822ae8",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:22.254978Z",
     "iopub.status.busy": "2023-10-18T10:08:22.253735Z",
     "iopub.status.idle": "2023-10-18T10:08:22.423638Z",
     "shell.execute_reply": "2023-10-18T10:08:22.422905Z"
    },
    "papermill": {
     "duration": 0.198792,
     "end_time": "2023-10-18T10:08:22.425781",
     "exception": false,
     "start_time": "2023-10-18T10:08:22.226989",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Jumlah duplikasi:  0\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>order_item_id</th>\n",
       "      <th>price</th>\n",
       "      <th>freight_value</th>\n",
       "      <th>product_name_lenght</th>\n",
       "      <th>product_description_lenght</th>\n",
       "      <th>product_photos_qty</th>\n",
       "      <th>product_weight_g</th>\n",
       "      <th>product_length_cm</th>\n",
       "      <th>product_height_cm</th>\n",
       "      <th>product_width_cm</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>112650.000000</td>\n",
       "      <td>112650.000000</td>\n",
       "      <td>112650.000000</td>\n",
       "      <td>111047.000000</td>\n",
       "      <td>111047.000000</td>\n",
       "      <td>111047.000000</td>\n",
       "      <td>112632.000000</td>\n",
       "      <td>112632.000000</td>\n",
       "      <td>112632.000000</td>\n",
       "      <td>112632.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>1.197834</td>\n",
       "      <td>120.653739</td>\n",
       "      <td>19.990320</td>\n",
       "      <td>48.775978</td>\n",
       "      <td>787.867029</td>\n",
       "      <td>2.209713</td>\n",
       "      <td>2093.672047</td>\n",
       "      <td>30.153669</td>\n",
       "      <td>16.593766</td>\n",
       "      <td>22.996546</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>0.705124</td>\n",
       "      <td>183.633928</td>\n",
       "      <td>15.806405</td>\n",
       "      <td>10.025581</td>\n",
       "      <td>652.135608</td>\n",
       "      <td>1.721438</td>\n",
       "      <td>3751.596884</td>\n",
       "      <td>16.153449</td>\n",
       "      <td>13.443483</td>\n",
       "      <td>11.707268</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.850000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>7.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>6.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>39.900000</td>\n",
       "      <td>13.080000</td>\n",
       "      <td>42.000000</td>\n",
       "      <td>348.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>300.000000</td>\n",
       "      <td>18.000000</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>15.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>74.990000</td>\n",
       "      <td>16.260000</td>\n",
       "      <td>52.000000</td>\n",
       "      <td>603.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>700.000000</td>\n",
       "      <td>25.000000</td>\n",
       "      <td>13.000000</td>\n",
       "      <td>20.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>134.900000</td>\n",
       "      <td>21.150000</td>\n",
       "      <td>57.000000</td>\n",
       "      <td>987.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>1800.000000</td>\n",
       "      <td>38.000000</td>\n",
       "      <td>20.000000</td>\n",
       "      <td>30.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>21.000000</td>\n",
       "      <td>6735.000000</td>\n",
       "      <td>409.680000</td>\n",
       "      <td>76.000000</td>\n",
       "      <td>3992.000000</td>\n",
       "      <td>20.000000</td>\n",
       "      <td>40425.000000</td>\n",
       "      <td>105.000000</td>\n",
       "      <td>105.000000</td>\n",
       "      <td>118.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       order_item_id          price  freight_value  product_name_lenght  \\\n",
       "count  112650.000000  112650.000000  112650.000000        111047.000000   \n",
       "mean        1.197834     120.653739      19.990320            48.775978   \n",
       "std         0.705124     183.633928      15.806405            10.025581   \n",
       "min         1.000000       0.850000       0.000000             5.000000   \n",
       "25%         1.000000      39.900000      13.080000            42.000000   \n",
       "50%         1.000000      74.990000      16.260000            52.000000   \n",
       "75%         1.000000     134.900000      21.150000            57.000000   \n",
       "max        21.000000    6735.000000     409.680000            76.000000   \n",
       "\n",
       "       product_description_lenght  product_photos_qty  product_weight_g  \\\n",
       "count               111047.000000       111047.000000     112632.000000   \n",
       "mean                   787.867029            2.209713       2093.672047   \n",
       "std                    652.135608            1.721438       3751.596884   \n",
       "min                      4.000000            1.000000          0.000000   \n",
       "25%                    348.000000            1.000000        300.000000   \n",
       "50%                    603.000000            1.000000        700.000000   \n",
       "75%                    987.000000            3.000000       1800.000000   \n",
       "max                   3992.000000           20.000000      40425.000000   \n",
       "\n",
       "       product_length_cm  product_height_cm  product_width_cm  \n",
       "count      112632.000000      112632.000000     112632.000000  \n",
       "mean           30.153669          16.593766         22.996546  \n",
       "std            16.153449          13.443483         11.707268  \n",
       "min             7.000000           2.000000          6.000000  \n",
       "25%            18.000000           8.000000         15.000000  \n",
       "50%            25.000000          13.000000         20.000000  \n",
       "75%            38.000000          20.000000         30.000000  \n",
       "max           105.000000         105.000000        118.000000  "
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(\"Jumlah duplikasi: \", df_order_items.duplicated().sum())\n",
    "df_order_items.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a5114854",
   "metadata": {
    "papermill": {
     "duration": 0.025294,
     "end_time": "2023-10-18T10:08:22.475460",
     "exception": false,
     "start_time": "2023-10-18T10:08:22.450166",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "tidak terdapat data yang duplikat, namun ada outlier pada kolom price dan freight_value."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b1fd89cf",
   "metadata": {
    "papermill": {
     "duration": 0.024328,
     "end_time": "2023-10-18T10:08:22.524018",
     "exception": false,
     "start_time": "2023-10-18T10:08:22.499690",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "### Menilai Data `orders`\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "37081485",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:22.574642Z",
     "iopub.status.busy": "2023-10-18T10:08:22.574308Z",
     "iopub.status.idle": "2023-10-18T10:08:22.641415Z",
     "shell.execute_reply": "2023-10-18T10:08:22.639938Z"
    },
    "papermill": {
     "duration": 0.094214,
     "end_time": "2023-10-18T10:08:22.643510",
     "exception": false,
     "start_time": "2023-10-18T10:08:22.549296",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 103887 entries, 0 to 103886\n",
      "Data columns (total 13 columns):\n",
      " #   Column                         Non-Null Count   Dtype  \n",
      "---  ------                         --------------   -----  \n",
      " 0   order_id                       103887 non-null  object \n",
      " 1   customer_id                    103887 non-null  object \n",
      " 2   order_status                   103887 non-null  object \n",
      " 3   order_purchase_timestamp       103887 non-null  object \n",
      " 4   order_approved_at              103712 non-null  object \n",
      " 5   order_delivered_carrier_date   101999 non-null  object \n",
      " 6   order_delivered_customer_date  100755 non-null  object \n",
      " 7   order_estimated_delivery_date  103887 non-null  object \n",
      " 8   payment_type                   103886 non-null  object \n",
      " 9   payment_value                  103886 non-null  float64\n",
      " 10  customer_zip_code_prefix       103887 non-null  int64  \n",
      " 11  customer_city                  103887 non-null  object \n",
      " 12  customer_state                 103887 non-null  object \n",
      "dtypes: float64(1), int64(1), object(11)\n",
      "memory usage: 11.1+ MB\n"
     ]
    }
   ],
   "source": [
    "orders.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "2067f423",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:22.695193Z",
     "iopub.status.busy": "2023-10-18T10:08:22.694318Z",
     "iopub.status.idle": "2023-10-18T10:08:22.758962Z",
     "shell.execute_reply": "2023-10-18T10:08:22.757913Z"
    },
    "papermill": {
     "duration": 0.091756,
     "end_time": "2023-10-18T10:08:22.760992",
     "exception": false,
     "start_time": "2023-10-18T10:08:22.669236",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(103887, 13)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "order_id                            0\n",
       "customer_id                         0\n",
       "order_status                        0\n",
       "order_purchase_timestamp            0\n",
       "order_approved_at                 175\n",
       "order_delivered_carrier_date     1888\n",
       "order_delivered_customer_date    3132\n",
       "order_estimated_delivery_date       0\n",
       "payment_type                        1\n",
       "payment_value                       1\n",
       "customer_zip_code_prefix            0\n",
       "customer_city                       0\n",
       "customer_state                      0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(orders.shape)\n",
    "orders.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "254bff4b",
   "metadata": {
    "papermill": {
     "duration": 0.025017,
     "end_time": "2023-10-18T10:08:22.809825",
     "exception": false,
     "start_time": "2023-10-18T10:08:22.784808",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "terdapat 175 missing value pada kolom `order_approved_at`, 1888 pada kolom `order_delivered_carrier_date`, 3132 pada kolom `order_delivered_customer_date`, 1 pada kolom `payment_type`, dan 1 pada kolom `payment_value`. missing value yang terdapat pada kolom tersebut terjadi karena order status berupa 'shipped' atau 'canceled'."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "9832736c",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:22.861559Z",
     "iopub.status.busy": "2023-10-18T10:08:22.861017Z",
     "iopub.status.idle": "2023-10-18T10:08:23.088464Z",
     "shell.execute_reply": "2023-10-18T10:08:23.087257Z"
    },
    "papermill": {
     "duration": 0.256735,
     "end_time": "2023-10-18T10:08:23.090570",
     "exception": false,
     "start_time": "2023-10-18T10:08:22.833835",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Jumlah duplikasi:  615\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>payment_value</th>\n",
       "      <th>customer_zip_code_prefix</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>103886.000000</td>\n",
       "      <td>103887.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>154.100380</td>\n",
       "      <td>35072.353490</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>217.494064</td>\n",
       "      <td>29743.416343</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>1003.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>56.790000</td>\n",
       "      <td>11367.500000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>100.000000</td>\n",
       "      <td>24360.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>171.837500</td>\n",
       "      <td>58418.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>13664.080000</td>\n",
       "      <td>99990.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       payment_value  customer_zip_code_prefix\n",
       "count  103886.000000             103887.000000\n",
       "mean      154.100380              35072.353490\n",
       "std       217.494064              29743.416343\n",
       "min         0.000000               1003.000000\n",
       "25%        56.790000              11367.500000\n",
       "50%       100.000000              24360.000000\n",
       "75%       171.837500              58418.000000\n",
       "max     13664.080000              99990.000000"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(\"Jumlah duplikasi: \", orders.duplicated().sum())\n",
    "orders.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e1afe373",
   "metadata": {
    "papermill": {
     "duration": 0.025605,
     "end_time": "2023-10-18T10:08:23.141635",
     "exception": false,
     "start_time": "2023-10-18T10:08:23.116030",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "terdapat 615 baris yang duplikat dan outlier pada kolom payment_value."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7b31a8a0",
   "metadata": {
    "papermill": {
     "duration": 0.027338,
     "end_time": "2023-10-18T10:08:23.193367",
     "exception": false,
     "start_time": "2023-10-18T10:08:23.166029",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## Cleaning Data\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1dd04c9e",
   "metadata": {
    "papermill": {
     "duration": 0.025179,
     "end_time": "2023-10-18T10:08:23.244537",
     "exception": false,
     "start_time": "2023-10-18T10:08:23.219358",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "### Membersihkan Data `df_order_items`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "ab3ef663",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:23.299596Z",
     "iopub.status.busy": "2023-10-18T10:08:23.298759Z",
     "iopub.status.idle": "2023-10-18T10:08:23.391982Z",
     "shell.execute_reply": "2023-10-18T10:08:23.390896Z"
    },
    "papermill": {
     "duration": 0.123359,
     "end_time": "2023-10-18T10:08:23.394389",
     "exception": false,
     "start_time": "2023-10-18T10:08:23.271030",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 112650 entries, 0 to 112649\n",
      "Data columns (total 18 columns):\n",
      " #   Column                         Non-Null Count   Dtype         \n",
      "---  ------                         --------------   -----         \n",
      " 0   order_id                       112650 non-null  object        \n",
      " 1   order_item_id                  112650 non-null  int64         \n",
      " 2   product_id                     112650 non-null  object        \n",
      " 3   seller_id                      112650 non-null  object        \n",
      " 4   shipping_limit_date            112650 non-null  datetime64[ns]\n",
      " 5   price                          112650 non-null  float64       \n",
      " 6   freight_value                  112650 non-null  float64       \n",
      " 7   product_category_name          111047 non-null  object        \n",
      " 8   product_name_lenght            111047 non-null  float64       \n",
      " 9   product_description_lenght     111047 non-null  float64       \n",
      " 10  product_photos_qty             111047 non-null  float64       \n",
      " 11  product_weight_g               112632 non-null  float64       \n",
      " 12  product_length_cm              112632 non-null  float64       \n",
      " 13  product_height_cm              112632 non-null  float64       \n",
      " 14  product_width_cm               112632 non-null  float64       \n",
      " 15  product_category_name_english  111023 non-null  object        \n",
      " 16  seller_city                    112650 non-null  object        \n",
      " 17  seller_state                   112650 non-null  object        \n",
      "dtypes: datetime64[ns](1), float64(9), int64(1), object(7)\n",
      "memory usage: 16.3+ MB\n"
     ]
    }
   ],
   "source": [
    "#data types\n",
    "df_order_items['shipping_limit_date'] = pd.to_datetime(df_order_items['shipping_limit_date'])\n",
    "df_order_items.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "ed80144a",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:23.446714Z",
     "iopub.status.busy": "2023-10-18T10:08:23.445978Z",
     "iopub.status.idle": "2023-10-18T10:08:23.466530Z",
     "shell.execute_reply": "2023-10-18T10:08:23.465455Z"
    },
    "papermill": {
     "duration": 0.049285,
     "end_time": "2023-10-18T10:08:23.468921",
     "exception": false,
     "start_time": "2023-10-18T10:08:23.419636",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'pc_gamer', 'portateis_cozinha_e_preparadores_de_alimentos'}"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# missing value pada kolom product_category_name_english\n",
    "x = df_order_items.loc[df_order_items[\"product_category_name\"].notnull() & df_order_items[\"product_category_name_english\"].isnull()]\n",
    "set(x[\"product_category_name\"])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "463faca7",
   "metadata": {
    "papermill": {
     "duration": 0.02599,
     "end_time": "2023-10-18T10:08:23.520681",
     "exception": false,
     "start_time": "2023-10-18T10:08:23.494691",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "karena dalam kolom `product_category_name_english` terdapat data NaN, sedangkan kolom `product_category_name` mempunyai datanya, maka data tersebut akan diterjemahkan untuk mengganti data yang kosong pada kolom `product_category_name_english`. sedangkan untuk data null lainnya akan didefinisikan sebagai 'not defined'."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "b23e5f4f",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:23.575122Z",
     "iopub.status.busy": "2023-10-18T10:08:23.574384Z",
     "iopub.status.idle": "2023-10-18T10:08:23.616240Z",
     "shell.execute_reply": "2023-10-18T10:08:23.615067Z"
    },
    "papermill": {
     "duration": 0.070543,
     "end_time": "2023-10-18T10:08:23.618645",
     "exception": false,
     "start_time": "2023-10-18T10:08:23.548102",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "df_order_items['product_category_name'].fillna('not defined', inplace=True)\n",
    "df_order_items['product_category_name_english'].fillna('not defined', inplace=True)\n",
    "\n",
    "df_order_items[\"product_category_name_english\"] = np.where(df_order_items[\"product_category_name\"] == 'pc_gamer', 'PC Gaming', df_order_items[\"product_category_name_english\"])\n",
    "df_order_items[\"product_category_name_english\"] = np.where(df_order_items[\"product_category_name\"] == 'portateis_cozinha_e_preparadores_de_alimentos', 'portable kitchen food preparers', df_order_items[\"product_category_name_english\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "3a520a89",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:23.670374Z",
     "iopub.status.busy": "2023-10-18T10:08:23.670036Z",
     "iopub.status.idle": "2023-10-18T10:08:23.718568Z",
     "shell.execute_reply": "2023-10-18T10:08:23.717342Z"
    },
    "papermill": {
     "duration": 0.077215,
     "end_time": "2023-10-18T10:08:23.721498",
     "exception": false,
     "start_time": "2023-10-18T10:08:23.644283",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "order_id                            0\n",
       "order_item_id                       0\n",
       "product_id                          0\n",
       "seller_id                           0\n",
       "shipping_limit_date                 0\n",
       "price                               0\n",
       "freight_value                       0\n",
       "product_category_name               0\n",
       "product_name_lenght              1603\n",
       "product_description_lenght       1603\n",
       "product_photos_qty               1603\n",
       "product_weight_g                   18\n",
       "product_length_cm                  18\n",
       "product_height_cm                  18\n",
       "product_width_cm                   18\n",
       "product_category_name_english       0\n",
       "seller_city                         0\n",
       "seller_state                        0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#cek kembali missing value pada df_order_items\n",
    "df_order_items.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "f0aa9604",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:23.776702Z",
     "iopub.status.busy": "2023-10-18T10:08:23.776323Z",
     "iopub.status.idle": "2023-10-18T10:08:24.025195Z",
     "shell.execute_reply": "2023-10-18T10:08:24.024009Z"
    },
    "papermill": {
     "duration": 0.278879,
     "end_time": "2023-10-18T10:08:24.027542",
     "exception": false,
     "start_time": "2023-10-18T10:08:23.748663",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Jumlah duplikasi:  0\n"
     ]
    }
   ],
   "source": [
    "# duplicate data\n",
    "df_order_items.drop_duplicates(inplace=True)\n",
    "print(\"Jumlah duplikasi: \", df_order_items.duplicated().sum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "693c5212",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:24.079355Z",
     "iopub.status.busy": "2023-10-18T10:08:24.078970Z",
     "iopub.status.idle": "2023-10-18T10:08:24.083495Z",
     "shell.execute_reply": "2023-10-18T10:08:24.082436Z"
    },
    "papermill": {
     "duration": 0.033441,
     "end_time": "2023-10-18T10:08:24.085827",
     "exception": false,
     "start_time": "2023-10-18T10:08:24.052386",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# #menambahkan kolom year dan month\n",
    "# df_order_items['year'] = df_order_items['shipping_limit_date'].dt.strftime('%Y')\n",
    "# df_order_items['month'] = df_order_items['shipping_limit_date'].dt.strftime('%m-%Y')\n",
    "# df_order_items"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "40dc4939",
   "metadata": {
    "papermill": {
     "duration": 0.026462,
     "end_time": "2023-10-18T10:08:24.137616",
     "exception": false,
     "start_time": "2023-10-18T10:08:24.111154",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "### Membersihkan Data `orders`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "b615b3d1",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:24.188884Z",
     "iopub.status.busy": "2023-10-18T10:08:24.188499Z",
     "iopub.status.idle": "2023-10-18T10:08:24.387828Z",
     "shell.execute_reply": "2023-10-18T10:08:24.386580Z"
    },
    "papermill": {
     "duration": 0.227317,
     "end_time": "2023-10-18T10:08:24.390064",
     "exception": false,
     "start_time": "2023-10-18T10:08:24.162747",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 103887 entries, 0 to 103886\n",
      "Data columns (total 13 columns):\n",
      " #   Column                         Non-Null Count   Dtype         \n",
      "---  ------                         --------------   -----         \n",
      " 0   order_id                       103887 non-null  object        \n",
      " 1   customer_id                    103887 non-null  object        \n",
      " 2   order_status                   103887 non-null  category      \n",
      " 3   order_purchase_timestamp       103887 non-null  datetime64[ns]\n",
      " 4   order_approved_at              103712 non-null  datetime64[ns]\n",
      " 5   order_delivered_carrier_date   101999 non-null  datetime64[ns]\n",
      " 6   order_delivered_customer_date  100755 non-null  datetime64[ns]\n",
      " 7   order_estimated_delivery_date  103887 non-null  datetime64[ns]\n",
      " 8   payment_type                   103886 non-null  object        \n",
      " 9   payment_value                  103886 non-null  float64       \n",
      " 10  customer_zip_code_prefix       103887 non-null  int64         \n",
      " 11  customer_city                  103887 non-null  object        \n",
      " 12  customer_state                 103887 non-null  object        \n",
      "dtypes: category(1), datetime64[ns](5), float64(1), int64(1), object(5)\n",
      "memory usage: 10.4+ MB\n"
     ]
    }
   ],
   "source": [
    "# membenarkan data types \n",
    "orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])\n",
    "orders['order_approved_at'] = pd.to_datetime(orders['order_approved_at'])\n",
    "orders['order_delivered_carrier_date'] = pd.to_datetime(orders['order_delivered_carrier_date'])\n",
    "orders['order_delivered_customer_date'] = pd.to_datetime(orders['order_delivered_customer_date'])\n",
    "orders['order_estimated_delivery_date'] = pd.to_datetime(orders['order_estimated_delivery_date'])\n",
    "orders['order_status'] = orders['order_status'].astype('category')\n",
    "\n",
    "orders.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "cea1fa2a",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:24.442795Z",
     "iopub.status.busy": "2023-10-18T10:08:24.442437Z",
     "iopub.status.idle": "2023-10-18T10:08:24.469264Z",
     "shell.execute_reply": "2023-10-18T10:08:24.468083Z"
    },
    "papermill": {
     "duration": 0.056321,
     "end_time": "2023-10-18T10:08:24.471687",
     "exception": false,
     "start_time": "2023-10-18T10:08:24.415366",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>order_id</th>\n",
       "      <th>customer_id</th>\n",
       "      <th>order_status</th>\n",
       "      <th>order_purchase_timestamp</th>\n",
       "      <th>order_approved_at</th>\n",
       "      <th>order_delivered_carrier_date</th>\n",
       "      <th>order_delivered_customer_date</th>\n",
       "      <th>order_estimated_delivery_date</th>\n",
       "      <th>payment_type</th>\n",
       "      <th>payment_value</th>\n",
       "      <th>customer_zip_code_prefix</th>\n",
       "      <th>customer_city</th>\n",
       "      <th>customer_state</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>49</th>\n",
       "      <td>ee64d42b8cf066f35eac1cf57de1aa85</td>\n",
       "      <td>caded193e8e47b8362864762a83db3c5</td>\n",
       "      <td>shipped</td>\n",
       "      <td>2018-06-04 16:44:48</td>\n",
       "      <td>2018-06-05 04:31:18</td>\n",
       "      <td>2018-06-05 14:32:00</td>\n",
       "      <td>NaT</td>\n",
       "      <td>2018-06-28</td>\n",
       "      <td>boleto</td>\n",
       "      <td>22.36</td>\n",
       "      <td>13215</td>\n",
       "      <td>jundiai</td>\n",
       "      <td>SP</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>161</th>\n",
       "      <td>6942b8da583c2f9957e990d028607019</td>\n",
       "      <td>52006a9383bf149a4fb24226b173106f</td>\n",
       "      <td>shipped</td>\n",
       "      <td>2018-01-10 11:33:07</td>\n",
       "      <td>2018-01-11 02:32:30</td>\n",
       "      <td>2018-01-11 19:39:23</td>\n",
       "      <td>NaT</td>\n",
       "      <td>2018-02-07</td>\n",
       "      <td>boleto</td>\n",
       "      <td>69.12</td>\n",
       "      <td>38600</td>\n",
       "      <td>paracatu</td>\n",
       "      <td>MG</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>169</th>\n",
       "      <td>36530871a5e80138db53bcfd8a104d90</td>\n",
       "      <td>4dafe3c841d2d6cc8a8b6d25b35704b9</td>\n",
       "      <td>shipped</td>\n",
       "      <td>2017-05-09 11:48:37</td>\n",
       "      <td>2017-05-11 11:45:14</td>\n",
       "      <td>2017-05-11 13:21:47</td>\n",
       "      <td>NaT</td>\n",
       "      <td>2017-06-08</td>\n",
       "      <td>credit_card</td>\n",
       "      <td>63.79</td>\n",
       "      <td>54762</td>\n",
       "      <td>camaragibe</td>\n",
       "      <td>PE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>241</th>\n",
       "      <td>4d630f57194f5aba1a3d12ce23e71cd9</td>\n",
       "      <td>6d491c9fe2f04f6e2af6ec033cd8907c</td>\n",
       "      <td>shipped</td>\n",
       "      <td>2017-11-17 19:53:21</td>\n",
       "      <td>2017-11-18 19:50:31</td>\n",
       "      <td>2017-11-22 17:28:34</td>\n",
       "      <td>NaT</td>\n",
       "      <td>2017-12-13</td>\n",
       "      <td>credit_card</td>\n",
       "      <td>240.23</td>\n",
       "      <td>91450</td>\n",
       "      <td>porto alegre</td>\n",
       "      <td>RS</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>314</th>\n",
       "      <td>3b4ad687e7e5190db827e1ae5a8989dd</td>\n",
       "      <td>1a87b8517b7d31373b50396eb15cb445</td>\n",
       "      <td>shipped</td>\n",
       "      <td>2018-06-28 12:52:15</td>\n",
       "      <td>2018-06-28 13:11:09</td>\n",
       "      <td>2018-07-04 15:20:00</td>\n",
       "      <td>NaT</td>\n",
       "      <td>2018-08-03</td>\n",
       "      <td>credit_card</td>\n",
       "      <td>865.01</td>\n",
       "      <td>20910</td>\n",
       "      <td>rio de janeiro</td>\n",
       "      <td>RJ</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>103196</th>\n",
       "      <td>dab8a6c6bd6ec448df5b3a6b6cb887bc</td>\n",
       "      <td>394653a10cab83cad40d7e2713f3ab89</td>\n",
       "      <td>shipped</td>\n",
       "      <td>2018-07-14 10:12:51</td>\n",
       "      <td>2018-07-16 12:30:58</td>\n",
       "      <td>2018-07-16 14:34:00</td>\n",
       "      <td>NaT</td>\n",
       "      <td>2018-08-03</td>\n",
       "      <td>boleto</td>\n",
       "      <td>121.90</td>\n",
       "      <td>25942</td>\n",
       "      <td>guapimirim</td>\n",
       "      <td>RJ</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>103354</th>\n",
       "      <td>492aed3c33bac22a8e04138319829283</td>\n",
       "      <td>58466c1166c377a56f6b2ae0d93ffbc0</td>\n",
       "      <td>shipped</td>\n",
       "      <td>2018-07-06 16:26:47</td>\n",
       "      <td>2018-07-06 16:35:10</td>\n",
       "      <td>2018-07-10 12:27:00</td>\n",
       "      <td>NaT</td>\n",
       "      <td>2018-07-26</td>\n",
       "      <td>credit_card</td>\n",
       "      <td>280.42</td>\n",
       "      <td>8270</td>\n",
       "      <td>sao paulo</td>\n",
       "      <td>SP</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>103543</th>\n",
       "      <td>274a7f7e4f1c17b7434a830e9b8759b1</td>\n",
       "      <td>670af30ca5b8c20878fecdafa5ee01b9</td>\n",
       "      <td>shipped</td>\n",
       "      <td>2018-06-23 13:25:15</td>\n",
       "      <td>2018-06-23 13:40:11</td>\n",
       "      <td>2018-07-04 13:51:00</td>\n",
       "      <td>NaT</td>\n",
       "      <td>2018-07-24</td>\n",
       "      <td>credit_card</td>\n",
       "      <td>9.31</td>\n",
       "      <td>49030</td>\n",
       "      <td>aracaju</td>\n",
       "      <td>SE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>103544</th>\n",
       "      <td>274a7f7e4f1c17b7434a830e9b8759b1</td>\n",
       "      <td>670af30ca5b8c20878fecdafa5ee01b9</td>\n",
       "      <td>shipped</td>\n",
       "      <td>2018-06-23 13:25:15</td>\n",
       "      <td>2018-06-23 13:40:11</td>\n",
       "      <td>2018-07-04 13:51:00</td>\n",
       "      <td>NaT</td>\n",
       "      <td>2018-07-24</td>\n",
       "      <td>voucher</td>\n",
       "      <td>48.63</td>\n",
       "      <td>49030</td>\n",
       "      <td>aracaju</td>\n",
       "      <td>SE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>103616</th>\n",
       "      <td>636cdd02667dc8d76d9296bf20a6890a</td>\n",
       "      <td>c162256b133c76f79181ce61d66545db</td>\n",
       "      <td>shipped</td>\n",
       "      <td>2018-02-17 14:31:22</td>\n",
       "      <td>2018-02-20 07:11:31</td>\n",
       "      <td>2018-02-20 19:18:58</td>\n",
       "      <td>NaT</td>\n",
       "      <td>2018-03-14</td>\n",
       "      <td>boleto</td>\n",
       "      <td>224.71</td>\n",
       "      <td>12042</td>\n",
       "      <td>taubate</td>\n",
       "      <td>SP</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1166 rows × 13 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                                order_id                       customer_id  \\\n",
       "49      ee64d42b8cf066f35eac1cf57de1aa85  caded193e8e47b8362864762a83db3c5   \n",
       "161     6942b8da583c2f9957e990d028607019  52006a9383bf149a4fb24226b173106f   \n",
       "169     36530871a5e80138db53bcfd8a104d90  4dafe3c841d2d6cc8a8b6d25b35704b9   \n",
       "241     4d630f57194f5aba1a3d12ce23e71cd9  6d491c9fe2f04f6e2af6ec033cd8907c   \n",
       "314     3b4ad687e7e5190db827e1ae5a8989dd  1a87b8517b7d31373b50396eb15cb445   \n",
       "...                                  ...                               ...   \n",
       "103196  dab8a6c6bd6ec448df5b3a6b6cb887bc  394653a10cab83cad40d7e2713f3ab89   \n",
       "103354  492aed3c33bac22a8e04138319829283  58466c1166c377a56f6b2ae0d93ffbc0   \n",
       "103543  274a7f7e4f1c17b7434a830e9b8759b1  670af30ca5b8c20878fecdafa5ee01b9   \n",
       "103544  274a7f7e4f1c17b7434a830e9b8759b1  670af30ca5b8c20878fecdafa5ee01b9   \n",
       "103616  636cdd02667dc8d76d9296bf20a6890a  c162256b133c76f79181ce61d66545db   \n",
       "\n",
       "       order_status order_purchase_timestamp   order_approved_at  \\\n",
       "49          shipped      2018-06-04 16:44:48 2018-06-05 04:31:18   \n",
       "161         shipped      2018-01-10 11:33:07 2018-01-11 02:32:30   \n",
       "169         shipped      2017-05-09 11:48:37 2017-05-11 11:45:14   \n",
       "241         shipped      2017-11-17 19:53:21 2017-11-18 19:50:31   \n",
       "314         shipped      2018-06-28 12:52:15 2018-06-28 13:11:09   \n",
       "...             ...                      ...                 ...   \n",
       "103196      shipped      2018-07-14 10:12:51 2018-07-16 12:30:58   \n",
       "103354      shipped      2018-07-06 16:26:47 2018-07-06 16:35:10   \n",
       "103543      shipped      2018-06-23 13:25:15 2018-06-23 13:40:11   \n",
       "103544      shipped      2018-06-23 13:25:15 2018-06-23 13:40:11   \n",
       "103616      shipped      2018-02-17 14:31:22 2018-02-20 07:11:31   \n",
       "\n",
       "       order_delivered_carrier_date order_delivered_customer_date  \\\n",
       "49              2018-06-05 14:32:00                           NaT   \n",
       "161             2018-01-11 19:39:23                           NaT   \n",
       "169             2017-05-11 13:21:47                           NaT   \n",
       "241             2017-11-22 17:28:34                           NaT   \n",
       "314             2018-07-04 15:20:00                           NaT   \n",
       "...                             ...                           ...   \n",
       "103196          2018-07-16 14:34:00                           NaT   \n",
       "103354          2018-07-10 12:27:00                           NaT   \n",
       "103543          2018-07-04 13:51:00                           NaT   \n",
       "103544          2018-07-04 13:51:00                           NaT   \n",
       "103616          2018-02-20 19:18:58                           NaT   \n",
       "\n",
       "       order_estimated_delivery_date payment_type  payment_value  \\\n",
       "49                        2018-06-28       boleto          22.36   \n",
       "161                       2018-02-07       boleto          69.12   \n",
       "169                       2017-06-08  credit_card          63.79   \n",
       "241                       2017-12-13  credit_card         240.23   \n",
       "314                       2018-08-03  credit_card         865.01   \n",
       "...                              ...          ...            ...   \n",
       "103196                    2018-08-03       boleto         121.90   \n",
       "103354                    2018-07-26  credit_card         280.42   \n",
       "103543                    2018-07-24  credit_card           9.31   \n",
       "103544                    2018-07-24      voucher          48.63   \n",
       "103616                    2018-03-14       boleto         224.71   \n",
       "\n",
       "        customer_zip_code_prefix   customer_city customer_state  \n",
       "49                         13215         jundiai             SP  \n",
       "161                        38600        paracatu             MG  \n",
       "169                        54762      camaragibe             PE  \n",
       "241                        91450    porto alegre             RS  \n",
       "314                        20910  rio de janeiro             RJ  \n",
       "...                          ...             ...            ...  \n",
       "103196                     25942      guapimirim             RJ  \n",
       "103354                      8270       sao paulo             SP  \n",
       "103543                     49030         aracaju             SE  \n",
       "103544                     49030         aracaju             SE  \n",
       "103616                     12042         taubate             SP  \n",
       "\n",
       "[1166 rows x 13 columns]"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    " orders.loc[orders['order_status'] == 'shipped']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "827bab1c",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:24.528588Z",
     "iopub.status.busy": "2023-10-18T10:08:24.528177Z",
     "iopub.status.idle": "2023-10-18T10:08:24.585054Z",
     "shell.execute_reply": "2023-10-18T10:08:24.583561Z"
    },
    "papermill": {
     "duration": 0.088771,
     "end_time": "2023-10-18T10:08:24.587412",
     "exception": false,
     "start_time": "2023-10-18T10:08:24.498641",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(103886, 13)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "order_id                            0\n",
       "customer_id                         0\n",
       "order_status                        0\n",
       "order_purchase_timestamp            0\n",
       "order_approved_at                 175\n",
       "order_delivered_carrier_date     1888\n",
       "order_delivered_customer_date    3132\n",
       "order_estimated_delivery_date       0\n",
       "payment_type                        0\n",
       "payment_value                       0\n",
       "customer_zip_code_prefix            0\n",
       "customer_city                       0\n",
       "customer_state                      0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "orders = orders.dropna(subset = [\"payment_type\",\"payment_value\"])\n",
    "print(orders.shape)\n",
    "orders.isna().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "69c3d094",
   "metadata": {
    "papermill": {
     "duration": 0.025851,
     "end_time": "2023-10-18T10:08:24.640406",
     "exception": false,
     "start_time": "2023-10-18T10:08:24.614555",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "karena missing value dalam table `orders` kebanyakan merupakan tipe data datetime yang menyangkut tentang waktu pengiriman paket, maka paket yang belum sampai kepada kurir atau pelanggan akan menjadi missing value. missing value ini juga berpengaruh pada order_status, maka missing value dengan tipe datetime tidak akan dihapus."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "d6891736",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:24.694611Z",
     "iopub.status.busy": "2023-10-18T10:08:24.694242Z",
     "iopub.status.idle": "2023-10-18T10:08:24.966189Z",
     "shell.execute_reply": "2023-10-18T10:08:24.965177Z"
    },
    "papermill": {
     "duration": 0.30201,
     "end_time": "2023-10-18T10:08:24.968494",
     "exception": false,
     "start_time": "2023-10-18T10:08:24.666484",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Jumlah duplikasi:  0\n"
     ]
    }
   ],
   "source": [
    "# duplicate data\n",
    "orders = orders.drop_duplicates()\n",
    "print(\"Jumlah duplikasi: \", orders.duplicated().sum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "bf29c8ce",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:25.026691Z",
     "iopub.status.busy": "2023-10-18T10:08:25.026132Z",
     "iopub.status.idle": "2023-10-18T10:08:26.671309Z",
     "shell.execute_reply": "2023-10-18T10:08:26.670508Z"
    },
    "papermill": {
     "duration": 1.677842,
     "end_time": "2023-10-18T10:08:26.673608",
     "exception": false,
     "start_time": "2023-10-18T10:08:24.995766",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# menambahkan kolom untuk EDA\n",
    "orders['year'] = orders['order_purchase_timestamp'].dt.strftime('%Y')\n",
    "orders['month'] = orders['order_purchase_timestamp'].dt.strftime('%m-%Y')\n",
    "# df_order_items\n",
    "\n",
    "orders[\"lama_pengiriman_hari\"] = (orders[\"order_delivered_customer_date\"] - orders[\"order_delivered_carrier_date\"]).dt.days\n",
    "orders[\"hari_pembelian\"] = orders[\"order_purchase_timestamp\"].dt.strftime('%A')\n",
    "\n",
    "orders['jam_pembelian'] = orders['order_purchase_timestamp'].apply(lambda x: x.hour)\n",
    "hours_bins = [-0.1, 6, 12, 18, 23]\n",
    "hours_labels = ['Subuh', 'Pagi', 'Siang', 'Malam']\n",
    "orders['waktu_hari_pembelian'] = pd.cut(orders['jam_pembelian'], hours_bins, labels=hours_labels)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5c2924c6",
   "metadata": {
    "papermill": {
     "duration": 0.025932,
     "end_time": "2023-10-18T10:08:26.725555",
     "exception": false,
     "start_time": "2023-10-18T10:08:26.699623",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# Exploratory Data Analysis (EDA)\n",
    "Tahap ini berguna untuk mengenal data yang akan ditangani sehingga dapat menganalisis data dengan efisien."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "b58928ff",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:26.778815Z",
     "iopub.status.busy": "2023-10-18T10:08:26.777992Z",
     "iopub.status.idle": "2023-10-18T10:08:26.782746Z",
     "shell.execute_reply": "2023-10-18T10:08:26.782008Z"
    },
    "papermill": {
     "duration": 0.033673,
     "end_time": "2023-10-18T10:08:26.784677",
     "exception": false,
     "start_time": "2023-10-18T10:08:26.751004",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# mendefinisikan fungsi yang akan digunakan untuk EDA\n",
    "def range(series):\n",
    "    return series.max() - series.min()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "98c1d5e4",
   "metadata": {
    "papermill": {
     "duration": 0.026587,
     "end_time": "2023-10-18T10:08:26.836560",
     "exception": false,
     "start_time": "2023-10-18T10:08:26.809973",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## Explore table `df_order_items`\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "df068306",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:26.889669Z",
     "iopub.status.busy": "2023-10-18T10:08:26.889010Z",
     "iopub.status.idle": "2023-10-18T10:08:27.109671Z",
     "shell.execute_reply": "2023-10-18T10:08:27.108875Z"
    },
    "papermill": {
     "duration": 0.249087,
     "end_time": "2023-10-18T10:08:27.111787",
     "exception": false,
     "start_time": "2023-10-18T10:08:26.862700",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>order_id</th>\n",
       "      <th>order_item_id</th>\n",
       "      <th>product_id</th>\n",
       "      <th>seller_id</th>\n",
       "      <th>shipping_limit_date</th>\n",
       "      <th>price</th>\n",
       "      <th>freight_value</th>\n",
       "      <th>product_category_name</th>\n",
       "      <th>product_name_lenght</th>\n",
       "      <th>product_description_lenght</th>\n",
       "      <th>product_photos_qty</th>\n",
       "      <th>product_weight_g</th>\n",
       "      <th>product_length_cm</th>\n",
       "      <th>product_height_cm</th>\n",
       "      <th>product_width_cm</th>\n",
       "      <th>product_category_name_english</th>\n",
       "      <th>seller_city</th>\n",
       "      <th>seller_state</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>112650</td>\n",
       "      <td>112650.000000</td>\n",
       "      <td>112650</td>\n",
       "      <td>112650</td>\n",
       "      <td>112650</td>\n",
       "      <td>112650.000000</td>\n",
       "      <td>112650.000000</td>\n",
       "      <td>112650</td>\n",
       "      <td>111047.000000</td>\n",
       "      <td>111047.000000</td>\n",
       "      <td>111047.000000</td>\n",
       "      <td>112632.000000</td>\n",
       "      <td>112632.000000</td>\n",
       "      <td>112632.000000</td>\n",
       "      <td>112632.000000</td>\n",
       "      <td>112650</td>\n",
       "      <td>112650</td>\n",
       "      <td>112650</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>unique</th>\n",
       "      <td>98666</td>\n",
       "      <td>NaN</td>\n",
       "      <td>32951</td>\n",
       "      <td>3095</td>\n",
       "      <td>93318</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>74</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>74</td>\n",
       "      <td>611</td>\n",
       "      <td>23</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>top</th>\n",
       "      <td>8272b63d03f5f79c56e9e4120aec44ef</td>\n",
       "      <td>NaN</td>\n",
       "      <td>aca2eb7d00ea1a7b8ebd4e68314663af</td>\n",
       "      <td>6560211a19b47992c3666cc44a7e94c0</td>\n",
       "      <td>2017-07-21 18:25:23</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>cama_mesa_banho</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>bed_bath_table</td>\n",
       "      <td>sao paulo</td>\n",
       "      <td>SP</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>freq</th>\n",
       "      <td>21</td>\n",
       "      <td>NaN</td>\n",
       "      <td>527</td>\n",
       "      <td>2033</td>\n",
       "      <td>21</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>11115</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>11115</td>\n",
       "      <td>27983</td>\n",
       "      <td>80342</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>first</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2016-09-19 00:15:34</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>last</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2020-04-09 22:35:08</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>NaN</td>\n",
       "      <td>1.197834</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>120.653739</td>\n",
       "      <td>19.990320</td>\n",
       "      <td>NaN</td>\n",
       "      <td>48.775978</td>\n",
       "      <td>787.867029</td>\n",
       "      <td>2.209713</td>\n",
       "      <td>2093.672047</td>\n",
       "      <td>30.153669</td>\n",
       "      <td>16.593766</td>\n",
       "      <td>22.996546</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>NaN</td>\n",
       "      <td>0.705124</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>183.633928</td>\n",
       "      <td>15.806405</td>\n",
       "      <td>NaN</td>\n",
       "      <td>10.025581</td>\n",
       "      <td>652.135608</td>\n",
       "      <td>1.721438</td>\n",
       "      <td>3751.596884</td>\n",
       "      <td>16.153449</td>\n",
       "      <td>13.443483</td>\n",
       "      <td>11.707268</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>NaN</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.850000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>7.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>6.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>NaN</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>39.900000</td>\n",
       "      <td>13.080000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>42.000000</td>\n",
       "      <td>348.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>300.000000</td>\n",
       "      <td>18.000000</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>15.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>NaN</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>74.990000</td>\n",
       "      <td>16.260000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>52.000000</td>\n",
       "      <td>603.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>700.000000</td>\n",
       "      <td>25.000000</td>\n",
       "      <td>13.000000</td>\n",
       "      <td>20.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>NaN</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>134.900000</td>\n",
       "      <td>21.150000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>57.000000</td>\n",
       "      <td>987.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>1800.000000</td>\n",
       "      <td>38.000000</td>\n",
       "      <td>20.000000</td>\n",
       "      <td>30.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>NaN</td>\n",
       "      <td>21.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>6735.000000</td>\n",
       "      <td>409.680000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>76.000000</td>\n",
       "      <td>3992.000000</td>\n",
       "      <td>20.000000</td>\n",
       "      <td>40425.000000</td>\n",
       "      <td>105.000000</td>\n",
       "      <td>105.000000</td>\n",
       "      <td>118.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                order_id  order_item_id  \\\n",
       "count                             112650  112650.000000   \n",
       "unique                             98666            NaN   \n",
       "top     8272b63d03f5f79c56e9e4120aec44ef            NaN   \n",
       "freq                                  21            NaN   \n",
       "first                                NaN            NaN   \n",
       "last                                 NaN            NaN   \n",
       "mean                                 NaN       1.197834   \n",
       "std                                  NaN       0.705124   \n",
       "min                                  NaN       1.000000   \n",
       "25%                                  NaN       1.000000   \n",
       "50%                                  NaN       1.000000   \n",
       "75%                                  NaN       1.000000   \n",
       "max                                  NaN      21.000000   \n",
       "\n",
       "                              product_id                         seller_id  \\\n",
       "count                             112650                            112650   \n",
       "unique                             32951                              3095   \n",
       "top     aca2eb7d00ea1a7b8ebd4e68314663af  6560211a19b47992c3666cc44a7e94c0   \n",
       "freq                                 527                              2033   \n",
       "first                                NaN                               NaN   \n",
       "last                                 NaN                               NaN   \n",
       "mean                                 NaN                               NaN   \n",
       "std                                  NaN                               NaN   \n",
       "min                                  NaN                               NaN   \n",
       "25%                                  NaN                               NaN   \n",
       "50%                                  NaN                               NaN   \n",
       "75%                                  NaN                               NaN   \n",
       "max                                  NaN                               NaN   \n",
       "\n",
       "        shipping_limit_date          price  freight_value  \\\n",
       "count                112650  112650.000000  112650.000000   \n",
       "unique                93318            NaN            NaN   \n",
       "top     2017-07-21 18:25:23            NaN            NaN   \n",
       "freq                     21            NaN            NaN   \n",
       "first   2016-09-19 00:15:34            NaN            NaN   \n",
       "last    2020-04-09 22:35:08            NaN            NaN   \n",
       "mean                    NaN     120.653739      19.990320   \n",
       "std                     NaN     183.633928      15.806405   \n",
       "min                     NaN       0.850000       0.000000   \n",
       "25%                     NaN      39.900000      13.080000   \n",
       "50%                     NaN      74.990000      16.260000   \n",
       "75%                     NaN     134.900000      21.150000   \n",
       "max                     NaN    6735.000000     409.680000   \n",
       "\n",
       "       product_category_name  product_name_lenght  product_description_lenght  \\\n",
       "count                 112650        111047.000000               111047.000000   \n",
       "unique                    74                  NaN                         NaN   \n",
       "top          cama_mesa_banho                  NaN                         NaN   \n",
       "freq                   11115                  NaN                         NaN   \n",
       "first                    NaN                  NaN                         NaN   \n",
       "last                     NaN                  NaN                         NaN   \n",
       "mean                     NaN            48.775978                  787.867029   \n",
       "std                      NaN            10.025581                  652.135608   \n",
       "min                      NaN             5.000000                    4.000000   \n",
       "25%                      NaN            42.000000                  348.000000   \n",
       "50%                      NaN            52.000000                  603.000000   \n",
       "75%                      NaN            57.000000                  987.000000   \n",
       "max                      NaN            76.000000                 3992.000000   \n",
       "\n",
       "        product_photos_qty  product_weight_g  product_length_cm  \\\n",
       "count        111047.000000     112632.000000      112632.000000   \n",
       "unique                 NaN               NaN                NaN   \n",
       "top                    NaN               NaN                NaN   \n",
       "freq                   NaN               NaN                NaN   \n",
       "first                  NaN               NaN                NaN   \n",
       "last                   NaN               NaN                NaN   \n",
       "mean              2.209713       2093.672047          30.153669   \n",
       "std               1.721438       3751.596884          16.153449   \n",
       "min               1.000000          0.000000           7.000000   \n",
       "25%               1.000000        300.000000          18.000000   \n",
       "50%               1.000000        700.000000          25.000000   \n",
       "75%               3.000000       1800.000000          38.000000   \n",
       "max              20.000000      40425.000000         105.000000   \n",
       "\n",
       "        product_height_cm  product_width_cm product_category_name_english  \\\n",
       "count       112632.000000     112632.000000                        112650   \n",
       "unique                NaN               NaN                            74   \n",
       "top                   NaN               NaN                bed_bath_table   \n",
       "freq                  NaN               NaN                         11115   \n",
       "first                 NaN               NaN                           NaN   \n",
       "last                  NaN               NaN                           NaN   \n",
       "mean            16.593766         22.996546                           NaN   \n",
       "std             13.443483         11.707268                           NaN   \n",
       "min              2.000000          6.000000                           NaN   \n",
       "25%              8.000000         15.000000                           NaN   \n",
       "50%             13.000000         20.000000                           NaN   \n",
       "75%             20.000000         30.000000                           NaN   \n",
       "max            105.000000        118.000000                           NaN   \n",
       "\n",
       "       seller_city seller_state  \n",
       "count       112650       112650  \n",
       "unique         611           23  \n",
       "top      sao paulo           SP  \n",
       "freq         27983        80342  \n",
       "first          NaN          NaN  \n",
       "last           NaN          NaN  \n",
       "mean           NaN          NaN  \n",
       "std            NaN          NaN  \n",
       "min            NaN          NaN  \n",
       "25%            NaN          NaN  \n",
       "50%            NaN          NaN  \n",
       "75%            NaN          NaN  \n",
       "max            NaN          NaN  "
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_order_items.describe(include=\"all\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3c923d9f",
   "metadata": {
    "papermill": {
     "duration": 0.025057,
     "end_time": "2023-10-18T10:08:27.162835",
     "exception": false,
     "start_time": "2023-10-18T10:08:27.137778",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "terdapat range yang luas pada kolom price san fright_value. dari rangkuman parameter statistik diatas dapat dilihat categori yang paling laris adalah bed_bath_table, dengan sao paulo (SP) brazil merupakan kota yang aktif menjual."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "22348dff",
   "metadata": {
    "papermill": {
     "duration": 0.027049,
     "end_time": "2023-10-18T10:08:27.217155",
     "exception": false,
     "start_time": "2023-10-18T10:08:27.190106",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "###  Price dengan category"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "bf136bd8",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:27.272016Z",
     "iopub.status.busy": "2023-10-18T10:08:27.271589Z",
     "iopub.status.idle": "2023-10-18T10:08:27.326581Z",
     "shell.execute_reply": "2023-10-18T10:08:27.325521Z"
    },
    "papermill": {
     "duration": 0.085744,
     "end_time": "2023-10-18T10:08:27.328762",
     "exception": false,
     "start_time": "2023-10-18T10:08:27.243018",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead tr th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe thead tr:last-of-type th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr>\n",
       "      <th></th>\n",
       "      <th>product_id</th>\n",
       "      <th colspan=\"4\" halign=\"left\">price</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th></th>\n",
       "      <th>count</th>\n",
       "      <th>max</th>\n",
       "      <th>min</th>\n",
       "      <th>mean</th>\n",
       "      <th>range</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>product_category_name_english</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>bed_bath_table</th>\n",
       "      <td>11115</td>\n",
       "      <td>1999.98</td>\n",
       "      <td>6.99</td>\n",
       "      <td>93.296327</td>\n",
       "      <td>1992.99</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>health_beauty</th>\n",
       "      <td>9670</td>\n",
       "      <td>3124.00</td>\n",
       "      <td>1.20</td>\n",
       "      <td>130.163531</td>\n",
       "      <td>3122.80</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>sports_leisure</th>\n",
       "      <td>8641</td>\n",
       "      <td>4059.00</td>\n",
       "      <td>4.50</td>\n",
       "      <td>114.344285</td>\n",
       "      <td>4054.50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>furniture_decor</th>\n",
       "      <td>8334</td>\n",
       "      <td>1899.00</td>\n",
       "      <td>4.90</td>\n",
       "      <td>87.564494</td>\n",
       "      <td>1894.10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>computers_accessories</th>\n",
       "      <td>7827</td>\n",
       "      <td>3699.99</td>\n",
       "      <td>3.90</td>\n",
       "      <td>116.513903</td>\n",
       "      <td>3696.09</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>cds_dvds_musicals</th>\n",
       "      <td>14</td>\n",
       "      <td>65.00</td>\n",
       "      <td>45.00</td>\n",
       "      <td>52.142857</td>\n",
       "      <td>20.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>la_cuisine</th>\n",
       "      <td>14</td>\n",
       "      <td>389.00</td>\n",
       "      <td>24.00</td>\n",
       "      <td>146.785000</td>\n",
       "      <td>365.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>PC Gaming</th>\n",
       "      <td>9</td>\n",
       "      <td>239.00</td>\n",
       "      <td>129.99</td>\n",
       "      <td>171.772222</td>\n",
       "      <td>109.01</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>fashion_childrens_clothes</th>\n",
       "      <td>8</td>\n",
       "      <td>110.00</td>\n",
       "      <td>39.99</td>\n",
       "      <td>71.231250</td>\n",
       "      <td>70.01</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>security_and_services</th>\n",
       "      <td>2</td>\n",
       "      <td>183.29</td>\n",
       "      <td>100.00</td>\n",
       "      <td>141.645000</td>\n",
       "      <td>83.29</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>74 rows × 5 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                              product_id    price                             \n",
       "                                   count      max     min        mean    range\n",
       "product_category_name_english                                                 \n",
       "bed_bath_table                     11115  1999.98    6.99   93.296327  1992.99\n",
       "health_beauty                       9670  3124.00    1.20  130.163531  3122.80\n",
       "sports_leisure                      8641  4059.00    4.50  114.344285  4054.50\n",
       "furniture_decor                     8334  1899.00    4.90   87.564494  1894.10\n",
       "computers_accessories               7827  3699.99    3.90  116.513903  3696.09\n",
       "...                                  ...      ...     ...         ...      ...\n",
       "cds_dvds_musicals                     14    65.00   45.00   52.142857    20.00\n",
       "la_cuisine                            14   389.00   24.00  146.785000   365.00\n",
       "PC Gaming                              9   239.00  129.99  171.772222   109.01\n",
       "fashion_childrens_clothes              8   110.00   39.99   71.231250    70.01\n",
       "security_and_services                  2   183.29  100.00  141.645000    83.29\n",
       "\n",
       "[74 rows x 5 columns]"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_order_items.groupby(by=\"product_category_name_english\").agg({\n",
    "    \"product_id\": \"count\", #jumlah pembelian\n",
    "    \"price\": [\"max\", \"min\", \"mean\", range]\n",
    "}).sort_values(by=(\"product_id\", \"count\"), ascending=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "124d85f4",
   "metadata": {
    "papermill": {
     "duration": 0.026971,
     "end_time": "2023-10-18T10:08:27.381704",
     "exception": false,
     "start_time": "2023-10-18T10:08:27.354733",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "bed_bath_table, health_beauty, sports_leisure, furniture_decor, dan computers_accessories merupakan category dengan pembelian terbanyak. Begitupula harga yang dijual dalam Brazilian E-Commerce ini sangat bervasiasi bahkan dalam satu kategorinya, range nya cukup besar."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e3f44d56",
   "metadata": {
    "papermill": {
     "duration": 0.02543,
     "end_time": "2023-10-18T10:08:27.434244",
     "exception": false,
     "start_time": "2023-10-18T10:08:27.408814",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "### Persebaran kota penjual"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "2515a06c",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:27.490289Z",
     "iopub.status.busy": "2023-10-18T10:08:27.489913Z",
     "iopub.status.idle": "2023-10-18T10:08:27.531715Z",
     "shell.execute_reply": "2023-10-18T10:08:27.530956Z"
    },
    "papermill": {
     "duration": 0.072437,
     "end_time": "2023-10-18T10:08:27.533976",
     "exception": false,
     "start_time": "2023-10-18T10:08:27.461539",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "seller_city\n",
       "sao paulo         694\n",
       "curitiba          127\n",
       "rio de janeiro     96\n",
       "belo horizonte     68\n",
       "ribeirao preto     52\n",
       "                 ... \n",
       "ivoti               1\n",
       "itirapina           1\n",
       "itau de minas       1\n",
       "itapui              1\n",
       "xaxim               1\n",
       "Name: seller_id, Length: 611, dtype: int64"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_order_items.groupby(by=\"seller_city\").seller_id.nunique().sort_values(ascending=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "89eee064",
   "metadata": {
    "papermill": {
     "duration": 0.026684,
     "end_time": "2023-10-18T10:08:27.587401",
     "exception": false,
     "start_time": "2023-10-18T10:08:27.560717",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "### Persebaran state penjual"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "1010a767",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:27.642347Z",
     "iopub.status.busy": "2023-10-18T10:08:27.641991Z",
     "iopub.status.idle": "2023-10-18T10:08:27.678787Z",
     "shell.execute_reply": "2023-10-18T10:08:27.677848Z"
    },
    "papermill": {
     "duration": 0.067521,
     "end_time": "2023-10-18T10:08:27.681022",
     "exception": false,
     "start_time": "2023-10-18T10:08:27.613501",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "seller_state\n",
       "SP    1849\n",
       "PR     349\n",
       "MG     244\n",
       "SC     190\n",
       "RJ     171\n",
       "RS     129\n",
       "GO      40\n",
       "DF      30\n",
       "ES      23\n",
       "BA      19\n",
       "CE      13\n",
       "PE       9\n",
       "PB       6\n",
       "MS       5\n",
       "RN       5\n",
       "MT       4\n",
       "RO       2\n",
       "SE       2\n",
       "AC       1\n",
       "PI       1\n",
       "AM       1\n",
       "MA       1\n",
       "PA       1\n",
       "Name: seller_id, dtype: int64"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_order_items.groupby(by=\"seller_state\").seller_id.nunique().sort_values(ascending=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "41585432",
   "metadata": {
    "papermill": {
     "duration": 0.025952,
     "end_time": "2023-10-18T10:08:27.733189",
     "exception": false,
     "start_time": "2023-10-18T10:08:27.707237",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "### seller, banyak produk, total order, dan range price"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "3222ef7f",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:27.787592Z",
     "iopub.status.busy": "2023-10-18T10:08:27.787239Z",
     "iopub.status.idle": "2023-10-18T10:08:28.241969Z",
     "shell.execute_reply": "2023-10-18T10:08:28.240471Z"
    },
    "papermill": {
     "duration": 0.485248,
     "end_time": "2023-10-18T10:08:28.244223",
     "exception": false,
     "start_time": "2023-10-18T10:08:27.758975",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead tr th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe thead tr:last-of-type th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr>\n",
       "      <th></th>\n",
       "      <th>product_id</th>\n",
       "      <th>order_id</th>\n",
       "      <th colspan=\"4\" halign=\"left\">price</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th></th>\n",
       "      <th>nunique</th>\n",
       "      <th>nunique</th>\n",
       "      <th>max</th>\n",
       "      <th>min</th>\n",
       "      <th>mean</th>\n",
       "      <th>range</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>seller_id</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>6560211a19b47992c3666cc44a7e94c0</th>\n",
       "      <td>256</td>\n",
       "      <td>1854</td>\n",
       "      <td>249.00</td>\n",
       "      <td>16.00</td>\n",
       "      <td>60.651663</td>\n",
       "      <td>233.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4a3ca9315b744ce9f8e9374361493884</th>\n",
       "      <td>399</td>\n",
       "      <td>1806</td>\n",
       "      <td>884.00</td>\n",
       "      <td>12.90</td>\n",
       "      <td>100.892260</td>\n",
       "      <td>871.10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>cc419e0650a3c5ba77189a1882b7556a</th>\n",
       "      <td>37</td>\n",
       "      <td>1706</td>\n",
       "      <td>229.99</td>\n",
       "      <td>6.00</td>\n",
       "      <td>58.754039</td>\n",
       "      <td>223.99</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1f50f920176fa81dab994f9023523100</th>\n",
       "      <td>23</td>\n",
       "      <td>1404</td>\n",
       "      <td>119.90</td>\n",
       "      <td>38.90</td>\n",
       "      <td>55.380223</td>\n",
       "      <td>81.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>da8622b14eb17ae2831f4ac5b9dab84a</th>\n",
       "      <td>222</td>\n",
       "      <td>1314</td>\n",
       "      <td>429.90</td>\n",
       "      <td>9.90</td>\n",
       "      <td>103.311779</td>\n",
       "      <td>420.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>ceb7b4fb9401cd378de7886317ad1b47</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>399.90</td>\n",
       "      <td>399.90</td>\n",
       "      <td>399.900000</td>\n",
       "      <td>0.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>cecd97bc34ed8330bd4cd15713eda670</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>57.99</td>\n",
       "      <td>57.99</td>\n",
       "      <td>57.990000</td>\n",
       "      <td>0.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5b92bfa4120daa27c574daa2e386c693</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>14.00</td>\n",
       "      <td>14.00</td>\n",
       "      <td>14.000000</td>\n",
       "      <td>0.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5aaa890629f83706d8d9bfecd8377c1c</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>48.90</td>\n",
       "      <td>48.90</td>\n",
       "      <td>48.900000</td>\n",
       "      <td>0.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7d81e74a4755b552267cd5e081563028</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>32.50</td>\n",
       "      <td>32.50</td>\n",
       "      <td>32.500000</td>\n",
       "      <td>0.00</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>3095 rows × 6 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                                 product_id order_id   price          \\\n",
       "                                    nunique  nunique     max     min   \n",
       "seller_id                                                              \n",
       "6560211a19b47992c3666cc44a7e94c0        256     1854  249.00   16.00   \n",
       "4a3ca9315b744ce9f8e9374361493884        399     1806  884.00   12.90   \n",
       "cc419e0650a3c5ba77189a1882b7556a         37     1706  229.99    6.00   \n",
       "1f50f920176fa81dab994f9023523100         23     1404  119.90   38.90   \n",
       "da8622b14eb17ae2831f4ac5b9dab84a        222     1314  429.90    9.90   \n",
       "...                                     ...      ...     ...     ...   \n",
       "ceb7b4fb9401cd378de7886317ad1b47          1        1  399.90  399.90   \n",
       "cecd97bc34ed8330bd4cd15713eda670          1        1   57.99   57.99   \n",
       "5b92bfa4120daa27c574daa2e386c693          1        1   14.00   14.00   \n",
       "5aaa890629f83706d8d9bfecd8377c1c          1        1   48.90   48.90   \n",
       "7d81e74a4755b552267cd5e081563028          1        1   32.50   32.50   \n",
       "\n",
       "                                                      \n",
       "                                        mean   range  \n",
       "seller_id                                             \n",
       "6560211a19b47992c3666cc44a7e94c0   60.651663  233.00  \n",
       "4a3ca9315b744ce9f8e9374361493884  100.892260  871.10  \n",
       "cc419e0650a3c5ba77189a1882b7556a   58.754039  223.99  \n",
       "1f50f920176fa81dab994f9023523100   55.380223   81.00  \n",
       "da8622b14eb17ae2831f4ac5b9dab84a  103.311779  420.00  \n",
       "...                                      ...     ...  \n",
       "ceb7b4fb9401cd378de7886317ad1b47  399.900000    0.00  \n",
       "cecd97bc34ed8330bd4cd15713eda670   57.990000    0.00  \n",
       "5b92bfa4120daa27c574daa2e386c693   14.000000    0.00  \n",
       "5aaa890629f83706d8d9bfecd8377c1c   48.900000    0.00  \n",
       "7d81e74a4755b552267cd5e081563028   32.500000    0.00  \n",
       "\n",
       "[3095 rows x 6 columns]"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_order_items.groupby(by=\"seller_id\").agg({\n",
    "    \"product_id\": \"nunique\",\n",
    "    \"order_id\": \"nunique\",\n",
    "    \"price\": [\"max\", \"min\", \"mean\", range]\n",
    "}).sort_values(by=(\"order_id\", \"nunique\"), ascending=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ba7fdd48",
   "metadata": {
    "papermill": {
     "duration": 0.029757,
     "end_time": "2023-10-18T10:08:28.301546",
     "exception": false,
     "start_time": "2023-10-18T10:08:28.271789",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "terlihat best seller pada umumnya memiliki banyak produk"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "25674acb",
   "metadata": {
    "papermill": {
     "duration": 0.027136,
     "end_time": "2023-10-18T10:08:28.357188",
     "exception": false,
     "start_time": "2023-10-18T10:08:28.330052",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "### melihat persebaran jumlah order disetiap tahun dan bulannya"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "a36fe1ae",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:28.413972Z",
     "iopub.status.busy": "2023-10-18T10:08:28.413085Z",
     "iopub.status.idle": "2023-10-18T10:08:28.453182Z",
     "shell.execute_reply": "2023-10-18T10:08:28.452149Z"
    },
    "papermill": {
     "duration": 0.071148,
     "end_time": "2023-10-18T10:08:28.455386",
     "exception": false,
     "start_time": "2023-10-18T10:08:28.384238",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "year\n",
       "2016      328\n",
       "2017    45101\n",
       "2018    54011\n",
       "Name: order_id, dtype: int64"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "orders.groupby(by=\"year\").order_id.nunique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "e469cd2b",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:28.511408Z",
     "iopub.status.busy": "2023-10-18T10:08:28.510745Z",
     "iopub.status.idle": "2023-10-18T10:08:28.553334Z",
     "shell.execute_reply": "2023-10-18T10:08:28.552284Z"
    },
    "papermill": {
     "duration": 0.073612,
     "end_time": "2023-10-18T10:08:28.556129",
     "exception": false,
     "start_time": "2023-10-18T10:08:28.482517",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "month\n",
       "01-2017     800\n",
       "01-2018    7269\n",
       "02-2017    1780\n",
       "02-2018    6728\n",
       "03-2017    2682\n",
       "03-2018    7211\n",
       "04-2017    2404\n",
       "04-2018    6939\n",
       "05-2017    3700\n",
       "05-2018    6873\n",
       "06-2017    3245\n",
       "06-2018    6167\n",
       "07-2017    4026\n",
       "07-2018    6292\n",
       "08-2017    4331\n",
       "08-2018    6512\n",
       "09-2016       3\n",
       "09-2017    4285\n",
       "09-2018      16\n",
       "10-2016     324\n",
       "10-2017    4631\n",
       "10-2018       4\n",
       "11-2017    7544\n",
       "12-2016       1\n",
       "12-2017    5673\n",
       "Name: order_id, dtype: int64"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "orders.groupby(by=\"month\").order_id.nunique()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1619f95f",
   "metadata": {
    "papermill": {
     "duration": 0.027714,
     "end_time": "2023-10-18T10:08:28.611912",
     "exception": false,
     "start_time": "2023-10-18T10:08:28.584198",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "dari dua code diatas, dapat dilihat bahwa persebaran order tidak merata karena order pada tahun 2020 hanya ada dibulan februari dan april, sedangkan 2016 hanya terdapat di 2 bulan yaitu oktober dan desember. Begitupula untuk tahun 2018  yang tidak genap 1 tahun, yaitu hanya terdapat pada bulan januari hingga agustus  sehingga hanya tahun 2017 yang memiliki data lengkap tetang jumlah ordernya."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a043b202",
   "metadata": {
    "papermill": {
     "duration": 0.026568,
     "end_time": "2023-10-18T10:08:28.665151",
     "exception": false,
     "start_time": "2023-10-18T10:08:28.638583",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## Explore table `orders`\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "2e2a4283",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:28.724154Z",
     "iopub.status.busy": "2023-10-18T10:08:28.723801Z",
     "iopub.status.idle": "2023-10-18T10:08:29.036042Z",
     "shell.execute_reply": "2023-10-18T10:08:29.034936Z"
    },
    "papermill": {
     "duration": 0.346135,
     "end_time": "2023-10-18T10:08:29.038198",
     "exception": false,
     "start_time": "2023-10-18T10:08:28.692063",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>order_id</th>\n",
       "      <th>customer_id</th>\n",
       "      <th>order_status</th>\n",
       "      <th>order_purchase_timestamp</th>\n",
       "      <th>order_approved_at</th>\n",
       "      <th>order_delivered_carrier_date</th>\n",
       "      <th>order_delivered_customer_date</th>\n",
       "      <th>order_estimated_delivery_date</th>\n",
       "      <th>payment_type</th>\n",
       "      <th>payment_value</th>\n",
       "      <th>customer_zip_code_prefix</th>\n",
       "      <th>customer_city</th>\n",
       "      <th>customer_state</th>\n",
       "      <th>year</th>\n",
       "      <th>month</th>\n",
       "      <th>lama_pengiriman_hari</th>\n",
       "      <th>hari_pembelian</th>\n",
       "      <th>jam_pembelian</th>\n",
       "      <th>waktu_hari_pembelian</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>103271</td>\n",
       "      <td>103271</td>\n",
       "      <td>103271</td>\n",
       "      <td>103271</td>\n",
       "      <td>103106</td>\n",
       "      <td>101410</td>\n",
       "      <td>100172</td>\n",
       "      <td>103271</td>\n",
       "      <td>103271</td>\n",
       "      <td>103271.000000</td>\n",
       "      <td>103271.000000</td>\n",
       "      <td>103271</td>\n",
       "      <td>103271</td>\n",
       "      <td>103271</td>\n",
       "      <td>103271</td>\n",
       "      <td>100171.000000</td>\n",
       "      <td>103271</td>\n",
       "      <td>103271.000000</td>\n",
       "      <td>103271</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>unique</th>\n",
       "      <td>99440</td>\n",
       "      <td>99440</td>\n",
       "      <td>8</td>\n",
       "      <td>98874</td>\n",
       "      <td>90732</td>\n",
       "      <td>81017</td>\n",
       "      <td>95663</td>\n",
       "      <td>458</td>\n",
       "      <td>5</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4119</td>\n",
       "      <td>27</td>\n",
       "      <td>3</td>\n",
       "      <td>25</td>\n",
       "      <td>NaN</td>\n",
       "      <td>7</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>top</th>\n",
       "      <td>fa65dad1b0e818e3ccc5cb0e39231352</td>\n",
       "      <td>9af2372a1e49340278e7c1ef8d749f34</td>\n",
       "      <td>delivered</td>\n",
       "      <td>2017-04-20 12:45:34</td>\n",
       "      <td>2017-04-22 09:10:13</td>\n",
       "      <td>2018-05-09 15:48:00</td>\n",
       "      <td>2017-06-22 16:04:46</td>\n",
       "      <td>2017-12-20 00:00:00</td>\n",
       "      <td>credit_card</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>sao paulo</td>\n",
       "      <td>SP</td>\n",
       "      <td>2018</td>\n",
       "      <td>11-2017</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Monday</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Siang</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>freq</th>\n",
       "      <td>25</td>\n",
       "      <td>25</td>\n",
       "      <td>100174</td>\n",
       "      <td>25</td>\n",
       "      <td>25</td>\n",
       "      <td>47</td>\n",
       "      <td>22</td>\n",
       "      <td>560</td>\n",
       "      <td>76782</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>16104</td>\n",
       "      <td>43332</td>\n",
       "      <td>55738</td>\n",
       "      <td>7816</td>\n",
       "      <td>NaN</td>\n",
       "      <td>16766</td>\n",
       "      <td>NaN</td>\n",
       "      <td>39508</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>first</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2016-09-04 21:15:19</td>\n",
       "      <td>2016-10-04 09:43:32</td>\n",
       "      <td>2016-10-08 10:34:01</td>\n",
       "      <td>2016-10-11 13:46:32</td>\n",
       "      <td>2016-09-30 00:00:00</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>last</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2018-10-17 17:30:18</td>\n",
       "      <td>2018-09-03 17:40:06</td>\n",
       "      <td>2018-09-11 19:48:28</td>\n",
       "      <td>2018-10-17 13:22:46</td>\n",
       "      <td>2018-11-12 00:00:00</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>154.845047</td>\n",
       "      <td>35088.683909</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>8.892574</td>\n",
       "      <td>NaN</td>\n",
       "      <td>14.780297</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>217.897537</td>\n",
       "      <td>29750.470243</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>8.757410</td>\n",
       "      <td>NaN</td>\n",
       "      <td>5.332535</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1003.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-17.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>57.490000</td>\n",
       "      <td>11380.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>11.000000</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>100.340000</td>\n",
       "      <td>24411.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>7.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>15.000000</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>172.455000</td>\n",
       "      <td>58431.500000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>12.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>19.000000</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>13664.080000</td>\n",
       "      <td>99990.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>205.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>23.000000</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                order_id                       customer_id  \\\n",
       "count                             103271                            103271   \n",
       "unique                             99440                             99440   \n",
       "top     fa65dad1b0e818e3ccc5cb0e39231352  9af2372a1e49340278e7c1ef8d749f34   \n",
       "freq                                  25                                25   \n",
       "first                                NaN                               NaN   \n",
       "last                                 NaN                               NaN   \n",
       "mean                                 NaN                               NaN   \n",
       "std                                  NaN                               NaN   \n",
       "min                                  NaN                               NaN   \n",
       "25%                                  NaN                               NaN   \n",
       "50%                                  NaN                               NaN   \n",
       "75%                                  NaN                               NaN   \n",
       "max                                  NaN                               NaN   \n",
       "\n",
       "       order_status order_purchase_timestamp    order_approved_at  \\\n",
       "count        103271                   103271               103106   \n",
       "unique            8                    98874                90732   \n",
       "top       delivered      2017-04-20 12:45:34  2017-04-22 09:10:13   \n",
       "freq         100174                       25                   25   \n",
       "first           NaN      2016-09-04 21:15:19  2016-10-04 09:43:32   \n",
       "last            NaN      2018-10-17 17:30:18  2018-09-03 17:40:06   \n",
       "mean            NaN                      NaN                  NaN   \n",
       "std             NaN                      NaN                  NaN   \n",
       "min             NaN                      NaN                  NaN   \n",
       "25%             NaN                      NaN                  NaN   \n",
       "50%             NaN                      NaN                  NaN   \n",
       "75%             NaN                      NaN                  NaN   \n",
       "max             NaN                      NaN                  NaN   \n",
       "\n",
       "       order_delivered_carrier_date order_delivered_customer_date  \\\n",
       "count                        101410                        100172   \n",
       "unique                        81017                         95663   \n",
       "top             2018-05-09 15:48:00           2017-06-22 16:04:46   \n",
       "freq                             47                            22   \n",
       "first           2016-10-08 10:34:01           2016-10-11 13:46:32   \n",
       "last            2018-09-11 19:48:28           2018-10-17 13:22:46   \n",
       "mean                            NaN                           NaN   \n",
       "std                             NaN                           NaN   \n",
       "min                             NaN                           NaN   \n",
       "25%                             NaN                           NaN   \n",
       "50%                             NaN                           NaN   \n",
       "75%                             NaN                           NaN   \n",
       "max                             NaN                           NaN   \n",
       "\n",
       "       order_estimated_delivery_date payment_type  payment_value  \\\n",
       "count                         103271       103271  103271.000000   \n",
       "unique                           458            5            NaN   \n",
       "top              2017-12-20 00:00:00  credit_card            NaN   \n",
       "freq                             560        76782            NaN   \n",
       "first            2016-09-30 00:00:00          NaN            NaN   \n",
       "last             2018-11-12 00:00:00          NaN            NaN   \n",
       "mean                             NaN          NaN     154.845047   \n",
       "std                              NaN          NaN     217.897537   \n",
       "min                              NaN          NaN       0.000000   \n",
       "25%                              NaN          NaN      57.490000   \n",
       "50%                              NaN          NaN     100.340000   \n",
       "75%                              NaN          NaN     172.455000   \n",
       "max                              NaN          NaN   13664.080000   \n",
       "\n",
       "        customer_zip_code_prefix customer_city customer_state    year  \\\n",
       "count              103271.000000        103271         103271  103271   \n",
       "unique                       NaN          4119             27       3   \n",
       "top                          NaN     sao paulo             SP    2018   \n",
       "freq                         NaN         16104          43332   55738   \n",
       "first                        NaN           NaN            NaN     NaN   \n",
       "last                         NaN           NaN            NaN     NaN   \n",
       "mean                35088.683909           NaN            NaN     NaN   \n",
       "std                 29750.470243           NaN            NaN     NaN   \n",
       "min                  1003.000000           NaN            NaN     NaN   \n",
       "25%                 11380.000000           NaN            NaN     NaN   \n",
       "50%                 24411.000000           NaN            NaN     NaN   \n",
       "75%                 58431.500000           NaN            NaN     NaN   \n",
       "max                 99990.000000           NaN            NaN     NaN   \n",
       "\n",
       "          month  lama_pengiriman_hari hari_pembelian  jam_pembelian  \\\n",
       "count    103271         100171.000000         103271  103271.000000   \n",
       "unique       25                   NaN              7            NaN   \n",
       "top     11-2017                   NaN         Monday            NaN   \n",
       "freq       7816                   NaN          16766            NaN   \n",
       "first       NaN                   NaN            NaN            NaN   \n",
       "last        NaN                   NaN            NaN            NaN   \n",
       "mean        NaN              8.892574            NaN      14.780297   \n",
       "std         NaN              8.757410            NaN       5.332535   \n",
       "min         NaN            -17.000000            NaN       0.000000   \n",
       "25%         NaN              4.000000            NaN      11.000000   \n",
       "50%         NaN              7.000000            NaN      15.000000   \n",
       "75%         NaN             12.000000            NaN      19.000000   \n",
       "max         NaN            205.000000            NaN      23.000000   \n",
       "\n",
       "       waktu_hari_pembelian  \n",
       "count                103271  \n",
       "unique                    4  \n",
       "top                   Siang  \n",
       "freq                  39508  \n",
       "first                   NaN  \n",
       "last                    NaN  \n",
       "mean                    NaN  \n",
       "std                     NaN  \n",
       "min                     NaN  \n",
       "25%                     NaN  \n",
       "50%                     NaN  \n",
       "75%                     NaN  \n",
       "max                     NaN  "
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "orders.describe(include=\"all\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7a8aa4c3",
   "metadata": {
    "papermill": {
     "duration": 0.027908,
     "end_time": "2023-10-18T10:08:29.094643",
     "exception": false,
     "start_time": "2023-10-18T10:08:29.066735",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "### melihat naik turunnya penjualan disetiap bulan 2017"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "8c79e313",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:29.151220Z",
     "iopub.status.busy": "2023-10-18T10:08:29.150846Z",
     "iopub.status.idle": "2023-10-18T10:08:29.206354Z",
     "shell.execute_reply": "2023-10-18T10:08:29.205201Z"
    },
    "papermill": {
     "duration": 0.086529,
     "end_time": "2023-10-18T10:08:29.208627",
     "exception": false,
     "start_time": "2023-10-18T10:08:29.122098",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "month\n",
      "01-2017       0.0\n",
      "02-2017     980.0\n",
      "03-2017     902.0\n",
      "04-2017    -278.0\n",
      "05-2017    1296.0\n",
      "06-2017    -455.0\n",
      "07-2017     781.0\n",
      "08-2017     305.0\n",
      "09-2017     -46.0\n",
      "10-2017     346.0\n",
      "11-2017    2913.0\n",
      "12-2017   -1871.0\n",
      "Name: order_id, dtype: float64\n",
      "----\n",
      "persentase kenaikan penjualan : \n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "month\n",
       "01-2017      0.000000\n",
       "02-2017    122.500000\n",
       "03-2017     50.674157\n",
       "04-2017    -10.365399\n",
       "05-2017     53.910150\n",
       "06-2017    -12.297297\n",
       "07-2017     24.067797\n",
       "08-2017      7.575758\n",
       "09-2017     -1.062110\n",
       "10-2017      8.074679\n",
       "11-2017     62.902181\n",
       "12-2017    -24.801166\n",
       "Name: order_id, dtype: float64"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_order_2017 = orders[orders['year'] == '2017']\n",
    "x = df_order_2017.groupby('month')['order_id'].nunique()\n",
    "x_diff  = x.diff().fillna(0)\n",
    "print(x_diff)\n",
    "\n",
    "# dalam persentase\n",
    "print(\"----\\npersentase kenaikan penjualan : \")\n",
    "x_percentage = x.pct_change().fillna(0) * 100\n",
    "x_percentage"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d678987b",
   "metadata": {
    "papermill": {
     "duration": 0.026486,
     "end_time": "2023-10-18T10:08:29.264144",
     "exception": false,
     "start_time": "2023-10-18T10:08:29.237658",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "dari statistik diatas, payment value terdiri dari range nilai yang luas, diperkirakan terdapat kesalahan pada input data dikolom order_delivered_customer_date karena nilai minimal kolom pengiriman bernilai minus. data yang terjadi kesalahan tersebut akan dihapus."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "b80e9498",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:29.324016Z",
     "iopub.status.busy": "2023-10-18T10:08:29.323628Z",
     "iopub.status.idle": "2023-10-18T10:08:29.350799Z",
     "shell.execute_reply": "2023-10-18T10:08:29.349486Z"
    },
    "papermill": {
     "duration": 0.059345,
     "end_time": "2023-10-18T10:08:29.353257",
     "exception": false,
     "start_time": "2023-10-18T10:08:29.293912",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "orders = orders[orders[\"lama_pengiriman_hari\"] > 0]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3256e16c",
   "metadata": {
    "papermill": {
     "duration": 0.027675,
     "end_time": "2023-10-18T10:08:29.408079",
     "exception": false,
     "start_time": "2023-10-18T10:08:29.380404",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "### penjualan per hari dan bagiannya"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "86d96f9e",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:29.464700Z",
     "iopub.status.busy": "2023-10-18T10:08:29.464336Z",
     "iopub.status.idle": "2023-10-18T10:08:29.510212Z",
     "shell.execute_reply": "2023-10-18T10:08:29.509196Z"
    },
    "papermill": {
     "duration": 0.07745,
     "end_time": "2023-10-18T10:08:29.512378",
     "exception": false,
     "start_time": "2023-10-18T10:08:29.434928",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "hari_pembelian\n",
       "Monday       15258\n",
       "Tuesday      15045\n",
       "Wednesday    14645\n",
       "Thursday     13961\n",
       "Friday       13320\n",
       "Sunday       11253\n",
       "Saturday     10285\n",
       "Name: order_id, dtype: int64"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "orders.groupby(by=\"hari_pembelian\").order_id.nunique().sort_values(ascending=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "de03f733",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:29.569873Z",
     "iopub.status.busy": "2023-10-18T10:08:29.569190Z",
     "iopub.status.idle": "2023-10-18T10:08:29.606911Z",
     "shell.execute_reply": "2023-10-18T10:08:29.605817Z"
    },
    "papermill": {
     "duration": 0.069335,
     "end_time": "2023-10-18T10:08:29.609313",
     "exception": false,
     "start_time": "2023-10-18T10:08:29.539978",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "waktu_hari_pembelian\n",
       "Siang    35927\n",
       "Malam    26756\n",
       "Pagi     26152\n",
       "Subuh     4932\n",
       "Name: order_id, dtype: int64"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "orders.groupby(by=\"waktu_hari_pembelian\").order_id.nunique().sort_values(ascending=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "a3a3ebc7",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:29.665288Z",
     "iopub.status.busy": "2023-10-18T10:08:29.664925Z",
     "iopub.status.idle": "2023-10-18T10:08:29.721306Z",
     "shell.execute_reply": "2023-10-18T10:08:29.720194Z"
    },
    "papermill": {
     "duration": 0.086852,
     "end_time": "2023-10-18T10:08:29.723519",
     "exception": false,
     "start_time": "2023-10-18T10:08:29.636667",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>hari_pembelian</th>\n",
       "      <th>waktu_hari_pembelian</th>\n",
       "      <th>order_id</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Monday</td>\n",
       "      <td>Siang</td>\n",
       "      <td>5855</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Tuesday</td>\n",
       "      <td>Siang</td>\n",
       "      <td>5782</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Wednesday</td>\n",
       "      <td>Siang</td>\n",
       "      <td>5560</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Thursday</td>\n",
       "      <td>Siang</td>\n",
       "      <td>5357</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Friday</td>\n",
       "      <td>Siang</td>\n",
       "      <td>5150</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Monday</td>\n",
       "      <td>Malam</td>\n",
       "      <td>4537</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Tuesday</td>\n",
       "      <td>Malam</td>\n",
       "      <td>4316</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Wednesday</td>\n",
       "      <td>Pagi</td>\n",
       "      <td>4296</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Tuesday</td>\n",
       "      <td>Pagi</td>\n",
       "      <td>4291</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Sunday</td>\n",
       "      <td>Siang</td>\n",
       "      <td>4252</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>Monday</td>\n",
       "      <td>Pagi</td>\n",
       "      <td>4232</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>Thursday</td>\n",
       "      <td>Pagi</td>\n",
       "      <td>4156</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>Friday</td>\n",
       "      <td>Pagi</td>\n",
       "      <td>4048</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>Sunday</td>\n",
       "      <td>Malam</td>\n",
       "      <td>3991</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>Wednesday</td>\n",
       "      <td>Malam</td>\n",
       "      <td>3989</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>Saturday</td>\n",
       "      <td>Siang</td>\n",
       "      <td>3971</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>Thursday</td>\n",
       "      <td>Malam</td>\n",
       "      <td>3712</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>Friday</td>\n",
       "      <td>Malam</td>\n",
       "      <td>3245</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>Saturday</td>\n",
       "      <td>Malam</td>\n",
       "      <td>2966</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>Saturday</td>\n",
       "      <td>Pagi</td>\n",
       "      <td>2688</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>Sunday</td>\n",
       "      <td>Pagi</td>\n",
       "      <td>2441</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>Friday</td>\n",
       "      <td>Subuh</td>\n",
       "      <td>877</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>Wednesday</td>\n",
       "      <td>Subuh</td>\n",
       "      <td>800</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>Thursday</td>\n",
       "      <td>Subuh</td>\n",
       "      <td>736</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>Saturday</td>\n",
       "      <td>Subuh</td>\n",
       "      <td>660</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>Tuesday</td>\n",
       "      <td>Subuh</td>\n",
       "      <td>656</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>26</th>\n",
       "      <td>Monday</td>\n",
       "      <td>Subuh</td>\n",
       "      <td>634</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>27</th>\n",
       "      <td>Sunday</td>\n",
       "      <td>Subuh</td>\n",
       "      <td>569</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   hari_pembelian waktu_hari_pembelian  order_id\n",
       "0          Monday                Siang      5855\n",
       "1         Tuesday                Siang      5782\n",
       "2       Wednesday                Siang      5560\n",
       "3        Thursday                Siang      5357\n",
       "4          Friday                Siang      5150\n",
       "5          Monday                Malam      4537\n",
       "6         Tuesday                Malam      4316\n",
       "7       Wednesday                 Pagi      4296\n",
       "8         Tuesday                 Pagi      4291\n",
       "9          Sunday                Siang      4252\n",
       "10         Monday                 Pagi      4232\n",
       "11       Thursday                 Pagi      4156\n",
       "12         Friday                 Pagi      4048\n",
       "13         Sunday                Malam      3991\n",
       "14      Wednesday                Malam      3989\n",
       "15       Saturday                Siang      3971\n",
       "16       Thursday                Malam      3712\n",
       "17         Friday                Malam      3245\n",
       "18       Saturday                Malam      2966\n",
       "19       Saturday                 Pagi      2688\n",
       "20         Sunday                 Pagi      2441\n",
       "21         Friday                Subuh       877\n",
       "22      Wednesday                Subuh       800\n",
       "23       Thursday                Subuh       736\n",
       "24       Saturday                Subuh       660\n",
       "25        Tuesday                Subuh       656\n",
       "26         Monday                Subuh       634\n",
       "27         Sunday                Subuh       569"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "orders.groupby([\"hari_pembelian\", 'waktu_hari_pembelian'])['order_id'].nunique().sort_values(ascending=False).reset_index()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "735f6af6",
   "metadata": {
    "papermill": {
     "duration": 0.028007,
     "end_time": "2023-10-18T10:08:29.780285",
     "exception": false,
     "start_time": "2023-10-18T10:08:29.752278",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "banyaknya penjualan harian tertinggi berada pada hari senin, dan terendah di hari sabtu dengan waktu siang di hari kerja merupakan puncak pembelian oleh konsumen."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "901a8f6c",
   "metadata": {
    "papermill": {
     "duration": 0.027359,
     "end_time": "2023-10-18T10:08:29.835824",
     "exception": false,
     "start_time": "2023-10-18T10:08:29.808465",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "### payment_type"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "d2a99419",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:29.893615Z",
     "iopub.status.busy": "2023-10-18T10:08:29.893243Z",
     "iopub.status.idle": "2023-10-18T10:08:29.910821Z",
     "shell.execute_reply": "2023-10-18T10:08:29.910009Z"
    },
    "papermill": {
     "duration": 0.050517,
     "end_time": "2023-10-18T10:08:29.913905",
     "exception": false,
     "start_time": "2023-10-18T10:08:29.863388",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "payment_type\n",
       "credit_card    163.022616\n",
       "boleto         144.934140\n",
       "debit_card     140.778868\n",
       "voucher         66.913499\n",
       "Name: payment_value, dtype: float64"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "orders.groupby(by=\"payment_type\").payment_value.mean().sort_values(ascending=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8b4208ac",
   "metadata": {
    "papermill": {
     "duration": 0.027496,
     "end_time": "2023-10-18T10:08:29.970333",
     "exception": false,
     "start_time": "2023-10-18T10:08:29.942837",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "pembeli yang menggunakan type transaksi credit card memiliki rata-rata pembayaran paling tinggi dibanding tipe traksaksi lainnya sedangkan tipe voucher  melakukan transaksi dengan rata-rata pembayaran paling kecil."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "5eec7902",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:30.031218Z",
     "iopub.status.busy": "2023-10-18T10:08:30.029682Z",
     "iopub.status.idle": "2023-10-18T10:08:30.074843Z",
     "shell.execute_reply": "2023-10-18T10:08:30.073743Z"
    },
    "papermill": {
     "duration": 0.07881,
     "end_time": "2023-10-18T10:08:30.077554",
     "exception": false,
     "start_time": "2023-10-18T10:08:29.998744",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "payment_type\n",
       "credit_card    72200\n",
       "boleto         18683\n",
       "voucher         3569\n",
       "debit_card      1439\n",
       "Name: order_id, dtype: int64"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "orders.groupby(by=\"payment_type\").order_id.nunique().sort_values(ascending=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "386421a8",
   "metadata": {
    "papermill": {
     "duration": 0.029056,
     "end_time": "2023-10-18T10:08:30.134636",
     "exception": false,
     "start_time": "2023-10-18T10:08:30.105580",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "tipe transaksi credit card paling banyak digunakan oleh pembeli sedangkan debit card yang paling sedikit digunakan dibandingkan dengan tipe transaksi lainnya."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b2c610ce",
   "metadata": {
    "papermill": {
     "duration": 0.02777,
     "end_time": "2023-10-18T10:08:30.191455",
     "exception": false,
     "start_time": "2023-10-18T10:08:30.163685",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "### lama pengiriman paket \n",
    "menggunakan nilai median karena terdapat outlier."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "59a4bc65",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:30.252953Z",
     "iopub.status.busy": "2023-10-18T10:08:30.252511Z",
     "iopub.status.idle": "2023-10-18T10:08:30.277741Z",
     "shell.execute_reply": "2023-10-18T10:08:30.276361Z"
    },
    "papermill": {
     "duration": 0.05852,
     "end_time": "2023-10-18T10:08:30.280095",
     "exception": false,
     "start_time": "2023-10-18T10:08:30.221575",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "customer_city\n",
       "novo brasil          145.0\n",
       "capinzal do norte    103.5\n",
       "adhemar de barros     92.0\n",
       "arace                 91.5\n",
       "marcelino vieira      71.0\n",
       "                     ...  \n",
       "iomere                 2.0\n",
       "moeda                  1.0\n",
       "bento de abreu         1.0\n",
       "delfim moreira         1.0\n",
       "bacaxa                 1.0\n",
       "Name: lama_pengiriman_hari, Length: 4083, dtype: float64"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "orders.groupby(by=\"customer_city\").lama_pengiriman_hari.median().sort_values(ascending=False) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "2c169a7e",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:30.341387Z",
     "iopub.status.busy": "2023-10-18T10:08:30.340917Z",
     "iopub.status.idle": "2023-10-18T10:08:30.500371Z",
     "shell.execute_reply": "2023-10-18T10:08:30.498916Z"
    },
    "papermill": {
     "duration": 0.192559,
     "end_time": "2023-10-18T10:08:30.503234",
     "exception": false,
     "start_time": "2023-10-18T10:08:30.310675",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>lama_pengiriman_hari</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>111043.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>9.012995</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>8.621737</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>4.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>7.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>12.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>205.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       lama_pengiriman_hari\n",
       "count         111043.000000\n",
       "mean               9.012995\n",
       "std                8.621737\n",
       "min                1.000000\n",
       "25%                4.000000\n",
       "50%                7.000000\n",
       "75%               12.000000\n",
       "max              205.000000"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# menggabungkan customer dengan seller\n",
    "cust = orders[[\"customer_city\",\"customer_state\",\"lama_pengiriman_hari\",\"order_id\",\"customer_id\"]]\n",
    "seller = df_order_items[[\"order_id\",\"seller_id\",\"seller_city\",\"seller_state\"]]\n",
    "cust_seller = cust.merge(seller, left_on='order_id', right_on='order_id',how='left')\n",
    "cust_seller.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "f598c1da",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:30.570624Z",
     "iopub.status.busy": "2023-10-18T10:08:30.570286Z",
     "iopub.status.idle": "2023-10-18T10:08:30.770184Z",
     "shell.execute_reply": "2023-10-18T10:08:30.768774Z"
    },
    "papermill": {
     "duration": 0.23417,
     "end_time": "2023-10-18T10:08:30.772609",
     "exception": false,
     "start_time": "2023-10-18T10:08:30.538439",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Jumlah duplikasi:  0\n"
     ]
    }
   ],
   "source": [
    "# duplicate data\n",
    "cust_seller = cust_seller.drop_duplicates()\n",
    "print(\"Jumlah duplikasi: \", cust_seller.duplicated().sum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "c6b428da",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:30.832639Z",
     "iopub.status.busy": "2023-10-18T10:08:30.832292Z",
     "iopub.status.idle": "2023-10-18T10:08:30.861110Z",
     "shell.execute_reply": "2023-10-18T10:08:30.860077Z"
    },
    "papermill": {
     "duration": 0.061335,
     "end_time": "2023-10-18T10:08:30.863217",
     "exception": false,
     "start_time": "2023-10-18T10:08:30.801882",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>seller_state</th>\n",
       "      <th>customer_state</th>\n",
       "      <th>lama_pengiriman_hari</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>CE</td>\n",
       "      <td>AM</td>\n",
       "      <td>138.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>AM</td>\n",
       "      <td>AL</td>\n",
       "      <td>87.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>BA</td>\n",
       "      <td>AC</td>\n",
       "      <td>63.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>GO</td>\n",
       "      <td>AM</td>\n",
       "      <td>29.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>RO</td>\n",
       "      <td>SE</td>\n",
       "      <td>28.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>407</th>\n",
       "      <td>GO</td>\n",
       "      <td>GO</td>\n",
       "      <td>2.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>408</th>\n",
       "      <td>RJ</td>\n",
       "      <td>RJ</td>\n",
       "      <td>2.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>409</th>\n",
       "      <td>RN</td>\n",
       "      <td>RN</td>\n",
       "      <td>2.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>410</th>\n",
       "      <td>PI</td>\n",
       "      <td>PI</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>411</th>\n",
       "      <td>DF</td>\n",
       "      <td>DF</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>412 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "    seller_state customer_state  lama_pengiriman_hari\n",
       "0             CE             AM                 138.0\n",
       "1             AM             AL                  87.0\n",
       "2             BA             AC                  63.0\n",
       "3             GO             AM                  29.5\n",
       "4             RO             SE                  28.0\n",
       "..           ...            ...                   ...\n",
       "407           GO             GO                   2.5\n",
       "408           RJ             RJ                   2.0\n",
       "409           RN             RN                   2.0\n",
       "410           PI             PI                   1.0\n",
       "411           DF             DF                   1.0\n",
       "\n",
       "[412 rows x 3 columns]"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# lama pengiriman antar state\n",
    "cust_seller.groupby(['seller_state', 'customer_state'])['lama_pengiriman_hari'].median().sort_values(ascending=False).reset_index()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "595e90c9",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:30.922481Z",
     "iopub.status.busy": "2023-10-18T10:08:30.922126Z",
     "iopub.status.idle": "2023-10-18T10:08:30.971749Z",
     "shell.execute_reply": "2023-10-18T10:08:30.970575Z"
    },
    "papermill": {
     "duration": 0.082383,
     "end_time": "2023-10-18T10:08:30.974176",
     "exception": false,
     "start_time": "2023-10-18T10:08:30.891793",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>seller_city</th>\n",
       "      <th>customer_city</th>\n",
       "      <th>lama_pengiriman_hari</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>belo horizonte</td>\n",
       "      <td>montanha</td>\n",
       "      <td>195.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>uberaba</td>\n",
       "      <td>lagarto</td>\n",
       "      <td>194.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>aracatuba</td>\n",
       "      <td>aracaju</td>\n",
       "      <td>187.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>farroupilha</td>\n",
       "      <td>paulinia</td>\n",
       "      <td>186.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>itajobi</td>\n",
       "      <td>perdizes</td>\n",
       "      <td>182.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>35429</th>\n",
       "      <td>mogi das cruzes</td>\n",
       "      <td>maua</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>35430</th>\n",
       "      <td>mogi das cruzes</td>\n",
       "      <td>mogi das cruzes</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>35431</th>\n",
       "      <td>mogi das cruzes</td>\n",
       "      <td>monte mor</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>35432</th>\n",
       "      <td>jacarei</td>\n",
       "      <td>holambra</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>35433</th>\n",
       "      <td>penapolis</td>\n",
       "      <td>lupercio</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>35434 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "           seller_city    customer_city  lama_pengiriman_hari\n",
       "0       belo horizonte         montanha                 195.0\n",
       "1              uberaba          lagarto                 194.0\n",
       "2            aracatuba          aracaju                 187.0\n",
       "3          farroupilha         paulinia                 186.0\n",
       "4              itajobi         perdizes                 182.0\n",
       "...                ...              ...                   ...\n",
       "35429  mogi das cruzes             maua                   1.0\n",
       "35430  mogi das cruzes  mogi das cruzes                   1.0\n",
       "35431  mogi das cruzes        monte mor                   1.0\n",
       "35432          jacarei         holambra                   1.0\n",
       "35433        penapolis         lupercio                   1.0\n",
       "\n",
       "[35434 rows x 3 columns]"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# lama pengiriman antar city\n",
    "cust_seller.groupby(['seller_city', 'customer_city'])['lama_pengiriman_hari'].median().sort_values(ascending=False).reset_index()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1e6869de",
   "metadata": {
    "papermill": {
     "duration": 0.030308,
     "end_time": "2023-10-18T10:08:31.033966",
     "exception": false,
     "start_time": "2023-10-18T10:08:31.003658",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# Visualization & Explanatory Analysis"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d7cfc0c3",
   "metadata": {
    "papermill": {
     "duration": 0.033845,
     "end_time": "2023-10-18T10:08:31.097297",
     "exception": false,
     "start_time": "2023-10-18T10:08:31.063452",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## Pertanyaan 1: Category barang yang paling banyak dibeli dan paling sedikit diminati? \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "5b8ee3bf",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:31.165889Z",
     "iopub.status.busy": "2023-10-18T10:08:31.164605Z",
     "iopub.status.idle": "2023-10-18T10:08:31.194801Z",
     "shell.execute_reply": "2023-10-18T10:08:31.193840Z"
    },
    "papermill": {
     "duration": 0.065223,
     "end_time": "2023-10-18T10:08:31.197702",
     "exception": false,
     "start_time": "2023-10-18T10:08:31.132479",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "df_category = df_order_items.groupby(by=\"product_category_name_english\")[\"product_id\"].count().reset_index() #jumlah pembelian\n",
    "df_category = df_category.rename(columns={\"product_category_name_english\": \"category\", \"product_id\": \"orders\"})\n",
    "# df_category"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "92701d51",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:31.266763Z",
     "iopub.status.busy": "2023-10-18T10:08:31.266083Z",
     "iopub.status.idle": "2023-10-18T10:08:31.849038Z",
     "shell.execute_reply": "2023-10-18T10:08:31.847681Z"
    },
    "papermill": {
     "duration": 0.616651,
     "end_time": "2023-10-18T10:08:31.851711",
     "exception": false,
     "start_time": "2023-10-18T10:08:31.235060",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "image/png": "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VCVLllTatGllsVjiNQzPhQsXNGHCBLVs2VL58uVT6tSp5eLiomzZsqlJkyaaN29ejPtl06ZNZjybNm1SRESEpk+frurVqytz5sxycHCwOi6f34+2LFmyRE2bNlX27Nnl4uIiT09P5c6dW1WqVNHgwYO1e/fuOK+fLf/884969+6t3Llzy9XVVT4+PmrcuLHWrVsXp/r37t3TvHnzFBQUpBIlSsjLy0tOTk7y9vZWtWrVNHLkSN29ezfGNp4/X0JDQ9WuXTtznbNly6ZOnTrpjz/+SPB6XrlyRffv35f07EFjYnjy5ImmTZum+vXry8fHRy4uLsqYMaOqVq2q0aNH6+HDh7G2cfToUXXp0kU5cuSQq6urcuTIofbt2ys0NDROMcTlWhOTs2fPqmDBgrJYLPLw8NDatWvNec8fz5FmzJghi8WioUOHRosj6k9YWFiCYopNhQoVzP+fPn062vz79+9r9OjR5nnn7OysTJkyqXbt2goJCdHTp0/tth15b4k8T/ft26cOHTooR44ccnNzU968efX+++/r6tWrVvV+++03tWrVSjlz5pSrq6vy5MmjAQMG6M6dO3aXFdv5n1jnxcmTJ/XNN9+oUaNG8vX1lZubm9zc3JQrVy61adNGa9assVkvLCxMFovFKum3evXq0fbziw51du7cOb3//vvKnz+/3N3d5e3trfr168c5ASAx9/fevXsVGBgoPz8/ubi4WP2dEWnHjh1q2bKlsmTJIldXV/n5+albt246duxYnOJ90fuMJD18+FBjx45VQECAMmbMKCcnJ6VPn14FCxZU/fr19e2339o8/yIiIrRhwwb169dP/v7+Zt20adOqRIkS6tevn86cORPjsgMCAmSxWBQQECBJOn78uPr06aN8+fLJ3d093uf+zZs35e/vL4vFIicnJ82aNeulxht5vOXNm1dubm7KkCGD6tSpk6QJJ9u2bVOnTp3k6+srV1dXpU2bViVLltTHH3+sK1eu2KxjsVishhfr2rVrtHPz+ftCQq8FSSG26/yL3H+fPyb+/vtv9ejRQ7lz55abm5t8fX315ptvRlvu4cOH1bVrV/PvpRw5cqhnz566fPlynNcrKa93sYnt74kXPX4i/3aIvEZERERo8uTJqlSpktKlS6fUqVOrWLFi+vzzz82/1wAAAAC8BAYAAADwnIiICMPb29uQZKROndq4devWC7eZK1cuQ1KMPyVLljQuXLiQoLpdunSJVm/q1KmGm5tbjPXefPNNIzw83GbMjx49Mho2bGi3br58+YywsDDz9yFDhthsJywszHjttddijKNy5crGtWvXbNbv0qWLIcnIlSuXsWPHDiNjxozR6m/cuNE4cuSI+fuXX34Z4/44cOBAnMvGxalTp2LcF4ZhGHfv3jWaNWsW43bw8PAwVqxYYbP+kCFDzHJ//fWX4evrG61+SEiIWT7yuLEVz5MnTwwHB4dYj6tatWoZd+7csRnPxo0bzXKrV682atasGeNxGXU/2oqnVatWscZTunRpe7sgVps2bTLSpEljt+2hQ4dabWNbqlWrFmuMfn5+xh9//GE3jqjny3fffWc4OjrabMfd3d3YvHlzgtb12rVrZjvFixdPUBtR/f3330ahQoViXO98+fIZf/31l9025s6dazg7O9us6+joaEybNi3GY8QwrLfd80JCQsz5p06dijb/zz//NHLkyGFIMtKlS2fs2LHDan7U43njxo02243px9YyYxK5rrHVnThxollu+PDhVvN2795tZMuWLca4ypUrZ1y8eNFm21GvET/88IPd/ZM/f37z3vT1118bFovFZrlSpUrZvV7EZ98m9Lw4efJknPZVx44do933ol7DY/qJeo2Ni6jrHRoaamTKlMlu2++++26MbSXm/p44caLNbRzVyJEj7d4nUqdObaxatcq8JlarVi3a8hLjPnP+/PlYrz2SjL59+0arG/V6bu/H3d3dWLx4sd1tHnX9li5daqROndruuW/vGhLpwoULRrFixQxJhqurq7Fs2bKXGu/WrVuNDBky2G3r66+/tttOQsR2TXv69KnRu3fvGNfPy8vL+PXXX6PVjcu5GfW+8CLXgkix7c+4iLpPY2pj9erVZrkePXpYzXvR+2/UY2Lt2rWGp6enzTYyZcpk/u0yZ84cw8XFxWa5XLlyGefOnbO5rOR0vYvp2mQYMf89kRjHT9S/HQ4fPmzUqFEjxvW4e/dujNsDAAAAQMI4CgAAAHjO0aNHzbeTq1SpojRp0rxwm0+fPlX58uXVsGFDlSxZUpkzZ9bjx4916tQpzZ49W2vWrNHvv/+utm3bWvVKIUm//vqrHj9+rKJFi0qSevbsaTWkgCSlS5fO6vfp06crKChIklSkSBF1795dJUuWlLu7u06dOqVp06Zp1apVmjZtmry8vPTNN99Ei/ntt982hxoqVKiQ+vXrp6JFi+r27dtasmSJJk6cqLZt28a43nfv3lWNGjV08uRJSVLTpk31xhtvyMfHR6dOndK4ceO0efNmbdu2TQ0bNtTWrVuVKlUqu221aNFCDx8+1EcffaRatWrJ3d1dhw4dUtasWVWgQAFVrFhRO3bsUEhIiAYOHGg3rpCQEElSqlSp1KVLlxjXITE8ffpUjRo10saNG2WxWNS2bVs1b95cfn5+Cg8P1+7du/XNN9/ozJkzatGihX777TeVLl3abnstW7bUuXPn9Pbbb6tx48ZKly6djh8/rly5csUpHsMwJEk1atRQvXr1VLRoUXl7e+vOnTs6efKkpkyZoh07dmjt2rXq3bu3Zs6cGWN7AwYM0MGDB9W4cWMFBgYqV65cunTpktl7VGwmTpyoBQsWSJIqV66soKAg5cmTRx4eHrp+/boOHz6s1atX6/r163Fq73lhYWFq1KiR7ty5IwcHB3Xr1k0tW7aUl5eXDh48qOHDh2vIkCEqU6ZMjO08efJERYsWVePGjVWmTBn5+PjIMAydPn1aS5Ys0fz583Xq1Ck1bdpU+/fvl6urq922fvnlF+3atUvFihXTu+++q6JFi+rBgwdasmSJxowZo/v376tTp046fvy4nJ2d47W+6dOnV65cuXT69GkdOHBAX331lT744AM5OMS/c9wLFy7I399fly5dkqenp7p166aaNWsqc+bMunXrln799VeNGTNGx48fV926dbVv3z55eXlZtbFr1y516tRJT548kYuLi/73v/+pfv36cnFx0a5du/TFF1+oR48ece6BLb727t2runXr6urVq8qaNat+/fVXFSlSJE51mzZtqjJlymjChAmaOHGiJOnQoUPRymXLli1RY4508OBB8/8+Pj7m/w8dOqTq1avr3r17ypQpk3r27KkqVaooQ4YMunz5spYvX65JkyZp9+7datKkibZu3SonJyebyzhw4IDmzp2rvHnzmtf5O3fuaPr06Zo9e7b++usv9evXTy1atNAHH3ygChUq6O2331aBAgV09epVjR07VqtWrdK+ffv02Wefafjw4Qle3xc5L54+fSpnZ2fVqVNHtWrVUqFChZQ+fXpdv35df/31l8aPH68jR45o9uzZyp07t1VvT9myZdOhQ4cUGhqqN954Q9Kz+2jZsmWt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evRoQ5JRpUoVqzrh4eHGokWLrL4bMYxn506ZMmUMSdHW094+AAAAiA3DhAEAgGTj2rVrkhLWxXbRokVVrFixaNPr1KmjVq1a6cSJEzp8+HCc27t8+bKmTp0qPz8/TZkyxepNN29vb02aNEmSzH8lacGCBbp+/bq5zEipUqXSyJEj5enpGW05mzZt0qFDh+Tn56dPP/3U6k3Cli1bqmnTprpz545CQkJsxjl27FilTZs22vTu3btLkqZOnWo1/dq1a1q6dKkyZ86sRo0axWFLxM306dN18eJF9evXTy1btrSaV7NmTfXq1Uvnzp3TypUro9X19vbWV199pVSpUsV5eTVq1LB6U1KSHBwc9MknnyhbtmxatmyZ3br2tpktly9fliRVqlRJrq6uVvPc3NxUsWLFOMcMAAAAAAnBZ+Xk+Vl5wIABev/99+Xo6Kg///xTX331lZo2barMmTOrbNmymjt3brQ6w4cPV0REhCZPnmy1XywWiz7++GOVLFlSixcv1tWrVyU967Vn1qxZcnR01NixY616zKlXr57NnpHi6ty5c6pSpYp27dql4cOH66uvvkpwWy/CMAydPn1aAwcO1E8//SSLxWLupzFjxuj+/fsaMWKEqlatalWvc+fOatq0qUJDQ7Vv375o7VatWtUcFlySnJyc9M4770h61kPxlClTrHoKDgwMVMaMGbVjxw6Fh4fHOf7cuXPrm2++seq1q3fv3kqXLp127txpDrkmSY6OjmrevLmcnZ2t2vD29taXX34pSTF+nwEAABAfJAMBAIBkwzCMF6r/6NEjLVu2TB999JG6deumwMBABQYG6tChQ5Kk48ePx7mtzZs3Kzw8XHXr1rX6si1S8eLF5enpqdDQUHPab7/9Jkk2v4xLkyaNVdfQkbZu3SpJatOmjc1kmE6dOlmViypr1qwqU6aMzfhbt26t9OnTa/bs2Xrw4IE5/YcfftCjR48UGBgY61Bc8bF27VpJUtOmTW3Or1y5siRZba9INWvWlLu7e7yXee3aNYWEhKhv37568803zf0dHh6u69ev6/r169HqxLTNbClYsKBSp06tkJAQTZkyxfwSHgAAAABeFT4rJ8/PyqlSpdI333yjkydP6ptvvlGTJk2UNWtWGYahPXv2qH379nr33XfN8hEREVq/fr08PT31+uuvR2vPYrHI399fERER2rt3ryRp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6623zGlNmjSR9GxoqHfffVcNGzbUkiVLzPn169dXqVKlNGjQIO3atUuS9P7778vR0VG7d++Wt7e3Wdbec+C4uHz5so4ePar8+fPbLZMmTRoVKVJE0rNOLZ5/pt29e3d9+eWXGjVqlDJlyiRJWrx4sc6fP68+ffrEOZYCBQqYnXRI0tOnT1WnTh2FhYVp7Nix0ZKBPD09tXLlSrOTDh8fH5UrV06rV69W27ZtEzUf4c8//9S1a9c0bdo0c99JUuvWrc3/79y5U1OmTNE333yj999/35xepUoV5c+fX6NGjdJXX31lTr9+/boWLFigGjVqmNOePHmizJkzKyQkxCoZKCQkRM7Ozmrfvr3dGEePHq0jR45o7dq1VnWj5gDENTdg7969evjwob7++msVL17cLBfT8pMThgl7Ac9fUFq3bi1HR0dt3LhRv/zyi548eaLOnTvryZMn5o+rq6uqVaumTZs2SZKOHTum8+fPq3379lZdleXKlUuVKlVKUFyenp7REmTat2+viIgIbdmyxZwWmUnn5eWlVKlSycnJSZ988omuXbumy5cvx3l5zy+rWLFikqTTp08nKP7nXb58WT169FCOHDnk6OgoJycn5cqVS5L0xx9/RCsf036xZ+XKlUqbNq0aNWpktb9KlCihLFmymPvLlg8//FC3bt0yf86ePZuwFQUAAAAAAAAAAACAf4mzZ89aPSf98MMP7ZYtV66cZsyYoc8++0w7d+5UeHi4Oe+3337T9evX1aVLF6tntREREapbt65CQ0N179493b9/X5s3b1br1q2tEoFeVLFixWJMBIqLyI4lpkyZYk4bN26cihYtqqpVq8arre+//16lSpWSq6ur+Xx8/fr1Np+NN2jQwGq0nuef1SdmPkLevHmVLl06DRgwQN9//72OHj0arczKlStlsVjUsWNHq32ZJUsWFS9ePNpz93Tp0lklAkmSo6OjOnbsqMWLF+vWrVuSniVFzZo1S02aNFGGDBnsxrh69Wrlz5/fKhHIVoxxyQ0oUaKEnJ2d1a1bN82cOTPaMGfJHclALyBLlixWvzs6OipDhgy6du2aLl26JEkqW7asnJycrH7mzZunq1evSpLZ7dnzbdmbFhdRu9V6vq3I5e3evVu1a9eW9OyCtH37doWGhuqjjz6SJD148CDOy3v+ZIvsei0+bdgTERGh2rVra/Hixerf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jx+3as/d3V2urq5W01xcXPTw4cMY47h27ZqyZs0abbqPj485P6rEeK5+5coVZc+ePU5lE+s5/rVr1+w+x7fF1ja5dOmSDh48GO0Zv6enpwzDMJ/x24s9Mv6osc+b9//au/e4r+f7f+CPq/M5HVQqKS2HFEYkOZSEFDYzpxGZwxCamcghNRZtzpPahszZNiw259KYTJbzcUzkEIlOUlSf3x9+XV9XxyvSVR/3++123bbP+/N6v9/P9+f9uj6uz+f16PW6LUcccUT++Mc/pkuXLmnYsGH69u2bqVOnlvvaVuX1XOyTTz5JoVBYpXu/POW5zvK+drvsskvuuuuuLFiwIH379k3Lli3ToUOH3HLLLat0fYllwipc48aNU1JSkkcffXSZb46Lt73wwgt59tlnM3r06BxxxBGlz7/++utrrNbyWtYv5tSpU0t/CRav73jmmWdm//33X+YxNt100yTJjTfemG7duuXqq68u8/zs2bPLPF78xj5//vwy25d8w1mZ+vXrl77ZnHbaabnuuuty6KGHZr311lul4wAAAAAAAACwtJkzZ+aee+7J4MGDS5eLSr4c6/3444/LtK1du3aGDBmSIUOG5IMPPiidJWifffbJK6+88o1radSoUd5///2ltr/33ntJ/m9se3Vaf/31884776z2465Io0aNljuOvyzLWjWncePGqVmzZq699tpl7vN1XqvGjRvnsssuy2WXXZa33347Y8aMyRlnnJEPP/ww9913X7mO8XVezwYNGqRSpUpr7N6vymu33377Zb/99sv8+fPzxBNPZNiwYTn00EPTunXrdOnSpdznNDNQBevTp08KhULefffddOrUaamfjh07Jvm/X7YlA0OjRo0q13mWTJ59m2655ZYUCoXSx2+99VYef/zxdOvWLcmXQZ927drl2WefXeY1d+rUqXS6sJKSkqWu+bnnnltqOrbWrVuXPvdVY8aMWaq+laUlTz755Hz00Uc54IADMmPGjPTv37/8Fw8AAAAAAADAcpWUlKRQKCw1DvzHP/4xCxcuXO5+TZs2zZFHHplDDjkkr776aubOnfuNa+nRo0fGjh1bGgBZ7E9/+lNq1aqVHXbY4RufY0m9evXKuHHjyr0M1erQvXv3vPjii3n22WfLbL/55pvLfYw+ffrkjTfeSKNGjZY5xr94zP7ratWqVfr375+ePXtm0qRJ5d7v67yetWvXTufOnXPHHXeUyQ0sWrQoN954Y1q2bJlNNtkkyTdbVWmxr/PaVa9ePbvuumsuuuiiJMnTTz+9Suc0M1AF69q1a4499tj069cvTz31VHbZZZfUrl0777//fh577LF07Ngxxx9/fDbbbLO0bds2Z5xxRgqFQho2bJi77747Dz74YLnO07Fjx9xxxx25+uqrs+2226ZSpUrp1KnTt3JNH374YX74wx/mmGOOycyZMzN48ODUqFGjzBqRo0aNSq9evbLnnnvmyCOPTIsWLfLxxx/n5ZdfzqRJk/LnP/85yZe/FL/61a8yePDg7Lrrrnn11VczdOjQtGnTJgsWLCg9XrNmzbL77rtn2LBhadCgQTbaaKM8/PDDueOOO5b5WiTJRRddlF69eqVy5crZcsstU61atSTJJptskr322iv33ntvdtppp6XWTQQAAAAAAADg66lXr1522WWX/OY3v0njxo3TunXrjB8/Ptdcc81SK7Z07tw5ffr0yZZbbpkGDRrk5Zdfzg033JAuXbqkVq1a37iWwYMH55577kn37t1z7rnnpmHDhrnpppvy97//PcOHD0/9+vW/8TmWNHTo0Nx7773ZZZddMmjQoHTs2DEzZszIfffdl1NPPTWbbbbZaj/ngAEDcu2116Z37945//zz07Rp09x0002rNLvSgAED8te//jW77LJLfv7zn2fLLbfMokWL8vbbb+eBBx7IL37xi3Tu3Lncx5s5c2a6d++eQw89NJtttlnq1q2biRMn5r777lvuCkPL8nVfz2HDhqVnz57p3r17TjvttFSrVi0jRozICy+8kFtuuaV0wpYOHTokSX7/+9+nbt26qVGjRtq0abPM5cGWp7yv3bnnnpt33nknPXr0SMuWLTNjxoxcfvnlqVq1anbddddyny8RBlorjBo1KjvssENGjRqVESNGZNGiRWnevHm6du2a7bffPklStWrV3H333TnllFNy3HHHpUqVKtl9993z0EMPpVWrVis9xymnnJIXX3wxgwYNysyZM1MoFMrM3rM6/frXv87EiRPTr1+/zJo1K9tvv31uvfXWtG3btrRN9+7d8+STT+aCCy7IgAED8sknn6RRo0Zp3759DjzwwNJ2Z511VubOnZtrrrkmw4cPT/v27TNy5MjceeedeeSRR8qc94YbbshJJ52UgQMHZuHChdlnn31yyy23LBV6OvTQQ/Ovf/0rI0aMyNChQ1MoFPLmm2+WSdsddNBBuffee80KBAAAAAAAALCa3XzzzTnllFNy+umnZ8GCBenatWsefPDB9O7du0y73XbbLWPGjMmll16auXPnpkWLFunbt2/OOuus1VLHpptumscffzyDBg3KiSeemM8++yybb755rrvuuhx55JGr5RxLatGiRZ588skMHjw4F154YaZPn571118/O+20Uxo2bPitnLNZs2YZP358TjnllBx//PGpVatWfvjDH+Z3v/td9ttvv3Ido3bt2nn00Udz4YUX5ve//33efPPN1KxZM61atcruu+++yjMD1ahRI507d84NN9yQyZMn54svvkirVq0ycODAnH766eU+ztd9PXfdddeMHTs2gwcPzpFHHplFixZlq622ypgxY9KnT5/Sdm3atMlll12Wyy+/PN26dcvChQtXuX+U97Xr3LlznnrqqQwcODDTpk3Leuutl06dOmXs2LHZYostyn2+JCkpfFuJEFiH/ehHP8oTTzyRyZMnp2rVqqu076xZs1K/fv1MmDAhderU+ZYqBACAirX4X8TA17H4c9PMmTNTr169ii4HlqKPAny3vfDCCxVdAgCs1ebMmZMuXbr4zARrMTMDwf83f/78TJo0KU8++WTuvPPOXHLJJascBAIAAAAAAAAAqEjCQKxUoVDIwoULV9imcuXKpWvmravef//97LjjjqlXr16OO+64nHTSSRVdEgAAAAAAAADrgO/KuPqa4vX8ZipVdAGs/caPH5+qVauu8Of666+v6DK/sdatW6dQKGTmzJm5+uqrU7ly5YouCQAAAAAAAIB1wPXXX7/ScfXx48dXdJnrDK/nN2NmIFZq2223zcSJE1fYpk2bNmuoGgAAAAAAAABYu+yzzz4rHVffdNNN11A16z6v5zcjDMRK1a1bN506daroMgAAAAAAAABgrdSoUaM0atSoossoGl7Pb8YyYQAAAAAAAAAAUCSEgQAAAAAAAAAAoEgIAwEAAAAAAAAAQJEQBgIAAAAAAAAAgCIhDAQAAAAAAAAAAEVCGAgAAAAAAAAAAIqEMBAAAAAAAAAAABQJYSAAAAAAAAAAACgSwkAAAAAAAAAAAFAkhIEAAAAAAAAAAKBICAMBAAAAAAAAAECREAYCAAAAAAAAAIAiIQwEAAAAAAAAAABFQhgIAAAAAAAAAACKhDAQAAAAAAAAAAAUCWEgAAAAAAAAAAAoEsJAAAAAAAAAAABQJISBAAAAAAAAAACgSAgDAQAAAAAAAABAkRAGAgAAAAAAAACAIiEMBAAAAAAAAAAARUIYCAAAAAAAAAAAioQwEAAAAAAAAAAAFAlhIAAAAAAAAAAAKBJVKroAKFbt27dPvXr1KroMAAAAAABWQYcOHSq6BABYq82aNauiSwBWwsxAAAAAAAAAAABQJISBAAAAAAAAAACgSAgDAQAAAAAAAABAkRAGAgAAAAAAAACAIiEMBAAAAAAAAAAARUIYCAAAAAAAAAAAioQwEAAAAAAAAAAAFAlhIAAAAAAAAAAAKBLCQAAAAAAAAAAAUCSEgQAAAAAAAAAAoEgIAwEAAAAAAAAAQJEQBgIAAAAAAAAAgCIhDAQAAAAAAAAAAEVCGAgAAAAAAAAAAIqEMBAAAAAAAAAAABQJYSAAAAAAAAAAACgSwkAAAAAAAAAAAFAkqlR0AVCsXnrppdSpU6eiywAAYBV06NChoksAAIC12gsvvFDRJQAAFWzOnDkVXQKwEmYGAgAAAAAAAACAIiEMBAAAAAAAAAAARUIYCAAAAAAAAAAAioQwEAAAAAAAAAAAFAlhIAAAAAAAAAAAKBLCQAAAAAAAAAAAUCSEgQAAAAAAAAAAoEgIAwEAAAAAAAAAQJEQBgIAAAAAAAAAgCIhDAQAAAAAAAAAAEVCGAgAAAAAAAAAAIqEMBAAAAAAAAAAABQJYSAAAAAAAAAAACgSwkAAAAAAAAAAAFAkhIEAAAAAAAAAAKBICAMBAAAAAAAAAECREAYCAAAAAAAAAIAiIQwEAAAAAAAAAABFQhgIAAAAAAAAAACKhDAQAAAAAAAAAAAUCWEgAAAAAAAAAAAoEsJAAAAAAAAAAABQJISBAAAAAAAAAACgSAgDAQAAAAAAAABAkRAGAgAAAAAAAACAIiEMBAAAAAAAAAAARUIYCAAAAAAAAAAAioQwEAAAAAAAAAAAFAlhIAAAAAAAAAAAKBLCQAAAAAAAAAAAUCSEgQAAAAAAAAAAoEgIA31HzZ07N+edd14eeeSRb+X4jzzySEpKSr7W8b/JvgAAAAAAAACsPUaPHp2SkpLSnypVqqRly5bp169f3n333aXa/+9//0v//v2zySabpGbNmqlVq1a22GKLnH322ctsvyzPPfdcfvrTn6Zt27apWbNmatasmXbt2uW4447LU089tbovsdxKSkpy3nnnVdj5+e6oUtEFUDHmzp2bIUOGJEm6detWscUsYZtttsmECRPSvn37ii4FAAAAAAAAgNXguuuuy2abbZbPPvss//znPzNs2LCMHz8+zz//fGrXrp0kueeee3LwwQencePG6d+/f77//e+npKQkzz//fK699tr8/e9/z9NPP73C84waNSr9+/fPpptumlNOOSVbbLFFSkpK8vLLL+eWW27Jdtttl9dffz1t27ZdE5ddxoQJE9KyZcs1fl6+e4SBvmMKhULmzZtX0WWsUL169bLDDjus0XN+9tlnqVGjRkpKStboeQEAAAAAAAC+Czp06JBOnTolSbp3756FCxfmV7/6Ve6666785Cc/yZtvvpmDDz44m2yyScaNG5f69euX7rvbbrvl5JNPzp133rnCc/zrX//KCSeckN69e+cvf/lLqlWrVuYYJ554Yv785z+nZs2a385FrsSaHgfnu8syYWvQtGnTcuyxx2bDDTdM9erVs/7666dr16556KGHknw5Q0+HDh3y6KOPZocddkjNmjXTokWLnHPOOVm4cGGZY3388cc54YQT0qJFi1SrVi0bb7xxzjrrrMyfP79Mu5KSkvTv3z8jR47M5ptvnurVq+f666/P+uuvnyQZMmRI6XRsRx55ZLnq/Caeeuqp7LvvvmnYsGFq1KiR73//+7n99tvLtFnWMmH/+9//cvDBB6d58+apXr16mjZtmh49euSZZ54pc63LmlKtdevWpdeW/N80dA888ECOOuqorL/++qlVq1bpa3fbbbelS5cuqV27durUqZM999xzpelSAAAAAAAAAMpvcTDmrbfeSpJccskl+fTTTzNixIgyQaDFSkpKsv/++6/wmL/+9a9TuXLljBo1qkwQ6Kt+/OMfp3nz5qWPn3rqqRx88MFp3bp1atasmdatW+eQQw4prWuxxePMY8eOzTHHHJNGjRqlXr166du3bz799NNMnTo1Bx54YNZbb71ssMEGOe200/LFF18sdQ1fHdNefMxx48bl+OOPT+PGjdOoUaPsv//+ee+998rsO3/+/PziF79Is2bNUqtWreyyyy75z3/+s9R4OCRmBlqjDj/88EyaNCkXXHBBNtlkk8yYMSOTJk3K9OnTS9tMnTo1Bx98cM4444wMHTo0f//733P++efnk08+ye9+97skybx589K9e/e88cYbGTJkSLbccss8+uijGTZsWJ555pn8/e9/L3Peu+66K48++mjOPffcNGvWLA0bNsx9992XvfbaKz/96U9z9NFHJ0lpQKg8dX4d48aNy1577ZXOnTtn5MiRqV+/fm699dYcdNBBmTt37grfoPbee+8sXLgww4cPT6tWrfLRRx/l8ccfz4wZM752PUcddVR69+6dG264IZ9++mmqVq2aX//61zn77LPTr1+/nH322fn888/zm9/8JjvvvHOefPLJZS5dNn/+/DIhrFmzZn3tmgAAAAAAAADWBUuOi1avXj3Vq1cv9/6vv/56kv8bp37ggQfStGnTrz17zsKFCzNu3Lh06tQpG2ywQbn3mzx5cjbddNMcfPDBadiwYd5///1cffXV2W677fLSSy+lcePGZdofffTR2X///XPrrbfm6aefzqBBg7JgwYK8+uqr2X///XPsscfmoYceykUXXZTmzZvn1FNPXWkNRx99dHr37p2bb745U6ZMyS9/+cscdthhGTt2bGmbfv365bbbbsvpp5+e3XbbLS+99FJ++MMfGp9mmYSB1qB//etfOfroo3PMMceUbttvv/3KtJk+fXr+9re/Zd99902S7LHHHvnss89y9dVX5/TTT0+rVq1y/fXX57nnnsvtt9+eH//4x0mSnj17pk6dOhk4cGAefPDB9OzZs/SYc+bMyfPPP58GDRqUbmvRokWSpGXLlku9mZanzq/jhBNOyBZbbJGxY8emSpUvu96ee+6Zjz76KIMGDUrfvn1TqdLSk1VNnz49r776ai677LIcdthhpdtXlvpcmR49emTUqFGlj6dMmZLBgwenf//+ueKKK0q39+zZM+3atcuQIUNy2223LXWcYcOGZciQId+oFgAAAAAAAIB1yYYbbljm8eDBg5e5kstiCxcuzIIFCzJv3ryMHz8+559/furWrVs6Nv72229n6623/tr1fPTRR/nss8+y0UYbLfPchUKh9HHlypVTUlKSJDnggANywAEHlGnbp0+fNG3aNDfffHNOPvnkMsfq06dPfvvb3yb5cix5woQJueWWW3LJJZfk5z//eZJk9913z/3335+bbrqpXGGgvfbaq8wY9ccff5zTTz89U6dOTbNmzfLSSy/llltuycCBAzNs2LDSczdt2jSHHHJIeV8ivkMsE7YGbb/99hk9enTOP//8PPHEE0tNCZakzJvdYoceemgWLVqUf/7zn0mSsWPHpnbt2mXekJKUzqzz8MMPl9m+2267lQkCrY46V9Xrr7+eV155JT/5yU+SJAsWLCj92XvvvfP+++/n1VdfXea+DRs2TNu2bfOb3/wml1xySZ5++uksWrToG9f0ox/9qMzj+++/PwsWLEjfvn3L1FejRo3suuuuZZYt+6ozzzwzM2fOLP2ZMmXKN64NAAAAAAAAYG02ZcqUMuOkZ5555grb77DDDqlatWrq1q2bPn36pFmzZrn33nvTtGnTb73WbbfdNlWrVi39ufjii0ufmzNnTgYOHJjvfe97qVKlSqpUqZI6derk008/zcsvv7zUsfr06VPm8eabb54k6d2791Lbl1xqbHmWzAhsueWWSf5vCbXx48cnSQ488MAy7Q444IDSiTjgq4SB1qDbbrstRxxxRP74xz+mS5cuadiwYfr27ZupU6eWtlnWG12zZs2SpHSZrunTp6dZs2alScXFmjRpkipVqiy1nNeqTIFW3jpX1QcffJAkOe2008q8yVatWjUnnHBCki+TmstSUlKShx9+OHvuuWeGDx+ebbbZJuuvv35OPvnkzJ49+2vXtOTrsrjG7bbbbqkab7vttuXWV7169dSrV6/MDwAAAAAAAEAxW3KMdGVLhP3pT3/KxIkT8/TTT+e9997Lc889l65du5Y+36pVq7z55ptfu57GjRunZs2aywzg3HzzzZk4cWLGjBmz1HOHHnpofve73+Xoo4/O/fffnyeffDITJ07M+uuvn88++2yp9g0bNizzuFq1asvdPm/evHLV3qhRozKPF7+Wi8+/OAOwZJ6gSpUqS+0LiWXC1qjGjRvnsssuy2WXXZa33347Y8aMyRlnnJEPP/ww9913X5L/C6R81eIQzuJf4kaNGuXf//53CoVCmUDQhx9+mAULFiy1ZuGSoaHVUeeqWlzTmWeeudzlvTbddNPl7r/RRhvlmmuuSZK89tpruf3223Peeefl888/z8iRI5N8+YY4f/78pfZdMhy12JKvy+Ia//KXvyxz6jgAAAAAAAAAvp7NN988nTp1Wu7ze+65Z6688so88cQT2WGHHVb5+JUrV85uu+2WBx54IO+//36ZySHat2+fJJk8eXKZfWbOnJl77rkngwcPzhlnnFG6ff78+fn4449XuYZvy+KswAcffJAWLVqUbl+wYMFyx8P5bjMzUAVp1apV+vfvn549e2bSpEml22fPnr1UGvHmm29OpUqVsssuuyRJevTokTlz5uSuu+4q0+5Pf/pT6fMrs2SScFXrXFWbbrpp2rVrl2effTadOnVa5k/dunXLdaxNNtkkZ599djp27FimptatW+e5554r03bs2LGZM2dOuY675557pkqVKnnjjTeWWyMAAAAAAAAAq9/Pf/7z1K5dOyeccEJmzpy51POFQiF33nnnCo9x5plnZuHChfnZz36WL774YqXnLCkpSaFQWGpWoz/+8Y9ZuHDhql3At2hxVuC2224rs/0vf/lLFixYUBElsZYzM9AaMnPmzHTv3j2HHnpoNttss9StWzcTJ07MfffdV2amnEaNGuX444/P22+/nU022ST/+Mc/8oc//CHHH398WrVqlSTp27dvrrrqqhxxxBGZPHlyOnbsmMceeyy//vWvs/fee2f33XdfaT1169bNRhttlL/97W/p0aNHGjZsmMaNG6dBgwblqvPrGDVqVHr16pU999wzRx55ZFq0aJGPP/44L7/8ciZNmpQ///nPy9zvueeeS//+/fPjH/847dq1S7Vq1TJ27Ng899xzZdKZhx9+eM4555yce+652XXXXfPSSy/ld7/7XerXr1+u+lq3bp2hQ4fmrLPOyv/+97/stddeadCgQT744IM8+eSTqV27doYMGfKNXgMAAAAAAAAAltamTZvceuutOeigg7L11lunf//++f73v58keemll3LttdemUCjkhz/84XKP0bVr11x11VU56aSTss022+TYY4/NFltskUqVKuX999/PX//61yRfLnG2+H932WWX/OY3v0njxo3TunXrjB8/Ptdcc03WW2+9b/2ay2uLLbbIIYcckosvvrh0BqQXX3wxF198cerXr59KlcwDQ1nCQGtIjRo10rlz59xwww2ZPHlyvvjii7Rq1SoDBw7M6aefXtquWbNmueqqq3Laaafl+eefT8OGDTNo0KAyIZQaNWpk3LhxOeuss/Kb3/wm06ZNS4sWLXLaaadl8ODB5a7pmmuuyS9/+cvsu+++mT9/fo444oiMGjWqXHV+Hd27d8+TTz6ZCy64IAMGDMgnn3ySRo0apX379jnwwAOXu1+zZs3Stm3bjBgxIlOmTElJSUk23njjXHzxxTnp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piOPPDI77bRTkuSggw5KSUlJunXrVvqzrPatW7cufTx58uSUlJRk+PDhOf/889OmTZtUr14948aNy3nnnZeSkpK8+OKLOeSQQ1K/fv00bdo0Rx11VGbOnFnmuF+dbuyRRx7JdtttlyTp169fSkpKyiy5tTpqS5Knnnoq++67bxo2bJgaNWrk+9//fm6//fZVfg1nzZqVY445Jo0aNUqdOnWy11575bXXXltm2//+97859NBD06RJk1SvXj2bb755rrrqqqXazZgxI7/4xS+y8cYbp3r16mnSpEn23nvvvPLKK6VtPv7445xwwglp0aJFqlWrlo033jhnnXVW5s+fX+ZYJSUl6d+/f0aOHJnNN9881atXz/XXX7/K1wkAAAAAAADA/3nwwQez3377pWXLlqlRo0a+973v5bjjjstHH320yseaP39+hg4dms033zw1atRIo0aN0r179zz++ONJ/m/8e/To0Uvt+9Xx9GTZy4Q9/fTT6dOnT+lYdfPmzdO7d++88847pW2WXCbskUceSUlJSW655ZacddZZad68eerVq5fdd989r7766lJ1PPTQQ+nRo0fq1auXWrVqpWvXrnn44YdX+bWAxcwM9DWdc8452X777XPiiSfm17/+dbp375569erlhBNOWKXjXHHFFdlkk03y29/+NvXq1Uu7du3yxBNPJEl+9KMf5aCDDspPf/rTPP/88znzzDOTJNdee+0yj7XNNtvkuuuuS79+/XL22Wend+/eSZKWLVt+rWtcVm3jxo3LXnvtlc6dO2fkyJGpX79+br311hx00EGZO3duuddBLBQK+cEPfpDHH3885557brbbbrv861//Sq9evZZq+9JLL2XHHXdMq1atcvHFF6dZs2a5//77c/LJJ+ejjz7K4MGDkySzZ8/OTjvtlMmTJ2fgwIHp3Llz5syZk3/+8595//33s9lmm2XevHnp3r173njjjQwZMiRbbrllHn300QwbNizPPPNM/v73v5c591133ZVHH3005557bpo1a5YmTZosVd/8+fPLBIlmzZq1Cq8yAAAAAAAAwLpnyXHR6tWrl3ulmTfeeCNdunTJ0Ucfnfr162fy5Mm55JJLstNOO+X5559P1apVy3WcBQsWpFevXnn00UczYMCA7LbbblmwYEGeeOKJvP3229lxxx1X+bq+6tNPP03Pnj3Tpk2bXHXVVWnatGmmTp2acePGZfbs2Svdf9CgQenatWv++Mc/ZtasWRk4cGD22WefvPzyy6lcuXKS5MYbb0zfvn2z33775frrr0/VqlUzatSo7Lnnnrn//vvTo0ePb3QNfDcJA31Nbdu2Tfv27ZMk7dq1yw477PC1jlOjRo3cf//9y3wz++lPf5pf/vKXSZLdd989r7/+eq699tpcc801KSkpWap9vXr10qFDh9L6vm5NK6qtV69e2WKLLTJ27NhUqfJl99lzzz3z0UcfZdCgQenbt28qVVr5hFP3339/xo0bl8svvzwnn3xykqRnz56pVq1azjrrrDJtTz311NStWzePPfZY6TqLPXv2zPz583PhhRfm5JNPToMGDXLZZZflxRdfzIMPPpjdd9+9dP/999+/9P9ff/31ee6553L77bfnxz/+cemx6tSpk4EDB+bBBx9Mz549S9vPmTMnzz//fBo0aLDcaxk2bFiGDBmy0msGAAAAAAAAKBYbbrhhmceDBw8uM8vOivzsZz8r/f+FQiE77rhjunXrlo022ij33ntv9t1333Id55Zbbsm4cePyhz/8IUcffXTp9n322adc+6/MK6+8kunTp+eaa67JfvvtV7r9wAMPLNf+7du3z4033lj6uHLlyjnwwAMzceLE7LDDDpk7d25OOeWU9OnTJ3feeWdpu7333jvbbLNNBg0alH//+9+r5Vr4brFMWAXbd999l5tqXPINbsstt8y8efPy4YcfronSlqrt9ddfzyuvvJKf/OQnSb5MWS7+2XvvvfP+++8vc0qzZVm85NjiYy126KGHlnk8b968PPzww/nhD3+YWrVqLXXOefPmlc6kdO+992aTTTYpEwRa0tixY1O7du0ccMABZbYvntFoyanWdttttxUGgZLkzDPPzMyZM0t/pkyZssL2AAAAAAAAAOu6KVOmlBknXbzSTXl8+OGH+dnPfpYNN9wwVapUSdWqVbPRRhslSV5++eVyH+fee+9NjRo1ctRRR61y/eXxve99Lw0aNMjAgQMzcuTIvPTSS6u0/7LG/JPkrbfeSpI8/vjj+fjjj3PEEUeUGQtftGhR9tprr0ycODGffvrp6rkYvlPMDFTBNthgg+U+16hRozKPF0+p9tlnn32rNS22ZG0ffPBBkuS0007Laaedtsx9yruG4/Tp01OlSpWlrrFZs2ZLtVuwYEGuvPLKXHnllSs857Rp09KqVauVnrdZs2ZLzazUpEmTVKlSJdOnTy+zfUX3Z7FVme4OAAAAAAAAoBjUq1evdGWXVbFo0aLsscceee+993LOOeekY8eOqV27dhYtWpQddthhlcbDp02blubNm5dr9Zqvo379+hk/fnwuuOCCDBo0KJ988kk22GCDHHPMMTn77LNXupzZysb8F4/BLzmZxVd9/PHHqV279je5DL6DhIFWsxo1amTmzJlLbV9eSGZZy319W75pbY0bN07y5Uw4X11666s23XTTctXSqFGjLFiwINOnTy/zBjh16tQy7Ro0aJDKlSvn8MMPz4knnrjMY7Vp0yZJsv766+edd95Z6Xn//e9/p1AolLm+Dz/8MAsWLCi9xsXW5P0BAAAAAAAAKHYvvPBCnn322YwePTpHHHFE6fbXX399lY+1/vrr57HHHsuiRYuWGwiqUaNGkmT+/Pllti85UcTydOzYMbfeemsKhUKee+65jB49OkOHDk3NmjVzxhlnrHLNX7V4fPrKK6/MDjvssMw2TZs2/Ubn4LvJMmGrWevWrfPaa6+VeSOZPn16Hn/88TVy/hXNHvRNa9t0003Trl27PPvss+nUqdMyf+rWrVuuY3Xv3j1JctNNN5XZfvPNN5d5XKtWrXTv3j1PP/10ttxyy2Wec3GYqFevXnnttdcyduzY5Z63R48emTNnTu66664y2//0pz+VPg8AAAAAAADAt2PxhAxLrr4yatSoVT5Wr169Mm/evIwePXq5bZo2bZoaNWrkueeeK7P9b3/72yqdq6SkJFtttVUuvfTSrLfeepk0adIq17ukrl27Zr311stLL7203DH4atWqfePz8N1jZqDV7PDDD8+oUaNy2GGH5Zhjjsn06dMzfPjwrzU92tfRtm3b1KxZMzfddFM233zz1KlTJ82bN0/z5s1XS22jRo1Kr169sueee+bII49MixYt8vHHH+fll1/OpEmT8uc//7lcx9ljjz2yyy675PTTT8+nn36aTp065V//+lduuOGGpdpefvnl2WmnnbLzzjvn+OOPT+vWrTN79uy8/vrrufvuu0vDPwMGDMhtt92W/fbbL2eccUa23377fPbZZxk/fnz69OmT7t27p2/fvrnqqqtyxBFHZPLkyenYsWMee+yx/PrXv87ee++d3XffvdyvBQAAAAAAAACrZrPNNkvbtm1zxhlnpFAopGHDhrn77rvz4IMPrvKxDjnkkFx33XX52c9+lldffTXdu3fPokWL8u9//zubb755Dj744JSUlOSwww7Ltddem7Zt22arrbbKk08+udREFctyzz33ZMSIEfnBD36QjTfeOIVCIXfccUdmzJiRnj17fp3LL6NOnTq58sorc8QRR+Tjjz/OAQcckCZNmmTatGl59tlnM23atFx99dXf+Dx89wgDrWZdu3bN9ddfnwsvvDD77bdfNt544wwePDj/+Mc/8sgjj3zr569Vq1auvfbaDBkyJHvssUe++OKLDB48OOedd95qqa179+558sknc8EFF2TAgAH55JNP0qhRo7Rv3z4HHnhgueusVKlSxowZk1NPPTXDhw/P559/nq5du+Yf//hHNttsszJt27dvn0mTJuVXv/pVzj777Hz44YdZb7310q5du+y9996l7erWrZvHHnss5513Xn7/+99nyJAhadCgQbbbbrsce+yxSb6cAm7cuHE566yz8pvf/CbTpk1LixYtctppp2Xw4MHlrh8AAAAAAACAVVe1atXcfffdOeWUU3LcccelSpUq2X333fPQQw+lVatWq3SsKlWq5B//+EeGDRuWW265JZdddlnq1q2brbbaKnvttVdpu4svvjhJMnz48MyZMye77bZb7rnnnrRu3XqFx2/Xrl3WW2+9DB8+PO+9916qVauWTTfddKklzr6Jww47LK1atcrw4cNz3HHHZfbs2WnSpEm23nrrHHnkkavlHHz3lBQKhUJFFwHFZNasWalfv34mTJiQOnXqVHQ5AABFqUOHDhVdAvANLP7cNHPmzDU2ky6sinWhj77wwgsVXQIAAPAdNWfOnHTp0mWt/swE33WVKroAAAAAAAAAAABg9bBMGKvdggULVvh8pUqVUqmSHBoAAAAAAAAAy2bcGb4+vxmsdlWrVl3hz1FHHVXRJQIAAAAAAACwlpo8efJKx52HDh1a0WXCWsvMQKx2EydOXOHzjRs3XkOVAAAAAAAAALCuad68+UrHnZs3b76GqoF1jzAQq12nTp0qugQAAAAAAAAA1lHVqlUz7gzfgGXCAAAAAAAAAACgSAgDAQAAAAAAAABAkRAGAgAAAAAAAACAIiEMBAAAAAAAAAAARUIYCAAAAAAAAAAAioQwEAAAAAAAAAAAFAlhIAAAAAAAAAAAKBLCQAAAAAAAAAAAUCSEgQAAAAAAAAAAoEgIAwEAAAAAAAAAQJEQBgIAAAAAAAAAgCIhDAQAAAAAAAAAAEVCGAgAAAAAAAAAAIqEMBAAAAAAAAAAABQJYSAAAAAAAAAAACgSwkAAAAAAAAAAAFAkhIEAAAAAAAAAAKBICAMBAAAAAAAAAECREAYCAAAAAAAAAIAiIQwEAAAAAAAAAABFQhgIAAAAAAAAAACKhDAQAAAAAAAAAAAUCWEgAAAAAAAAAAAoEsJAAAAAAAAAAABQJKpUdAFQrNq3b5969epVdBkAAABAEerQoUNFlwAAAHxHzZo1q6JLAFbCzEAAAAAAAAAAAFAkhIEAAAAAAAAAAKBICAMBAAAAAAAAAECREAYCAAAAAAAAAIAiIQwEAAAAAAAAAABFQhgIAAAAAAAAAACKhDAQAAAAAAAAAAAUCWEgAAAAAAAAAAAoEsJAAAAAAAAAAABQJISBAAAAAAAAAACgSAgDAQAAAAAAAABAkRAGAgAAAAAAAACAIiEMBAAAAAAAAAAARUIYCAAAAAAAAAAAioQwEAAAAAAAAAAAFAlhIAAAAAAAAAAAKBLCQAAAAAAAAAAAUCSqVHQBUKxeeuml1KlTp6LLAAD4xjp06FDRJQAAS3jhhRcqugQAAOA7as6cORVdArASZgYCAAAAAAAAAIAiIQwEAAAAAAAAAABFQhgIAAAAAAAAAACKhDAQAAAAAAAAAAAUCWEgAAAAAAAAAAAoEsJAAAAAAAAAAABQJISBAAAAAAAAAACgSAgDAQAAAAAAAABAkRAGAgAAAAAAAACAIiEMBAAAAAAAAAAARUIYCAAAAAAAAAAAioQwEAAAAAAAAAAAFAlhIAAAAAAAAAAAKBLCQAAAAAAAAAAAUCSEgQAAAAAAAAAAoEgIAwEAAAAAAAAAQJEQBgIAAAAAAAAAgCIhDAQAAAAAAAAAAEVCGAgAAAAAAAAAAIqEMBAAAAAAAAAAABQJYSAAAAAAAAAAACgSwkAAAAAAAAAAAFAkhIEAAAAAAAAAAKBICAMBAAAAAAAAAECREAYCAAAAAAAAAIAiIQwEAAAAAAAAAABFQhgIAAAAAAAAAACKhDAQAAAAAAAAAAAUCWEgAAAAAAAAAAAoEsJAAAAAAAAAAABQJISBAAAAAAAAAACgSAgDLWHEiBEZPXp0RZfBN3TkkUemdevWFV0GAAAAAAAAAF/T6NGjU1JSksmTJ6+R83Xr1i3dunVbbcdb0/VXhMmTJ6ekpORbzVmUlJTkvPPO+9aOX4yEgZYgDFQczjnnnNx5550VXQYAAAAAAAAAFK0NNtggEyZMSO/evSu6FL6iSkUX8F1QKBQyb9681KxZs6JLKXpz585NrVq10rZt24ouBQAAAAAAAACKWvXq1bPDDjtUdBks4WvNDPTKK6/kkEMOSdOmTVO9evW0atUqffv2zfz585MkL7zwQvbbb780aNAgNWrUyNZbb53rr7++zDEeeeSRlJSU5Oabb87AgQOzwQYbpE6dOtlnn33ywQcfZPbs2Tn22GPTuHHjNG7cOP369cucOXPKHKOkpCT9+/fPqFGjsskmm6R69epp3759br311jLtzjvvvJSUlCx1HUtOydW6deu8+OKLGT9+fEpKSlJSUlJmqalZs2bltNNOS5s2bVKtWrW0aNEiAwYMyKeffrrMukaOHJnNN9881atXL73+q6++OltttVXq1KmTunXrZrPNNsugQYNW6fW/6qqrsssuu6RJkyapXbt2OnbsmOHDh+eLL75Yqu19992XHj16pH79+qlVq1Y233zzDBs2rEybf//739lnn33SqFGj1KhRI23bts2AAQPKtPnvf/+bQw89NE2aNEn16tWz+eab56qrrirTZtGiRTn//POz6aabpmbNmllvvfWy5ZZb5vLLLy9tM23atBx77LHZcMMNU7169ay//vrp2rVrHnrooTLHuvbaa7PVVlulRo0aadiwYX74wx/m5ZdfLtPmyCOPTJ06dfL8889njz32SN26ddOjR4/S55ZcJqxQKGTEiBHZeuutU7NmzTRo0CAHHHBA/ve//5Vp9/TTT6dPnz6l19q8efP07t0777zzzvJvCgAAAAAAAADLtbKcwRNPPJGuXbumRo0aad68ec4888xljoGPHTs23bp1S6NGjVKzZs20atUqP/rRjzJ37txy11IoFDJ8+PBstNFGqVGjRrbZZpvce++9ZdpMmzYt1apVyznnnLPMaykpKckVV1xRum1N1t+tW7d06NAhEyZMyI477piaNWumdevWue6665Ikf//737PNNtukVq1a6dixY+67774y+y9rPD1Zdrbiz3/+czp37lyaOdh4441z1FFHlT6/vGXCVna/p02blhNOOCHt27dPnTp10qRJk+y222559NFHV3r9c+fOLc1uLM4UdOrUKbfcckt5Xr7vhFWeGejZZ5/NTjvtlMaNG2fo0KFp165d3n///YwZMyaff/55Jk+enB133DFNmjTJFVdckUaNGuXGG2/MkUcemQ8++CCnn356meMNGjQo3bt3z+jRozN58uScdtppOeSQQ1KlSpVstdVWueWWW/L0009n0KBBqVu3bplfpiQZM2ZMxo0bl6FDh6Z27doZMWJE6f4HHHDAKl3bnXfemQMOOCD169fPiBEjknyZYku+7Ey77rpr3nnnnQwaNChbbrllXnzxxZx77rl5/vnn89BDD5X5pbjrrrvy6KOP5txzz02zZs3SpEmT3HrrrTnhhBNy0kkn5be//W0qVaqU119/PS+99NIq1fnGG2/k0EMPLQ0lPfvss7ngggvyyiuv5Nprry1td8011+SYY47JrrvumpEjR6ZJkyZ57bXX8sILL5S2uf/++7PPPvtk8803zyWXXJJWrVpl8uTJeeCBB0rbvPTSS9lxxx3TqlWrXHzxxWnWrFnuv//+nHzyyfnoo48yePDgJMnw4cNz3nnn5eyzz84uu+ySL774Iq+88kpmzJhReqzDDz88kyZNygUXXJBNNtkkM2bMyKRJkzJ9+vTSNsOGDcugQYNyyCGHZNiwYZk+fXrOO++8dOnSJRMnTky7du1K237++efZd999c9xxx+WMM87IggULlvu6HXfccRk9enROPvnkXHTRRfn4448zdOjQ7Ljjjnn22WfTtGnTfPrpp+nZs2fatGmTq666Kk2bNs3UqVMzbty4zJ49e5nHnT9/fukbVvJlaAwAAAAAAACgmC05Llq9evXS8fUlrSxn8MYbb6RHjx5p3bp1Ro8enVq1amXEiBG5+eabyxxn8uTJ6d27d3beeedce+21WW+99fLuu+/mvvvuy+eff55atWqVq/YhQ4ZkyJAh+elPf5oDDjggU6ZMyTHHHJOFCxdm0003TZKsv/766dOnT66//voMGTIklSr931wr1113XapVq5af/OQnSb4cU1+T9SfJ1KlT069fv5x++ulp2bJlrrzyyhx11FGZMmVK/vKXv2TQoEGpX79+hg4dmh/84Af53//+l+bNm5f7+EkyYcKEHHTQQTnooINy3nnnpUaNGnnrrbcyduzYFe63svtdvXr1fPzxx0mSwYMHp1mzZpkzZ07uvPPOdOvWLQ8//HC6deu23OOfeuqpueGGG3L++efn+9//fj799NO88MILZXIH33UlhUKhsCo79OjRI5MmTcprr72W9ddff6nnDznkkNx5553573//mw033LB0+957753x48fnvffeS/369fPII4+ke/fu2WeffTJmzJjSdj//+c9z2WWX5eSTTy4zo8wPf/jD/POf/yxz80pKSlKzZs28+eabadq0aZJk4cKF6dChQxYsWJD//ve/Sb5Mrw0ZMiRLXuro0aPTr1+/vPnmm6Wptw4dOqRx48Z55JFHyrS98MILc9ZZZ+Xf//53OnXqVLr9r3/9aw444ID84x//SK9evUrrql+/ft588800aNCgtO1JJ52UG2+8MZ988km5XuvyWLRoURYtWpRbbrkl/fr1y7Rp09KgQYPMmTMnLVq0yJZbbpl//vOfy5wZKUm+973vJflyNqcaNWoss81ee+2VF198MS+++GLq1atX5nr++Mc/5r333kuDBg2yzz775J133snTTz+93Hrr1q2bo48+Opdeeukyn58xY0aaN2+e7t275+9//3vp9ilTpqRdu3b50Y9+lJtuuinJl2nF66+/Ptdee2369etX5jhHHnlkHnnkkdJZn5544ol06dIlF198cU499dTSdu+880422WSTnHTSSbnooovyn//8J506dcpdd92V/fbbb7nX8VWL+9eSJkyYkDp16pTrGAAAa7MOHTpUdAlAkZk1a1bq16+fmTNnlvmcCWuLdaGPfvUfewEAAKxJc+bMSZcuXZbaPnjw4Jx33nnL3GdlOYODDz44Y8aMWebY/yuvvFI6pr94fP6ZZ57JVltt9bXqnzFjRjbYYIP06tUrd9xxR+n2xx9/PF27ds2uu+5amhe4++67s+++++aBBx5Iz549S+tq1apVunTpkr/85S9rvP7ky5mBxo8fn6eeeirbbrttkuTjjz9OkyZNUq1atbz++uulwZ9nn302W2+9da644oqcdNJJSZYeT19syWzFxRdfnNNOOy0zZsxI/fr1l1nL5MmT06ZNm1x33XU58sgjk6z8fi/LwoULUygUstdee6VevXpl7k1JSUmZ/tWxY8d873vfy5133lmuY38XrdIyYXPnzs348eNz4IEHLveGjR07Nj169CgTBEq+7Exz587NhAkTymzv06dPmcebb755kqR3795Lbf/444+XWiqsR48epb9MSVK5cuUcdNBBef3111frsk733HNPOnTokK233joLFiwo/dlzzz1TUlKyVHhot912KxMESpLtt98+M2bMyCGHHJK//e1v+eijj75WLU8//XT23XffNGrUKJUrV07VqlXTt2/fLFy4MK+99lqSL9+oZs2alRNOOGG5QaDXXnstb7zxRn76058uNwg0b968PPzww/nhD3+YWrVqlbn2vffeO/PmzcsTTzxRen3PPvtsTjjhhNx///3LnCFn++23z+jRo3P++efniSeeWGpatAkTJuSzzz4rfZNYbMMNN8xuu+2Whx9+eKlj/uhHP1rpa3bPPfekpKQkhx12WJlraNasWbbaaqvS+/e9730vDRo0yMCBAzNy5Mhyzdp05plnZubMmaU/U6ZMWek+AAAAAAAAAOuyKVOmlBknPfPMM5fZrjw5g3Hjxi137P+rtt5661SrVi3HHntsrr/++vzvf/9b5bonTJiQefPmlc7qs9iOO+6YjTbaqMy2Xr16pVmzZqXLbyVfrr7z3nvvlVkqa03Wv9gGG2xQGgRKkoYNG6ZJkybZeuuty8wAtDiD8dZbb63yObbbbrskyYEHHpjbb78977777kr3Kc/9XmzkyJHZZpttUqNGjVSpUiVVq1bNww8/nJdffnmF+22//fa59957c8YZZ+SRRx7JZ599Vv6L+o5YpTDQJ598koULF6Zly5bLbTN9+vRssMEGS21f3NmWnJapYcOGZR5Xq1ZthdvnzZtXZnuzZs2WOtfibatzCqgPPvggzz33XKpWrVrmp27duikUCksFe5b1Ghx++OG59tpr89Zbb+VHP/pRmjRpks6dO+fBBx8sdx1vv/12dt5557z77ru5/PLL8+ijj2bixIm56qqrkqS0k0+bNi1JVnivytNm+vTpWbBgQa688sqlrn3vvfdOktJrP/PMM/Pb3/42TzzxRHr16pVGjRqlR48eeeqpp0qPd9ttt+WII47IH//4x3Tp0iUNGzZM3759M3Xq1NLzJct+/Zo3b77UPa1Vq1a5/oXeBx98kEKhkKZNmy51HU888UTpNdSvXz/jx4/P1ltvnUGDBmWLLbZI8+bNM3jw4GWu55h8Od1dvXr1yvwAAAAAAAAAFLMlx0iXt0RYeXMGKxr7X6xt27Z56KGH0qRJk5x44olp27Zt2rZtW2bVoZVZPOZcnvNVqVIlhx9+eO68887MmDEjyZcrEG2wwQbZc889K6T+xZbMVCRf5irKm7Uoj1122SV33XVXFixYkL59+6Zly5bp0KFDbrnlluXuU577nSSXXHJJjj/++HTu3Dl//etf88QTT2TixInZa6+9VhruueKKKzJw4MDcdddd6d69exo2bJgf/OAHpatHkVRZlcYNGzZM5cqVVzjjTqNGjfL+++8vtf29995LkjRu3HgVS1yxxSGSZW1r1KhRkpTOejN//vwyb0CrMjNP48aNU7NmzVx77bXLff6rljcbT79+/dKvX798+umn+ec//5nBgwenT58+ee2115ZKGS7LXXfdlU8//TR33HFHmfbPPPNMmXaLE3YrulfladOgQYNUrlw5hx9+eE488cRltmnTpk2SL98ITz311Jx66qmZMWNGHnrooQwaNCh77rlnpkyZklq1aqVx48a57LLLctlll+Xtt9/OmDFjcsYZZ+TDDz/MfffdV3rPlteHyvs6L6lx48YpKSnJo48+usz/CH11W8eOHXPrrbemUCjkueeey+jRozN06NDUrFkzZ5xxRrnOBwAAAAAAAED5cwYrGvv/qp133jk777xzFi5cmKeeeipXXnllBgwYkKZNm+bggw9eaT2Lx6SXd77WrVuX2davX7/85je/ya233pqDDjooY8aMyYABA1K5cuUKqX91qFGjRubPn7/U9mVlKPbbb7/st99+mT9/fp544okMGzYshx56aFq3br3M5eLKc7+T5MYbb0y3bt1y9dVXl9k+e/bsldZfu3btDBkyJEOGDMkHH3xQOkvQPvvsk1deeWWl+38XrNLMQDVr1syuu+6aP//5z8sN0vTo0SNjx44tDf8s9qc//Sm1atXKDjvs8PWrXYaHH344H3zwQenjhQsX5rbbbkvbtm1Lk2aLf1mfe+65MvvefffdSx2vevXqy0yZ9enTJ2+88UYaNWqUTp06LfWz5BvCytSuXTu9evXKWWedlc8//zwvvvhiufZbHH75anilUCjkD3/4Q5l2O+64Y+rXr5+RI0eWrue3pE022SRt27bNtddeu8xf9OTLmXe6d++ep59+OltuueUyr33xm+VXrbfeejnggANy4okn5uOPP15qrcEkadWqVfr375+ePXtm0qRJSZIuXbqkZs2aufHGG8u0feedd0qXoPs6+vTpk0KhkHfffXeZ19CxY8el9ikpKclWW22VSy+9NOutt15pjQAAAAAAAACUT3lyBt27d1/u2P/yVK5cOZ07dy5dRae847k77LBDatSokZtuuqnM9scff3yZS2ltvvnm6dy5c6677rrcfPPNmT9/fvr161dh9a8OrVu3zocfflim3s8//zz333//cvepXr16dt1111x00UVJkqeffnqZ7cpzv5Mvx+OXnMjjueeey4QJE1blUtK0adMceeSROeSQQ/Lqq69m7ty5q7R/sVqlmYGSL6dq2mmnndK5c+ecccYZ+d73vpcPPvggY8aMyahRozJ48ODcc8896d69e84999w0bNgwN910U/7+979n+PDhqV+//mq9gMaNG2e33XbLOeeck9q1a2fEiBF55ZVXcuutt5a22XvvvdOwYcP89Kc/zdChQ1OlSpWMHj06U6ZMWep4i2eFue2227LxxhunRo0a6dixYwYMGJC//vWv2WWXXfLzn/88W265ZRYtWpS33347DzzwQH7xi1+kc+fOK6z1mGOOSc2aNdO1a9dssMEGmTp1aoYNG5b69euXrrW3Mj179ky1atVyyCGH5PTTT8+8efNy9dVX55NPPinTrk6dOrn44otz9NFHZ/fdd88xxxyTpk2b5vXXX8+zzz6b3/3ud0mSq666Kvvss0922GGH/PznP0+rVq3y9ttv5/777y9987v88suz0047Zeedd87xxx+f1q1bZ/bs2Xn99ddz9913Z+zYsUmSffbZJx06dEinTp2y/vrr56233spll12WjTbaKO3atcvMmTPTvXv3HHroodlss81St27dTJw4Mffdd1/233//JF+GiM4555wMGjQoffv2zSGHHJLp06dnyJAhqVGjRgYPHlyu12lJXbt2zbHHHpt+/frlqaeeyi677JLatWvn/fffz2OPPZaOHTvm+OOPzz333JMRI0bkBz/4QTbeeOMUCoXccccdmTFjRnr27Pm1zg0AAAAAAADwXbaynMHZZ5+dMWPGZLfddsu5556bWrVq5aqrrsqnn35a5jgjR47M2LFj07t377Rq1Srz5s0rXd1n9913L1ctDRo0yGmnnZbzzz8/Rx99dH784x9nypQpOe+885a51FeSHHXUUTnuuOPy3nvvZccdd8ymm25a5vk1Wf/qcNBBB+Xcc8/NwQcfnF/+8peZN29errjiiixcuLBMu3PPPTfvvPNOevTokZYtW2bGjBm5/PLLU7Vq1ey6667LPf7K7nfdunXTp0+f/OpXv8rgwYOz66675tVXX83QoUPTpk2bLFiwYIX1d+7cOX369MmWW26ZBg0a5OWXX84NN9yQLl26pFatWqvlNVrXrXIYaKuttsqTTz6ZwYMH58wzz8zs2bPTrFmz7LbbbqlWrVo23XTTPP744xk0aFBOPPHEfPbZZ9l8881z3XXX5cgjj1ztF7Dvvvtmiy22yNlnn5233347bdu2zU033ZSDDjqotE29evVy3333ZcCAATnssMOy3nrr5eijj06vXr1y9NFHlznekCFD8v777+eYY47J7Nmzs9FGG2Xy5MmpXbt2Hn300Vx44YX5/e9/nzfffDM1a9ZMq1atsvvuu5drZqCdd945o0ePzu23355PPvkkjRs3zk477ZQ//elPpUt2rcxmm22Wv/71rzn77LOz//77p1GjRjn00ENz6qmnplevXmXa/vSnP03z5s1z0UUX5eijj06hUEjr1q1zxBFHlLbZc889889//jNDhw7NySefnHnz5qVly5bZd999S9u0b98+kyZNyq9+9aucffbZ+fDDD7PeeuulXbt22XvvvUvbde/ePX/961/zxz/+MbNmzUqzZs3Ss2fPnHPOOalatWpq1KiRzp0754YbbsjkyZPzxRdfpFWrVhk4cGBOP/300uOceeaZadKkSa644orcdtttqVmzZrp165Zf//rXadeuXblep2UZNWpUdthhh4waNSojRozIokWL0rx583Tt2jXbb799kqRdu3ZZb731Mnz48Lz33nulfXr06NFlXjcAAAAAAAAAymdlOYMOHTrkoYceyi9+8YscccQRadCgQQ4//PD86Ec/yrHHHlt6nK233joPPPBABg8enKlTp6ZOnTrp0KFDxowZkz322KPc9QwdOrR0spEbbrghm222WUaOHJnf/va3y2x/8MEHZ8CAAXnnnXeWOYHFmq7/m2rTpk3+9re/ZdCgQTnggAOywQYb5NRTT820adMyZMiQ0nadO3fOU089lYEDB2batGlZb7310qlTp4wdOzZbbLHFco+/svudJGeddVbmzp2ba665JsOHD0/79u0zcuTI3HnnnXnkkUdWWP9uu+2WMWPG5NJLL83cuXPTokWL9O3bN2edddZqeX2KQUlheWtIrQNKSkpy4oknls5yA2uDWbNmpX79+pkwYULq1KlT0eUAAHxjHTp0qOgSgCKz+HPTzJkzU69evYouB5ayLvTRF154oaJLAAAAvqPmzJmTLl26rNWfmeC7rlJFFwAAAAAAAAAAAKweq7xMGN+ela17V6lSpVSqJL8FAAAAAAAAAEtauHBhVrQ4UklJSSpXrrwGK1o163r9rD3W6WRJoVAoqiXCqlatusKfo446qqJLBAAAAAAAAIC1Uo8ePVY45t62bduKLnGF1vX6WXuYGWgtMnHixBU+37hx4zVUCQAAAAAAAACsW0aNGpXZs2cv9/nq1auvwWpW3bpeP2sPYaC1SKdOnSq6BAAAAAAAAABYJ2266aYVXcI3sq7Xz9pjnV4mDAAAAAAAAAAA+D/CQAAAAAAAAAAAUCSEgQAAAAAAAAAAoEgIAwEAAAAAAAAAQJEQBgIAAAAAAAAAgCIhDAQAAAAAAAAAAEVCGAgAAAAAAAAAAIqEMBAAAAAAAAAAABQJYSAAAAAAAAAAACgSwkAAAAAAAAAAAFAkhIEAAAAAAAAAAKBICAMBAAAAAAAAAECREAYCAAAAAAAAAIAiIQwEAAAAAAAAAABFQhgIAAAAAAAAAACKhDAQAAAAAAAAAAAUCWEgAAAAAAAAAAAoEsJAAAAAAAAAAABQJISBAAAAAAAAAACgSAgDAQAAAAAAAABAkRAGAgAAAAAAAACAIiEMBAAAAAAAAAAARUIYCAAAAAAAAAAAioQwEAAAAAAAAAAAFIkqFV0AFKv27dunXr16FV0GAAAAUIQ6dOhQ0SUAAADfUbNmzaroEoCVMDMQAAAAAAAAAAAUCWEgAAAAAAAAAAAoEsJAAAAAAAAAAABQJISBAAAAAAAAAACgSAgDAQAAAAAAAABAkRAGAgAAAAAAAACAIiEMBAAAAAAAAAAARaJKRRcAxaZQKCRJZs2aVcGVAAAArJ0Wf15a/PkJ1jY+2wMAACyfz/Ww9hMGgtVs+vTpSZINN9ywgisBAABYu82ePTv169ev6DJgKbNnz07isz0AAMCKTJ8+3ed6WEsJA8Fq1rBhwyTJ22+/7T9+fC2zZs3KhhtumClTpqRevXoVXQ7rIH2Ib0of4pvSh/im9KHiVygUMnv27DRv3ryiS4Flat68eaZMmZK6deumpKSkostZivfJ4uFeFg/3sni4l8XDvSwe7mXxcC+Lx8yZM9OqVavScVFg7SMMBKtZpUqVkiT169f3hwzfSL169fQhvhF9iG9KH+Kb0of4pvSh4uYfT7A2q1SpUlq2bFnRZayU98ni4V4WD/eyeLiXxcO9LB7uZfFwL4vH4nFRYO3jtxMAAAAAAAAAAIqEMBAAAAAAAAAAABQJYSBYzapXr57BgwenevXqFV0K6yh9iG9KH+Kb0of4pvQhvil9CGDFvE8WD/eyeLiXxcO9LB7uZfFwL4uHe1k83EtY+5UUCoVCRRcBAAAAAAAAAAB8c2YGAgAAAAAAAACAIiEMBAAAAAAAAAAARUIYCAAAAAAAAAAAioQwEAAAAAAAAAAAFAlhIAAAAAAAAAAAKBLCQLCajRgxIm3atEmNGjWy7bbb5tFHH63okljDhg0blu222y5169ZNkyZN8oMf/CCvvvpqmTaFQiHnnXdemjdvnpo1a6Zbt2558cUXy7SZP39+TjrppDRu3Di1a9fOvvvum3feeadMm08++SSHH3546tevn/r16+fwww/PjBkzvu1LZA0bNmxYSkpKMmDAgNJt+hAr8+677+awww5Lo0aNUqtWrWy99db5z3/+U/q8PsSKLFiwIGeffXbatGmTmjVrZuONN87QoUOzaNGi0jb6EF/1z3/+M/vss0+aN2+ekpKS3HXXXWWeX5P95e23384+++yT2rVrp3Hjxjn55JPz+eeffxuXDfCtW9n761cdd9xxKSkpyWWXXbbG6qP8VnQvv/jiiwwcODAdO3ZM7dq107x58/Tt2zfvvfdexRXMcq2Ov3tYO5XncxDrjpV9L8K6Z1nfkbLuKM+4CesW46Gw9hMGgtXotttuy4ABA3LWWWfl6aefzs4775xevXrl7bffrujSWIPGjx+fE088MU888UQefPDBLFiwIHvssUc+/fTT0jbDhw/PJZdckt/97neZOHFimjVrlp49e2b27NmlbQYMGJA777wzt956ax577LHMmTMnffr0ycKFC0vbHHrooXnmmWdy33335b777sszzzyTww8/fI1eL9+uiRMn5ve//3223HLLMtv1IVbkk08+SdeuXVO1atXce++9eemll3LxxRdnvfXWK22jD7EiF110UUaOHJnf/e53efnllzN8+PD85je/yZVXXlnaRh/iqz799NNstdVW+d3vfrfM59dUf1m4cGF69+6dTz/9NI899lhuvfXW/PWvf80vfvGLb+/iAb5FK3t/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\n",
      "text/plain": [
       "<Figure size 2400x600 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))\n",
    " \n",
    "colors = [\"#800000\", \"#D3D3D3\", \"#D3D3D3\", \"#D3D3D3\", \"#D3D3D3\"]\n",
    " \n",
    "sns.barplot(x=\"orders\", y=\"category\", data=df_category.sort_values(by=\"orders\", ascending=False).head(5), palette=colors, ax=ax[0])\n",
    "ax[0].set_ylabel(None)\n",
    "ax[0].set_xlabel(None)\n",
    "ax[0].set_title(\"Category Terlaris\", loc=\"center\", fontsize=15)\n",
    "ax[0].tick_params(axis ='y', labelsize=12)\n",
    " \n",
    "sns.barplot(x=\"orders\", y=\"category\", data=df_category.sort_values(by=\"orders\", ascending=True).head(5), palette=colors, ax=ax[1])\n",
    "ax[1].set_ylabel(None)\n",
    "ax[1].set_xlabel(None)\n",
    "ax[1].invert_xaxis()\n",
    "ax[1].yaxis.set_label_position(\"right\")\n",
    "ax[1].yaxis.tick_right()\n",
    "ax[1].set_title(\"Category Sedikit Peminat\", loc=\"center\", fontsize=15)\n",
    "ax[1].tick_params(axis='y', labelsize=12)\n",
    " \n",
    "plt.suptitle(\"Category Terlaris dan Sedikit Peminat berdasarkan Total Pembelian\", fontsize=20)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5db68acb",
   "metadata": {
    "papermill": {
     "duration": 0.035492,
     "end_time": "2023-10-18T10:08:31.919026",
     "exception": false,
     "start_time": "2023-10-18T10:08:31.883534",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "dari kedua grafik diatas, dapat diketahui bed_bath_table merupakan caterogy yang paling banyak dibeli sedangkan security dan service adalah ketogori yang paling sedikit dibeli."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6c39e201",
   "metadata": {
    "papermill": {
     "duration": 0.030118,
     "end_time": "2023-10-18T10:08:31.979456",
     "exception": false,
     "start_time": "2023-10-18T10:08:31.949338",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## Pertanyaan 2: Berapa lama rata-rata pengiriman paket pengiriman paket terlama ? dari mana ke mana?\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2e51bba1",
   "metadata": {
    "papermill": {
     "duration": 0.030108,
     "end_time": "2023-10-18T10:08:32.040445",
     "exception": false,
     "start_time": "2023-10-18T10:08:32.010337",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "### pengiriman antar state"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "f95820dc",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:32.103781Z",
     "iopub.status.busy": "2023-10-18T10:08:32.103319Z",
     "iopub.status.idle": "2023-10-18T10:08:32.141280Z",
     "shell.execute_reply": "2023-10-18T10:08:32.139948Z"
    },
    "papermill": {
     "duration": 0.072849,
     "end_time": "2023-10-18T10:08:32.143718",
     "exception": false,
     "start_time": "2023-10-18T10:08:32.070869",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>seller_state</th>\n",
       "      <th>customer_state</th>\n",
       "      <th>lama_pengiriman_hari</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>CE</td>\n",
       "      <td>AM</td>\n",
       "      <td>138.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>AM</td>\n",
       "      <td>AL</td>\n",
       "      <td>87.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>BA</td>\n",
       "      <td>AC</td>\n",
       "      <td>63.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>ES</td>\n",
       "      <td>PA</td>\n",
       "      <td>34.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>GO</td>\n",
       "      <td>AM</td>\n",
       "      <td>29.500000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>407</th>\n",
       "      <td>PA</td>\n",
       "      <td>PR</td>\n",
       "      <td>3.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>408</th>\n",
       "      <td>PB</td>\n",
       "      <td>RN</td>\n",
       "      <td>3.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>409</th>\n",
       "      <td>RN</td>\n",
       "      <td>RN</td>\n",
       "      <td>2.571429</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>410</th>\n",
       "      <td>DF</td>\n",
       "      <td>DF</td>\n",
       "      <td>1.756098</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>411</th>\n",
       "      <td>PI</td>\n",
       "      <td>PI</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>412 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "    seller_state customer_state  lama_pengiriman_hari\n",
       "0             CE             AM            138.000000\n",
       "1             AM             AL             87.000000\n",
       "2             BA             AC             63.000000\n",
       "3             ES             PA             34.000000\n",
       "4             GO             AM             29.500000\n",
       "..           ...            ...                   ...\n",
       "407           PA             PR              3.000000\n",
       "408           PB             RN              3.000000\n",
       "409           RN             RN              2.571429\n",
       "410           DF             DF              1.756098\n",
       "411           PI             PI              1.000000\n",
       "\n",
       "[412 rows x 3 columns]"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_pengiriman_state = cust_seller.groupby(['seller_state', 'customer_state'])['lama_pengiriman_hari'].mean().sort_values(ascending=False).reset_index()\n",
    "df_pengiriman_state "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "cc39525f",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:32.206186Z",
     "iopub.status.busy": "2023-10-18T10:08:32.205713Z",
     "iopub.status.idle": "2023-10-18T10:08:32.591186Z",
     "shell.execute_reply": "2023-10-18T10:08:32.589914Z"
    },
    "papermill": {
     "duration": 0.419375,
     "end_time": "2023-10-18T10:08:32.593182",
     "exception": false,
     "start_time": "2023-10-18T10:08:32.173807",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "image/png": "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LsEZIzPFRiaVRbSRuWWZSjYyqSyijcwuC6UUFosFxcXFYJjJWwJyOp1wu90p25HL5VAqM1//b7L5Us7gMAyD0tLStNnLyspKOSV2ptjIpLKINjK3LFPJRiaVRbSRuWWZrJmbUJRKpeiYpBExGklERERERERkyiE6OCIiIiIiIiJTDtHBSQGFQoH77rsPCoXijLeRSWURbWRuWaaSjUwqi2gjs8sicmbypQwyFhEREREREZnaiDM4IiIiIiIiIlMO0cERERERERERmXKIDo6IiIiIiIjIlEN0cERERERERESmHKKDkyT9/f3YsGEDqquroVAoUFZWhosvvhjvvfceAKCyshKEkIjXL3/5SwDAjh07IJFIsHbt2jC77e3tIIRAKpWip6cn7LO+vj5IpVIQQnDFFVeE2TUajVi7di0OHDgQUdZbbrkFEokEL7zwQsRnN9xwQ9RyBsq1d+9efPWrX0V+fj6USiUqKytx9dVXY3h4OKwubr/9dtTW1kKpVKKgoADLli3Dn//8Z9jt9uBxO3bswLp165CdnQ2lUolZs2bhsccew/XXXx/8XqlUivLycnznO9+B2WwOK2us830+X9TrkclkqK6uxp133gmbzRas22ivnTt3Bm0MDg7i1ltvRXl5ORQKBQoLC7FmzRp8+umnwWP27t2LK6+8EgUFBVAqlaivr8fNN9+MpqampO2E9hG1Wo2ZM2fiySefDLuO//zP/4xos+9+97sghMRsu9DXDTfcEFEvseq4srISjz/+eNT+kagcE9tpYt/m0y56vR6LFy/G66+/HvGdfOzt27cv5nnJXE+09ispKeFVH/HujfXr1yddJ3K5HLW1tfjFL34Rpn80sR4KCgpwwQUX4KmnngLLssHjoo1HgeSmyfaNifcJANxxxx1YuXJl0naSGU/43DfRxtZE/SNAvHFRZIpCRRLS1tZGi4uL6fTp0+lLL71Ejx8/Tg8dOkQfe+wx2tDQQCmltKKigj744IO0r68v7GW1WimllN5000309ttvpxqNhnZ0dITZBkDLysroww8/HPa9jzzyCC0vL6cA6OWXX07Xrl0btLt371560UUX0bKysrBzbDYbzcrKovfccw89//zzI67l+uuvD7MTeI2MjNCBgQGak5NDr7/+erpnzx7a2tpK33vvPXr77bcHy3zixAlaWFhIGxsb6ZYtW+iRI0fo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OBxR7W7atInq9frg311dXXTx4sW0tLSUulwueu6559KHH3447Jz/+7//o0VFRWHX8NOf/jT4t9VqpYQQ+u9//5tSSmlbWxsFQPfu3Rv1Oyml9JVXXqGJhqRk6kBERESEUkrFGRwRkUnk8ssvR29vL1577TWsWbMG27Ztw7x587B58+a459lsNtx9992YPn06DAYDtFotjh07lnD2Yvfu3di8eXNw9kir1WLNmjVgWTZu0PDY2Bi0Wi00Gg3Kysrgdrvx8ssvQy6XY/fu3XjwwQfDbN58883o6+uD3W4P2pg9e3bw3xqNBjqdDoODg8lVVBrrQERERAQQg4xFRCYdpVKJCy64ABdccAF+/vOf49vf/jbuu+8+3HDDDTHPueuuu/D222/j17/+NWpra6FSqXDFFVfA7XbH/S6WZXHrrbfi+9//fsRn5eXlMc/T6XTYs2cPGIZBQUEBNBpNmM0HHngAl112WdRrCyCTycI+I4SAZdmo38cwDOgEnV+PxxP2t9A6EBEREQFEB0dE5JQzffr0sG3hMpkMPp8v7JiPP/4YN9xwA772ta8B4OJR2tvbw46Ry+UR582bNw+HDx9GbW0trzIxDBPznHnz5uH48eO8bcYjLy8PFosFNpst6ExNzJGTTB2IiIiIxEJcohIRmSRMJhNWr16NZ599FgcOHEBbWxteeuklPProo7j00kuDx1VWVuK9995Df38/zGYzAKC2thYvv/wy9u3bh/379+Paa6+NmA2prKzERx99hJ6eHgwPDwMA7rnnHnz66ae47bbbsG/fPjQ3N+O1117Dhg0bBF/Hz3/+czzzzDO4//77cfjwYRw9ehRbtmzBT3/6U8E2Fy1aBLVajR//+MdoaWnB888/H7Fsl0wdiIiIiMRCdHBERCYJrVaLRYsW4be//S2WL1+OmTNn4mc/+xluvvlm/OEPfwge99hjj+Hdd99FWVkZ5s6dCwD47W9/i+zsbCxZsgQXX3wx1qxZg3nz5oXZf/DBB9He3o6amhrk5eUB4OJgPvzwQzQ3N+Pcc8/F3Llz8bOf/QxFRUWCr2PNmjV444038O6772LBggVYvHgxfvOb36CiokKwzZycHDz77LP417/+hVmzZuHvf/877r///rBjkqkDERERkVgQOnEhXERERCTNHD9+HI2NjWhubk7rUpeIiIhILMQZHBERkUllZGQE//jHP5CVlYWysrLTXRwREZEvCWKQsYiIyKRy0003Yffu3XjiiSegUChOd3FERES+JIhLVCIiIiIiIiJTDnGJSkRERERERGTKITo4IiIiIiIiIlMO0cERERERERERmXKIDo6IiIiIiIjIlEN0cERERERERESmHKKDIyIiIiIiIjLlEB0cERERERERkSmH6OCIiIiIiIiITDn+P+htvQiVPvZDAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 640x480 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "cmap = sns.cubehelix_palette(start=.5, rot=-.75, as_cmap=True)\n",
    "\n",
    "plt.scatter(df_pengiriman_state['seller_state'], df_pengiriman_state['customer_state'], c=df_pengiriman_state['lama_pengiriman_hari'], cmap=cmap, s=100)\n",
    "plt.xlabel('State Penjual')\n",
    "plt.ylabel('State Pembeli')\n",
    "\n",
    "plt.colorbar(label='Lama Pengiriman (Hari)')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "6bb56dcd",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:32.659331Z",
     "iopub.status.busy": "2023-10-18T10:08:32.658953Z",
     "iopub.status.idle": "2023-10-18T10:08:32.922245Z",
     "shell.execute_reply": "2023-10-18T10:08:32.920948Z"
    },
    "papermill": {
     "duration": 0.299124,
     "end_time": "2023-10-18T10:08:32.924634",
     "exception": false,
     "start_time": "2023-10-18T10:08:32.625510",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAgMAAAG1CAYAAABkoPeiAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8qNh9FAAAACXBIWXMAAA9hAAAPYQGoP6dpAAAfyElEQVR4nO3dfVSUdf7/8dcYKt5mmmZmtpU/FBEEUzBvKjGz+9ays21qHbWycLMbXLA0rTyFVogK4k2ZbrVurOa61mZlap066y1yXLewNMFCUyrv8oY7+fz+4DBfZzXldkDez8c5niPXXHPNZ94zzTy9BsjjnHMCAABm1avpBQAAgJpFDAAAYBwxAACAccQAAADGEQMAABhHDAAAYBwxAACAcQFl2SkjI0POOdWvX7+61wMAAKpIYWGhPB6PIiIizrpfmc4MOOdUVb+byDmngoKCKjve+Yo5lGAOJZhDCebADEoxhxKVnUNZ37/LdGag9IxAaGhohRZzquPHjyszM1MdO3ZU48aNK3288xVzKMEcSjCHEsyBGZRiDiUqO4dt27aVaT++ZwAAAOOIAQAAjCMGAAAwjhgAAMA4YgAAAOOIAQAAjCMGAAAwjhgAAMA4YgAAAOOIAQAAjCMGAAAwjhgAAMA4YgAAAOOIAQAAjCMGAAAwjhgAAMA4YgAAAOOIAQAAjCMGAAAwjhgAAMA4YgAAAOOIAQAAjCMGAAAwjhgAAMA4YgAAAOOIAQAAjCMGAAAwjhgAAMA4YgAAAOOIAQAAjCMGAAAwjhgAAMA4YgAAAOMCanoB/uScU35+frn2lySPx1Pu22rYsGGFrgcAgL+ZioH8/Hzde++9frmtJUuWKDAw0C+3BQBAZfAxAQAAxpk6M3CqJv/v9/LU++2774qLdGzH8jLte6brAABwvjAbA556AWV6gy/vvgAAnG/4mAAAAOOIAQAAjCMGAAAwjhgAAMA4YgAAAOOIAQAAjCMGAAAwjhgAAMA4YgAAAOOIAQAAjCMGAAAwjhgAAMA4YgAAAOOIAQAAjCMGAAAwjhgAAMA4YgAAAOOIAQAAjCMGAAAwjhgAAMA4YgAAAOOIAQAAjCMGAAAwjhgAAMA4YgAAAOOIAQAAjCMGAAAwjhgAAMA4YgAAAOOIAQAAjCMGAAAwjhgAAMA4YgAAAOOIAQAAjCMGAAAwjhgAAMA4YgAAAOOIAQAAjCMGAAAwjhgAAMA4YgAAAOOIAQAAjCMGAAAwjhgAAMA4YgAAAOOIAQAAjCMGAAAwjhgAAMA4YgAAAOOIAQAAjCMGAAAwjhgAAMA4YgAAAOOIAQAAjCMGAAAwjhgAAMA4YgAAAOOIAQAAjCMGAAAwjhgAAMA4YgAAAOOIAQAAjCMGAAAwjhgAAMA4YgAAAOOIAQAAjCMGAAAwjhgAAMA4YgAAAONqPAacc3LO1fQy6hRmCgAojxqNAeec4uPjFR8fz5tXFWGmAIDyCqjJG8/Pz1dmZqb374GBgTW5nDqBmQIAyqvGPyYAAAA1ixgAAMA4YgAAAOOIAQAAjCMGAAAwjhgAAMA4YgAAAOOIAQAAjCMGAAAwjhgAAMA4YgAAAOOIAQAAjCMGAAAwjhgAAMA4YgAAAOOIAQAAjCMGAAAwjhgAAMA4YgAAAOOIAQAAjCMGAAAwjhgAAMA4YgAAAOOIAQAAjCMGAAAwjhgAAMA4YgAAAOOIAQAAjCMGAAAwjhgAAMA4YgAAAOOIAQAAjCMGAAAwjhgAAMA4YgAAAOOIAQAAjCMGAAAwjhgAAMA4YgAAAOOIAQAAjCMGAAAwjhgAAMA4YgAAAOOIAQAAjCMGAAAwjhgAAMA4YgAAAOOIAQAAjCMGAAAwjhgAAMA4YgAAAOOIAQAAjCMGAAAwjhgAAMA4YgAAAOOIAQAAjCMGAAAwjhgAAMA4YgAAAOOIAQAAjCMGAAAwjhgAAMA4YgAAAOOIAQAAjCMGAAAwjhgAAMA4YgAAAOOIAQAAjCMG6ri4uDjdcccdiouL827buHGjRo4cqY0bN5b7eJW5LiqP+Vccs0NtVRuem8RAHbZnzx5lZmZKkjIzM/XDDz8oLy9Pqamp+umnn5Samqq8vLwyH68y10XlMf+KY3aorWrLc5MYqMOeeeYZn69jY2O1dOlSHThwQJJ04MABLV26tMzHq8x1UXnMv+KYHWqr2vLcDKiRWz0Df9SQP4vrXLeVl5engoIC5eXlqV69qmuyU2/3xIkTPpedOHFCaWlp3q+dc1q6dKmio6PVrl27sx537969Wrp0qZxz5b4uKo/5VxyzQ21Vm56bNRoDpQOQpOHDh/v9tj3VcMxS/r4/FeWc09y5c/XCCy/I4znzREr3OfX+lfW6qDzmX3HMDrVVbXtu8jGBccXFxcrIyFBOTs5v7pOTk6OMjAwVFxeX+7qoPOZfccwOtVVte27W6JmBU6vn7bffVmBgYLXeXl5envdf7NVRXOW5P8ePH9c333yjTp06qXHjxlW2hlPvY1nUq1dP4eHhat++/W/u0759e0VERGjr1q0+T9yyXBeVx/wrjtmhtqptz81ac2YgMDDQL39q0/1p0KBBjd9Hj8ejRx999Kxx9Fv7lOW6qDzmX3HMDrVVbXtu1poYQNVr1KjRaV//4Q9/8D7JPB6PhgwZoksvvfScx2rXrp2GDBlSoeui8ph/xTE71Fa16blJDNRhCQkJPl8nJiZqyJAhatmypSSpZcuWGjJkSJmPV5nrovKYf8UxO9RWteW5SQzUYZdddpmCg4MlScHBwbr88ssVGBiomJgYtW7dWjExMeX6WKEy10XlMf+KY3aorWrLc7PW/J4BVI9XXnnltG2RkZGKjIys0PEqc11UHvOvOGaH2qo2PDc5MwAAgHHEAAAAxhEDAAAYRwwAAGAcMQAAgHHEAAAAxhEDAAAYRwwAAGAcMQAAgHHEAAAAxhEDAAAYRwwAAGAcMQAAgHHEAAAAxhEDAAAYRwwAAGAcMQAAgHHEAAAAxhEDAAAYRwwAAGAcMQAAgHHEAAAAxhEDAAAYRwwAAGAcMQAAgHHEAAAAxhEDAAAYRwwAAGAcMQAAgHHEAAAAxhEDAAAYRwwAAGAcMQAAgHHEAAAAxhEDAAAYRwwAAGAcMQAAgHHEAAAAxhEDAAAYRwwAAGAcMQAAgHHEAAAAxhEDAAAYRwwAAGAcMQAAgHHEAAAAxhEDAAAYRwwAAGAcMQAAgHHEAAAAxhEDAAAYRwwAAGAcMQAAgHHEAAAAxhEDAAAYRwwAAGAcMQAAgHHEAAAAxhEDAAAYRwwAAGAcMQAAgHHEAAAAxhEDAAAYRwwAAGAcMQAAgHHEAAAAxhEDAAAYF1CTN96wYUMFBwd7/47KY6YAgPKq0RjweDyaNm2a9++oPGYKACivGo0BiTes6sBMAQDlwfcMAABgHDEAAIBxxAAAAMYRAwAAGEcMAABgHDEAAIBxxAAAAMYRAwAAGEcMAABgHDEAAIBxxAAAAMYRAwAAGEcMAABgHDEAAIBxxAAAAMYRAwAAGEcMAABgHDEAAIBxxAAAAMYRAwAAGEcMAABgHDEAAIBxxAAAAMYRAwAAGEcMAABgHDEAAIBxxAAAAMYRAwAAGEcMAABgHDEAAIBxxAAAAMYRAwAAGEcMAABgHDEAAIBxxAAAAMYRAwAAGEcMAABgHDEAAIBxxAAAAMYRAwAAGEcMAABgHDEAAIBxxAAAAMYRAwAAGEcMAABgHDEAAIBxxAAAAMYRAwAAGEcMAABgHDEAAIBxxAAAAMYRAwAAGEcMAABgHDEAAIBxxAAAAMYRAwAAGEcMAABgHDEAAIBxxAAAAMYRAwAAGEcMAABgHDEAAIBxxAAAAMYRAwAAGEcMAABgHDEAAIBxxAAAAMYRAwAAGEcMAABgXEBNL6CmuOKiMl9+rn3Lux8AALWJ2Rg4tmN5tewLAMD5ho8JAAAwztSZgYYNG2rJkiVl3t85J0nyeDwVui0AAM4HpmLA4/EoMDCwppcBAECtwscEAAAYRwwAAGAcMQAAgHHEAAAAxhEDAAAYRwwAAGAcMQAAgHHEAAAAxhEDAAAYRwwAAGAcMQAAgHHEAAAAxhEDAAAYRwwAAGAcMQAAgHHEAAAAxhEDAAAYRwwAAGAcMQAAgHHEAAAAxhEDAAAYRwwAAGAcMQAAgHHEAAAAxhEDAAAYRwwAAGAcMQAAgHHEAAAAxhEDAAAYRwwAAGAcMQAAgHHEAAAAxhEDAAAY53HOuXPttGXLFjnn1KBBg0rfoHNOhYWFql+/vjweT6WPd75iDiWYQwnmUII5MINSzKFEZedQUFAgj8ej7t27n3W/gLIcrCofCI/HUyVRcb5jDiWYQwnmUII5MINSzKFEZefg8XjK9B5epjMDAACg7uJ7BgAAMI4YAADAOGIAAADjiAEAAIwjBgAAMI4YAADAOGIAAADjiAEAAIwjBgAAMI4YAADAOGIAAADjiAEAAIzzawwUFxdr1qxZ6tevn7p166aRI0dq9+7d/lyC3x06dEiTJk3Sddddp+7du+uPf/yjNm/e7L08MzNTw4YNU3h4uG644QYtWLCgBlfrH1lZWYqIiNCyZcu82yzNYfny5br11lsVGhqq2267TStXrvReZmUOhYWFSkpK0g033KCIiAjdf//92rJli/fyuj6H1NRUDR8+3Gfbue5zXXz9PNMc1qxZo3vuuUcRERGKjo7WtGnTlJeX573cyhxONXHiREVHR/tsq/I5OD9KTk521157rfvss89cZmamGzlypBs4cKDLz8/35zL8asSIEe7OO+90mzZtct99952bMmWKCwsLczt37nQHDhxwUVFRbsKECW7nzp1u6dKlLjQ01C1durSml11tCgoK3N133+2CgoLce++955xzpuawfPlyFxwc7BYtWuSys7NdSkqK69y5s9uyZYupOcycOdP16dPHffHFFy47O9tNmDDBde/e3e3bt6/Oz2HhwoWuU6dObtiwYd5tZbnPde3180xz2LRpkwsODnbz5s1z2dnZ7vPPP3fXX3+9Gz9+vHcfC3M41apVq1xQUJDr37+/z/aqnoPfYiA/P99FRES4xYsXe7cdPnzYhYWFuQ8++MBfy/Cr7OxsFxQU5NLT073biouL3cCBA92MGTPc3LlzXb9+/VxhYaH38sTERDdo0KCaWK5fJCYmuuHDh/vEgJU5FBcXu/79+7upU6f6bB85cqSbO3eumTk459ydd97pEhISvF//+uuvLigoyH300Ud1dg779u1zo0aNcuHh4e7mm2/2efE/132uS6+fZ5tDbGysGzFihM/+y5cvd126dHH5+flm5lBq//79rlevXm7YsGE+MVAdc/DbxwTbt2/XsWPH1KtXL++25s2bq0uXLtq0aZO/luFXF110kebPn6+uXbt6t3k8HjnndPjwYW3evFk9e/ZUQECA9/JevXopKytLv/zyS00suVpt2rRJaWlpmjZtms92K3PYtWuX9uzZozvuuMNn+4IFCzR69Ggzc5CkFi1aaO3atcrJydHJkyeVlpamBg0aKDg4uM7O4auvvtKFF16oFStWqFu3bj6Xnes+16XXz7PNYeTIkYqLizvtOkVFRTp69KiZOUiSc07jx4/XXXfdpcjISJ/LqmMOfouBffv2SZIuvfRSn+1t2rTRjz/+6K9l+FXz5s11/fXXq0GDBt5tK1eu1Pfff6++fftq3759atu2rc912rRpI0nau3evX9da3Y4cOaK4uDhNnDjxtOeAlTlkZ2dLko4fP65Ro0bp2muv1b333qs1a9ZIsjMHSZowYYICAgI0YMAAhYaGKikpSTNmzFCHDh3q7Byio6OVmJioyy+//LTLznWf69Lr59nm0KVLF3Xu3Nn7dUFBgRYuXKiQkBC1bNnSzBwkadGiRfrpp5/09NNPn3ZZdczBbzFw4sQJSfJ5Y5Skhg0bKj8/31/LqFHp6el69tlnNWDAAEVHRysvL++M85BU52by/PPPKzw8/LR/FUsyM4ejR49KkuLj43X77bfrzTff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\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.set(style=\"whitegrid\")  \n",
    "sns.boxplot(x=df_pengiriman_state['lama_pengiriman_hari'])\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "18aa9093",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:32.991432Z",
     "iopub.status.busy": "2023-10-18T10:08:32.991047Z",
     "iopub.status.idle": "2023-10-18T10:08:33.004583Z",
     "shell.execute_reply": "2023-10-18T10:08:33.003218Z"
    },
    "papermill": {
     "duration": 0.05043,
     "end_time": "2023-10-18T10:08:33.006893",
     "exception": false,
     "start_time": "2023-10-18T10:08:32.956463",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>lama_pengiriman_hari</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>412.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>14.035265</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>9.258877</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>9.748715</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>12.960246</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>16.925000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>138.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       lama_pengiriman_hari\n",
       "count            412.000000\n",
       "mean              14.035265\n",
       "std                9.258877\n",
       "min                1.000000\n",
       "25%                9.748715\n",
       "50%               12.960246\n",
       "75%               16.925000\n",
       "max              138.000000"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_pengiriman_state.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "9a074b87",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:33.075609Z",
     "iopub.status.busy": "2023-10-18T10:08:33.075037Z",
     "iopub.status.idle": "2023-10-18T10:08:33.084165Z",
     "shell.execute_reply": "2023-10-18T10:08:33.082965Z"
    },
    "papermill": {
     "duration": 0.045789,
     "end_time": "2023-10-18T10:08:33.086235",
     "exception": false,
     "start_time": "2023-10-18T10:08:33.040446",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "27.689427166400844"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Q1 = (df_pengiriman_state['lama_pengiriman_hari']).quantile(0.25)\n",
    "Q3 = (df_pengiriman_state['lama_pengiriman_hari']).quantile(0.75)\n",
    "IQR = Q3 - Q1\n",
    " \n",
    "maximum = Q3 + (1.5*IQR)\n",
    "maximum"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "b0bb787e",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:33.158107Z",
     "iopub.status.busy": "2023-10-18T10:08:33.157668Z",
     "iopub.status.idle": "2023-10-18T10:08:33.169242Z",
     "shell.execute_reply": "2023-10-18T10:08:33.168140Z"
    },
    "papermill": {
     "duration": 0.050453,
     "end_time": "2023-10-18T10:08:33.171379",
     "exception": false,
     "start_time": "2023-10-18T10:08:33.120926",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>seller_state</th>\n",
       "      <th>customer_state</th>\n",
       "      <th>lama_pengiriman_hari</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>SP</td>\n",
       "      <td>RR</td>\n",
       "      <td>27.030303</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  seller_state customer_state  lama_pengiriman_hari\n",
       "9           SP             RR             27.030303"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_pengiriman_state[df_pengiriman_state['lama_pengiriman_hari'] <= 27.69].head(1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "befe6516",
   "metadata": {
    "papermill": {
     "duration": 0.032778,
     "end_time": "2023-10-18T10:08:33.238718",
     "exception": false,
     "start_time": "2023-10-18T10:08:33.205940",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "paket antar state yang paling lama dikirimkan adalah dalam waktu 138 hari, yaitu dari state CE ke AM. Namun, data ini merupakan data outlier sehingga dimungkinkan terjadi error saat input data. Adapun maximum yang tidak termasuk outlier adalah 27.69 hari yaitu dari state SP ke state RR."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ab3ed4a4",
   "metadata": {
    "papermill": {
     "duration": 0.033921,
     "end_time": "2023-10-18T10:08:33.304975",
     "exception": false,
     "start_time": "2023-10-18T10:08:33.271054",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "### pengiriman antar kota"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "e3f4cbc9",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:33.376249Z",
     "iopub.status.busy": "2023-10-18T10:08:33.374900Z",
     "iopub.status.idle": "2023-10-18T10:08:33.422285Z",
     "shell.execute_reply": "2023-10-18T10:08:33.421269Z"
    },
    "papermill": {
     "duration": 0.086717,
     "end_time": "2023-10-18T10:08:33.425413",
     "exception": false,
     "start_time": "2023-10-18T10:08:33.338696",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>seller_city</th>\n",
       "      <th>customer_city</th>\n",
       "      <th>lama_pengiriman_hari</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>belo horizonte</td>\n",
       "      <td>montanha</td>\n",
       "      <td>195.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>uberaba</td>\n",
       "      <td>lagarto</td>\n",
       "      <td>194.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>aracatuba</td>\n",
       "      <td>aracaju</td>\n",
       "      <td>187.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>farroupilha</td>\n",
       "      <td>paulinia</td>\n",
       "      <td>186.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>itajobi</td>\n",
       "      <td>perdizes</td>\n",
       "      <td>182.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>35429</th>\n",
       "      <td>santa barbara d oeste</td>\n",
       "      <td>sao caetano do sul</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>35430</th>\n",
       "      <td>sando andre</td>\n",
       "      <td>sao bernardo do campo</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>35431</th>\n",
       "      <td>belo horizonte</td>\n",
       "      <td>setubinha</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>35432</th>\n",
       "      <td>cajamar</td>\n",
       "      <td>limeira</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>35433</th>\n",
       "      <td>osasco</td>\n",
       "      <td>sertaozinho</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>35434 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                 seller_city          customer_city  lama_pengiriman_hari\n",
       "0             belo horizonte               montanha                 195.0\n",
       "1                    uberaba                lagarto                 194.0\n",
       "2                  aracatuba                aracaju                 187.0\n",
       "3                farroupilha               paulinia                 186.0\n",
       "4                    itajobi               perdizes                 182.0\n",
       "...                      ...                    ...                   ...\n",
       "35429  santa barbara d oeste     sao caetano do sul                   1.0\n",
       "35430            sando andre  sao bernardo do campo                   1.0\n",
       "35431         belo horizonte              setubinha                   1.0\n",
       "35432                cajamar                limeira                   1.0\n",
       "35433                 osasco            sertaozinho                   1.0\n",
       "\n",
       "[35434 rows x 3 columns]"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_pengiriman_city = cust_seller.groupby(['seller_city', 'customer_city'])['lama_pengiriman_hari'].mean().sort_values(ascending=False).reset_index()\n",
    "df_pengiriman_city"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "d717529f",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:33.496200Z",
     "iopub.status.busy": "2023-10-18T10:08:33.494940Z",
     "iopub.status.idle": "2023-10-18T10:08:33.767110Z",
     "shell.execute_reply": "2023-10-18T10:08:33.766072Z"
    },
    "papermill": {
     "duration": 0.308857,
     "end_time": "2023-10-18T10:08:33.769301",
     "exception": false,
     "start_time": "2023-10-18T10:08:33.460444",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.set(style=\"whitegrid\")  # Mengatur gaya plot\n",
    "\n",
    "sns.boxplot(x=df_pengiriman_city['lama_pengiriman_hari'])\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "b5ca551d",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:33.839701Z",
     "iopub.status.busy": "2023-10-18T10:08:33.838808Z",
     "iopub.status.idle": "2023-10-18T10:08:33.849170Z",
     "shell.execute_reply": "2023-10-18T10:08:33.848322Z"
    },
    "papermill": {
     "duration": 0.047935,
     "end_time": "2023-10-18T10:08:33.851278",
     "exception": false,
     "start_time": "2023-10-18T10:08:33.803343",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "24.25"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Q1 = (df_pengiriman_city['lama_pengiriman_hari']).quantile(0.25)\n",
    "Q3 = (df_pengiriman_city['lama_pengiriman_hari']).quantile(0.75)\n",
    "IQR = Q3 - Q1\n",
    " \n",
    "maximum = Q3 + (1.5*IQR)\n",
    "maximum"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "4f403329",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:33.920710Z",
     "iopub.status.busy": "2023-10-18T10:08:33.919684Z",
     "iopub.status.idle": "2023-10-18T10:08:33.933166Z",
     "shell.execute_reply": "2023-10-18T10:08:33.932140Z"
    },
    "papermill": {
     "duration": 0.050564,
     "end_time": "2023-10-18T10:08:33.935256",
     "exception": false,
     "start_time": "2023-10-18T10:08:33.884692",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>seller_city</th>\n",
       "      <th>customer_city</th>\n",
       "      <th>lama_pengiriman_hari</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1768</th>\n",
       "      <td>sao jose dos campos</td>\n",
       "      <td>belem</td>\n",
       "      <td>24.25</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              seller_city customer_city  lama_pengiriman_hari\n",
       "1768  sao jose dos campos         belem                 24.25"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_pengiriman_city[df_pengiriman_city['lama_pengiriman_hari'] <= 24.25].head(1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7f8afa79",
   "metadata": {
    "papermill": {
     "duration": 0.033585,
     "end_time": "2023-10-18T10:08:34.002272",
     "exception": false,
     "start_time": "2023-10-18T10:08:33.968687",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "paket antar kota yang paling lama dikirimkan adalah dalam waktu 195 hari, yaitu dari kota belo horizonte ke kota montanha. Namun, data ini merupakan data outlier sehingga dimungkinkan terjadi error saat input data. Adapun hari maximum yang tidak termasuk outlier untuk pengiriman antarkota adalah 24.3 hari yaitu dari kota sao jose dos campos ke kota belem."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "79d8fd22",
   "metadata": {
    "papermill": {
     "duration": 0.03491,
     "end_time": "2023-10-18T10:08:34.070521",
     "exception": false,
     "start_time": "2023-10-18T10:08:34.035611",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## Pertanyaan 3: Berapa rata-rata payment value dari tiap tipe transaksi? dan transaksi tipe apa yang paling sering digunakan?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "c10aeed1",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:34.139810Z",
     "iopub.status.busy": "2023-10-18T10:08:34.139211Z",
     "iopub.status.idle": "2023-10-18T10:08:34.156500Z",
     "shell.execute_reply": "2023-10-18T10:08:34.155335Z"
    },
    "papermill": {
     "duration": 0.054545,
     "end_time": "2023-10-18T10:08:34.158884",
     "exception": false,
     "start_time": "2023-10-18T10:08:34.104339",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>payment_type</th>\n",
       "      <th>payment_value</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>boleto</td>\n",
       "      <td>144.934140</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>credit_card</td>\n",
       "      <td>163.022616</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>debit_card</td>\n",
       "      <td>140.778868</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>voucher</td>\n",
       "      <td>66.913499</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  payment_type  payment_value\n",
       "0       boleto     144.934140\n",
       "1  credit_card     163.022616\n",
       "2   debit_card     140.778868\n",
       "3      voucher      66.913499"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_payment = orders.groupby(by=\"payment_type\")[\"payment_value\"].mean().reset_index()\n",
    "df_payment"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "21ad36b5",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:34.227945Z",
     "iopub.status.busy": "2023-10-18T10:08:34.227241Z",
     "iopub.status.idle": "2023-10-18T10:08:34.474053Z",
     "shell.execute_reply": "2023-10-18T10:08:34.472904Z"
    },
    "papermill": {
     "duration": 0.28496,
     "end_time": "2023-10-18T10:08:34.477590",
     "exception": false,
     "start_time": "2023-10-18T10:08:34.192630",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA1YAAAHICAYAAABNr3txAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8qNh9FAAAACXBIWXMAAA9hAAAPYQGoP6dpAABh4klEQVR4nO3dZ3gUZf/28XMpIaGEKkV6cRNCGpDQEQgg3KAooDegQekIAkoHKQKCgKAQqoI0KdJFpIPUvxQpUoQghiZIlRJKejLPC57szZKA2WxINub7OQ4P2WtmZ367O9dkz5lrZk2GYRgCAAAAACRbprQuAAAAAADSO4IVAAAAANiJYAUAAAAAdiJYAQAAAICdCFYAAAAAYCeCFQAAAADYiWAFAAAAAHYiWAEAAACAnQhWAAAAAGAnghUAhzB16lS5ublpxYoVaV0KJAUEBMjNzU0xMTEpvuy2bdvKzc1NFy9etLS5ubnp5ZdfTvF12cIRt0FHrCkpHOHzfJpBgwbJzc1Ne/fuTetSnms/S6rVq1fLzc1NkyZNStX1Xr58WW5ubmrTpk2qrhd4nrKkdQEAAPTo0UM5c+ZM6zKAVPXuu+/q/v37ypQp4x3ndnV1VY8ePVSkSJG0LgVIMQQrAECa69mzZ1qXAKS6du3apXUJacbV1ZV+j3+djHeIBAAAAABSGMEKSKfirxO4dOmSRo8erRo1aqhixYpq1aqVNm/enOhzzp49q759+6pmzZry9PRU/fr1NX78eIWGhlrNF39dx44dO9S+fXt5enqqdu3aOnbsmCRp69atatu2rapXry5vb281btxYX3zxhe7fv5/sdcaLjY3VtGnTVK9ePXl5eem1117TwoULFRcXl2De/fv3q0ePHqpVq5Y8PT1VuXJltWrVSqtWrbKa78CBA3Jzc9OsWbM0cuRIVaxYUVWqVNGiRYskSZGRkZo3b55atWolPz8/eXp6qlatWvroo4/0+++/J/q+X79+XRMnTlS9evXk6emphg0bavr06Um6ViL+mob169dr0aJFeuWVVyzv46xZsxJdxt27dzV+/Hg1aNBAnp6eqlGjhvr06aOzZ88m+lrnz5+vjRs3qkWLFvL29latWrU0fvx4RUVF6erVq+rdu7f8/f1VtWpVde3a1ep6p8ddvnxZPXr0UMWKFVW5cmV16dJFx48fT3TeXbt2qV27dvLz85O3t7def/31p352T0rsmpz79+9r6tSpeuONN1SxYkV5enqqbt26Gjx4sP766y+redu2bSs/Pz/duXNHw4cPV61ateTl5aVXX31Vixcv/sf1P86WbfDatWsaPny46tSpI09PT7388ssaNmyYrl+/bjVf/Ge+evVqffTRR/L29lb16tW1detWSVJMTIxmzZqlxo0by9vbW40aNbJsn4k5efKk+vXrp7p168rT01MVK1bUG2+8oblz5yo2NtZq3r/++ksDBgywbDs1a9ZUr1699NtvvyVY7sWLFzV8+HA1bNhQ3t7e8vHxUZMmTTR58mRFRERYzevm5qauXbtq2bJlqlGjhnx9fdWvX7+n1rxr1y7LtnvmzBlL+40bNzRu3Dg1adJEvr6+8vLyUsOGDTV69GjduXPHahkBAQF6/fXX9ddff6lv376qWrWqvL291bJlS23YsOGp605MWFiYPvvsM9WsWVM+Pj568803tXbt2kTn3bJlizp27Kjq1aurQoUK8vf317vvvquffvopwbyRkZGaOnWqpV83atRI8+fP15o1ayzbwOOv58lrrFJ7f/S477//Xs2bN5e3t7eqVaum3r17J+hrUtK3v/jrqEaNGqVp06bJz89PlSpV0sSJE7nGCv9KDAUE0rmPPvpIFy9e1KuvvqqYmBht2bJFvXr1Uv/+/dWpUyfLfPv371e3bt0UHR2tBg0aqFixYgoODtbcuXO1fft2fffdd8qXL5/VsocOHapChQrp3Xff1R9//KHy5ctr48aN6t27t4oVK6amTZvKyclJhw4d0qxZs3To0CEtWbJEJpMp2eucNm2a7t+/r6ZNmypbtmzavn27Ro8erdOnT2vMmDGW+VauXKmhQ4eqQIECCggIkKurq/78809t375dH3/8scLDwxUYGGi17AULFshkMql169a6dOmSfH19FRcXp86dO+vAgQOqVKmS3nzzTcXGxurIkSPauHGjdu/erY0bN6pQoUJWy/rggw/0119/qWHDhnJyctKGDRs0ZcoUhYeHP/PL5ePmzp2rU6dOqXHjxqpTp452796tL774QkeOHNHMmTMt7+ONGzf09ttv69KlS6patapeeeUV3bx5U5s2bdKOHTv0zTffqHLlylbL/uGHH/THH3+oUaNG8vf316ZNmzR37lzdvn1be/fuVeHChfXmm2/q5MmT2rlzp/7880/9+OOPypLF+s9CYGCgcuTIodatW+vKlSvaunWr9u7dq9mzZ6t69eqW+WbPnq2JEycqX758atSokVxdXfV///d/Gj16tA4ePKigoCDL60mKsLAwtW7dWmfPnlXNmjVVs2ZNRUREaO/evVq9erX27dunjRs3ysXFxfKcmJgYtW3bVmFhYWrUqJGio6O1bt06jRo1SpkyZUryF7ikboN//PGH3n33Xd25c0d169ZV2bJl9eeff2rlypXavn27Fi1apNKlS1st+4svvlCOHDkUGBioM2fOyNfXV4Zh6IMPPtDOnTtVpkwZtWrVSteuXdOYMWOUP3/+BPX93//9n95//325uLioQYMGKlCggK5du6Zt27Zp/PjxunnzpgYOHChJun37tt59913dvHlTr7zyil588UX99ddf2rx5s3bu3Knly5fL3d1dknT69Gm98847iomJUYMGDfTiiy/q9u3b2rZtm2bOnKlz585pypQpVrWcOHFC+/bt0xtvvCHDMOTh4ZHoe7pv3z717NlTefLk0fz581WuXDlJ0vXr19WyZUvduXNH9erVU0BAgO7fv6+dO3dq4cKFOnLkiFUQkR4dZGjVqpVy586t119/XaGhoVq/fr169+6tnDlzJvmmGSNGjFBUVJSaNGmimJgYbd26Vf3799fly5fVvXt3y3xTpkzR9OnTVaJECTVp0kTOzs4KCQnRrl27dODAAc2cOVMBAQGSHm2DHTt21MGDB2U2m9WmTRtdu3ZN48ePV7Fixf6xprTcH61cuVKhoaFq0KCBqlevrgMHDmjDhg06evSo1q9fr+zZs0uybfuLt3nzZkVGRuqNN97Q3bt35evrm6SagHTHAJAuDRw40DCbzYa/v79x8eJFS/uff/5p1KpVy6hQoYLx559/GoZhGBEREUbNmjUNX19f4+TJk1bLWbJkiWE2m40+ffpY2qZMmWKYzWYjICDAiIiIsJq/efPmhq+vr3H//n1LW1xcnNGuXTvDbDYbR44csWudFSpUMH777TdL++3bt41mzZoZZrPZOHDggGEYhhEVFWVUqVLFqFGjhnHr1i2rZe/atcswm81GixYtLG379+83zGaz4e7uboSEhFjNv2nTJsNsNhuDBg1K8B5/9NFHhtlsNhYtWpTgfX/llVeMO3fuWNovXrxoeHh4GH5+fkZUVFSCZT1u1apVhtlsNsxms7FlyxZLe1hYmPHee+8ZZrPZ+OGHHyzt3bt3N8xms7Fs2TKr5Zw6dcrw8vIy6tWrZ0RHR1u9VrPZbPz000+WeUNCQiztffv2NeLi4gzDePTZtWnTxuqzMwzDqFevnmE2m402bdpYbQN79uwxypcvb9SvX9+IjY01DMMwTp48abi7uxuvvvqqcfv2bcu8sbGxRp8+fRLUHhgYaJjNZuPChQuWNrPZbNSuXdvyeM6cOYbZbDamTp1q9ZpjY2ONVq1aGWaz2dixY0eCZbZp08YICwuztP/yyy+G2Ww2mjRpkuhn8ThbtkHDMIw33njDcHd3N3bt2mW1nJ07dxpms9lo1aqVpS3+M69YsWKCbfaHH34wzGaz0bFjR6v3eufOnYa7u7thNpuN5cuXW9pfffVVw9PT0zh37pzVckJCQgw3NzejatWqlraFCxcmeL5hGMaaNWsMs9lsDBs2zNLWtWtXw2w2G7/88ovVvH///bdRqVIlw93d3arfx29PS5cuTfBePv55/vLLL4aPj49Rs2ZN4+zZs1bzjRo1yjCbzcb3339v1R4eHm4EBAQYZrPZOHPmjKU9frv86KOPLNu8YRjG999/b5jNZqNz584JanlSfB+uUqWKcfnyZUv75cuXjZdfftkoX768ZZ968+ZNw8PDw2jatKnVdmUY/9uP9ezZ09I2f/58S9vj9cXvZ8xms7Fq1aoEryd+3rTcH3l4eBiHDh2ytMfGxlr2DZs2bbK027L9Xbp0yfK69+zZYzV//LTWrVs/sz4gPWEoIJDOdejQQSVKlLA8Ll68uLp06WI5Wi9J27dv182bN9WmTZsER5TbtGmjUqVKadOmTXrw4IHVtICAAGXLli3BOiMiInTixAnLY5PJpC+++EL79u1TxYoV7Vrnm2++qQoVKlge582bVx999JGkR2dhpEdDtUaOHKnx48cnOONVrVo1SUowhEiSzGazypYta9Xm5uamzz77TL169Uowf/yybt++nWBa69atlSdPHsvjEiVKqGzZsrp3716i605MzZo11bBhQ8tjFxcXDR48WNKjITmS9Pfff+unn36Sl5eX/vvf/1o9v3z58pZhUT///LPVtLJly1qOosc/jq+3U6dOlrNHJpPJ8pklNuRn0KBBVttArVq11KBBA126dElHjhyRJK1YsUJxcXHq16+f8ubNa5k3U6ZMGjBggGUeW9SoUUOjRo1KcHF/pkyZVKVKFUmJfy7t2rWzOovl7++vXLlyPXWoY2KSsg0eP35cp06d0iuvvJLgDEmdOnVUs2ZN/frrrwmGalarVi3BNhu/zP79+1u913Xq1LHaPiTJMAx9+OGH+uKLLxKcDStbtqwKFChgtf0ZhiFJOnbsmKKjoy3tTZo00bZt2zR8+HBLW9u2bTV+/Hj5+/tbLTd//vx66aWXFBcXp7t37+pJjRs3TtAW7+jRo+rSpYtcXV21cOFClSlTxmp606ZNNXLkSDVr1syq3dnZ2XJWI7HPuVOnTlZnV+vVqydJNn3OnTp1UtGiRS2PixYtqs6dOys2Ntay78ySJYs+//xzffrpp1bblZT4vmb16tXKnDmzBg8ebFVfo0aNVLVq1X+sKS33R7Vr17Y6850pUybLPiT+fbV1+4vn6uqqmjVrJqkOID1jKCCQzj0+HCtepUqVJEmnTp2SJEsIOn/+vKZOnZpg/syZMysmJka///671R/W4sWLJ5j37bff1pAhQ9SuXTuVKVNGNWvWVK1atVStWjU5Oztb5kvuOv38/BLMG/8FK/71ODs7W77M/fXXXwoJCdHly5d1/vx5HT16VJISXGfytNdTqlQplSpVStHR0Tp16pQuXLigy5cv68yZM9q/f/9Tl1WqVKkEba6urpJk9QX2WeK/KD3Ozc1NOXLksLzWkydPyjAMRUVFJfo+Xrt2TdKj96ZOnTrPrC9Hjhy6e/euVRCXZPncoqKirNqdnJzk5eWVYDm+vr7avHmzTp06JT8/P8tnvWfPnkSvv3J2dlZwcLAMw0jycEB3d3e5u7srMjJSx48f14ULF3Tp0iX9/vvvNn8uuXLlSvT6v6dJyjYY/5pv3bqV6OcSFhYm6dHn93iYT2wbPHXqlLJnzy6z2ZxgWuXKla2umTSZTGrQoIEk6ebNmzpz5owuXbqkCxcu6MSJE7p165akR+9N5syZ1bhxY82YMUMrVqzQli1bVK1aNdWqVUu1a9dOUEv8F9+7d+/q999/159//qk///xTJ0+etFyP9eR1Zrlz51bu3LkT1C09ukauU6dOCgsLk6+vb4Iv4tKjfVWlSpX04MEDq3UGBwfrwIEDia5TSvg529r3pKR9znny5FHTpk0lSRcuXNDZs2d1+fJlnT17VocPH5b0v+0wKipKp0+f1osvvpjoLcT9/f0tr+lp0nJ/lNgy4g8CxG/Ptm5/8YoVK2bTUGAgvSJYAelc4cKFE7TF/x7QvXv3rP6/fft2bd++/anLevKGEk8eoZUeHc0vUKCAFi5cqAMHDmjhwoVauHChsmfPrtatW6tv377KkiVLstdZoECBBPPkyJFD0v/+uEvSr7/+qs8//9xy1iRTpkwqVaqU/P39deLECcuR+sc9HvziGYahefPmac6cOfr7778lSdmzZ5eHh4fKly+vmzdvJrqsxM7kxX9xSGz+xDzt91ty5sxpqSX+/fn9998TXLj+uCffx/jrIRLj5OSUpPoKFCiQ6JehJz+P+M964cKFz1zew4cPk/xbVVFRUZo2bZqWLFliCUWurq7y8vLSSy+9pEOHDiX6vGd9LkmVlG0w/jUfPHhQBw8efOqynvxcEtsG79+/rzx58iRa5+NnIeKdPXtW48eP1+7duy3bWvHixVW5cmX98ccfCg0NtbS/8MILWr16tb7++mtt27ZNmzdvtgS1atWqacSIEZbAE38Tic2bN1tuelCoUCFVqlRJhQoV0uXLlxNs24m9nnhhYWEqWLCgypQpo71792rFihV66623rOZ58OCBJkyYoDVr1lhujpEvXz75+PioRIkSOn36dJL6X3K+tCd1X7Nz5059+eWXlv6XJUsWlStXTl5eXgoJCbHUF3+m5oUXXkh0fU9eF5WYtNwfJbaMx+uKZ8v2F+9Z2wnwb0KwAtK5J+/UJf3vy1z80cb4LwuTJk1SkyZN7F5n3bp1VbduXYWHh+vIkSPas2eP1qxZo7lz58rV1VXdunVL9joTO7MQf4e1+CPjV69eVYcOHWQYhgYNGqTq1aurVKlScnZ2VmRkpJYtW5bk9S1YsEDjx49XhQoVNHLkSLm7u6to0aIymUz67rvvtHv37iQvy1aJfXaGYej+/fuWIXXx72ObNm00YsSI51ZLYuLDw5Oe/Dzia9y7d2+iN1tIjgkTJujbb79VjRo11L59e7m5uVm+mE6cOPGpwSolJGUbjH/N/fr1U+fOne1aX548efTgwYNEz+g9/gU//nG7du1069YtdevWTfXq1VPZsmUt9SQ23KpIkSIaMWKEPvnkE505c0b79u3TunXrtH//fr3//vvatGmTJKlLly4KDg7WO++8o6ZNm6pcuXKW1/vf//5Xly9ftul1Zc+eXYsWLZJhGGrWrJnGjx+vl19+2SpgDBgwQD/99JOaNGmiVq1a6aWXXrJsQ71799bp06dtWqctkvI5nzhxQt27d5erq6tGjx4tX19flSxZUk5OTjp79qxlyK70v23iaWdHnxz2nJi03B8lRXK2PyAj4RorIJ2LvwX64+LP4vj4+Eh6dC2OpKfeJnvGjBmaOXNmotdPPO7BgweaPn265s2bJ+nRGa2aNWtq0KBBluFQ8Ufvk7vOx6/dihc/5CZ+WNqWLVsUFhamDh06qH379nJ3d7ccEf3jjz8kJf0o7Zo1ayRJQUFBljsXxn+5DQkJSdIykiuxzy44OFhhYWFJ/uzWr1+vyZMnP5cvoA8ePND58+cTtMeHmvjPI77GxF7PgwcPNGbMmGfeOjwxa9asUbZs2TRz5swEX8bjP5ekfsa2Sso2GH/d4NM+l8WLF2vatGlJCiOenp4KDw9P9PbnT76ne/fu1Y0bN/Taa6/pww8/lLe3t+VL7e3bty3X38S/Nxs2bNAnn3yi+/fvy2Qyyc3NTe3atdOyZctUqlQpXbhwQTdu3NDvv/+u4OBg+fv7a/jw4apcubIlXERHR+vChQtWy02KXLlyqWTJkipVqpS6d++u+/fv65NPPrFMv3fvnrZv366iRYtq0qRJqlatmlUwT4vP+clt+8cff1RsbKz69++vt956Sy+99JLljO+T9eXMmVOlS5fWxYsXE73OKH6Y8rOk5f4oKWzd/oCMhmAFpHMzZsywDBmRHl1k/M033yhHjhyWawMaNGigPHnyaPHixQm+qG3YsEFBQUFas2aNZUz+02TPnl3Lli3TlClTEnzhvnTpkiRZbimc3HUuX77csizp0fCkadOmKVOmTJZhRPEh6vHXLT06Uzd69GhJSvLvt8QvK/7agHi//PKL5YYLtly3YYu1a9dafdl6+PChxo4dK0mWG1W8+OKLqlmzpk6ePKkFCxZYPf/cuXMaOXKkZs2aleQhdrYKCgqyuqZjw4YNOnDggCpUqCBPT09Jj4aHSo/OMt28edPq+V988YW+/fZbBQcH27TebNmyKSYmJkHwXrdunXbu3Cnp+X0uSdkGK1WqpDJlymjr1q2W36KKd/jwYY0dO1bz58+3upnH08R/1uPHj7c6q3H48GGtX7/eat6nbfuRkZEaNmyY5Xqk+O3/9OnTWrp0aYJge+/ePd29e1c5cuRQ3rx5LcPAQkNDrfpObGysxo4dazkLbuvvIsXr2LGjzGazduzYYfmtKCcnJ2XKlEnh4eEJzubMmjXL8ltXyV3nP5k7d67V9nXu3DktWLBALi4ulptpPG3/cPXqVX355ZcJ6nvrrbcUGxur8ePHW7X//PPP2rZt2z/WlJb7o6SwdfsDMhqGAgLp3N9//63XX39d9evXV3R0tLZs2aLw8HCNHTvWMtY/Z86c+vzzz9WjRw+1adNGAQEBKlmypM6ePatdu3Ype/bsGjdunDJlevaxlkyZMmnQoEHq06ePWrRooUaNGumFF17QxYsX9dNPPylfvnyWYVHJXWfu3LnVsmVLNWnSRHFxcdq2bZtu3bqlvn37Wn5vp169esqTJ4+WLVuma9euyc3NTX///be2b9+u8PBw5cyZU/fv31dMTEyC32V6UosWLfTrr7+qc+fO+s9//iNXV1edPn1ae/fuVd68eRUZGfmPZ/KSy8nJSYGBgWrUqJHy5MmjnTt36vLly2rVqpXq1q1rme/TTz/VO++8o88++0ybN2+Wj4+P7t69q02bNiksLExDhgxJ0m/k2MrV1VUHDhzQm2++qRo1auj8+fPavn278uTJo/Hjx1vmq1Spkrp3764ZM2aoadOmCggIUN68eXXw4EGdOHFCZcqUUZ8+fWxad8uWLfXVV1/pzTffVOPGjZU1a1YdP35chw4dUoECBfT3338/t88lKdtgpkyZNGHCBLVv397yI9Vubm66evWqtm7dKsMwNHbsWMvR/GcJCAhQy5YttWrVKjVr1kz16tXTnTt3tGXLFhUtWtRytkh6dDOLUqVK6f/+7//0zjvvqGLFirp375527dqlmzdvKm/evLpz547u3r0rFxcXvffee1q3bp0mT56sAwcOyMPDQ+Hh4dq6davu3r2rYcOGycnJSaVKlVKlSpV05MgRvfnmm6pevbqio6O1Z88eXbhwQfnz59etW7eS/Z5nzZpVo0ePVuvWrTVmzBjVrFlT+fPn13/+8x+tW7dOLVq0sNzZ75dfftGpU6csn3NS72qXHK+99poaN26sBw8eaPPmzQoPD9f48eMt1181bdpU8+bN0+TJk3Xy5EmVKFFCV65c0fbt25U1a1ZlzZrV6j1p27attmzZou+//17BwcGqWrWq5TeecufOrdu3bz9zP5uW+6OksHX7AzIazlgB6dynn36qevXqafPmzdq6dat8fX21YMECvf7661bz1alTRytWrFDjxo3166+/asGCBTpz5oxee+01rVy50nLL7X/SpEkTzZkzR5UqVdLPP/+sefPm6dixY2revLlWrVpldaex5Kxz6NChevPNN7V161Z9//33KlKkiIKCgtSlSxfLPAULFtS3336revXq6bfffrP8kOjLL7+s1atXq3HjxoqOjk5wC/LE/Pe//9WYMWP04osv6scff9SKFSt0+/Zt9ejRQxs3blT27Nm1e/fuRO/EZa+3335bvXr10pEjR7Ry5Urlzp1bY8aM0ahRo6zmK1q0qFavXq127drpxo0bWrhwoXbv3q1KlSpp7ty5evfdd1O8NunRUK5FixYpX758Wrx4sQ4dOqQmTZpo5cqVeumll6zm/fDDDzVjxgx5eHho27ZtWrJkiR4+fKj3339f3333nc3XXvXs2VP9+/eXq6urVqxYobVr1yo2NlbDhg2zXEMXf+YqpSVlG5QeDeFbvXq13nrrLYWEhOjbb7/V4cOHVbduXX333XcJbpX+LGPGjNHw4cOVI0cOrVixQr/++qt69OiR4PotFxcXzZ07V6+++qouXbqkb7/9Vnv37pWXl5eWLFli2RZ27Ngh6dGt0pcsWaJ33nlHV69e1eLFi7Vu3TqVK1dOM2fOtPyItslk0vTp09WmTRvdu3dPixYt0k8//aTixYtr1qxZlh98jV9ucvj4+Oidd97R3bt3NXLkSEmP9l9du3aVYRj67rvvtHHjRuXMmVMTJkxQUFCQpOf3OU+ePFl16tTR2rVrtWHDBlWoUEHz5s2zuvW7m5ub5s2bJz8/P+3fv1+LFi1ScHCwmjVrprVr18rPz0+XLl2y3FbfyclJc+bMUYcOHRQaGqolS5bo999/19ChQy375GfdWCYt90dJYev2B2Q0JoOBsEC6NGjQIH3//feaN2+eatSokdblwAarV6/W4MGD9f7776t3795pXQ6AFHL58mXlzZs30TOVffv21bp167RixQp5e3unQXUAnjfOWAEAAKSAsWPHqlKlSjp58qRV+7lz57R9+3blzZvXMpwUwL8P11gBAACkgDZt2mjHjh1q27atXnnlFRUsWFBXr17Vtm3bFBkZqbFjxyb5d+QApD8EKwAAgBRQq1YtLVmyRHPnztX+/fv1999/K0+ePKpVq5Y6dOiQ5GtZAaRPXGMFAAAAAHbiGisAAAAAsBPBCgAAAADsxDVWT/j1119lGIayZs2a1qUAAAAASEPR0dEymUxJukaSYPUEwzDEZWcAAAAAbMkFBKsnxJ+p8vLySuNKAAAAAKSlEydOJHlerrECAAAAADsRrAAAAADATgQrAAAAALATwQoAAAAA7ESwAgAAAAA7EawAAAAAwE4EKwAAAACwE8EKAAAAAOxEsAIAAAAAOxGsAAAAAMBOBCsAAAAAsBPBCgAAAADsRLACAAAAADsRrAAAAADATgQrAAAAALATwQoAAAAA7ESwSgVxsbFpXQIyCLY1AACAtJElrQvICDJlzqyFXbroxu+/p3Up+Bcr6OamtrNmpXUZAAAAGZJDBasZM2Zo3759WrhwoaXtxo0bGjdunHbv3q3MmTOrVq1aGjJkiPLlyydJiouL07Rp07RixQrdu3dPlStX1ieffKKSJUum1ctI1I3ff9fl48fTugwAAAAAz4HDDAWcP3++pkyZYtUWFRWlDh066NKlS5o3b56+/vprnTp1SgMHDrTMM2PGDC1dulSjR4/WsmXLZDKZ1LlzZ0VFRaX2SwAAAACQQaV5sLp+/bo6deqkoKAglS5d2mraunXr9Ndff2nmzJny8vKSr6+vPv74Y50/f14PHjxQVFSU5s6dq549e6pOnTpyd3fXpEmTdP36dW3dujWNXhEAAACAjCbNg9XJkyeVO3durV27Vj4+PlbT9uzZo2rVqqlAgQKWttq1a2vbtm3KmTOnTp8+rYcPH6patWqW6a6urvLw8NDBgwdT7TUAAAAAyNjS/BqrgIAABQQEJDrtwoUL8vPz0/Tp07VmzRrFxMSoVq1a6t+/v1xdXXXt2jVJUpEiRayeV7BgQV29ejXZNRmGobCwsGQ//3Emk0kuLi4psiwgKcLDw2UYRlqXAQAAkO4ZhiGTyZSkedM8WD3LgwcPtGbNGlWvXl1ffPGFQkNDNXbsWHXv3l0LFy5UeHi4JMnJycnqedmyZVNoaGiy1xsdHa3g4GC7ao/n4uIiDw+PFFkWkBTnz5+39A0AAADY58ms8TQOHayyZs2q7Nmz64svvlDWrFklSblz59Zbb72lEydOyNnZWdKjm1zE/1uSIiMj7TpLlDVrVpUrV86+4v+/pCZcIKWULl2aM1YAAAApICQkJMnzOnSwKly4sOLi4iyhSpJeeuklSdLly5dVrFgxSY9uyV6iRAnLPDdu3JC7u3uy12symZQ9e/ZkPx9ISww9BQAASBm2nCRJ85tXPIufn59Onz6tiIgIS9uZM2ckSSVLlpS7u7ty5sypAwcOWKbfu3dPp06dkp+fX6rXCwAAACBjcuhg1bp1a2XOnFl9+/bVmTNndPjwYQ0dOlRVq1ZVhQoV5OTkpMDAQE2cOFE//fSTTp8+rd69e6tw4cJq2LBhWpcPAAAAIINw6KGA+fLl0+LFizV27Fj997//lZOTkxo0aKDBgwdb5unVq5diYmI0dOhQRUREyN/fX3PmzEnyRWYAAAAAYC+TwVXuVk6cOCFJ8vLyStHlflGnji4fP56iywQeV8zbW3137UrrMgAAAP41bMkGDj0UEAAAAADSA4IVAAAAANiJYAUAAAAAdiJYAQAAAICdCFYAAAAAYCeCFQAAAADYiWAFAAAAAHYiWAEAAACAnQhWAAAAAGAnghUAAAAA2IlgBQAAAAB2IlgBAAAAgJ0IVgAAAABgJ4IVAAAAANiJYAUAAAAAdiJYAQAAAICdCFYAAAAAYCeCFQAAAADYiWAFAAAAAHYiWAEAAACAnQhWAAAAAGAnghUAAAAA2IlgBQAAAAB2IlgBAAAAgJ0IVgAAAABgJ4IVAAAAANiJYAUAAAAAdiJYAXjuDMNI6xKQQbCtAQDSSpa0LgDAv5/JZNKlS5cUGRmZ1qXgXyxbtmwqXrx4WpcBAMigCFYAUkVkZKQiIiLSugwAAIDngqGAAAAAAGAnghUAAAAA2IlgBQAAAAB2cqhgNWPGDLVt2/ap04cOHaqAgACrtri4OE2ZMkW1a9eWj4+POnTooIsXLz7vUgEAAADAwmGC1fz58zVlypSnTt+2bZtWrFiRoH3GjBlaunSpRo8erWXLlslkMqlz586Kiop6nuUCAAAAgEWaB6vr16+rU6dOCgoKUunSpROd58aNGxo2bJiqVKli1R4VFaW5c+eqZ8+eqlOnjtzd3TVp0iRdv35dW7duTY3yAQAAACDtg9XJkyeVO3durV27Vj4+PgmmG4ahQYMG6fXXX08QrE6fPq2HDx+qWrVqljZXV1d5eHjo4MGDz712AACSih8vRmphWwPSRpr/jlVAQECC66YeN3/+fN28eVNfffWVvv76a6tp165dkyQVKVLEqr1gwYK6evVqsmsyDENhYWHJfv7jTCaTXFxcUmRZQFKEh4c71B9V+gBSm6P1Ael//YAfysbzFv9D2Y7YD4D0yDAMmUymJM2b5sHqWU6fPq1p06Zp8eLFcnJySjA9PDxckhJMy5Ytm0JDQ5O93ujoaAUHByf7+Y9zcXGRh4dHiiwLSIrz589b+oYjoA8gtTlaH5D+1w/4oWykFkfsB0B6lVgOSYzDBqvIyEj169dP3bp1k7u7e6LzODs7S3p0rVX8v+Ofa88R8qxZs6pcuXLJfv7jkppwgZRSunRphzpKSR9AanO0PiDRD5D6HLEfAOlRSEhIkud12GB17Ngx/fHHH5o2bZqmT58u6dGZpJiYGFWsWFEjR45UqVKlJD26uUWJEiUsz71x48ZTw1hSmEwmZc+e3a76gbTCsDtkdPQBgH4ApBRbDow5bLDy9vbWli1brNoWLlyoLVu2aOHChcqfP7+cnJyUM2dOHThwwBKs7t27p1OnTikwMDAtygYAAACQATlssHJ2dlbJkiWt2nLnzq0sWbJYtQcGBmrixInKly+fihYtqgkTJqhw4cJq2LBhapcMAAAAIINy2GCVVL169VJMTIyGDh2qiIgI+fv7a86cOUm+yAwAAAAA7OVQwWrcuHHPnN6zZ0/17NnTqi1z5szq37+/+vfv/zxLAwAAAICnSvMfCAYAAACA9I5gBQAAAAB2IlgBAAAAgJ0IVgAAAABgJ4IVAAAAANiJYAUAAAAAdiJYAQAAAICdCFYAAAAAYCeCFQAAAADYiWAFAAAAAHYiWAEAAACAnQhWAAAAAGAnghUAAAAA2IlgBQAAAAB2IlgBAAAAgJ0IVgAAAABgJ4IVAAAAANiJYAUAAAAAdiJYAQAAAICdCFYAAAAAYCeCFQAAAADYiWAFAAAAAHYiWAEAAACAnQhWAAAAAGAnghUAAAAA2IlgBQAAAAB2IlgBAAAAgJ0IVgAAAABgJ4IVAAAAANiJYAUAAAAAdiJYAQAAAICdCFYAAAAAYCeCFQAAAADYyaGC1YwZM9S2bVurtu3bt6tly5aqWLGiAgICNH78eEVERFimx8XFacqUKapdu7Z8fHzUoUMHXbx4MbVLBwAAAJCBOUywmj9/vqZMmWLVdujQIfXo0UONGjXSmjVrNGLECG3cuFEjR460zDNjxgwtXbpUo0eP1rJly2QymdS5c2dFRUWl9ksAAAAAkEGlebC6fv26OnXqpKCgIJUuXdpq2tKlS1WtWjV16dJFJUuW1Msvv6zevXtr7dq1ioqKUlRUlObOnauePXuqTp06cnd316RJk3T9+nVt3bo1jV4RAAAAgIwmzYPVyZMnlTt3bq1du1Y+Pj5W0zp06KABAwYkeE5MTIwePHig06dP6+HDh6pWrZplmqurqzw8PHTw4MHnXjsAAAAASFKWtC4gICBAAQEBiU7z8PCwehwVFaV58+apQoUKypcvnw4dOiRJKlKkiNV8BQsW1NWrV5Ndk2EYCgsLS/bzH2cymeTi4pIiywKSIjw8XIZhpHUZFvQBpDZH6wMS/QCpzxH7AZAeGYYhk8mUpHnTPFglVUxMjAYMGKCQkBAtXrxY0qOdhiQ5OTlZzZstWzaFhoYme13R0dEKDg5OfrGPcXFxSRAQgefp/Pnzlr7hCOgDSG2O1gck+gFSnyP2AyC9ejJrPE26CFYPHjzQRx99pAMHDmjKlCmWIYPOzs6SHp3Jiv+3JEVGRtp1ZDBr1qwqV66cfUX/f0lNuEBKKV26tEMdpaQPILU5Wh+Q6AdIfY7YD4D0KCQkJMnzOnywunHjhjp37qzLly9r9uzZVtdTxQ8BvHHjhkqUKGH1HHd392Sv02QyKXv27MkvGkhDDDdCRkcfAOgHQEqx5cBYmt+84llCQ0P13nvv6fbt21qyZIlVqJIkd3d35cyZUwcOHLC03bt3T6dOnZKfn19qlwsAAAAgg3LoM1Zjx47VpUuX9M033yhfvny6efOmZVq+fPnk5OSkwMBATZw4Ufny5VPRokU1YcIEFS5cWA0bNkzDygEAAABkJA4brOLi4rRhwwZFR0frvffeSzD9p59+UrFixdSrVy/FxMRo6NChioiIkL+/v+bMmZPki8wAAAAAwF4OFazGjRtn+XemTJl0/Pjxf3xO5syZ1b9/f/Xv3/95lgYAAAAAT+XQ11gBAAAAQHpAsAIAAAAAOxGsAAAAAMBOBCsAAAAAsBPBCgAAAADsRLACAAAAADsRrAAAAADATgQrAAAAALATwQoAAAAA7ESwAgAAAAA7EawAAAAAwE4EKwAAAACwE8EKAAAAAOxEsAIAAAAAOxGsAAAAAMBOBCsAAAAAsBPBCgAAAADsRLACAAAAADsRrAAAAADATgQrAAAAALATwQoAAAAA7ESwAgAAAAA7ZUnKTPXr19f06dPl7u6ugIAAmUymp85rMpm0bdu2FCsQAAAAABxdkoJVlSpVlCNHDsu/nxWsAAAAACCjSVKwGjt2rOXf48aNe27FAAAAAEB6lKRg9aQHDx7o4cOHKlSokKKiovTtt9/q2rVratSokfz9/VO6RgAAAABwaDbfvOL48eMKCAjQwoULJUmjR4/WxIkTtXbtWr333nv66aefUrxIAAAAAHBkNgerSZMmqUyZMmrVqpUiIiL0448/6u2339Yvv/yiN998U1999dXzqBMAAAAAHJbNwerYsWPq1q2bihcvrn379ikiIkKvv/66JKlJkyb6448/UrxIAAAAAHBkNgerTJkyycnJSZK0a9cuubq6ytvbW9Kja6+cnZ1TtkIAAAAAcHA237zC09NTK1eulLOzszZu3Ki6devKZDLp1q1bmj17tjw9PZ9HnQAAAADgsGw+Y9W/f3/t27dPbdq0UebMmdWtWzdJ0quvvqoLFy7oo48+SukaAQAAAMCh2XzGqkKFCtqyZYvOnj2rl156SdmzZ5ckjRgxQpUqVdILL7yQ4kUCAAAAgCOz+YxVcHCwcubMKR8fH0uokqRGjRopW7ZsGjx4cLKLmTFjhtq2bZtgfYGBgfL19VXdunU1Z84cq+lxcXGaMmWKateuLR8fH3Xo0EEXL15Mdg0AAAAAYCubg1W7du0UHBycoH3jxo1q0qSJfvzxx2QVMn/+fE2ZMsWq7c6dO2rfvr1KlSqlVatWqWfPngoKCtKqVass88yYMUNLly7V6NGjtWzZMplMJnXu3FlRUVHJqgMAAAAAbGVzsKpQoYLatWunkydPSpKuX7+u7t27q3fv3ipWrJhWrlxp0/KuX7+uTp06KSgoSKVLl7aatnz5cjk5OWnEiBEqW7asWrZsqXbt2mn27NmSpKioKM2dO1c9e/ZUnTp15O7urkmTJun69evaunWrrS8NAAAAAJLF5mD11Vdfyc/PT+3bt9fUqVPVtGlTHT58WCNHjtTSpUvl7u5u0/JOnjyp3Llza+3atfLx8bGadujQIfn7+ytLlv9dClatWjWdP39et27d0unTp/Xw4UNVq1bNMt3V1VUeHh46ePCgrS8NAAAAAJLF5ptXODk5acqUKRo4cKCmT5+uqlWratKkScqXL1+yCggICFBAQECi065duyaz2WzVVrBgQUnSlStXdO3aNUlSkSJFEsxz9erVZNUjSYZhKCwsLNnPf5zJZJKLi0uKLAtIivDwcBmGkdZlWNAHkNocrQ9I9AOkPkfsB0B6ZBiGTCZTkuZNUrBK7OzPW2+9pQsXLui3337TgQMHVKBAAcs0f3//JJb6bBEREZYfI46XLVs2SVJkZKTCw8MlKdF5QkNDk73e6OjoRK8jSw4XFxd5eHikyLKApDh//rylbzgC+gBSm6P1AYl+gNTniP0ASK+ezBpPk6Rg1bZtW6ukFp/c4o+E9O7d2/LYZDKlWChxdnZOcBOKyMhISVL27Nnl7Ows6dG1VvH/jp/HniODWbNmVbly5ZL9/MclNeECKaV06dIOdZSSPoDU5mh9QKIfIPU5Yj8A0qOQkJAkz5ukYPXtt98muxh7FC5cWDdu3LBqi39cqFAhxcTEWNpKlChhNY+t13o9zmQyWd1KHkhPGG6EjI4+ANAPgJRiy4GxJAWrKlWqJLsYe/j7+2vp0qWKjY1V5syZJUn79u1T6dKllT9/fuXKlUs5c+bUgQMHLMHq3r17OnXqlAIDA9OkZgAAAAAZj803r5Cko0eP6pdfflF0dLTlNHP8DR8OHz6s5cuXp0hxLVu21DfffKMhQ4aoU6dOOn78uBYsWKCRI0dKejTeMTAwUBMnTlS+fPlUtGhRTZgwQYULF1bDhg1TpAYAAAAA+Cc2B6vFixdr9OjRiY7bzZQpk2rVqpUihUlS/vz59c0332jMmDFq3ry5XnjhBQ0YMEDNmze3zNOrVy/FxMRo6NChioiIkL+/v+bMmZPki8wAAAAAwF42B6tFixapVq1amjhxombNmqX79+/r448/1q5duzRo0CA1a9Ys2cWMGzcuQZu3t7eWLVv21OdkzpxZ/fv3V//+/ZO9XgAAAACwh80/EHz58mUFBgYqd+7c8vLy0uHDh+Xs7KxGjRqpa9euaXajCwAAAABIKzYHq6xZs1pubV6qVCldvHhR0dHRkqRKlSrpwoULKVogAAAAADg6m4NV+fLltWPHDklSyZIlFRcXp6NHj0qSrl27lqLFAQAAAEB6YPM1Vu3bt1ePHj0UGhqqsWPHqn79+howYIAaNWqkH3/8UZUrV34edQIAAACAw7L5jFWDBg301VdfqVy5cpKkUaNGqXTp0lq6dKnKlCmj4cOHp3iRAAAAAODIkvU7VnXr1lXdunUlSXnz5tXcuXNTsiYAAAAASFeSFawuXbqkyMhIlStXTqGhoZo8ebKuXr2qxo0b64033kjhEgEAAADAsdk8FHD37t36z3/+o1WrVkmSRowYoeXLl+v69esaPHiwVqxYkeJFAgAAAIAjszlYzZgxQ7Vq1dIHH3yg+/fva+vWrerSpYu+//57denShd+xAgAAAJDh2BysTp8+rffee085c+bUnj17FBsbq0aNGkmSatasqYsXL6Z4kQAAAADgyGwOVtmyZVNMTIwkac+ePcqfP7/c3d0lSX///bdcXV1TtkIAAAAAcHA237yicuXKmjt3rkJDQ7Vx40a1aNFCkvTbb79p2rRpqlSpUooXCQAAAACOzOYzVoMHD9b169fVr18/FStWTN26dZMkde3aVVFRUerXr1+KFwkAAAAAjszmM1bFixfX+vXrdevWLRUoUMDSPn36dHl4eMjJySlFCwQAAAAAR5es37EymUxWoUqSfH19U6IeAAAAAEh3bA5Wt2/f1pgxY7Rz506Fh4fLMAyr6SaTSadOnUqxAgEAAADA0dkcrEaMGKFdu3apadOmKly4sDJlsvkyLQAAAAD4V7E5WO3Zs0cff/yxWrVq9TzqAQAAAIB0x+bTTU5OTipevPjzqAUAAAAA0iWbg1XDhg21bt2651ELAAAAAKRLNg8F9PDw0OTJk3Xp0iX5+PjI2dnZarrJZNIHH3yQYgUCAAAAgKOzOViNGjVKknTw4EEdPHgwwXSCFQAAAICMxuZgdfr06edRBwAAAACkWyl+r/T79++n9CIBAAAAwKHZfMYqKipK8+fP1y+//KLo6GjLDwQbhqGwsDCFhITo2LFjKV4oAAAAADgqm4PV559/rkWLFslsNuv27dvKli2b8uXLpzNnzig6Olo9evR4HnUCAAAAgMOyeSjgli1b1K5dO61du1Zt27aVp6enVqxYoS1btqho0aKKi4t7HnUCAAAAgMOyOVjdvn1bderUkSS5ubnpxIkTkqRChQqpS5cu2rBhQ8pWCAAAAAAOzuZglStXLkVFRUmSSpUqpatXr+rBgwdWjwEAAAAgI7E5WPn5+WnhwoUKCwtTsWLF5OLioq1bt0qSfv31V+XMmTPFiwQAAAAAR2ZzsPrggw909OhRde3aVVmyZNHbb7+t4cOHq0WLFgoKClKjRo2eR50AAAAA4LBsviugu7u7Nm7cqDNnzkiS+vbtq5w5c+rIkSMKCAhQly5dUrxIAAAAAHBkNgerESNG6PXXX1fNmjUlSSaTSe+//36KFwYAAAAA6YXNQwF//PFHRUREPI9anio6OlqTJk1S3bp1VbFiRb399ts6cuSIZXpwcLACAwPl6+urunXras6cOalaHwAAAICMzeZg5eXlpd27dz+PWp5q5syZWrVqlUaPHq01a9aoTJky6ty5s65fv647d+6offv2KlWqlFatWqWePXsqKChIq1atStUaAQAAAGRcNg8FdHNz08KFC7V582aVK1dO+fPnt5puMpn02WefpViBkvTTTz/p1VdfVa1atSRJgwYN0ooVK3T06FFduHBBTk5OGjFihLJkyaKyZcvq4sWLmj17tlq2bJmidQAAAABAYmwOVlu3blXBggUlSSEhIQoJCUnxop6UJ08e7dixQ4GBgSpSpIiWLVsmJycnlS9fXitXrpS/v7+yZPnfS6lWrZq+/vpr3bp1K0HwAwAAAICUZnOw2r59+/Oo45mGDBmi3r17q379+sqcObMyZcqkoKAglShRQteuXZPZbLaaPz74XblyJVnByjAMhYWFpUjtJpNJLi4uKbIsICnCw8NlGEZal2FBH0Bqc7Q+INEPkPocsR8A6ZFhGDKZTEma1+ZgNXjwYHXv3l3FixdPMO3cuXP6/PPP9dVXX9m62Gc6e/asXF1dNX36dBUqVEgrVqzQwIEDtWjRIkVERMjJyclq/mzZskmSIiMjk7W+6OhoBQcH2123JLm4uMjDwyNFlgUkxfnz5xUeHp7WZVjQB5DaHK0PSPQDpD5H7AdAevVk1niaJAWrK1euWP79/fffq0GDBsqcOXOC+Xbv3q29e/cmscSk+euvv9S/f3/Nnz9ffn5+kh7dQCMkJERTp06Vs7OzoqKirJ4TH6iyZ8+erHVmzZpV5cqVs6/w/y+pCRdIKaVLl3aoo5T0AaQ2R+sDEv0Aqc8R+wGQHtly2VOSgtWoUaO0a9cuSY/+OPTo0SPR+QzDsPy+VUo5fvy4oqOj5eXlZdXu4+Oj3bt368UXX9SNGzespsU/LlSoULLWaTKZkh3KgLTGcCNkdPQBgH4ApBRbDowlKViNHDlSe/fulWEY+vjjj9WtWzeVKFHCap5MmTLJ1dVVVatWta3af1CkSBFJ0u+//y5vb29L+5kzZ1SyZEn5+vpq6dKlio2NtZxF27dvn0qXLs2NKwAAAACkiiQFq0KFCql58+aSHqW2unXrKm/evM+1sHje3t7y8/PTwIED9cknn6hw4cJas2aN9u3bpyVLlqh48eL65ptvNGTIEHXq1EnHjx/XggULNHLkyFSpDwAAAABsvnlFfMBKLZkyZdKMGTM0efJkDR48WKGhoTKbzZo/f758fX0lSd98843GjBmj5s2b64UXXtCAAQNSvU4AAAAAGZfNwSot5M6dW5988ok++eSTRKd7e3tr2bJlqVwVAAAAADySKa0LAAAAAID0jmAFAAAAAHYiWAEAAACAnZJ0jdXgwYPVvXt3FS9eXIMHD37mvCaTSZ999lmKFAcAAAAA6UGSgtWBAwf03nvvWf79LPy6PAAAAICMJknBavv27Yn+GwAAAADwHK6xOnv2bEovEgAAAAAcms2/Y3X37l19+eWXOnjwoKKjo2UYhiTJMAyFhYUpNDRUwcHBKV4oAAAAADgqm89YjR07VqtWrVKpUqWUOXNm5cqVS15eXoqOjta9e/c0atSo51EnAAAAADgsm4PVnj171KNHD82cOVOtW7dW4cKFNXnyZG3atElubm4KCQl5HnUCAAAAgMOyOVjdu3dPlStXliS99NJL+u233yRJOXLkUIcOHbRz584ULRAAAAAAHJ3NwSpv3ry6f/++JKlkyZK6deuW7ty5I0kqVKiQrl+/nrIVAgAAAICDszlYVa9eXV999ZUuX76sYsWKKU+ePFq9erUkaceOHcqbN2+KFwkAAAAAjszmYPXhhx/q1q1bGjRokEwmk7p06aIJEyaoSpUqmj9/vlq2bPk86gQAAAAAh2Xz7daLFi2qDRs26MKFC5Kk9u3bq0CBAjpy5Ii8vb3VvHnzlK4RAAAAAByazcFKkpydneXu7m55/Nprr+m1115LsaIAAAAAID1JUrAaPHhwkhdoMpn02WefJbsgAAAAAEhvkhSsDhw4kOQFmkymZBcDAAAAAOlRkoLV9u3bn3cdAAAAAJBu2XxXQAAAAACAtSSdsapfv76mT58ud3d3BQQEPHO4n8lk0rZt21KsQAAAAABwdEkKVlWqVFGOHDks/+Y6KgAAAAD4nyQFq7Fjx1r+PW7cuOdWDAAAAP69DMPgAD1SRVpsa8n6HStJCg0NVXh4uOLi4hJMe/HFF+0qCgAAAP8+JpNJly5dUmRkZFqXgn+xbNmyqXjx4qm+XpuD1YULFzRo0CAdO3bsqfMEBwfbVRQAAAD+nSIjIxUREZHWZQApzuZg9emnn+rChQvq0aOHChcurEyZuLEgAAAAgIzN5mB16NAhjRkzRq+++urzqAcAAAAA0h2bTzflzJlTuXPnfh61AAAAAEC6ZHOwev3117V48WIZhvE86gEAAACAdMfmoYAuLi46fPiwGjZsKC8vLzk7O1tNN5lM+uyzz1KsQAAAAABwdDYHq++//165cuVSXFxconcG5LcJAAAAAGQ0Nger7du3P486AAAAACDd4l7pAAAAAGCndBOs1qxZoyZNmsjLy0tNmzbVxo0bLdOCg4MVGBgoX19f1a1bV3PmzEnDSgEAAABkNOkiWP3www/6+OOP1apVK61bt05NmjRRnz599Ouvv+rOnTtq3769SpUqpVWrVqlnz54KCgrSqlWr0rpsAAAAABmEzddYpTbDMBQUFKT33ntP7733niTpgw8+0JEjR/TLL7/ol19+kZOTk0aMGKEsWbKobNmyunjxombPnq2WLVumcfUAAAAAMgKHP2N17tw5/fXXX3rttdes2ufMmaOuXbvq0KFD8vf3V5Ys/8uI1apV0/nz53Xr1q3ULhcAAABABuTwZ6wuXLggSQoLC1PHjh116tQpFStWTN26dVNAQICuXbsms9ls9ZyCBQtKkq5cuaL8+fPbvE7DMBQWFmZ37dKj28+7uLikyLKApAgPD3eoH/CmDyC1OVofkOgHSH30AyBl+oFhGEn+OSmHD1YPHjyQJA0cOFA9evRQv379tHnzZnXv3l3z5s1TRESEnJycrJ6TLVs2SVJkZGSy1hkdHa3g4GD7Cv//XFxc5OHhkSLLApLi/PnzCg8PT+syLOgDSG2O1gck+gFSH/0ASLl+8GTWeBqHD1ZZs2aVJHXs2FHNmzeXJJUvX16nTp3SvHnz5OzsrKioKKvnxAeq7NmzJ3ud5cqVs6Pq/+EHk5HaSpcu7VBHKekDSG2O1gck+gFSH/0ASJl+EBISkuR5HT5YFS5cWJISDPcrV66cdu7cqaJFi+rGjRtW0+IfFypUKFnrNJlMyQ5lQFpjmAUyOvoAQD8ApJTpB7YcEHD4m1d4eHgoR44cOnbsmFX7mTNnVKJECfn7++vw4cOKjY21TNu3b59Kly6drOurAAAAAMBWDh+snJ2d1alTJ02fPl3r1q3Tn3/+qZkzZ+rnn39W+/bt1bJlSz148EBDhgxRSEiIVq9erQULFqhr165pXToAAACADMLhhwJKUvfu3eXi4qJJkybp+vXrKlu2rKZOnaqqVatKkr755huNGTNGzZs31wsvvKABAwZYrscCAAAAgOctXQQrSWrfvr3at2+f6DRvb28tW7YslSsCAAAAgEccfiggAAAAADg6ghUAAAAA2IlgBQAAAAB2IlgBAAAAgJ0IVgAAAABgJ4IVAAAAANiJYAUAAAAAdiJYAQAAAICdCFYAAAAAYCeCFQAAAADYiWAFAAAAAHYiWAEAAACAnQhWAAAAAGAnghUAAAAA2IlgBQAAAAB2IlgBAAAAgJ0IVgAAAABgJ4IVAAAAANiJYAUAAAAAdiJYAQAAAICdCFYAAAAAYCeCFQAAAADYiWAFAAAAAHYiWAEAAACAnQhWAAAAAGAnghUAAAAA2IlgBQAAAAB2IlgBAAAAgJ0IVgAAAABgJ4IVAAAAANiJYAUAAAAAdiJYAQAAAICdCFYAAAAAYKd0FazOnz+vihUravXq1Za24OBgBQYGytfXV3Xr1tWcOXPSsEIAAAAAGVG6CVbR0dHq16+fwsLCLG137txR+/btVapUKa1atUo9e/ZUUFCQVq1alYaVAgAAAMhosqR1AUk1depU5ciRw6pt+fLlcnJy0ogRI5QlSxaVLVtWFy9e1OzZs9WyZcs0qhQAAABARpMuzlgdPHhQy5Yt0/jx463aDx06JH9/f2XJ8r98WK1aNZ0/f163bt1K7TIBAAAAZFAOf8bq3r17GjBggIYOHaoiRYpYTbt27ZrMZrNVW8GCBSVJV65cUf78+ZO1TsMwrIYc2sNkMsnFxSVFlgUkRXh4uAzDSOsyLOgDSG2O1gck+gFSH/0ASJl+YBiGTCZTkuZ1+GA1YsQI+fr66rXXXkswLSIiQk5OTlZt2bJlkyRFRkYme53R0dEKDg5O9vMf5+LiIg8PjxRZFpAU58+fV3h4eFqXYUEfQGpztD4g0Q+Q+ugHQMr1gyfzxtM4dLBas2aNDh06pB9//DHR6c7OzoqKirJqiw9U2bNnT/Z6s2bNqnLlyiX7+Y9LasIFUkrp0qUd6iglfQCpzdH6gEQ/QOqjHwAp0w9CQkKSPK9DB6tVq1bp1q1bqlu3rlX7J598ojlz5ujFF1/UjRs3rKbFPy5UqFCy12symewKZkBaYpgFMjr6AEA/AKSU6Qe2HBBw6GA1ceJERUREWLW98sor6tWrl5o0aaL169dr6dKlio2NVebMmSVJ+/btU+nSpZN9fRUAAAAA2Mqh7wpYqFAhlSxZ0uo/ScqfP7+KFi2qli1b6sGDBxoyZIhCQkK0evVqLViwQF27dk3jygEAAABkJA4drP5J/vz59c033+j8+fNq3ry5pk2bpgEDBqh58+ZpXRoAAACADMShhwIm5vfff7d67O3trWXLlqVRNQAAAACQzs9YAQAAAIAjIFgBAAAAgJ0IVgAAAABgJ4IVAAAAANiJYAUAAAAAdiJYAQAAAICdCFYAAAAAYCeCFQAAAADYiWAFAAAAAHYiWAEAAACAnQhWAAAAAGAnghUAAAAA2IlgBQAAAAB2IlgBAAAAgJ0IVgAAAABgJ4IVAAAAANiJYAUAAAAAdiJYAQAAAICdCFYAAAAAYCeCFQAAAADYiWAFAAAAAHYiWAEAAACAnQhWAAAAAGAnghUAAAAA2IlgBQAAAAB2IlgBAAAAgJ0IVgAAAABgJ4IVAAAAANiJYAUAAAAAdiJYAQAAAICdCFYAAAAAYCeCFQAAAADYiWAFAAAAAHZy+GB19+5dDR8+XC+//LIqVaqkNm3a6NChQ5bpwcHBCgwMlK+vr+rWras5c+akYbUAAAAAMiKHD1Z9+vTRsWPH9OWXX2rlypWqUKGCOnbsqLNnz+rOnTtq3769SpUqpVWrVqlnz54KCgrSqlWr0rpsAAAAABlIlrQu4FkuXryon3/+Wd99950qVaokSRoyZIh2796tdevWydnZWU5OThoxYoSyZMmismXL6uLFi5o9e7ZatmyZxtUDAAAAyCgc+oxV3rx5NWvWLHl6elraTCaTDMNQaGioDh06JH9/f2XJ8r98WK1aNZ0/f163bt1Ki5IBAAAAZEAOfcbK1dVVderUsWrbuHGj/vzzT9WqVUuTJk2S2Wy2ml6wYEFJ0pUrV5Q/f/5krdcwDIWFhSWv6CeYTCa5uLikyLKApAgPD5dhGGldhgV9AKnN0fqARD9A6qMfACnTDwzDkMlkStK8Dh2snnT48GF9/PHHql+/vgICAjR27Fg5OTlZzZMtWzZJUmRkZLLXEx0dreDgYLtqjefi4iIPD48UWRaQFOfPn1d4eHhal2FBH0Bqc7Q+INEPkProB0DK9YMn88bTpJtgtW3bNvXr108+Pj768ssvJUnOzs6Kioqymi8+UGXPnj3Z68qaNavKlSuX/GIfk9SEC6SU0qVLO9RRSvoAUpuj9QGJfoDURz8AUqYfhISEJHnedBGsFi1apDFjxqhhw4aaOHGiJTUWLlxYN27csJo3/nGhQoWSvT6TyWRXMAPSEsMskNHRBwD6ASClTD+w5YCAQ9+8QpKWLFmiTz/9VO+8844mT55sdSrO399fhw8fVmxsrKVt3759Kl26dLKvrwIAAAAAWzl0sDp//rw+++wzNWzYUF27dtWtW7d08+ZN3bx5U/fv31fLli314MEDDRkyRCEhIVq9erUWLFigrl27pnXpAAAAADIQhx4KuHnzZkVHR2vr1q3aunWr1bTmzZtr3Lhx+uabbzRmzBg1b95cL7zwggYMGKDmzZunUcUAAAAAMiKHDlbvv/++3n///WfO4+3trWXLlqVSRQAAAACQkEMPBQQAAACA9IBgBQAAAAB2IlgBAAAAgJ0IVgAAAABgJ4IVAAAAANiJYAUAAAAAdiJYAQAAAICdCFYAAAAAYCeCFQAAAADYiWAFAAAAAHYiWAEAAACAnQhWAAAAAGAnghUAAAAA2IlgBQAAAAB2IlgBAAAAgJ0IVgAAAABgJ4IVAAAAANiJYAUAAAAAdiJYAQAAAICdCFYAAAAAYCeCFQAAAADYiWAFAAAAAHYiWAEAAACAnQhWAAAAAGAnghUAAAAA2IlgBQAAAAB2IlgBAAAAgJ0IVgAAAABgJ4IVAAAAANiJYAUAAAAAdiJYAQAAAICdCFYAAAAAYCeCFQAAAADY6V8RrOLi4jRlyhTVrl1bPj4+6tChgy5evJjWZQEAAADIIP4VwWrGjBlaunSpRo8erWXLlslkMqlz586KiopK69IAAAAAZADpPlhFRUVp7ty56tmzp+rUqSN3d3dNmjRJ169f19atW9O6PAAAAAAZQLoPVqdPn9bDhw9VrVo1S5urq6s8PDx08ODBNKwMAAAAQEaRJa0LsNe1a9ckSUWKFLFqL1iwoK5evWrz8qKjo2UYho4fP54i9UmSyWRSjREjFBsdnWLLBJ6UOWtWnThxQoZhpHUpCZhMJsXExDhkbfj3iI6Odtg+INEPkDroB0DK9oPo6GiZTKYkzZvug1V4eLgkycnJyao9W7ZsCg0NtXl58W9cUt/ApMpZoECKLg94mpTedlNKlizpfneDdMJR+4BEP0DqoR8AKdMPTCZTxglWzs7Okh5daxX/b0mKjIyUi4uLzcurWLFiitUGAAAAIGNI99dYxQ8BvHHjhlX7jRs3VLhw4bQoCQAAAEAGk+6Dlbu7u3LmzKkDBw5Y2u7du6dTp07Jz88vDSsDAAAAkFGk+6GATk5OCgwM1MSJE5UvXz4VLVpUEyZMUOHChdWwYcO0Lg8AAABABpDug5Uk9erVSzExMRo6dKgiIiLk7++vOXPmJLihBQAAAAA8DyaD+10CAAAAgF3S/TVWAAAAAJDWCFYAAAAAYCeCFQAAAADYiWAFAAAAAHYiWAEAAACAnQhWAAAAAGAnghUcAnf9B5KP/oN/A7ZjAOkdwQrP3YEDB+Tm5qYDBw5IklavXi03NzddvnxZkhQSEqI2bdqkZYlJ5ubmpqlTp6Z1GXAwAQEBGjRokF3LeLJfJMW9e/c0cOBAHTp0yK51A09j63b55P7+aR7fl0ZFRWns2LH68ccf7a73eRs0aJACAgLSugxAEtujIyJYIdXVrVtXy5YtU8GCBSVJGzdu1K+//prGVQHpT3BwsNasWaO4uLi0LgWwybJly/TWW29Jkm7cuKH58+crJiYmjasCAPtkSesCkPHky5dP+fLlS+syAABpxNfXN61LAIAUxxmrDMowDC1evFhNmzaVt7e3GjZsqNmzZ8swDA0aNEjvvfeePvnkE/n5+al58+aKiYlRXFycZs2apYYNG8rT01ONGjXSwoULEyx76dKlatSokby9vRUYGKgrV65YTX98aMnUqVM1bdo0SckbZvfzzz/rnXfeUcWKFVWrVi0NHz5coaGhlukHDx5Ux44d5e/vL09PTwUEBGjq1KmWI/yXL1+Wm5ub5s2bp//85z+qUqWKVq9eLUn65Zdf1KpVK/n4+KhRo0bau3evTbUhY4mOjtbo0aPl7+8vf39/DRw4ULdv37ZM//nnn/X222+rcuXKqlq1qvr27aurV68+c5mHDh1SYGCgfHx8VKVKFatlHjhwQO+++64k6d1331Xbtm0tz9uwYYNatGihihUrqmbNmgn6BZCYuLg4zZgxQ3Xr1pWPj4+6d++eYLs5c+aMunbtqkqVKqlSpUr64IMPdOnSpQTLCgkJ0dtvvy0vLy81bNgwwd+K+P395cuXVb9+fUnS4MGDbR7WdOvWLX388ceqUaOGKlasqHfeeUeHDx+2TL99+7ZGjhypevXqydPTU1WqVNEHH3xgNbSxbdu26tevn3r16qVKlSqpS5cukqTQ0FANHjxYVatWlb+/vyZMmMDZYWjYsGGqVq1agjOsEyZMUJUqVRQVFaUTJ06oY8eOqlq1qipVqqT3339ff/zxh2Xepw2Zbdu2rdW+/Fnf1R63evVqNWrUSF5eXmrWrJl2795tNf3KlSvq06ePqlSpIh8fH7333ns6deqUZfqzvgvBNpyxyqC+/PJLzZkzR+3atVPNmjV18uRJTZo0SVFRUZIefaEzmUyaOnWqHj58qCxZsmj48OFavXq1unbtqooVK+rgwYP67LPPdO/ePX3wwQeSpEWLFunTTz9V27ZtVbduXe3bt0/Dhg17ah1vvfWWrl27ppUrV2rZsmUqXLhwkl/Drl279P777ysgIECTJk1SaGioJkyYoIsXL2rBggU6ffq02rVrp8aNG2vSpEkyDEM//PCDpk2bplKlSum1116zLGvSpEkaPny4XF1d5enpqZMnT6pDhw6qWrWqgoKCLDsl4Gk2btwob29vjRs3Trdv39bEiRN18eJFLV26VD/88IMGDBigJk2aqGvXrrpz546mTJmiVq1a6fvvv1f+/PkTLO/gwYNq3769qlWrpsmTJys0NFRBQUF69913tXLlSlWoUEHDhw/XqFGjNHz4cFWtWlWSNGPGDAUFBentt99W7969denSJQUFBeno0aNavny5nJ2dU/utQToxYcIEffvtt3r//ffl6+urTZs26YsvvrBMP3/+vFq3bq0yZcpo3Lhxio2N1cyZM9WmTRv98MMPVtvx2LFj1bZtW3Xr1k07duzQ6NGjlS1bNv33v/+1WmfBggU1bdo09ejRQ926ddMrr7yS5HrDwsLUunVrRUdHq2/fvipcuLAWLFigTp06aeXKlSpTpoy6du2q0NBQ9e3bVy+88IKCg4MVFBSk4cOHa+7cuZZlbdy4UY0bN9b06dMVGxuruLg4derUSZcvX1a/fv2UP39+ffPNNzp+/LhlGDsyptdff13Lly/Xvn37VLt2bUmPAtCGDRvUuHFjHTlyRJ06dZK/v7/GjBmjqKgoff3112rdurWWL1+usmXLJnldz/quFv+96+rVq5o1a5Y+/PBDubi46Msvv1TPnj21fft25c+fX7dv31br1q3l4uKiYcOGycXFRQsWLNA777yjlStXWtXz5HchJIOBDCc0NNSoUKGC8dlnn1m1jx071mjfvr0xcOBAw2w2GxcuXLBMO3funOHm5mZ8/fXXVs+ZNGmS4eXlZdy+fduIi4szqlevbvTs2dNqnuHDhxtms9nYv3+/YRiGsWrVKsNsNhuXLl0yDMMwpkyZYpjNZptfR4sWLYw33njDqm3Tpk3GK6+8Yly7ds34/vvvjU6dOhmxsbGW6bGxsUblypWNYcOGGYZhGJcuXTLMZrPRt29fq+X07NnTqF27thEZGWlpW79+vWE2m40pU6bYXCv+3erVq2dUrVrVuH//vqVt69athtlsNvbs2WPUrFnTaNeundVzLl68aFSoUMH4/PPPDcNI2C9atWplvPrqq0ZMTIzlOefOnTPKly9vLFq0yDAMw9i/f79V37p7967h6elpDBkyxGpdBw8eNMxms7F48eKUf/H4V4j/uzBu3Dir9o4dO1q2yz59+hjVq1e32s7v3LljVK5c2fK8+G0yfh8br3v37sbLL79s2R8/vi+N3w+vWrXKppoXLVpkuLm5GcHBwZa2iIgIo3HjxsZ3331nXLt2zWjbtq1x8OBBq+d9+umnRoUKFSyPAwMDDU9PT+Phw4eWth07dhhms9nYsWOHpe3hw4dG1apVjXr16tlUJ/5d4uLijICAAGPQoEGWtvh97KFDh4w333zTaNy4sdW+OzQ01KhSpYrx4YcfGoaRcN8dLzAw0AgMDLQ851nf1QzDsHxfCwkJsUz/+eefDbPZbGzbts0wDMP48ssvDS8vL+Py5cuWeSIjI4369etbvq897bsQbMdQwAzo6NGjio6OVsOGDa3aBw0aZDmC5+zsrBIlSlim7d+/X4ZhKCAgQDExMZb/AgICFBkZqcOHD+vcuXO6deuWZVhHvP/85z8p/hoiIiJ08uRJNWjQwKq9UaNG2rx5swoVKqQ33nhDs2fPVnR0tP744w9t27ZNU6dOVWxsrKKjo62eZzabrR4fPnxYtWvXlpOTk6XtlVdeUebMmVP8teDfoU6dOsqZM6flcUBAgLJmzarly5fr5s2bVmdIJalEiRKqWLFiondPCw8P17Fjx1SnTh0ZhmHpb8WLF1fZsmX1888/J1rD0aNHFRUVlWBdfn5+Klq06D/eqQ0ZV/zfhWftv/fv36+qVavK2dnZsk3mzJlTfn5+CYZKN2nSxOpxw4YNde3aNZ07dy7Faj506JCKFSsmd3d3S1u2bNm0ceNGtW7dWoUKFdK3334rPz8/XblyRfv27dOiRYt05MiRBH8DihUrpuzZs1stO2vWrHr55ZctbdmzZ1edOnVSrH6kTyaTSc2aNdPWrVsto3zWrVun4sWLq3z58jpx4oSaNGli9X3B1dVV9erVs2kfnJTvapKUN29eq7NOxYsXlyTdv39fkrRv3z6VL19ehQoVsvTbTJky6eWXX07Qb5/8LgTbMRQwA7p7964kPfMGEvnz55fJZErwnKZNmyY6//Xr1y3Le3K5L7zwgh3VJi40NFSGYSQ6hCpeRESEPv30U/3www+KiYlRsWLFVLFiRWXJkiXB+OQCBQokWP6TryNLlizKmzdvyr0I/Ks8uQ1lypRJefLksfxxe3J6fNvj49zj3bt3T3FxcZo9e7Zmz56dYHq2bNkSrSH+epinrSu+FuBJ8dvOs/bfd+/e1YYNG7Rhw4YEz/+n/X78vjolr/W7e/fuM/8GSNLatWv15Zdf6urVq8qTJ4/c3d0THQ6b2N+APHnyKFMm6+PPz+PvGdKfN954QzNmzNDu3btVt25dbdq0SW+//bbu378vwzBSZB+clO9qkqwOCEiyfHeLvx7w7t27unjxoipUqJDo88PDw61qhH0IVhmQq6urpEcX9ZYpU8bSfvXqVV28eDHBkbzHn7NgwQLlyJEjwfQXX3xR9+7dk/ToYuLHxe8cUlLOnDllMpmsbg4gPfo9lH379snb21tffvmlNm/erMmTJ6tGjRqWnU/16tX/cfl58uTR33//bdVmGAY3AMBTxW//8WJjY3Xnzh3LWawntydJunnzZqJhPUeOHDKZTGrXrl2iBzNcXFwSrSF37tyWdT05jv/mzZuWI5nAk+K3w1u3bln9XXh8/50rVy7VqFFD7du3T/D8LFmsv048ua+M3/7/KQjZIleuXIn+vtavv/6qnDlzKjQ0VAMHDlRgYKA6duxouYb3888/t7rBRWLy5s2rO3fuKDY21urMw/P4e4b0p2TJkvL19dXGjRuVNWtW3blzR82aNVOuXLlkMpmeur/PkyePpIThJ97Dhw8t37H+6bta5cqVk1Rrrly5VKVKFQ0YMCDR6Y+PzIH9GAqYAXl7eytr1qz66aefrNoXLFigDz/80OpMVTx/f39J0p07d+Tl5WX57+7du5o8ebLu3r2rUqVKqUiRItq0aZPVc3fs2PHMep48IpgUOXLkUPny5RO8hv/7v/9Tly5ddO3aNR0+fFhVq1ZVgwYNLKHqt99+0+3bt//xzk7Vq1fX7t27rY7k7NmzJ9HQCUjS3r17re4StXnzZsXExKhVq1Z64YUXEvz46aVLl3T06FFVqlQpwbJy5swpDw8PnTt3zqq/vfTSS5o2bZplOMmTQ1N9fHzk5OSUYF2HDh3SlStXEl0XIEkVK1aUs7PzM/ffVapUUUhIiMqXL2/ZJj09PTV//nxt3brV6nl79uyxerx+/XoVKVJEJUuWTLDu5A6x9vPz06VLl/T7779b2qKiotSzZ08tX75cv/76q+Li4tSrVy9LqIqNjbUMf3rW34Hq1asrJiZG27Zts1r204bhIuOJv/veunXr5Ovrq1KlSil79uzy9PTUhg0bFBsba5n3/v372rlzpyUMxR9we/zOsKGhoTp79qzlcXK+qyWmSpUqOn/+vEqXLm3192Tt2rVasWIFlzikMM5YZUD58uXTu+++qwULFsjJyUnVqlXTiRMntGjRIvXp00dnzpxJ8Byz2axmzZpp2LBh+uuvv+Tp6anz589r0qRJKlasmEqVKiWTyaR+/fqpb9++Gjp0qBo3bqyjR4/qu+++e2Y98Udl1q1bJx8fnyQfVe/Vq5e6deumjz76SC1atNDt27f1xRdfqF69eipfvry8vb21ceNGfffddypbtqxOnz6tmTNnymQyWQWmxHzwwQfatm2bOnbsqE6dOunOnTuaNGmSsmbNmqTakPH8/fff6tmzp9q2basLFy7oyy+/VM2aNVWzZk316dNHgwcPVu/evfXGG2/ozp07mjZtmnLnzp3o0X9J6tOnj7p06aK+ffuqWbNmio2N1dy5c3Xs2DF169ZN0qMjkZK0c+dO5c6dW+7u7urSpYumTZumrFmzqn79+rp8+bKCgoJUrlw5tWjRItXeD6QvOXLkUPfu3TV58mS5uLioWrVq2rVrl1Ww6t69u1q3bq2uXbuqTZs2ypYtm5YtW6Zt27ZpypQpVstbuHChcuTIIQ8PD61fv1579uzR559/nuiXwfjteN++fSpbtqx8fHySVHOLFi20cOFCdevWTR9++KHy5cunxYsXKyIiQm3btrV8aR01apRatmype/fuadGiRTp9+rSkR3cVfPy6yMdVr15dtWrV0tChQ3Xr1i0VLVpU3377rW7fvp2iZ92QfjVt2lRjx47V+vXrNWTIEEt73759Ld8dAgMDFR0drVmzZikqKko9evSQ9OjnBooUKaJp06YpV65cypQpk2bNmmU1GuGfvqs9eZb4adq1a6cffvhB7dq1U4cOHZQ3b15t2LBBy5cv1+DBg1P2TQF3Bcyo4uLijDlz5hgNGjQwPD09jcaNG1vuGDZw4MBE73oUHR1tTJs2zahfv75RoUIF4+WXXzY++eQT486dO1bzrV+/3mjatKnh6elptGjRwli3bt0z7wp47do1o2XLlkaFChWMTz75xKbXsXPnTqNly5aGp6enUbt2bWPMmDHGgwcPDMN4dLeqPn36GFWqVDF8fX2NV1991ViwYIExbNgwo2bNmkZMTMwz70b122+/GYGBgYa3t7dRr149Y+3atUaNGjW4KyASqFevnjF69Ghj6NChhq+vr1GlShVjxIgRVncZ27Rpk9G8eXOjQoUKRtWqVY1+/foZV65csUx/sl8YhmHs3bvXePvttw1vb2+jcuXKxrvvvmt1h7PY2FijT58+hpeXl9G0aVNL+5IlS4wmTZoYFSpUMGrWrGmMGDHCuHv37nN+F/Bv8O233xr169c3PD09jbZt2xpLliyx2i5/++03o2PHjkbFihUNX19f47///a/l7mOG8b+7na1fv96yX2/cuLGxbt06q/U8eYfVsWPHGr6+voafn5/V3Vj/ybVr14w+ffoY/v7+RsWKFY127doZp06dskxftGiR5fXUrVvXGDhwoOWOnTt37jQMw/pObI8LCwszRo0aZVStWtXw9fU1Pv74Y2P06NHcFRAW3bt3NypUqGDcvn3bqn3//v2Wfbefn5/x/vvvG2fOnLGa59ixY0arVq0s2+a8efOMYcOGWW2Lz/quZhiJf19L7HvNxYsXjV69ehn+/v6Gt7e30axZM2PFihXPfA6Sx2QYT1zFDwAAAACwCUMB4VAMw7Aal/w0mTNnTvL4YgBA+vH4tYpPYzKZuDYEgMPhjBUcyurVq5M05nfs2LFcLwIA/0Jubm7/OE+VKlW0cOHCVKgGAJKOYAWHcufOnURvn/ukYsWK8ZtSAPAvdOLEiX+cJ0eOHFa3oAYAR0CwAgAAAAA78TtWAAAAAGAnghUAAAAA2IlgBQAAAAB2IlgBAAAAgJ0IVgAAAABgJ4IVAAAAANiJYAUAAAAAdvp/pF/a0j6wCSQAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 1000x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(10, 5))\n",
    "\n",
    "colors = [\"#800000\", \"#D3D3D3\", \"#D3D3D3\", \"#D3D3D3\"]\n",
    "\n",
    "sns.barplot( \n",
    "    x=\"payment_type\",\n",
    "    y=\"payment_value\",\n",
    "    data=df_payment.sort_values(by=\"payment_value\", ascending = False),\n",
    "    palette=colors\n",
    ")\n",
    "plt.title(\"persebaran pembelian berdasarkan bagian hari\", loc=\"center\", fontsize=15)\n",
    "plt.ylabel(\"nilai transaksi\")\n",
    "plt.xlabel(None)\n",
    "plt.tick_params(axis='x', labelsize=12)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "37e3fc29",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:34.551875Z",
     "iopub.status.busy": "2023-10-18T10:08:34.550816Z",
     "iopub.status.idle": "2023-10-18T10:08:34.741075Z",
     "shell.execute_reply": "2023-10-18T10:08:34.739931Z"
    },
    "papermill": {
     "duration": 0.230781,
     "end_time": "2023-10-18T10:08:34.743432",
     "exception": false,
     "start_time": "2023-10-18T10:08:34.512651",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, 'Payment Type Distribution')"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAdUAAAGaCAYAAABZt9lOAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8qNh9FAAAACXBIWXMAAA9hAAAPYQGoP6dpAABb2ElEQVR4nO3dd3xUVf7/8de56YUEQockENLoIUoTUIqAgqiguIqK6yqKgK5iRf2uva2KoKKIFVx/dsGKYlkRlg4CoQYINYFAgEAS0uee3x83GYgECGR6Ps/Hg4fJzM2dz8zEvOece4rSWmuEEEIIUWuGuwsQQgghfIWEqhBCCOEgEqpCCCGEg0ioCiGEEA4ioSqEEEI4iISqEEII4SASqkIIIYSDSKgKIYQQDiKhKkQ1ZE2UmvGE18kTahCikoSqOK3Ro0eTnJxc5V/Hjh3p168fTz75JEePHnV3iQ63bds2Ro0adcr7Z8+efdJrUt2/zMxMF1Z9skmTJlWpp23btnTp0oVhw4bxxhtvUFJSUuX40aNHM3r06Bqff9WqVYwdO/aMx73++uskJyef8+OczvTp03nvvfdO+VhCuJq/uwsQnq99+/Y8/vjj9u/LysrYsGEDr7zyCps2beKTTz5BKeXGCh3rxx9/ZPXq1ae8v1+/fnz22Wf27+fPn8/06dOZNm0ajRs3tt/epEkTp9ZZE40bN2batGkAmKZJfn4+K1asYPr06SxatIgPPviAoKAggCrvcU188cUXbNu27YzHXXPNNVx44YVnX3wNTJ06lTvvvNMljyVETUioijMKDw+nS5cuVW7r1q0bx44d47XXXmPt2rUn3e/LoqKiiIqKsn+/fft2ANq1a0d0dLS7yqpWYGDgSe9N3759SUlJ4c477+T9999n3LhxACQkJDilhmbNmtGsWTOnnNudjyVEdaT7V5yzjh07ArB3714AbDYbb7/9NsOGDaNz58506dKF6667jiVLlgCwdetWkpOTq7TyAPbv30+7du2YM2cOmZmZJCcnM2/ePMaPH0+XLl3o1asXb775JgUFBTzyyCOcf/759OrVi5deeqnK9bSSkhJefPFF+vbtS8eOHbn88suZO3dulccaMGAAr732Gv/+97/p1asXnTt35tZbb2XHjh2A1X1Y2bJLTk7m9ddfP6fXpry8nD59+nDfffeddN+QIUN4+OGH7fVMmTKF559/nu7du9O9e3ceeOABcnNzq/zMypUrufHGG0lJSaF79+489NBDHD58+JxqAxg0aBCdO3fm008/td/2127ZxYsXc+2115Kamkq3bt0YP368/QPEpEmTmDNnDllZWSQnJzN79mz7e/fBBx8wZMgQunfvzuzZs0/ZJfvGG2/Qq1cvUlNTGT9+PHv27LHfd6qfOfE9qbx/2rRp9q+r+7m5c+dy1VVXkZqaSu/evXnssceqXLZ4/fXXGTRoEPPnz+fyyy+nY8eOXHLJJcyZM+esX1chJFTFOasMopiYGABefvll3njjDa699lreffddnnrqKXJzc7n77rspLCwkMTGRlJQUvvnmmyrn+eabbwgODuaSSy6x3/boo4+SlJTE9OnT6dmzJ6+++iojR44kODiYV199lQEDBvDuu+/y008/AdZglQkTJvDpp5/yj3/8g+nTp5OamsrEiRP5+uuvqzzehx9+yPbt23n++ed55plnWL9+PZMmTQKs7sORI0cC8Nlnn3HNNdec02vj7+/P8OHD+fXXXykoKLDfvnbtWrZv385VV11lv+3jjz9m1apVPPfcc9x///0sWLCAMWPGYJomACtWrODmm28mODiYqVOn8sgjj7B8+XJuuukmiouLz6k+gD59+pCdnU1WVtZJ9+3Zs4dx48bRoUMHpk+fzjPPPMP27du5/fbbMU2T8ePH07dvXxo3bsxnn31Gv3797D87ZcoUbr31Vp555hl69uxZ7WOvWrWK7777jscee4xnnnmGzZs3c/PNN1NaWlrj+is/nI0cOfKkD2qV3nzzTSZOnEhKSgqvvfYaEyZMYN68eYwePbrKa5eTk8NTTz3FTTfdxNtvv010dDSTJk0iIyOjxvUIAdL9K2pAa015ebn9+6NHj7J8+XKmT59Oly5d7C3WAwcOMHHixCqtneDgYO666y7S09NJTU3l6quv5rHHHmPPnj32MP76668ZMmQIoaGh9tbXhRdeyD333ANY3ZI//PADDRs25LHHHgOgd+/e/Pjjj/z5558MGTKExYsXs3DhQqZMmcLQoUPt5ygqKuLll19m2LBh+Ptbv+4RERG8+eab+Pn5AbB7925ef/11cnNzq3Qf1rZL++qrr+add95h3rx5XH311QDMmTOH2NhYunbtaj9OKcUHH3xAvXr1AKt7ecKECSxYsIB+/foxefJk4uLimDFjhr3mlJQULrvsMr766ituuOGGc6qvUaNGABw8eJCWLVtWuS8tLY3i4mLGjh1L06ZNAWjevDm//fYbhYWFxMbGEhUVVaV7ubCwEIDBgwfbP5icimEYvPfee/bHjY+PZ/jw4cyZM4drr722RvVXPm6zZs2qfa+OHj3K9OnTueaaa6pcL05KSuKGG25g9uzZXH/99QAUFRXx7LPPcsEFFwDQunVr+vfvzx9//EF8fHyN6hECpKUqamDFihV06NDB/q9Xr17ce++9dOjQgVdeecU+SGny5MncfPPNHD58mNWrVzN79my+/fZbwBrcBHDZZZcREhJib62mpaWRkZFRpeUGkJqaav+6cvBPSkqK/TalFJGRkeTn5wOwZMkSlFL07duX8vJy+78BAwaQk5PD1q1b7T/bqVMnezgB9hAtKipyzAtWIS4ujvPPP9/+XEtLS5k7dy7Dhw+vMrCrf//+9kAFq0s4ICCAlStXUlRUxNq1a+nbt6/9w015eTkxMTHEx8ezaNGiWtdZ3SCzlJQUgoKCGDlyJM8//zyLFy+mbdu2TJw4kfDw8NOeLykp6YyP2aVLlypB3rZtW6Kjo1m8ePHZP4FTWLNmDaWlpVx++eVVbu/atSstW7Zk2bJlJ9VUqfJ3ovKDghA1JS1VcUYdOnTgySefBKw/wEFBQTRv3vykP67r1q3jySefZN26dQQHB5OQkGD/w1l57TM8PJxLL72Ub7/9ljvvvJM5c+bQqlWrKi23yuP+KiQk5JQ1HjlyBK015513XrX3HzhwgHbt2lV7HsOwPltWdrc60siRI3nkkUfYu3cva9euJS8vjxEjRlQ55q+jhA3DoH79+uTl5ZGXl4dpmrzzzju88847J52/cuTuuThw4ACAvSV6oujoaD766CPefvttPv/8c2bOnElERATXX389d999t/01q05lC/h0qjumYcOG5OXlncUzOL3K66bVPVajRo3sH8gqnfh7Ufn8ZA6sOFsSquKMwsLC6NSp02mPKSgoYMyYMSQnJ/P9998THx+PYRj88ccfzJs3r8qxV199NXPmzCEtLc1+fau26tWrR2hoKB9++GG197dq1arWj3EuLr30Up555hnmzZvH6tWrueCCC2jRokWVY44cOVLle5vNRm5uLlFRUYSFhaGU4uabb+ayyy476fyn+6BxJosXL6ZVq1bVhipA586dmTZtGqWlpaxatYrPPvuMt956i+TkZHsX+7mqLjxzcnLsPRSVrWebzWbvVTh27NhZPUZkZCRgdW//tQs3JyfHfvlBCEeS7l/hENu3b+fIkSPcdNNNJCYm2j/pL1iwAKjaCuzWrRutW7fmpZdeIjc3l+HDh9f68bt3705hYSFaazp16mT/t3XrVt54440q14TP5HStsLMVGhrK0KFD+f7771m4cOFJrVSAhQsXVhmg89tvv1FeXs4FF1xAeHg47du3Z/v27VWeV2JiItOmTTupC7Om5s+fT1pa2ikXuZg5cyYDBgygtLSUwMBALrjgAp5++mkA9u3bB9TudVq9enWVlmJaWhpZWVn2gU2VPRWVjwXw559/nnSe09WQkpJCYGAg3333XZXbV65cyd69e0/ZqyFEbUhLVThEXFwc4eHhvPXWW/j7++Pv78+8efP48ssvgZOvV1599dVMnjyZ3r1707x581o/ft++fe3TPsaPH098fDxpaWm8/vrr9OnTp8q80jOJiIgA4PvvvyclJaXWLZqRI0dy7bXXEh4ezuDBg0+6Pzs7m3HjxnHTTTexb98+XnnlFfr06UOPHj0AuPfee7n99tu57777uOKKK7DZbLz//vusXbvWPsf0VEpLS1mzZg1gdWXm5eWxcuVKPvzwQ3r06MGNN95Y7c/17NmTl19+mQkTJnDjjTfi5+fHp59+SmBgIP379wes1+ngwYP88ccf9q71mjJNk9tvv5077riD3NxcJk+eTFJSEldccQVgvZ/PP/88//rXv7jtttvIzs5m2rRphIWFVTlPREQEq1evZsWKFSddQqhfvz63334706ZNIyAggIsvvpjMzExeffVVEhISTrqOL4QjSEtVOES9evV488030Vpz99138+CDD7J3714++ugjwsLCWLlyZZXjK6dgOOoPm2EYvP3221x22WXMmDGDW2+9lU8//ZSbb76ZKVOmnNW5Bg8eTKdOnZg0aVKVJfDOVZcuXWjQoAGXXXYZwcHBJ91/2WWXERsbyz333MPrr7/OiBEjeOONN+z39+nTh/fee4/s7Gz++c9/8uCDD+Ln58cHH3xwxhHKOTk5XHvttVx77bWMGjWKSZMmsWzZMh588EHeffddAgICqv25tm3b8tZbb1FQUMC9997LnXfeyZEjR3j//fdp06YNYL13LVu2ZMKECSdNWzqT/v37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\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df_payment = orders.groupby(by=\"payment_type\")[\"order_id\"].nunique().reset_index()\n",
    "palette_color = sns.color_palette('Reds') \n",
    "\n",
    "plt.pie(df_payment[\"order_id\"], labels=df_payment[\"payment_type\"], colors=palette_color, autopct='%.0f%%')\n",
    "plt.title(\"Payment Type Distribution\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "95702b9f",
   "metadata": {
    "papermill": {
     "duration": 0.039275,
     "end_time": "2023-10-18T10:08:34.819088",
     "exception": false,
     "start_time": "2023-10-18T10:08:34.779813",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "penggunaan credit card adalah tipe transaksi yang paling sering digunakan dan digunankan untuk transaksi yang bernilai besar dibandingkan tipe transaksi lain."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "157e68fd",
   "metadata": {
    "papermill": {
     "duration": 0.035941,
     "end_time": "2023-10-18T10:08:34.891184",
     "exception": false,
     "start_time": "2023-10-18T10:08:34.855243",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## Pertanyaan 4: Bagaimana perbandingan penjualan tahun 2017 dan 2018?\n",
    "karena tahun 2018 hanya terdata sampai bulan agustus maka dalam EDA ini,perbandingan dilakukan untuk bulan januari sampai agustus saja."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "1699d217",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:34.963178Z",
     "iopub.status.busy": "2023-10-18T10:08:34.962808Z",
     "iopub.status.idle": "2023-10-18T10:08:35.450349Z",
     "shell.execute_reply": "2023-10-18T10:08:35.448545Z"
    },
    "papermill": {
     "duration": 0.525716,
     "end_time": "2023-10-18T10:08:35.452789",
     "exception": false,
     "start_time": "2023-10-18T10:08:34.927073",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "orders['nomor_bulan'] = orders['order_purchase_timestamp'].dt.strftime('%m')\n",
    "df_tanggal_penjualan = orders.groupby(by=[\"nomor_bulan\",\"year\"]).order_id.nunique().reset_index()\n",
    "df_tanggal_penjualan[\"nomor_bulan\"] = df_tanggal_penjualan[\"nomor_bulan\"].astype(str).astype(int)\n",
    "df_tanggal_penjualan = df_tanggal_penjualan[df_tanggal_penjualan[\"nomor_bulan\"] < 9]\n",
    "\n",
    "month_names = {\n",
    "    1: 'Jan',\n",
    "    2: 'Feb',\n",
    "    3: 'Mar',\n",
    "    4: 'Apr',\n",
    "    5: 'Mei',\n",
    "    6: 'Jun',\n",
    "    7: 'Jul',\n",
    "    8: 'Aug'\n",
    "}\n",
    "df_tanggal_penjualan['nama_bulan'] = df_tanggal_penjualan['nomor_bulan'].map(month_names)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "420646df",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:35.526240Z",
     "iopub.status.busy": "2023-10-18T10:08:35.525829Z",
     "iopub.status.idle": "2023-10-18T10:08:36.199503Z",
     "shell.execute_reply": "2023-10-18T10:08:36.198185Z"
    },
    "papermill": {
     "duration": 0.712025,
     "end_time": "2023-10-18T10:08:36.201707",
     "exception": false,
     "start_time": "2023-10-18T10:08:35.489682",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0.5, 33.20312499999997, '')"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABPwAAAIzCAYAAACUUwetAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8qNh9FAAAACXBIWXMAAA9hAAAPYQGoP6dpAABRWUlEQVR4nO3de5yWdZ0//tdwGAYCQhGBXA+ECZIBKpNkIoZSHjpN2LauUOI5W900QQ1zYQu1QlFMUmBMywNYkplmRW5bv8xUMLXiYLg45QFJPKByGA7z+6MvUxPEzMDADZfP5+Mxj535XJ/rc73v2Xc3t6+5DmV1dXV1AQAAAAAKoVWpCwAAAAAAWo7ADwAAAAAKROAHAAAAAAUi8AMAAACAAhH4AQAAAECBCPwAAAAAoEAEfgAAAABQIAI/AAAAACgQgd9WWLRoURYtWlTqMgAAAABgE21KXcCuqLa2ttQlAAAAAMBmOcMPAAAAAApE4AcAAAAABSLwAwAAAIACEfgBAAAAQIEI/AAAAACgQAR+AAAAAFAgJQ38Hn744fTp02ezX0cffXSSZMGCBRk5cmQGDhyYo446KtXV1Q3W2LBhQ6ZMmZIhQ4ZkwIABOfXUU1NTU9NgTmNrAAAAAEBRlDTwO/jgg/OrX/2qwddNN92UNm3a5Oyzz84rr7yS0aNHZ7/99stdd92Vc889N9dee23uuuuu+jWmTp2amTNn5itf+UpmzZqVsrKynHHGGamtrU2SJq0BAAAAAEXRppQHLy8vT7du3ep/Xrt2ba644op88IMfzCc/+cnceOONKS8vz/jx49OmTZv07t07NTU1mT59ekaMGJHa2trcdNNNGTNmTIYOHZokmTx5coYMGZI5c+bkhBNOyJ133rnFNQAAAACgSHaqe/jddttteeGFF3LJJZckSebOnZvKysq0afO3XHLw4MFZsmRJli9fnoULF+bNN9/M4MGD67d37tw5/fr1y6OPPtqkNQAAAACgSHaawG/NmjW54YYb8pnPfCZ77rlnkmTp0qXp0aNHg3kbtz3//PNZunRpkqRnz56bzHnhhReatAYAAAAAFElJL+n9ez/4wQ+yZs2ajBo1qn5s9erVKS8vbzCvXbt2Sf4aEK5atSpJNjvntddea9IaW6uuri4rV67c6v0BAAAAdmUdOnQodQn8EztN4Hf33Xfngx/8YHbbbbf6sYqKivqHb2y0MaTr0KFDKioqkiS1tbX132+c0759+yatsbXWrl2bBQsWbPX+AAAAALuyQw89tNQl8E/sFIHfyy+/nN/+9rc566yzGoz36NEjy5YtazC28efu3btn3bp19WP77LNPgzl9+/Zt0hpbq23bttl///23en8AAAAA2B52isDvscceS1lZWd773vc2GK+srMzMmTOzfv36tG7dOkny0EMPpVevXunatWs6deqUjh075uGHH64P/FasWJH58+dn5MiRTVpja5WVlTl1FQAAAICdzk7x0I6FCxdm7733rr8Md6MRI0bkjTfeyLhx47J48eLMnj07t9xyS/2ZgOXl5Rk5cmQmTZqUBx54IAsXLsz555+fHj16ZPjw4U1aAwAAAACKZKc4w++ll15Kly5dNhnv2rVrZsyYkYkTJ6aqqirdunXL2LFjU1VVVT/nvPPOy7p163LppZdm9erVqaysTHV1df2DOpqyBgAAAAAURVldXV1dqYvY1fzud79LkrznPe8pcSUAAAAA0NBOcUkvAAAAANAyBH4AAAAAUCACPwAAAAAoEIEfAAAAABSIwA8AAAAACkTgR4vYsH59qUvYbor82gAAAIDiaVPqAiiGVq1b5ztnnpllixaVupQWtWefPhk1bVqpy4C3hA3r16dV69alLmO7KPJrAwAAdj4CP1rMskWL8uyTT5a6DGAX5Q8HAAAALUPgB8BOwx8OAAAAtp17+AEAAABAgQj8AAAAAKBABH4AAAAAUCACPwAAAAAoEIEfAAAAABSIwA8AAAAACkTgBwAAAAAFIvADAAAAgAIR+AEAAABAgQj8AAAohA3r15e6hO2iqK8LANh+2pS6AAAAaAmtWrfOd848M8sWLSp1KS1mzz59MmratFKXAQDsYgR+AAAUxrJFi/Lsk0+WugwAgJJySS8AAAAAFIjADwAAAAAKROAHAAAAAAUi8AMAAACAAhH4AQC7hA3r15e6hO2iqK8LAIDS8ZReAGCX0Kp163znzDOzbNGiUpfSYvbs0yejpk0rdRkAABSMwA8A2GUsW7Qozz75ZKnLAACAnZpLegEAAACgQAR+AAAAAFAgAj8AAAAAKBCBHwAAAAAUiMAPAAAAAApE4AcAAAAABSLwAwAAAIACEfgBAAAAQIEI/AAAAACgQAR+AAAAAFAgAj8AAAAAKBCBH7BDbFi/vtQl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jB5hV9PswO+rX/1qunbtmu985zvp0KFDDjrooCTJVVddlTVr1uSGG25ocuB31113Zfny5ZvM/6//+q9UV1fnHe94R5YtW9Zg28afu3fvnnXr1tWP7bPPPg3m9O3bN0nSo0ePLa6xtcrKypy6+hZS9FO32XZ6hMboEbZEf9AYPUJj9AiN0SM0Ro8US7MDv4ceeiiXX355OnfunPXr1zfY9qlPfSqf//znm7zWpEmTsnr16gZjH/zgB3Peeefl+OOPz3333ZeZM2dm/fr1ad26df3xe/Xqla5du6ZTp07p2LFjHn744frAb8WKFZk/f35GjhyZJKmsrNziGgAAAEDLqKure0ucDQc7u626h9/G4Owf1dbWNut/2P/sDLuuXbtmr732yogRIzJjxoyMGzcup59+ep588snccsstmTBhQpK/3rtv5MiRmTRpUnbffffstdde+frXv54ePXpk+PDhSdLoGgAAAEDLKCsrS+3imtSt2vp75u+MWnXplLZ792x8Iuwkmh34DRo0KNOmTcvhhx9e//CLsrKybNiwIXfccUcOOeSQFiuua9eumTFjRiZOnJiqqqp069YtY8eOTVVVVf2c8847L+vWrcull16a1atXp7KyMtXV1fUP6mjKGgAAAEDLqFu1JnUri/WAkLqKdqUuAZql2YHfF77whZx00kn54Ac/mMMOOyxlZWWprq7O008/nZqamtx+++3bVNCiRYsa/Ny/f//MmjXrn85v3bp1xowZkzFjxvzTOY2tAQAAAABF0aq5OxxwwAG56667cthhh+Xhhx9O69at8+tf/zr77LNPZs6cmQMPPHB71AkAAAAANMFW3cNvv/32y1VXXdXStQAAAAAA26hJgd/zzz/frEXf8Y53bFUxAAAAAMC2aVLgN2zYsGY9fXfBggVbXRAAAAAAsPWaFPhdfvnl9YHfa6+9lkmTJuV973tfjjvuuHTr1i2vvvpq/ud//if/+7//m4svvni7FgwAAAAA/HNNCvw+8YlP1H//uc99LlVVVfnyl7/cYM5HPvKRTJw4Mffff38+9alPtWyVAAAAAECTNPspvQ8++GCOPfbYzW476qij8tvf/nabiwIAAAAAtk6zA7/ddtstjz/++Ga3/eY3v0n37t23tSYAAAAAYCs16ZLev/fJT34yU6dOzapVqzJs2LDsvvvueemll/LjH/84d9xxR774xS9ujzoBAAAAgCZoduD32c9+Nq+//npuvvnmVFdXJ0nq6upSUVGR//zP/8zJJ5/c4kUCAAAAAE3T7MBvxYoVueiii3LOOefk8ccfz2uvvZbddtstBx98cDp06LA9agQAAACALfrqV7+a2267LQ8++GA6depUPz5t2rR885vfzIMPPphnn302V111VR599NEkyfve975cfPHF2XvvvevnL1y4MN/4xjcyd+7cvP7669l9993zoQ99KBdeeGEqKiqSJH369Mm5556bn//853nmmWdy2mmn5ZxzztmxL3gLmn0Pv09+8pP50Y9+lE6dOmXIkCH58Ic/nPe///3CPgAAAABK5sQTT8yaNWvy4x//uMH43XffnWOPPTYvvvhi/u3f/i3Lly/PlVdemYkTJ+bPf/5zTjrppCxfvjxJsmzZspx88slZtWpVrrzyykyfPj3HHXdcvvOd7+Tmm29usO43v/nNfOhDH8rVV1+do48+eke9zCZp9hl+G8/oAwAAAICdRe/evXPwwQfnBz/4QT75yU8mSZ588sk8/fTT+e///u984xvfSEVFRW6++eZ07NgxyV/P8DvmmGMyY8aMXHTRRXnqqady4IEH5tprr62fc/jhh+ehhx7Ko48+mrPPPrv+eP3798+ZZ565419oEzT7DL9Pf/rT+drXvpbf/OY3efnll7dHTQAAAOyk6urqSl0CwD81YsSIzJ07N88++2ySZPbs2dlnn30yaNCg/OY3v8lhhx2WioqKrFu3LuvWrUvHjh0zaNCg/PrXv06SHHHEEbn11lvTrl27LFmyJD//+c9zww035OWXX05tbW2DYx1wwAE7/PU1VbPP8PvBD36Q559/PqNHj97s9rKyssyfP3+bCwMAAGDnU1ZWltrFNalbtabUpbSYVl06pe3ePUtdBtACjj/++Fx++eW55557cvrpp+f+++/PZz7zmSTJq6++mh/96Ef50Y9+tMl+u+++e5Jkw4YNufrqq3Pbbbdl5cqV6dmzZ/r375927dptss8ee+yxfV/MNmh24PfRj350e9QBAADALqJu1ZrUrVxV6jJaTF3Fpv8hD+ya3va2t+XYY4/N/fffnwMPPDArVqzIxz/+8SRJp06dcvjhh2/2JLY2bf4akU2bNi0333xzxo8fnw996EP1D/848cQTd9hraAnNDvz+4z/+Y3vUAQAAAADb7MQTT8zs2bNz0003ZfDgwXnHO96RJHnve9+bxYsX58ADD6wP+Orq6nLhhRdm3333zYEHHph58+Zl//33bxDwvfjii3nqqafynve8pySvZ2s0O/BLktra2syePTsPP/xwVqxYkd122y2DBg1KVVXVZk9xBAAAAIAd4dBDD8073/nOPPLII5k0aVL9+DnnnJN/+7d/y1lnnZWTTjop7dq1y6xZs/Kzn/0sU6ZMSfLXB3FMnTo106ZNy8CBA1NTU5Mbb7wxtbW1WbVq1zmzudmB34oVK/LpT386CxcuzDve8Y5069YtS5Ysyb333pvbbrstt99+e/3pjgAAAACwox111FH5y1/+kuHDh9eP9e3bN7fddlsmT56csWPHpq6uLgcccECuv/76HH300UmSs846K6+88kq+/e1v5/rrr0/Pnj3zsY99LGVlZbnxxhvz2muv5e1vf3upXlaTNTvwu+qqq7J06dLceuutGTRoUP343Llzc9555+Xaa6/NpZde2qJFAgAAAEBT1NXV5f/7//6/fOxjH0tFRUWDbe9+97szY8aMf7pveXl5Lrvsslx22WWbbPv729wtWrSo5QreDlo1d4cHHnggn//85xuEfUkyaNCgnHfeefnpT3/aYsUBAAAAQFO88cYb+cY3vpGzzz47zzzzTP3Ted+Kmn2G35tvvpm99957s9v23nvvvPrqq9taEwAAAAA0S0VFRWbOnJkNGzZk4sSJ2WeffUpdUsk0O/B75zvfmZ///Od5//vfv8m2Bx54IPvuu2+LFAYAAAAATdWmTZv86le/KnUZO4VmB36nnXZaLrjggtTW1uYjH/lI9thjj7z00kv54Q9/mO9+97sZP378digTAAAAAGiKZgd+xx9/fJ555pnccMMN+e53v5vkrzdDLC8vz+c+97l86lOfavEiAQAAAICmaXbglyTnnHNORo4cmccff7z+ccQDBgzYJR5LDAAAAABFtlWBX5J07tw5Rx55ZEvWAgAAAABso1alLgAAAAAAaDkCPwAAAAAoEIEfAAAAABSIwA8AAACAHaKurm6XOvarr76ayy67LEceeWQOOeSQnHTSSZk7d2799gULFmTkyJEZOHBgjjrqqFRXV//TtaZOnZpRo0Y1GBs1alT69Omz2a+777672fVu1KSHdjT3AB//+Me3ohQAAAAAiqysrCy1i2tSt2rNjj1u+3Yp33/fZu93wQUXZPny5bn66quz++675/bbb89pp52W2bNnZ/fdd8/o0aNzzDHHZMKECXn88cczYcKEdOnSJSNGjGiwzs0335wpU6aksrKywfh1112XtWvXNhi79NJL86c//SnHHHNM81/o/9OkwO/iiy9u8oJlZWUCPwAAAAA2q27VmtStXFXqMhpVU1OTBx98MHfccUcOOeSQJMm4cePyy1/+Mvfee28qKipSXl6e8ePHp02bNundu3dqamoyffr0+sDvxRdfzLhx4zJv3rz06tVrk2N06dKlwc/33ntvfvWrX2X27Nnp2LHjVtfepMDvgQce2OoDAACw86irq0tZWVmpywAA2OnttttumTZtWg466KD6sbKystTV1eW1117L73//+1RWVqZNm7/Fa4MHD86NN96Y5cuXp2vXrvnDH/6Qt7/97bnnnnty/fXX57nnnvunx1u5cmW+9rWv5TOf+Uz69OmzTbU3KfDba6+9mrxgKa/FBgBgy0p1Gc321qpLp7Tdu2epywAACqRz584ZOnRog7H7778/f/rTn3LEEUdk8uTJOeCAAxps33PPPZMkzz//fLp27Zphw4Zl2LBhTTrezJkz8+abb+azn/3sNtfepMDvH91333155JFHsnbt2vqAr66uLitXrszjjz+eX/7yl9tcGAAA28euchlNc9RVtCt1CQBAwc2bNy9f/OIXc/TRR2fYsGG54oorUl5e3mBOu3Z//UyyZk3z/ri6fv36fOc738m///u/p1OnTttca7MDv2984xv5xje+kU6dOmXdunVp27Zt2rRpk5dffjmtWrXKJz/5yW0uCgAAAAB2Fj/72c9y4YUXZsCAAbn66quTJBUVFamtrW0wb2PQ16FDh2at/8gjj+T555/Pv/7rv7ZIva2au8P3v//9fPSjH80jjzySU045JR/4wAfy61//Ot/73vfSpUuXvOtd72qRwgAAAACg1G699dace+65OfLIIzN9+vRUVFQkSXr06JFly5Y1mLvx5+7duzfrGD/72c/Sv3//7L333i1Sc7MDvxdffDEf+9jHUlZWlne/+9357W9/myQ56KCDcvbZZ+e73/1uixQGAAAAAKV0++2358tf/nJOPvnkXHPNNQ0u4a2srMy8efOyfv36+rGHHnoovXr1SteuXZt1nHnz5mXw4MEtVnezA78OHTrUP9ltv/32y7PPPpvVq1cnSQ488MA8++yzLVYcAAAAAJTCkiVLcvnll2f48OE566yzsnz58vzlL3/JX/7yl7z++usZMWJE3njjjYwbNy6LFy/O7Nmzc8stt+Sss85q1nHWr1+fxYsXb/IAkG3R7Hv4vec978n3v//9HH744dlnn33SunXr/PrXv86wYcPy9NNPb3KzQgAAAADYqKz9jn/Y1tYc8yc/+UnWrl2bOXPmZM6cOQ22VVVV5corr8yMGTMyceLEVFVVpVu3bhk7dmyqqqqadZxXX301a9euTZcuXZpd4z/T7MDv7LPPzujRo/P666/nhhtuyEc/+tFcfPHFOeyww/KrX/0qxxxzTIsVBwAAAEBx1NXVpXz/fUt27I1XrTbF2WefnbPPPnuLc/r3759Zs2Y1ab0rr7xys+Ndu3bNokWLmlxXUzQ78KusrMz3vve9+kIuu+yytGrVKo899liOPfbYXHLJJS1aIAAAAADF0JzArUjH3tGaHfg9//zz6d27d/r27ZskadeuXb785S8n+eujh//whz/kkEMOadkqAQAAAIAmafZDO44++ugsWLBgs9uefPLJjB49epuLAgAAAAC2TpPO8PvqV7+aV199Nclfr3eeOnVqdtttt03mLViwIJ06dWrRAgEAAACApmtS4Ne7d+9MnTo1yV+vd/7973+/ydN4W7dunU6dOrmHHwAAAACUUJMCvxNPPDEnnnhikmTYsGGZOnVq/T38AAAAAICdR7Mf2vE///M/9d8//fTTef3117Pbbrtl331L80hlAAAAAOBvmh34Jcm9996br371q3nppZfqx/bYY4984QtfyMc//vGWqg0AAAAAaKatOsNvzJgxGTx4cC644ILsscceWbZsWe65555ccskl6dKlS4466qjtUCoAAAAA0JhmB37f/OY3c+yxx2by5MkNxkeMGJHzzz8/N954o8APAAAAAEqkVXN3eOqpp1JVVbXZbVVVVVm4cOE2FwUAAABA8WxYv36XOvarr76ayy67LEceeWQOOeSQnHTSSZk7d2799gULFmTkyJEZOHBgjjrqqFRXV//TtaZOnZpRo0ZtMv673/0uI0eOzMEHH5yhQ4fma1/7Wmpra5td699r9hl+u+22W1599dXNbnvllVdSXl6+TQUBAAAAUEytWrfOd848M8sWLdqhx92zT5+Mmjat2ftdcMEFWb58ea6++ursvvvuuf3223Paaadl9uzZ2X333TN69Ogcc8wxmTBhQh5//PFMmDAhXbp0yYgRIxqsc/PNN2fKlCmprKxsMP7yyy/n9NNPz4c+9KFMnDgxNTU1ueiii1JXV5eLLrpoq19vswO/973vfbnuuusyaNCgvOMd76gff+6553L99dfn/e9//1YXAwAAAECxLVu0KM8++WSpy2hUTU1NHnzwwdxxxx055JBDkiTjxo3LL3/5y9x7772pqKhIeXl5xo8fnzZt2qR3796pqanJ9OnT6wO/F198MePGjcu8efPSq1evTY7x2GOP5dVXX83YsWPTsWPH7LvvvvnoRz+aX/3qV9sU+DX7kt4LLrgga9asybHHHptPf/rT+cIXvpBPf/rTOe6447Jy5cp84Qtf2OpiAAAAAGBnsNtuu2XatGk56KCD6sfKyspSV1eX1157LXPnzk1lZWXatPnb+XSDBw/OkiVLsnz58iTJH/7wh7z97W/PPffckwEDBmxyjC5duiRJ7rjjjqxfvz7PPvtsfvGLX2x2bnM0O/Dr1q1bvv/972fUqFFZvXp1fv/732f16tUZNWpU7r777uy1117bVBAAAAAAlFrnzp0zdOjQBrevu//++/OnP/0pRxxxRJYuXZoePXo02GfPPfdMkjz//PNJkmHDhuWqq67K3nvvvdljDBo0KGeeeWauvfbavOc978nRRx+dbt265Utf+tI21d7sS3offfTR9OvXL2PGjNlk24oVK3LfffflhBNO2KaiAAAAAGBnMm/evHzxi1/M0UcfnWHDhuWKK67Y5FkW7dq1S5KsWbOmSWuuWLEizzzzTE4++eR89KMfzZ///OdcccUVGT9+fK644oqtrrXZZ/h9+tOfztNPP73ZbfPnz88ll1yy1cUAAAAAwM7mZz/7WU477bT0798/V199dZKkoqJik6fpbgz6OnTo0KR1J02alBUrVuSSSy7Ju9/97hx77LG58sorM3v27CxcuHCr623SGX4XXXRRXnjhhSRJXV1dxo8fn44dO24y75lnnskee+yx1cUAAAAAwM7k1ltvzcSJEzN8+PBMmjSp/qy+Hj16ZNmyZQ3mbvy5e/fuTVp73rx5+cAHPtBgbOP9+5YsWZK+fftuVc1NOsPvQx/6UOrq6lJXV1c/tvHnjV+tWrXKwIEDm3264fLlyzNmzJgMHjw4Bx98cM4888wsXry4fvuCBQsycuTIDBw4MEcddVSqq6sb7L9hw4ZMmTIlQ4YMyYABA3LqqaempqamwZzG1gAAAACAf3T77bfny1/+ck4++eRcc801DS7hrayszLx587J+/fr6sYceeii9evVK165dm7R+jx49smjRogZjTz31VJJkv/322+q6m3SG37BhwzJs2LAkyahRozJ+/Pj07t17qw/69z772c+mVatWmT59ejp06JBrr702p5xySubMmZPVq1dn9OjROeaYYzJhwoQ8/vjjmTBhQrp06VL/eOOpU6dm5syZueKKK9K9e/d8/etfzxlnnJF777035eXleeWVVxpdAwAAAAD+3pIlS3L55Zdn+PDhOeuss+qfvJv89XLeESNGZMaMGRk3blxOP/30PPnkk7nlllsyYcKEJh9j9OjROf3003PNNdfkE5/4RJ577rlMmDAhQ4cOzYEHHrjVtTf7oR3f+c53tvpg/+iVV17Jv/zLv+Szn/1s3vWudyVJzjnnnHzsYx/LH//4xzz00EMpLy/P+PHj06ZNm/Tu3Ts1NTWZPn16RowYkdra2tx0000ZM2ZMhg4dmiSZPHlyhgwZkjlz5uSEE07InXfeucU1AAAAANhx9uzTZ5c45k9+8pOsXbs2c+bMyZw5cxpsq6qqypVXXpkZM2Zk4sSJqaqqSrdu3TJ27NhUVVU1+RhHHHFEbrzxxlx//fW55ZZbsttuu2X48OH5z//8z2bX+/eaHfi1pN12263+RodJ8tJLL6W6ujo9evTI/vvvn+uuuy6VlZVp0+ZvZQ4ePDg33nhjli9fnueeey5vvvlmBg8eXL+9c+fO6devXx599NGccMIJmTt37hbXaOoplgAA8FZQV1eXsrKyUpcBQEFtWL8+o6ZNK9mxW7Vu3eT5Z599ds4+++wtzunfv39mzZrVpPWuvPLKzY4PHTq0/kS2llLSwO/vfelLX6o/G++b3/xmOnTokKVLl+aAAw5oMG/PPfdMkjz//PNZunRpkqRnz56bzNn4kJHG1tjawK+uri4rV67cqn2LpqysLO3bty91GdvVqlWrGtzDkubRIzRGj9CYovfIjuqPov8ei2xH90jt4prUrVqz3Y+3o7Tq0ilt9+7Z+MRdmPcRGrMjekR/7Nq2pkea+iTav9ecwK2llfLYO9pOE/h95jOfyac+9anccccd+dznPpfbb789q1evbnAzxCRp165dkr8+5njVqlVJstk5r732WpI0usbWWrt2bRYsWLDV+xdJ+/bt069fv1KXsV0tWbKkvt9oPj1CY/QIjSl6j+yo/ij677HIdnSP1K1ak7qVxXnPqqtoV+oStjvvIzRmR/SI/ti1bU2PHHroodupGrbVThP47b///kmSL3/5y3n88cdz6623pqKiIrW1tQ3mbQzpOnTokIqKiiRJbW1t/fcb52z8q0Jja2yttm3b1tf8VvdWuOSjV69ezszZBnqExugRGlP0HtlR/VH032OR6REao0dozI7oEf2xa/N5tVhKGvgtX748Dz30UI477ri0/n+nVbZq1Sq9e/fOsmXL0qNHjyxbtqzBPht/7t69e9atW1c/ts8++zSY07dv3yRpdI2tVVZWtk2BIbsWp6XTGD1CY/QIW6I/aIweoTF6hMboERqjR4qlVSkPvmzZsnzhC1/II488Uj+2du3azJ8/P717905lZWXmzZuX9evX129/6KGH0qtXr3Tt2jV9+/ZNx44d8/DDD9dvX7FiRebPn59BgwYlSaNrAAAAAECRlDTw69u3b4444ohMmDAhc+fOzVNPPZWLLrooK1asyCmnnJIRI0bkjTfeyLhx47J48eLMnj07t9xyS84666wkf71338iRIzNp0qQ88MADWbhwYc4///z06NEjw4cPT5JG1wAAAACAIinpJb1lZWW55pprctVVV+Xzn/98Xn/99QwaNCi33XZb3vGOdyRJZsyYkYkTJ6aqqirdunXL2LFjU1VVVb/Geeedl3Xr1uXSSy/N6tWrU1lZmerq6voHdXTt2rXRNQAAAACgKEr+0I5OnTpl/PjxGT9+/Ga39+/fP7Nmzfqn+7du3TpjxozJmDFj/umcxtYAAAAAgKIo6SW9AAAAAEDLEvgBAAAAQIEI/AAAAACgQAR+AAAAAFAgAj8AAAAAKBCBHwAAAAAUiMAPAAAAAApE4AcAAAAABSLwAwAAAIACEfgBAAAAQIEI/AAAAACgQAR+AAAAAFAgAj8AAAAAKBCBHwAAAAAUiMAPAAAAAApE4AcAAAAABSLwAwAAAIACEfgBAAAAQIEI/AAAAACgQAR+AAAAAFAgAj8AAAAAKBCBHwAAAAAUiMAPAAAAAApE4AcAAAAABSLwAwAAAIACEfgBAAAAQIEI/AAAAACgQAR+ALuQurq6UpcAAADATq5NqQsAoOnKyspSu7gmdavWlLqUFtWqS6e03btnqcsAAAAoBIEfwC6mbtWa1K1cVeoyWlRdRbtSlwAAAFAYLukFAAAAgAIR+AEAAABAgQj8AAAAAKBABH4AAAAAUCACPwAAAAAoEIEfAAAAABSIwA8AAAAACkTgBwAAAAAFIvADAAAAgAIR+AEAAABAgQj8AAAAAKBABH4AAAAAUCACPwAAAAAoEIEfAAAAABSIwA8ACqSurq7UJQAAACXWptQFAAAtp6ysLLWLa1K3ak2pS2lRrbp0Stu9e5a6DAAA2CUI/ACgYOpWrUndylWlLqNF1VW0K3UJAACwy3BJLwAAAAAUiMAPAAAAAApE4AcAAAAABSLwAwAAAIACEfgBAAAAQIEI/AAAAACgQAR+AAAAAFAgAj8AAAAAKBCBHwAAAAAUiMAPAAAAAApE4AcAAAAABSLwAwAAAIACEfgBAAAAQIGUPPB79dVXc9lll+XII4/MIYcckpNOOilz586t375gwYKMHDkyAwcOzFFHHZXq6uoG+2/YsCFTpkzJkCFDMmDAgJx66qmpqalpMKexNQAAAACgKEoe+F1wwQV54okncvXVV+d73/te3v3ud+e0007L008/nVdeeSWjR4/Ofvvtl7vuuivnnnturr322tx11131+0+dOjUzZ87MV77ylcyaNStlZWU544wzUltbmyRNWgMAAAAAiqJNKQ9eU1OTBx98MHfccUcOOeSQJMm4cePyy1/+Mvfee28qKipSXl6e8ePHp02bNundu3dqamoyffr0jBgxIrW1tbnpppsyZsyYDB06NEkyefLkDBkyJHPmzMkJJ5yQO++8c4trAAAAAECRlPQMv9122y3Tpk3LQQcdVD9WVlaWurq6vPbaa5k7d24qKyvTps3fcsnBgwdnyZIlWb58eRYuXJg333wzgwcPrt/euXPn9OvXL48++miSNLoGAAAAABRJSc/w69y5c/2ZeRvdf//9+dOf/pQjjjgikydPzgEHHNBg+5577pkkef7557N06dIkSc+ePTeZ88ILLyRJli5dusU1unbtulW119XVZeXKlVu1b9GUlZWlffv2pS5ju1q1alXq6upKXcYuS4+0jLfC77HI9AhbsqP+ndEjuy49QmP0CI3xWYTGbE2PdOjQYTtVw7YqaeD3j+bNm5cvfvGLOfroozNs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7yO777573va2t7V0iQDs4nwGoYgEfjRbXV1dZsyYkeOOOy4HHXRQDj300Jx11ln585//XD+nT58+ufPOOzN69Oj0798/Q4YMyY033ljCqtnR6urqMn369Bx99NEZMGBAPvaxj+Wee+7ZZN7Pf/7zfPCDH0z//v0zevToBn3Erq9///55xzvekR//+McNxu+7774cd9xxDc7Mueuuu/Lxj388/fv3z8CBAzNq1Kj84Q9/qN8+bNiwXH755Tn++ONz2GGH5Te/+c0Oex1sf08//XSeeOKJvP/978+xxx6bRx55JE8//XT99lGjRuXyyy/P2LFjM3DgwBx55JGZNm1a6urqkvztNgHTp0/PYYcdlqqqqqxfv75UL4cW1Jz3kcceeywnn3xy+vfvn6OOOioTJkzIG2+8Ub/dJXlvHdddd12GDRvWYGz27Nnp06dP/c/Dhg3LtGnTcu655+bggw/OYYcdlssvvzzr1q3b0eVSYk3pF4qrKZ9BLr744gb7XHzxxRk1alT9z3/6059yxhln5OCDD84RRxyRm266KcOHD3eLAUpK4Eez3XLLLbnxxhszZsyY/OQnP8nUqVOzZMmSXHnllQ3mfe1rX8vHP/7x/OAHP8iIESNy9dVXZ+7cuSWqmh1t8uTJuf3223PppZfmhz/8YT796U9n/Pjxue222xrMq66uzpe+9KX6y6xOOumkrFq1qkRVsz0cd9xxDf5Dvba2Ng888ECDSyXmzJmT//qv/8opp5yS+++/P7fccktWr169ySXjd9xxRy699NLMmDEjhxxyyA57DWx/3/ve99KhQ4cceeSROeaYY1JeXp477rijwZzbb7897du3z1133ZXzzz8/119/faZPn95gzv/+7/9m1qxZufzyy9O6desd+RLYjpryPrJw4cKccsopef/735977rknkyZNyh/+8Ieceuqp9cEw/KPrrrsulZWV+f73v59zzz033/72t3PvvfeWuixgB2rKZ5AtWbVqVU455ZRs2LAhd9xxR6655pp8//vfdyIDJSfwo9n22WefXHnllRk2bFj22muvHHbYYTnuuOOyaNGiBvOqqqrysY99LL169crnP//5vP3tb8+8efNKVDXbww9/+MMcfPDBDb5OPfXUrFy5MjfffHMuuuiifOADH8g+++yTESNG5JRTTkl1dXWDNS699NIMGTIkBxxwQL72ta/lzTff9EG7YI477rgGl+M9+OCD2W233dKvX7/6OV26dMlXvvKVfPzjH89ee+2VAQMG5JOf/OQm7ytDhw7N4Ycfnve85z0pLy/foa+D7WfdunX54Q9/mA984ANp3759OnXqlKFDh+YHP/hBgz8AvPOd78z48ePTu3fvVFVVZdSoUfn2t7/dIMw59dRTs99+++XAAw8sxUthO2nK+0h1dXXe97735Zxzzsl+++2XQYMG5aqrrsoTTzyRRx55pFSls5MbMmRIPv3pT2e//fbLyJEj07dv3zz22GOlLgvYQZr6GWRLfvSjH+Xll1/OVVddlb59+2bQoEGZNGmSPzZRch7aQbMNGzYsTzzxRKZMmZKampo8/fTT+eMf/5ju3bs3mNe7d+8GP3fs2DFr167dkaWynQ0bNiwXXnhhg7GKioosXrw4a9asyUUXXZRLLrmkftu6detSW1ub1atX148NGjSo/vvOnTtnv/32y1NPPbX9i2eHOeigg7L33nvX33T/Rz/6UT784Q83mFNZWZndd989U6dOTU1NTZYsWZIFCxZkw4YNDebtu+++O7J0dpBf/OIX+ctf/pLjjz++fuz444/PnDlzct999+XEE09Mkrz3ve9tcPnmwIEDM3369Lzyyiv1Y/vtt98Oq5sdpynvI/Pnz09NTU0OPvjgTfZ/+umnc9hhh+2octmF/OPn1U6dOvm8Cm8hTf0MsiXz589Pr1690qVLl/qxPn36pFOnTtujZGgygR+b9dJLL2X58uX1963Y+NeJ1q1bZ/r06bnuuuvyiU98Iu9973szatSoPPDAA7nvvvsarLG5s2/8laNY3va2t202gFm6dGmS5Jprrsk73/nOTbb/fW/84yV369evd+ZWAW28HO/f//3f88ADD+S73/1ug+333Xdfxo4dmw9/+MPp379/TjzxxDz11FP57//+7wbzKioqdmTZ7CAb729z3nnnbbJt5syZ9R+227Rp+LHl7/9t2sgTWIursfeRDRs25CMf+UjOPvvsTfbdfffdd1SZ7EBb+rz69z9vtLl78/m8+tbREv1C8TT1M8g/9sff/2GgdevWm/yRGnYGLulls6qrq3PBBRfU/7xixYokf/3A/M1vfjP/8R//kfHjx+dTn/pUBg4cmGeeecaHI+q9853vTJs2bfL8889n3333rf/6xS9+kerq6rRq9be3nt///vf137/88st55pln8q53vasUZbMdbbwc73vf+1723nvvTc6ouOGGG3LiiSfmq1/9ak4++eRUVlbW3/fEe0uxvfzyy/nFL36RT3ziE7n77rsbfJ144on53e9+V//wlt/97ncN9n3sscfyL//yL3n7299eitLZwRp7H3nXu96VP/7xjw3+3Vm/fn2uuOKKTZ7wSzFs6fNq27Zt88YbbzT4N6SmpmaH18jOQ7/wj5r6GaRt27Z5/fXXG+z7pz/9qf77vn37pqamJq+++mr92P/93/9tsg/saAI/Nuvwww/P4sWL8/3vfz9PP/10rrjiinTu3DkHH3xwevbsmQcffDCLFy/O//3f/2Xy5Mn56U9/mtra2lKXzU6iU6dO+bd/+7dcc801ufvuu/PnP/853//+9/P1r389e+yxR4O5l112WR566KEsWLAg559/fnr27NnglHqK4cADD8y+++6bq6++usFN9jfq2bNnHnvssfzhD3/In/70p9x888259dZbk8R7S8H94Ac/yLp163L66afngAMOaPB19tlnp3Xr1vU3zp47d26mTJmSJUuW5Hvf+15uu+22nH766SV+Bewojb2PnHrqqVmwYEEuu+yyLF68OE888UQuvPDCLFmyxKXeBbWlz6uHHHJIVqxYkWnTpuXZZ5/ND3/4Q0/LfIvTL/yjpn4GOeSQQ/LrX/86//M//5M///nPmTJlSoNbEH34wx/ObrvtljFjxmThwoV5/PHHM2bMmCRpcCsS2NEEfmzWkCFDcvHFF+e6665LVVVV/vjHP+ab3/xmOnbsmK997WtZvXp1RowYkZEjR+app57KhAkTsnz58jz77LOlLp2dxCWXXJJTTjklU6ZMyXHHHZfrr78+//Ef/5Fzzz23wbxzzjknl1xyST71qU+lvLw8M2bMcElvQR133HF54403NhvofulLX8oee+yRkSNH5pOf/GR+/vOf52tf+1qS5IknntjRpbIDzZ49O4cffvgmZ2slyd57753hw4fnvvvuyxtvvJGjjz46f/zjH/Oxj30sN9xwQy6++OKcdNJJJaiaUtnS+8jAgQMzY8aMPPXUU/nEJz6RM888M3vvvXe+9a1v+XeloLb0efW9731vzj///Nx66605/vjjc/fdd+eiiy4qdcmUkH7hHzX1M8hnPvOZfOhDH8qYMWNSVVWVl156Kaecckr93I3/DVNbW5t//dd/zbnnnptPfOITSZK2bdvuqJcDmyirc60UALCTGzVqVPbaa69ceeWVpS4FAKDes88+m2eeeSZHHHFE/diLL76YI488MrfddluDhxTCjuQMPwAAAICtsGbNmpx55pmprq7On//858yfPz9f+tKXst9++2XAgAGlLo+3MIEfAAAAwFbo3bt3rr766vzwhz/Mhz/84YwePTodOnTIt771LZf0UlIu6QUAAACAAnGGHwAAAAAUiMAPAAAAAApE4AcAAAAABSLwAwAAAIACEfgBAAAAQIEI/AAAAACgQAR+AAAAAFAgAj8AAAAAKBCBHwAAAAAUyP8PexJkFtGAUXgAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 1289x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "custom_palette = [\"#FFC0CB\", \"#800000\"]  \n",
    "sns.catplot(x='nama_bulan', y='order_id', hue='year', data=df_tanggal_penjualan, kind='bar', height=6, aspect=2, palette = custom_palette)\n",
    "plt.ylabel(\"total order\")\n",
    "plt.xlabel(None)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "1eebd15f",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:36.274087Z",
     "iopub.status.busy": "2023-10-18T10:08:36.273709Z",
     "iopub.status.idle": "2023-10-18T10:08:36.285295Z",
     "shell.execute_reply": "2023-10-18T10:08:36.284323Z"
    },
    "papermill": {
     "duration": 0.050295,
     "end_time": "2023-10-18T10:08:36.287377",
     "exception": false,
     "start_time": "2023-10-18T10:08:36.237082",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>year</th>\n",
       "      <th>order_id</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2017</td>\n",
       "      <td>21364</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2018</td>\n",
       "      <td>51461</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   year  order_id\n",
       "0  2017     21364\n",
       "1  2018     51461"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_tahun_penjualan = df_tanggal_penjualan.groupby(\"year\").order_id.sum().reset_index()\n",
    "df_tahun_penjualan"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "cc37d6d6",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:36.360586Z",
     "iopub.status.busy": "2023-10-18T10:08:36.359491Z",
     "iopub.status.idle": "2023-10-18T10:08:36.366004Z",
     "shell.execute_reply": "2023-10-18T10:08:36.364928Z"
    },
    "papermill": {
     "duration": 0.044472,
     "end_time": "2023-10-18T10:08:36.368023",
     "exception": false,
     "start_time": "2023-10-18T10:08:36.323551",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "140.87717655869687"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#persentase kenaikan dari 2017 ke 2018\n",
    "(51461 - 21364) / 21364 *100"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4b41ce18",
   "metadata": {
    "papermill": {
     "duration": 0.034482,
     "end_time": "2023-10-18T10:08:36.438119",
     "exception": false,
     "start_time": "2023-10-18T10:08:36.403637",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "pada tahun 2018, terjadi peningkatan pembelian secara signifikan dibandingkan tahun 2017 dengan peningkatan 140.87%."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0e5faa52",
   "metadata": {
    "papermill": {
     "duration": 0.035134,
     "end_time": "2023-10-18T10:08:36.510160",
     "exception": false,
     "start_time": "2023-10-18T10:08:36.475026",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## Pertanyaan 5: Bulan apa yang terjadi peningkatan penjualan tertinggi? \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "06e9ed1f",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:36.583766Z",
     "iopub.status.busy": "2023-10-18T10:08:36.583175Z",
     "iopub.status.idle": "2023-10-18T10:08:36.635664Z",
     "shell.execute_reply": "2023-10-18T10:08:36.634335Z"
    },
    "papermill": {
     "duration": 0.093322,
     "end_time": "2023-10-18T10:08:36.638368",
     "exception": false,
     "start_time": "2023-10-18T10:08:36.545046",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "df_tanggal =  orders.groupby(by=[\"month\",\"year\"]).order_id.nunique().reset_index()\n",
    "df_tanggal[\"month\"] = pd.to_datetime(df_tanggal[\"month\"], format='%m-%Y')\n",
    "# df_tanggal"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "8f269e68",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:36.709891Z",
     "iopub.status.busy": "2023-10-18T10:08:36.709523Z",
     "iopub.status.idle": "2023-10-18T10:08:37.377158Z",
     "shell.execute_reply": "2023-10-18T10:08:37.375945Z"
    },
    "papermill": {
     "duration": 0.706002,
     "end_time": "2023-10-18T10:08:37.379437",
     "exception": false,
     "start_time": "2023-10-18T10:08:36.673435",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABmUAAAJKCAYAAADdrEFGAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8qNh9FAAAACXBIWXMAAA9hAAAPYQGoP6dpAADccElEQVR4nOzdd3hUZfrG8XtSJoX0EFIgCaEklIQeqgJSFAtNLOuKHbuirm1d3VV2V11XXAuKFdGfBRugFEWq0nsnhJZCSQKkkN5nfn8gA4ckkECSScL3c11ccp5zzjtPCrvJued9X5PVarUKAAAAAAAAAAAAdcrB3g0AAAAAAAAAAABcCghlAAAAAAAAAAAA6gGhDAAAAAAAAAAAQD0glAEAAAAAAAAAAKgHhDIAAAAAAAAAAAD1gFAGAAAAAAAAAACgHhDKAAAAAAAAAAAA1ANCGQAAAAAAAAAAgHpAKAMAAAAAAAAAAFAPnOzdAAAAAHAhZs2apeeee67G9/Xu3VtffPFFHXRUd/76179q9uzZlZ5zdHSUi4uLmjdvrq5du+qmm25S796967lDad++fWrfvn29v251rFu3TrfffrskadeuXXJyqttfg6ZMmaJ3331XPXr00IwZM+r0terKqY+hMg4ODjKbzfL391fnzp01evRoDRs2rJ47NDr1vweBgYFavny53fqIioqSJE2fPl39+/e3Wx8AAABouAhlAAAA0Cj5+/urR48eFeqpqalKTU2V2WxWdHR0hfORkZH10V6d8PDwqNC/1WpVQUGBDh48qLlz52ru3Lm6//779Ze//KVeekpMTNS///1vFRQUNNoAAlWr7N+R1WpVUVGRDh8+rIULF2rhwoUaOXKkXn/9dZlMJjt1CgAAADQOhDIAAABolAYNGqRBgwZVqJ96h39AQECTCwk6depU5SyfvLw8vfTSS5o7d64+/PBD9e7dW5dddlmd9zRv3jytXLmy0oAMjd+5/h2VlJTorbfe0rRp0zR37lz17t1bN910Uz13eJKnp6ciIiIUEBBgl9cHAAAAqos9ZQAAAIAmwMPDQ6+++qoCAwMlSV9++aWdO0JTZzab9cwzz6hLly6SZNdlAYcPH64FCxY0uqUJAQAAcOkhlAEAAACaCGdnZw0ePFiStHXrVrv2gkvHqf1k9u7dq4KCAjt3AwAAADRshDIAAAC4JEVFRSkqKkrp6el66qmn1L17d/Xs2VO33367ysrKbNfFx8fr2Wef1eDBgxUdHa0+ffronnvu0a+//lrpuLfddpuioqK0fPlyxcfH67HHHlP//v0VHR2toUOH6pVXXlFmZmadfVweHh6SpPz8/Arn8vLy9N5772nMmDHq3r27unXrppEjR+qdd95RTk5OhetnzZqlqKgoPfHEE9q0aZNGjx6t6OhoXXbZZfrss88UFRVl2wx+8+bNioqK0pAhQ2z3n/ocr169utJeT32upkyZYqsdPnxYUVFRGjhwoCwWi7766iuNGTNGXbt2Vd++ffXwww/rwIEDkqTMzEz961//sn1tBg0apH/+85/Kzc2t8vNTUlKid999V1deeaViYmI0cOBAPffcc0pMTKzy4x84cGClY53qNSoqSocPH670mszMTP3nP//R8OHDFR0drQEDBmjixInasWNHpddbrVYtWbJEEydO1BVXXKEuXbqoS5cuGjJkiJ5++ulK7/vrX/+qqKgozZgxQ4cPH9Zzzz2ngQMHKjo6WgMHDtTzzz9fZX+14dT3nFTx+66kpESff/65br75ZvXs2VNdunTRVVddpVdffVXHjh2rMNa6desUFRWlm266SaWlpfr00081atQode3aVb169dIdd9yhxYsXV7ivqq/Vqe+xN998s9Lep0yZoqioKN12220VzuXk5Oijjz7Srbfeqj59+qhz587q1auXrr/+ek2ZMkXZ2dnV+vycsn79ej399NMaNmyYunXrpujoaF1++eV69NFHtWbNmip7mzx5sjIzM/Xvf/9bQ4YMUXR0tPr3768nnnhCe/bsqVEPAAAAsD9CGQAAAFzSHn30Uc2bN0+hoaFyc3NTQECAnJxObr341Vdf6frrr9ePP/6o7OxstW/fXu7u7lq5cqUmTpyoJ598UuXl5ZWOu3z5ct1www1avHixfH19FRwcrMOHD+vzzz/Xn/70J+Xl5dXJx5OcnCxJCg4ONtQPHDigUaNG6Z133tHevXvVokULhYeHKyEhwRbUnAo7zpaQkKAJEyboyJEjat++vXJycuTj46MePXrYXsfDw0M9evSosCn8hbJYLHrsscf0z3/+U5mZmQoPD1deXp4WL16sW265RVu2bNGYMWP09ddfy9XVVSEhIUpLS9NXX32le++9V1artdJx77vvPk2ZMkUFBQWKjIxUTk6OZs2apdGjR2vFihW10vspx44d09ixYzV9+nRJUkREhLKzs/Xrr7/qlltuqfAg3mq16qmnntJDDz2kX3/9VeXl5Wrfvr0CAgKUmpqqOXPm6E9/+pN+//33Sl8vLi5Oo0eP1o8//ig3NzeFh4fr6NGj+uGHH3TjjTcqNTW1Vj++U059z7m6usrX19fw8d9000165ZVXtG3bNnl7e6tdu3ZKTU3VZ599ppEjR2rTpk2VjllaWqp7771Xr732mo4dO6a2bduqvLxca9eu1cMPP1zn+0UlJSVp1KhReuONN7R161b5+fkpKipKjo6O2rVrl959913dfPPNlYaflXnjjTd02223ac6cOcrPz1ebNm0UEhKizMxMLVy4UHfeeae+/fbbSu9NSUnRmDFjbEsStm3bVllZWfr555918803a9euXbX2cQMAAKDuEcoAAADgkrZz50598cUXmjNnjpYvX66///3vkk6GKv/617/k4OCg559/Xhs3btTs2bO1bNkyffbZZ/L399e8efMMszzO9MUXX2jAgAFatmyZ5s+fr0WLFmnq1KlydHRUcnKyfvjhh1r/WBISEmwP7AcNGmSrFxQU6MEHH9SRI0c0dOhQLVu2TL/++qt++ukn/fbbbxo8eLCOHDmihx56SEVFRRXGjY+PV2RkpJYtW6bZs2fr999/1+jRozVjxgyNGzdOkhQZGakZM2bonXfeqZWP5fjx41q6dKn+85//6Pfff9ecOXM0a9Ysubm5KTs7W3/+85/l7++vX375RQsWLNDChQv1yiuvSJK2bNmiDRs2VDru5s2b9Y9//EMrVqzQzJkztXz5cl155ZUqLi7WU089VauzmA4fPixHR0d9//33WrRokebOnatffvlFrVu3Vmlpqf73v/8Zrp89e7bmzZsnV1dXffTRR1q+fLlmzpypJUuWaN68eWrfvr3Kysqq/Bx/9913ateunX7++Wf9+uuvmj9/vr755hs1a9ZMmZmZ+vTTT2vtYzslMzNTP/30kyRpwIABtkDTarVq4sSJ2r17t3r27Kmff/5ZS5cu1axZs7Rq1SqNGzdOJ06c0MMPP6zjx49XGDcuLk7btm3T5MmTtXbtWs2aNUvLly9Xv379JElvvfWWYUZbbfv73/+u1NRUdevWTcuWLdMvv/yiWbNmae3atXrttdfk4OCgxMRE/fjjj+cda926dfroo4/k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LoDVahWrvgEAAAAAAAAAAEnVzgwIZS7AqRkyMTExdu4EAAAAAAAAAADY244dO6p1HXvKAAAAAAAAAAAA1ANCGQAAAAAAAAAAgHpAKAMAAAAAAAAAAFAPCGUAAAAAAAAAAADqAaEMAAAAAAAAAABAPSCUAQAAAAAAAAAAqAeEMgAAAAAAAAAAAPWAUAYAAAAAAAAAAKAeEMoAAAAAAAAAAADUA0IZAAAAAAAAAACAekAoAwAAAAAAAAAAUA8IZQAAAAAAAAAAAOoBoQwAAAAAAAAAAEA9IJQBAAAAAAAAAACoB4QyAAAAAAAAAAAA9YBQBgAAAAAAAAAAoB4QygAAAAAAcAGsVqs27zmmeSsTdDyr0N7tAAAAoBFwsncDAAAAAAA0Rj+vTtIHs7ZLkr5fsleTJw5SgK+bnbsCAABAQ2bXmTLr1q1TVFRUpX+GDh0qSdq9e7fGjx+vbt26afDgwZo2bZphDIvFonfeeUeXX365unbtqrvvvlvJycmGa843BgAAAAAANVFaZtE3C/fYjjNzijVtzk47dgQAAIDGwK6hTPfu3bVy5UrDn08//VROTk564IEHlJWVpbvuukutW7fWzJkz9eijj+rtt9/WzJkzbWNMnTpV33zzjf7973/r22+/lclk0r333quSkhJJqtYYAAAAAADUxNqdqTqRV2yordqeos17jtmpIwAAADQGdg1lzGazAgICbH98fHz06quv6sorr9SNN96o7777TmazWS+99JLatm2rcePG6c4779THH38sSSopKdGnn36qRx99VIMGDVKHDh305ptv6ujRo1q0aJEknXcMAAAAAABqasGapErrH83ertKy8vptBgAAAI2GXUOZs3311VdKTU3Vc889J0nauHGjYmNj5eR0euubvn37KjExURkZGYqPj1d+fr769u1rO+/l5aVOnTppw4YN1RoDAAAAAICaSDmep+370ys9d+R4vn78/UA9dwQAAIDGosGEMsXFxfrggw90xx13qEWLFpKktLQ0BQUFGa47dS4lJUVpaWmSpODg4ArXpKamVmsMAAAAAABqYsHa5HOe/2bRXh3LKqinbgAAANCYNJhQ5qefflJxcbFuu+02W62oqEhms9lwnYuLi6STIU5hYaEkVXpNcXFxtcYAAAAAAKC6SsvKtXj9QUOtR1QLmUynj0tKy/XJTzvruTMAAAA0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z9W7d2/df//9+vzzz5Wfn+90aeWK408GPjblYFOvwdicgc29+9iege39S3ZnwFAGlZLb7VZkZKTatGmjPn36aMqUKVq7dq3mzJkT8v8owfH3IQe7MrCp12BszsDm3ouzOQebe/chAzKwuX+v1ytJioyMVLt27SRJzz77rLp166apU6daMZix+fj7kEERm3KwqddgbM7A5t59bM/A9v4lizMwQCWQnp5uDh48GLBtyZIlZtu2bf6/f/nll2bAgAFmwoQJZs2aNRVdIsoRx78IOdiVgU29BmNzBjb3XpzNOdjcuw8ZkIHt/W/ZssWsW7fOpKenm7y8PGOMMUeOHDE7d+4MeNy4ceNMz549zQcffOB/XCiw/fgbQwY+NuVgU6/B2JyBzb372J6B7f0bQwY+LmOMcXowBLvNnDlT3333nbZu3arTTjtN3bp101VXXeXf7/F4FBYWJpfLpa+++kr33XefunXrptGjR6t79+4OVo6ywPEvQg52ZWBTr8HYnIHNvRdncw429+5DBmRge///+Mc/9P777ys3N1cREREaOnSoRowY4b9+utfrlcfjUWRkpCTpL3/5i9auXas77rhDZ599dpW/x4ztx18iAx+bcrCp12BszsDm3n1sz8D2/iUyCOD0VAh2mzVrljn11FPNG2+8Yd544w1z2223mSFDhpg77rjD/5jCwkLj9Xr9f//6669Nly5dzJ133hlSnxSzEce/CDnYlYFNvQZjcwY2916czTnY3LsPGZCB7f2/+eabpk+fPuarr74yu3btMvPmzTOjR482559/vlmyZIkxxvh7Lyws9H/dFVdcYQYNGmSysrIcqbus2H78jSEDH5tysKnXYGzOwObefWzPwPb+jSGD32IoA8fk5+ebCRMmmIULF/q3paSkmIULF5qePXuaCRMm+Ld7PJ6Af5Tfffed2b59e0WWizLG8S9CDnZlYFOvwdicgc29F2dzDjb37kMGZGB7/8YYM23aNDN58uSAbd9++60ZP368GTJkiPn+++8D9rndbv+f9+3bVyE1lheOPxn42JSDTb0GY3MGNvfuY3sGtvdvDBmUJszpM3Vgt+3bt2vr1q3+v9epU0cXXHCBJk2apOXLl2vKlCmS5D91zfx6tb2+ffuqefPmTpSMMsTxL0IOdmVgU6/B2JyBzb0XZ3MONvfuQwZkYHv/krRr1y4VFBT4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TAjfzi8zM1OZmZmqU6eOJOmKK67QTz/9pISEBMXGxuqee+7RV199pby8vJDJwdfLm2++qaSkJBljVLduXfXu3VuvvfaasrKy/P82QnkxJklZWVnauHGjNm/erO3bt+tvf/ubYmJilJqaqpSUFN1+++0hd/x/a//+/dq1a5dcLpciIiKUm5srSWrdurVatWqlefPmKTU1VVJo/iyweQ3gdrslSTt27FBmZqYuueQSLViwQLm5uZo4caI2b94sSb87kKnqbHrf93tsf/8v2fW9wBqANYDtawAb3/9LrAGKYw1wgpw4PQehy3e9wD179pghQ4aYBx980L+v+GmM1113nRkxYkSp1xFE1eU7/h988IEZP3682bp1q3/fkiVLTPv27c369esDviZUT130nZa6YsUKc/vtt5u0tDRjjDHz5s3zn85d/FIGoerDDz8048aNs+J7YdWqVebNN980xhT1Mm3aNJOcnOzv64477jD9+vUz6enpTpZZboqfir1161bTp08fs337dpOTk2MWLFhgkpKSTKdOnfynMIfi6/+9995r+vbta55++mlzxx13BJyu/fjjj5vu3bsHXFs+FGVlZZkzzzzT3HPPPWbp0qVmwoQJATk8+eSTpmvXrmbnzp0OVln2fJcscrvd/n8LH3/8sRkyZIhZtWqVf1+oy8rKMiNGjDBt27Y1/fr1M8OHDzdZWVn+TP7xj3+Ybt26/e4lPqq6L774wgwYMMDMmjXLvy05OdmceeaZZs+ePeaWW24x559/vv97JlTYvAb49NNP/X/2er0mMzPT3HHHHWbXrl3GmKJMhg0bZi688MKAS5mFEtYARXj/fxRrANYArAGK2LAGsPX9vzGsAXxYA5wYzpRBmfjss88kSZGRkfJ6vapbt67OPfdcrVq1SvPmzZMkRUVF+T8Zcd111ykjI0M7d+50rGaUneLHX5IGDBigu+++W82aNfM/Jjc3V7Gxsf7TeiVpwYIFWrp0acUWW46WL1+uL774QitXrvR/Aqx79+6aOHGiatWqJUm65pprdNddd/k/Mef7tGyoKJ7BkSNHNGzYME2dOjXgMiWh8r1QvNesrCx169ZNI0eOlCSFhYXpzjvvVIMGDfyfjvnrX/8qj8ej9evXO1l2mSqeQXp6un97kyZN1Lx5cxUWFio2NlZr1qxRXFycCgoK9Nprr0mS/1PUVVXx3lNSUiRJDzzwgJKSkvTCCy+oZcuWqlmzpv8TkX/7298UHR3t/9RoqCiew+HDh1WjRg1dfvnl2rx5s1566SUVFhaqZs2a/p//f/vb3xQbG6vvvvvO4cr/vOK9+z75Hx4e7j/mZ511lmJjYzV79mz/PhNinwwr7fgvWrRIzz77rAYNGqSBAweqRo0aKiwslCTdfvvtiomJ0bJlyxyuvOwUzyA7O1t9+/ZV37599c4772jUqFF66KGHNGzYMPXq1UsnnXSSRo8erZycHCUnJztdepmwfQ1w+PBhTZo0Sffff7+kok+L16xZUw8++KCaNGkir9erk046SXPmzFFeXp4mTpyoLVu2OFx12WENwPt/H9YArAEk1gC2rAFsfv8vsQaQWAOUFe4pgz/Ntxj57rvvdN999yksLEzR0dEaM2aMdu3apffee08ej0djx45VVFSUJKlmzZoyxoTcC5ONfnv8paLLMvguzWB+vb5samqq3G63qlWrJkmaOXOmnnvuOb333nuO1V6WnnjiCb3zzjuqWbOm9u7dq759+2ro0KG65JJLlJiYKLfbLZfLpfDwcF1zzTX+r8nJydH48eNVu3ZtZxsoA7/NoFevXjrvvPN04YUXSpL/etKh8L3w21779Omjs88+WxdddJGkou9735svl8slY4xyc3MVFxcXEsdaKv17ftiwYbrooosUGRmpmjVravny5frnP/+ptWvX6sUXX9Tq1av1+OOPKywsTDfeeKPTLZyw3/v3/te//lV5eXk644wzJBUtzt1utw4cOKD4+HjVr1/f2eLL0G9z6N27t0aOHKnRo0frl19+0Ycffqg2bdpIKvqlrMfjUVZWlurWrauGDRs6XP2f83vf/+Hh4SooKFBUVJRuvfVWTZs2TW+//bYuuuiiKn2viN8q7XXwrLPO0sUXX6whQ4Zoz549WrFihaSi419YWKjDhw+rXr16OumkkxyuvmyU9nPv8ssv14MPPqgPP/xQ77//vg4fPqybb75Z1157raSinw9hYWH+X2JXZawBikRGRuqNN95Qfn6+Hn74YUlHL+UTFlb0GchGjRppzpw5GjdunMaNG6eXXnpJLVu2dKzmssAagPf/PqwBWAOwBrBnDWDz+3+JNYDEGqBMOXB2DkJMamqq6devn+nQoYO5++67A/YdPHjQTJw40YwYMcJMmjTJ5Obmmv3795un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IiJ06623atWqVfrggw8kKeQWpTZlYFOvwdicgc29F2dzDjb37kMGZGBz/77PJv7www9asGCBFi1aJEkKCwvz5+AbzrRt21bdunXTZ599pr179zpTcDmw+fj7FM8gMjJSkjRw4EAtXrxY48aNU1JSkpo1aybp6DqoZcuW/j+HCptysKnXYGzOwObefWzPwPb+JTKoLBjKWC7YYkSSmjRposmTJ8vtdmv37t1avHixpKO/tM/NzVXt2rXl9XpD8hR+G3D8i7AotysDm3oNxuYMbO69OJtzsLl3HzIgA9v7l44OIGJiYpSfn6/XXntN8+fPlxSYgyTVr19fl156qZYsWaJ//etfys3NdaLkMsPx//11kNvtVkxMjDp37qzDhw/r448/lnR0HWSMUWJiYsDzVFU25WBTr8HYnIHNvfvYnoHt/UtkUNkwlLHc7y1GJCkpKUnTp09X9+7dtXjxYt1111167bXXNGXKFH3xxRe66qqrFBYWFnKfmLIFx7+IzYtyH5sysKnXYGzOwObei7M5B5t79yEDMrC9f+noPWN27NihLl26qGPHjnrrrbeC5jBgwADdcMMNeuONN6r82eIc/9/PICIiwn/puujoaL3++ut69dVXtXTpUj322GNasmSJRo4cKanqnzlkUw429RqMzRnY3LuP7RnY3r9EBpUN95SBJGns2LHyeDxq2LChfvrpJ40cOVLXXHONf//u3bv18ccf68MPP1RkZKTq1aunm2++WW3btnWuaJQZjn+R38uh+PXFJenll1/W7Nmz9cknn6hWrVrOFFwObMrApl6DsTkDm3svzuYcbO7dhwzIwOb+PR6PMjIy9Ne//lXjxo1T27ZtNX36dG3YsKFEDi6Xy/8LiLS0NCUkJDhYedmx+fj7HGsdtHHjRs2YMUM//fSTatSoodq1a2vKlClKSkpyruhyYFMONvUajM0Z2Ny7j+0Z2N6/RAaVhoHV3G63SU1NNZdffrn58ssvzf79+80dd9xhzj33XDNv3rygX5Ofn1+xhaJccPyLHG8OHo/HeL1e/98PHz7sQLXlw6YMbOo1GJszsLn34mzOwebefciADGztv3gvxhiTk5NjXn/9dbN161ZjjDHbt283d955Z4kc3G53RZZZ7mw9/sX9kXVQdna2SU5ONsnJySYrK8uZgsuJTTnY1GswNmdgc+8+tmdge//GkEFl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\n",
      "text/plain": [
       "<Figure size 2000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(20, 6))\n",
    "\n",
    "ax = sns.lineplot(x='month', y='order_id', data=df_tanggal, estimator=None,linewidth=3)\n",
    "ax.set(xticks=df_tanggal.month.values)\n",
    "\n",
    "plt.title(\"Tren Pertumbuhan Penjualan\", loc=\"center\", fontsize=18)\n",
    "plt.ylabel(\"total order\")\n",
    "plt.xlabel(None)\n",
    "ax.grid(False)\n",
    "for tick in ax.get_xticklabels():\n",
    "    tick.set_rotation(45)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "0791127a",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:37.454749Z",
     "iopub.status.busy": "2023-10-18T10:08:37.454402Z",
     "iopub.status.idle": "2023-10-18T10:08:37.524962Z",
     "shell.execute_reply": "2023-10-18T10:08:37.523639Z"
    },
    "papermill": {
     "duration": 0.111316,
     "end_time": "2023-10-18T10:08:37.527395",
     "exception": false,
     "start_time": "2023-10-18T10:08:37.416079",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>tanggal_hari</th>\n",
       "      <th>order_id</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>24</td>\n",
       "      <td>1116</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>25</td>\n",
       "      <td>479</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>27</td>\n",
       "      <td>383</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>26</td>\n",
       "      <td>368</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>28</td>\n",
       "      <td>359</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>29</td>\n",
       "      <td>298</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>23</td>\n",
       "      <td>267</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>30</td>\n",
       "      <td>251</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>21</td>\n",
       "      <td>213</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>16</td>\n",
       "      <td>212</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>20</td>\n",
       "      <td>210</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>13</td>\n",
       "      <td>189</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>22</td>\n",
       "      <td>187</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>14</td>\n",
       "      <td>178</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>09</td>\n",
       "      <td>178</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>06</td>\n",
       "      <td>175</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>17</td>\n",
       "      <td>174</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>15</td>\n",
       "      <td>172</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>12</td>\n",
       "      <td>165</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>08</td>\n",
       "      <td>164</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>10</td>\n",
       "      <td>159</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>11</td>\n",
       "      <td>152</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>07</td>\n",
       "      <td>148</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>19</td>\n",
       "      <td>145</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>18</td>\n",
       "      <td>137</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>03</td>\n",
       "      <td>134</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>26</th>\n",
       "      <td>05</td>\n",
       "      <td>127</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>27</th>\n",
       "      <td>02</td>\n",
       "      <td>116</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>01</td>\n",
       "      <td>107</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>29</th>\n",
       "      <td>04</td>\n",
       "      <td>102</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   tanggal_hari  order_id\n",
       "0            24      1116\n",
       "1            25       479\n",
       "2            27       383\n",
       "3            26       368\n",
       "4            28       359\n",
       "5            29       298\n",
       "6            23       267\n",
       "7            30       251\n",
       "8            21       213\n",
       "9            16       212\n",
       "10           20       210\n",
       "11           13       189\n",
       "12           22       187\n",
       "13           14       178\n",
       "14           09       178\n",
       "15           06       175\n",
       "16           17       174\n",
       "17           15       172\n",
       "18           12       165\n",
       "19           08       164\n",
       "20           10       159\n",
       "21           11       152\n",
       "22           07       148\n",
       "23           19       145\n",
       "24           18       137\n",
       "25           03       134\n",
       "26           05       127\n",
       "27           02       116\n",
       "28           01       107\n",
       "29           04       102"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bulan_11 = orders[orders[\"nomor_bulan\"] == '11']\n",
    "bulan_11 = bulan_11.copy()  \n",
    "bulan_11['tanggal_hari'] = bulan_11['order_purchase_timestamp'].dt.strftime('%d')\n",
    "bulan_11.groupby(by=\"tanggal_hari\")[\"order_id\"].nunique().sort_values(ascending=False).reset_index()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "658f04a1",
   "metadata": {
    "papermill": {
     "duration": 0.036744,
     "end_time": "2023-10-18T10:08:37.601833",
     "exception": false,
     "start_time": "2023-10-18T10:08:37.565089",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "pembelian terbanyak terjadi pada bulan novembertahun 2017, terutama pada tanggal 24 November 2017."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "03a5d2e6",
   "metadata": {
    "papermill": {
     "duration": 0.036923,
     "end_time": "2023-10-18T10:08:37.676849",
     "exception": false,
     "start_time": "2023-10-18T10:08:37.639926",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## Pertanyaan 6: hari apa yang sering digunakan oleh pembeli untuk melakukan transaksi?\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "6cb007ce",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:37.753572Z",
     "iopub.status.busy": "2023-10-18T10:08:37.752788Z",
     "iopub.status.idle": "2023-10-18T10:08:37.788202Z",
     "shell.execute_reply": "2023-10-18T10:08:37.786839Z"
    },
    "papermill": {
     "duration": 0.077511,
     "end_time": "2023-10-18T10:08:37.790671",
     "exception": false,
     "start_time": "2023-10-18T10:08:37.713160",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "df_bagian_hari = orders.groupby(by=\"waktu_hari_pembelian\")[\"order_id\"].nunique().reset_index()\n",
    "df_bagian_hari.rename(columns={\n",
    "    \"order_id\": \"total_orders\"\n",
    "}, inplace=True)\n",
    "# df_bagian_hari"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "d9595722",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:37.870085Z",
     "iopub.status.busy": "2023-10-18T10:08:37.869706Z",
     "iopub.status.idle": "2023-10-18T10:08:38.264921Z",
     "shell.execute_reply": "2023-10-18T10:08:38.263640Z"
    },
    "papermill": {
     "duration": 0.437921,
     "end_time": "2023-10-18T10:08:38.267361",
     "exception": false,
     "start_time": "2023-10-18T10:08:37.829440",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA2cAAAHICAYAAADKnpJ3AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8qNh9FAAAACXBIWXMAAA9hAAAPYQGoP6dpAABcPElEQVR4nO3df3zN9f//8fsZZhvmx8zPEo2zNRujrVZ+bESEfqzVR95NDUkp8iMiEiF5RyLhjZFIfufdW0l+hIqWnxEbphli5vfP/fb6/uG7k2NTO2tzXtnterm42F6v5+t5Hmfn9Tzn3M/r+Xodi2EYhgAAAAAATuXi7AIAAAAAAIQzAAAAADAFwhkAAAAAmADhDAAAAABMgHAGAAAAACZAOAMAAAAAEyCcAQAAAIAJEM4AAAAAwAQIZwAAAABgAoQzALeNjz76SL6+vlq8eLGzS4Gkli1bytfXV1lZWYXed+fOneXr66ukpCTbMl9fXzVv3rzQb8sRZtwHzVhTfpjh8byZQYMGydfXV5s2bXJ2KUU6zvJr2bJl8vX11YQJE27p7R49elS+vr7q1KnTLb1doCiVdHYBAAAUhldffVVly5Z1dhnALfXcc8/p4sWLcnEpfp+3e3p66tVXX1X16tWdXQpQaAhnAIDbQq9evZxdAnDLRUdHO7sEp/H09GTc47ZT/D5mAQAAAAATIpwBxVjOeRNHjhzRqFGj9OCDD6pRo0bq2LGjVq1alec2Bw8eVP/+/dWkSRMFBATooYce0tixY3X+/Hm7djnnuXz33Xfq0qWLAgIC1KxZM/3yyy+SpNWrV6tz58564IEH1KBBA7Vt21bjx4/XxYsXC3ybObKzszV58mS1aNFCgYGBevTRRzV37lxdvXo1V9uffvpJr776qpo2baqAgADde++96tixo5YuXWrXLjY2Vr6+vpo+fbpGjBihRo0a6b777tO8efMkSenp6Zo9e7Y6duyo4OBgBQQEqGnTpurTp4/27duX59/9xIkTGjdunFq0aKGAgAC1bt1aH3/8cb7OHck5x+Orr77SvHnz9PDDD9v+jtOnT8+zj3Pnzmns2LFq1aqVAgIC9OCDD6pfv346ePBgnvf1k08+0cqVK/Xkk0+qQYMGatq0qcaOHauMjAwdP35cffv2VUhIiO6//3716NHD7vyv6x09elSvvvqqGjVqpHvvvVcvvviidu3alWfbDRs2KDo6WsHBwWrQoIEef/zxmz52N8rrHKWLFy/qo48+0hNPPKFGjRopICBA4eHhGjx4sH7//Xe7tp07d1ZwcLDOnj2rYcOGqWnTpgoMDFSHDh302Wef/eXtX8+RfTA5OVnDhg1TWFiYAgIC1Lx5c7311ls6ceKEXbucx3zZsmXq06ePGjRooAceeECrV6+WJGVlZWn69Olq27atGjRooDZt2tj2z7zs2bNHr7/+usLDwxUQEKBGjRrpiSee0KxZs5SdnW3X9vfff9fAgQNt+06TJk3Uu3dv/frrr7n6TUpK0rBhw9S6dWs1aNBADRs2VLt27fThhx8qLS3Nrq2vr6969OihhQsX6sEHH1RQUJBef/31m9a8YcMG2767f/9+2/KUlBS99957ateunYKCghQYGKjWrVtr1KhROnv2rF0fLVu21OOPP67ff/9d/fv31/33368GDRooMjJSX3/99U1vOy9XrlzRu+++qyZNmqhhw4Z66qmn9OWXX+bZ9ttvv1W3bt30wAMPqH79+goJCdFzzz2ntWvX5mqbnp6ujz76yDau27Rpo08++UTLly+37QPX358bzzm71c9H1/viiy8UERGhBg0aKDQ0VH379s011qT8738555W98847mjx5soKDg9W4cWONGzeOc85wW2JaIwD16dNHSUlJ6tChg7KysvTtt9+qd+/eGjBggF544QVbu59++kkvv/yyMjMz1apVK91xxx2Ki4vTrFmztG7dOn3++eeqVKmSXd9Dhw5V1apV9dxzz+nAgQO65557tHLlSvXt21d33HGH2rdvL1dXV23dulXTp0/X1q1bNX/+fFkslgLf5uTJk3Xx4kW1b99epUuX1rp16zRq1CjFx8dr9OjRtnZLlizR0KFDVblyZbVs2VKenp46fPiw1q1bpzfffFOpqamKioqy63vOnDmyWCx65plndOTIEQUFBenq1avq3r27YmNj1bhxYz311FPKzs7W9u3btXLlSm3cuFErV65U1apV7fp65ZVX9Pvvv6t169ZydXXV119/rUmTJik1NfVP36Beb9asWdq7d6/atm2rsLAwbdy4UePHj9f27ds1depU298xJSVF//rXv3TkyBHdf//9evjhh3Xy5El98803+u677zRz5kzde++9dn3/97//1YEDB9SmTRuFhITom2++0axZs3TmzBlt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9u2SpMWLF+vq1at6/fXXVbFiRVtbFxcXDRw40NbGEQ8++KDeeeedXBdMcHFx0X333Scp78clOjra7mhaSEiIypUrd9Npm3nJzz64a9cu7d27Vw8//HCuIzVhYWFq0qSJduzYkWvaaWhoaK59NqfPAQMG2P2tw8LC7PYPSTIMQ6+99prGjx+f66icj4+PKleubLf/GYYhSfrll1+UmZlpW96uXTutWbNGw4YNsy3r3Lmzxo4dq5CQELt+vby8VK9ePV29elXnzp3Tjdq2bZtrWY6dO3fqxRdflKenp+bOnau7777bbn379u01YsQIPfbYY3bL3dzcbEdX8nqcX3jhBbujvC1atJAkhx7nF154QTVr1rT9XrNmTXXv3l3Z2dm2586SJUvq3//+t0aOHGm3X0l5P9csW7ZMJUqU0ODBg+3qa9Omje6///6/rMmZz0fNmjWzOwLv4uJiew7J+bs6uv/l8PT0VJMmTfJVB/BPxrRGAHZTy3I0btxYkrR3715JsgWpxMREffTRR7nalyhRQllZWdq3b5/di/Odd96Zq+2//vUvDRkyRNHR0br77rvVpEkTNW3aVKGhoXJzc7O1K+htBgcH52qb8yYt5/64ubnZ3hD+/vvvSkhI0NGjR5WYmKidO3dKUq7zbm52f2rXrq3atWsrMzNTe/fu1aFDh3T06FHt379fP/300037ql27dq5lnp6ekmT3JvjP5LzZup6vr6/KlClju6979uyRYRjKyMjI8++YnJws6drfJiws7E/rK1OmjM6dO2cX5iXZHreMjAy75a6urgoMDMzVT1BQkFatWqW9e/cqODjY9lh///33eZ6P5ubmpri4OBmGke+pjX5+fvLz81N6erp27dqlQ4cO6ciRI9q3b5/Dj0u5cuXyPB/yZvKzD+bc59OnT+f5uFy5ckXStcfv+g8E8toH9+7dKw8PD1mt1lzr7r33XrtzSC0Wi1q1aiVJOnnypPbv368jR47o0KFD2r17t06fPi3p2t+mRIkSatu2raZMmaLFixfr22+/VWhoqJo2bapmzZrlqiXnzfO5c+e0b98+HT58WIcPH9aePXts56fdeN5d+fLlVb58+Vx1S9fOGXzhhRd05coVBQUF5XozL117rmrcuLEuXbpkd5txcXGKjY3N8zal3I+zo2NPyt/jXKFCBbVv316SdOjQIR08eFBHjx7VwYMHtW3bNkl/7IcZGRmKj49XjRo18rw8fEhIiO0+3Ywzn4/y6iPng4Sc/dnR/S/HHXfc4dC0ZuCfinAGQNWqVcu1LOf7oi5cuGD3/7p167Ru3bqb9nXjRTpu/KRYunZUoXLlypo7d65iY2M1d+5czZ07Vx4eHnrmmWfUv39/lSxZssC3Wbly5VxtypQpI+mPNwiStGPHDv373/+2Hb1xcXFR7dq1FRISot27d9uOGFzv+vCYwzAMzZ49WzExMTp16pQkycPDQ/7+/rrnnnt08uTJPPvK64hizpuPvNrn5Wbf71O2bFlbLTl/n3379uW6GMD1bvw75pwfkhdXV9d81Ve5cuU831Dd+HjkPNZz58790/4uX76c7+8yy8jI0OTJkzV//nxbsPL09FRgYKDq1aunrVu35rndnz0u+ZWffTDnPm/ZskVbtmy5aV83Pi557YMXL15UhQoV8qzz+qMhOQ4ePKixY8dq48aNtn3tzjvv1L333qsDBw7o/PnztuXe3t5atmyZ/vOf/2jNmjVatWqVLeyFhoZq+PDhttCUc2GOVatW2S4kUbVqVTVu3FhVq1bV0aNHc+3bed2fHFeuXFGVKlV09913a9OmTVq8eLGefvppuzaXLl3S+++/r+XLl9suOFKpUiU1bNhQtWrVUnx8fL7GX0He+Of3uWb9+vX64IMPbOOvZMmSqlu3rgIDA5WQkGCrL+eIkbe3d563d+N5Ynlx5vNRXn1cX1cOR/a/HH+2nwC3E8IZgFxXUJP+eEOY86lnzhuOCRMmqF27dn/7NsPDwxUeHq7U1FRt375d33//vZYvX65Zs2bJ09NTL7/8coFvM68jHDlXvsv5hP748ePq2rWrDMPQoEGD9MADD6h27dpyc3NTenq6Fi5cmO/bmzNnjsaOHav69etrxIgR8vPzU82aNWWxWPT5559r48aN+e7LUXk9doZh6OLFi7bpgTl/x06dOmn48OFFVktecgLIjW58PHJq3LRpU54XsCiI999/X59++qkefPBBdenSRb6+vrY3t+PGjbtpOCsM+dkHc+7z66+/ru7du/+t26tQoYIuXbqU55HF60NCzu/R0dE6ffq0Xn75ZbVo0UI+Pj62evKaOla9enUNHz5cb7/9tvbv36/NmzdrxYoV+umnn/TSSy/pm2++kSS9+OKLiouL07PPPqv27durbt26tvv7f//3fzp69KhD98vDw0Pz5s2TYRh67LHHNHbsWDVv3twupAwcOFBr165Vu3bt1LFjR9WrV8+2D/Xt21fx8fEO3aYj8vM47969Wz179pSnp6dGjRqloKAg3XXXXXJ1ddXBgwdt04+lP/aJmx2lvXEKd16c+XyUHwXZ/4DihHPOANgub3+9nKNJDRs2lHTt3CRJN70E+pQpUzR16tQ8zye53qVLl/Txxx9r9uzZkq4dWWvSpIkGDRpkm9qVcxShoLd5/blsOXKmD+VMsfv222915coVde3aVV26dJGfn5/tk9kDBw5Iyv+nxcuXL5ckTZw40XZFyZw3yAkJCfnqo6Dyeuzi4uJ05cqVfD92X331lT788MMieRN76dIlJSYm5lqeE4xyHo+cGvO6P5cuXdLo0aP/9LLweVm+fLlKly6tqVOn5npDn/O45PcxdlR+9sGc8yhv9rh89tlnmjx5cr4CTUBAgFJTU/O8tP2Nf9NNmzYpJSVFjz76qF577TU1aNDA9sb4zJkztvORcv42X3/9td5++21dvHhRFotFvr6+io6O1sKFC1W7dm0dOnRIKSkp2rdvn+Li4hQSEqJhw4bp3nvvtQWUzMxMHTp0yK7f/ChXrpzuuusu1a5dWz179tTFixf19ttv29ZfuHBB69atU82aNTVhwgSFhobahXtnPM437tv/+9//lJ2drQEDBujpp59WvXr1bEeeb6yvbNmyqlOnjpKSkvI87ypnyvWfcebzUX44uv8BxQ3hDICmTJlim/4iXTtxe+bMmSpTpoztXIlWrVqpQoUK+uyzz3K92fv66681ceJELV++3HaOws14eHho4cKFmjRpUq437UeOHJEk2+WiC3qbixYtsvUlXZtqNXnyZLm4uNimROUEsevvt3TtiOGoUaMkKd/f75PTV865Ejl+/vln20UsHDmPxRFffvml3Ru2y5cva8yYMZJku/hHjRo11KRJE+3Zs0dz5syx2/63337TiBEjNH369HxPF3TUxIkT7c5x+frrrxUbG6v69esrICBA0rWprtK1o10nT5602378+PH69NNPFRcX59Dtli5dWllZWbnC+4oVK7R+/XpJRfe45GcfbNy4se6++26tXr3a9l1lObZt26YxY8bok08+sbtAys3kPNZjx461O7qybds2ffXVV3Ztb7bvp6en66233rKdn5Wz/8fHx2vB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377y9PRU06ZNHepn27ZtysjI0FtvvaWMjAyNHTtWL730kjZs2GD35Ag4Q2JioiTpzjvv1Lhx4zR//ny9/vrr8vX1VXJysj7++GO99tprWr9+vTw8PPTTTz+pZ8+eatGihV577TUlJSXp7bffVnp6upPvCWCvIK8LhmGoR48eOn/+vPr37y9vb2/FxcVp4sSJGjZsmGbNmmVru2rVKvn4+Gjo0KEyDENjx45V7969tW7dOpUoUYKxAqdq166dXnvtNR07dkw1atSQJF26dEkbN27U7NmztXHjRkmO7fM5HNnmq6++kr+/v0aPHq1jx45p5MiRioqKkpubm9544w2dO3dOo0eP1jvvvMMMp0LEu0s43b/+9S+dPHlSMTExeueddyRJFStWVNOmTdW5c2c1bNjQ4T5feeUVvfjii5Kk5s2b69ChQ5o8ebLD4czV1VXTp09XhQoVJF17chw6dKgSEhLk5+fncF1AQRiGoaysLNvv58+f188//6ypU6cqKChIAQEB+uSTT9S3b1+7owhubm7q1auX9u3bp0aNGumjjz5S3bp1NXnyZNs5al5eXurXr98tv0/AnynI60JKSorc3d31xhtvKDg4WJJ0//336+jRo1qwYIFd26ysLMXExKhs2bKSpMuXL+uNN95QXFycAgICGCtwqvDwcHl4eOibb75R165dJUmrV69WpUqVdO+999raObLPF2SbzMxMTZ48WeXLl7fV8MMPP2jNmjW68847JUlxcXH673//W7h/gGKOcAZTeO211xQdHa3vv/9emzdvVmxsrP73v/9pxYoVGjx4sJ5//nmH+suZ8pKjVatW+uijj3T58mWH+qlbt64tmEnSHXfcIUm6ePGiQ/0Af8eWLVtUv359u2UuLi564IEHNHLkSFksFo0fP17StekqSUlJSkxM1Lp16yRde4HNyMjQjh079Morr9hdPKRNmzYcBYYpOfq6ULVqVX366aeSrk31TUpK0sGDB7V9+3ZlZmbata1bt64tmOVsK1274AJjBc7m5uamli1bauXKlbZw9tVXX6ldu3Z2+6Qj+3xBtvHx8bEFM0ny9vZWpUqVbMFMkipUqMB7okLGswxMo3z58urQoYM6dOggSdq7d68GDhyocePG6bHHHnOoL29vb7vfvby8ZBiGLl265FA/Hh4edr+7uFw7TfPq1asO9QP8HfXr19eIESMkXbuSV+nSpVW9enW7N5e7d+/WiBEjtHv3brm5ualu3bqqWbOmpGtH3s6dO6fs7Gx5eXnZ9V2yZElVrFjx1t0ZwAGOvi58+eWX+uCDD3T8+HFVqFBBfn5+cnNzy9XO3d3d7vfrn9sZKzCDRx55xHYeWJkyZbR582b16dMnV7v87vMF2eb615gcN44dFD4uCAKnOnHihJo2barFixfnWufv768+ffooIyNDR44ckSRlZ2fbtbly5Uqe/d743U+nTp1SiRIlVL58edunTvntC3C2MmXKKDAwUIGBgQoICFC9evXsXjQvXbqkF154QR4eHlqxYoV27NihpUuXKjIy0tbGy8tLpUqV0unTp+36vnr1qs6ePXvL7gvwVxx9XcixdetWvfHGG2rdurU2bNig2NhYzZkzx+GrjzJWYAbNmzdXuXLltGrVKq1evVp33HGH7SJQOQqyzxfWOEHRIZzBqSpXrqySJUtq/vz5eZ5o/dtvv6l06dK66667VLZsWSUnJ9ut3759e579fv/997afr169qm+++UYNGzaUm5ub7U3t9X1lZmZq165dhXGXgFvut99+07lz5/Tcc8+pXr16tqMAOSeNX716VSVKlFDjxo21Zs0au23XrVtndz4b4GyOvC5cb8eOHbp69ap69+6tatWqSbr2IdymTZsk5X/GA2MFZuDq6qqHHnpI3377rVauXKn27dvnalOQfb6wxgmKDtMa4VQlSpTQ8OHD9corrygyMlLPPvusfHx8lJqaqh9//FGfffaZXnvtNZUvX14tWrTQunXrNHr0aLVq1Urbtm3T8uXL8+z3ww8/VHZ2tqpXr67PP/9ciYmJmj17tqRr02QaNWqkefPm6a677lLFihU1d+5cpaWl5ZrGCPwT1KlTR2XLltW0adNUsmRJlSxZUqtWrdKSJUskXTuPRpJ69+6tzp07q3fv3nrqqad07NgxTZw4UZIK7Uusgb/LkdeF6zVo0ECS9M477ygyMlIXLlzQvHnzFB8fL+na7Ii8pmnlhbECM2jXrp169OghFxcXDR06NNf6guzzhTlOUDQ4cganCw8P16JFi2S1WjVt2jR169ZN/fr1U1xcnCZMmGC76mJkZKS6d++ur7/+Wt27d9f27dttL5Y3Gj16tD799FP17NlTJ06c0IwZM3TffffZ1r/33nsKCAjQW2+9pUGDBumee+5x+KIjgFmUK1dOU6ZMkWEYeu211zRw4EAdO3ZM8+bNU5kyZbR161ZJUnBwsD766CMlJiaqZ8+emj17tt566y1J16ZOAmaR39eF691///0aNmyYduzYoe7du2vMmDGqUaOGJk+eLOnaV6PkF2MFZvDggw/K09NT9erVk4+PT671BdnnC3OcoGhYjBu/4REAcFtau3atqlWrZnflxwMHDqhDhw6aMmWKHnroISdWB5gHYwWAszCtEQCKiR9++EFff/21Xn/9ddWpU0fJycmaOnWq7r77boe/AxC4nTFWADgLR84AoJhIS0vTxIkTtWrVKqWkpKhChQpq1qyZ+vfvr8qVKzu7PMA0GCsAnIVwBgAAAAAmwAVBAAAAAMAECGcAAAAAYAKEMwAAAAAwAcIZAAAAAJgA4QwAAAAATIBwBgAAAAAmQDgDAAAAABMgnAEAAACACfw/9pbFO6Fv1icAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 1000x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(10, 5))\n",
    "\n",
    "colors = [\"#D3D3D3\", \"#D3D3D3\", \"#800000\", \"#D3D3D3\"]\n",
    "\n",
    "sns.barplot( \n",
    "    x=\"waktu_hari_pembelian\",\n",
    "    y=\"total_orders\",\n",
    "    data=df_bagian_hari.sort_values(by=\"total_orders\"),\n",
    "    palette=colors\n",
    ")\n",
    "plt.title(\"persebaran pembelian berdasarkan bagian hari\", loc=\"center\", fontsize=15)\n",
    "plt.ylabel(\"total order\")\n",
    "plt.xlabel(None)\n",
    "plt.tick_params(axis='x', labelsize=12)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "2e75b5af",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:38.346957Z",
     "iopub.status.busy": "2023-10-18T10:08:38.346317Z",
     "iopub.status.idle": "2023-10-18T10:08:38.393729Z",
     "shell.execute_reply": "2023-10-18T10:08:38.392649Z"
    },
    "papermill": {
     "duration": 0.091408,
     "end_time": "2023-10-18T10:08:38.396015",
     "exception": false,
     "start_time": "2023-10-18T10:08:38.304607",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>hari_pembelian</th>\n",
       "      <th>total_orders</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Monday</td>\n",
       "      <td>15258</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Tuesday</td>\n",
       "      <td>15045</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Wednesday</td>\n",
       "      <td>14645</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Thursday</td>\n",
       "      <td>13961</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Friday</td>\n",
       "      <td>13320</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Sunday</td>\n",
       "      <td>11253</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Saturday</td>\n",
       "      <td>10285</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  hari_pembelian  total_orders\n",
       "0         Monday         15258\n",
       "1        Tuesday         15045\n",
       "2      Wednesday         14645\n",
       "3       Thursday         13961\n",
       "4         Friday         13320\n",
       "5         Sunday         11253\n",
       "6       Saturday         10285"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_hari = orders.groupby(by=\"hari_pembelian\").order_id.nunique().sort_values(ascending=False).reset_index()\n",
    "df_hari.rename(columns={\n",
    "    \"order_id\": \"total_orders\"\n",
    "}, inplace=True)\n",
    "df_hari"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "7acc07f8",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-10-18T10:08:38.476457Z",
     "iopub.status.busy": "2023-10-18T10:08:38.476112Z",
     "iopub.status.idle": "2023-10-18T10:08:38.786896Z",
     "shell.execute_reply": "2023-10-18T10:08:38.785812Z"
    },
    "papermill": {
     "duration": 0.353483,
     "end_time": "2023-10-18T10:08:38.789574",
     "exception": false,
     "start_time": "2023-10-18T10:08:38.436091",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA2cAAAHICAYAAADKnpJ3AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8qNh9FAAAACXBIWXMAAA9hAAAPYQGoP6dpAABvYklEQVR4nO3deXwNZ///8fchIoldrLUvTSKWBAmxR0op3YjeqGhRS2tfGrTU0lJ1oxpLtIilllpKVZWqpUpL7S03STWK2qOW2LLK/P7wy3ydJjhJEznh9Xw8+qjMXHPNlfmcc3LeZ66ZYzEMwxAAAAAAIEvlyOoBAAAAAAAIZwAAAABgFwhnAAAAAGAHCGcAAAAAYAcIZwAAAABgBwhnAAAAAGAHCGcAAAAAYAcIZwAAAABgBwhnAAAAAGAHCGcAkMGmT58ud3d3rVy5MquHAkkBAQFyd3dXYmJihvfduXNnubu769SpU+Yyd3d3NW7cOMP3lRb2+Bi0xzHZwh7qeT/Dhw+Xu7u7du7c+Uj3u3r1arm7u2vq1KmPdL/Ak8AhqwcAAMDjpG/fvsqbN29WDwPINFWqVFHfvn3l4+OT1UMBHjuEMwAAMlC/fv2yeghApqpSpYqqVKmS1cMAHktMawQAAAAAO0A4A5Dlkq+bOH36tMaNG6f69eurZs2aat++vTZu3JjqNsePH9eQIUPUoEEDVatWTc8884wmTpyo6Ohoq3bJ17n88MMP6tq1q6pVq6ZGjRrpt99+kyRt2rRJnTt3Vr169VSjRg21bNlSU6ZM0Y0bN9K9z2R37tzRjBkz1LRpU1WvXl0vvPCCFi1apKSkpBRtf/nlF/Xt21cNGzZUtWrVVLt2bbVv316rVq2yard79265u7tr9uzZGjt2rGrWrKk6depo8eLFkqS4uDjNnz9f7du3l4+Pj6pVq6aGDRtq4MCB+v3331M97hcvXtTkyZPVtGlTVatWTc2bN9fMmTNtukYr+dqTb7/9VosXL9azzz5rHsfZs2en2se1a9c0ceJENWvWTNWqVVP9+vU1ePBgHT9+PNXfdcGCBdqwYYPatm2rGjVqqGHDhpo4caLi4+N1/vx5DRo0SL6+vqpbt6569epldf3Xvc6cOaO+ffuqZs2aql27tnr27KlDhw6l2vbHH39Uly5d5OPjoxo1auill166b+3+KbVrlG7cuKHp06fr5ZdfVs2aNVWtWjX5+/vrnXfe0dmzZ63adu7cWT4+Prp69apGjRqlhg0bqnr16nr++ee1ZMmSh+7/Xml5DF64cEGjRo1SkyZNVK1aNTVu3FjvvfeeLl68aNUuuearV6/WwIEDVaNGDdWrV0+bNm2SJCUmJmr27Nlq2bKlatSooRYtWpiPz9QcOXJEb7/9tvz9/VWtWjXVrFlTL7/8subNm6c7d+5YtT179qyGDh1qPnYaNGig/v3763//+1+Kfk+dOqVRo0apefPmqlGjhry8vNSqVSt98sknio2NtWrr7u6uXr16afny5apfv768vb319ttv33fMP/74o/nYPXbsmLk8KipKH330kVq1aiVvb29Vr15dzZs317hx43T16lWrPgICAvTSSy/p7NmzGjJkiOrWrasaNWooMDBQ69evv+++UxMbG6tPPvlEzzzzjKpVq6amTZvqv//9r2JiYlK0/f777/XGG2+oXr16qlq1qnx9ffXaa69py5YtVu0eVGeuOQMyD9MaAdiNgQMH6tSpU3r++eeVmJio77//Xv3791dwcLC6d+9utvvll1/01ltvKSEhQc2aNVPp0qUVHh6uefPmaevWrfriiy9UuHBhq75Hjhyp4sWL67XXXtMff/yhKlWqaMOGDRo0aJBKly6t1q1by9HRUfv27dPs2bO1b98+LV26VBaLJd37nDFjhm7cuKHWrVsrd+7c2rp1q8aNG6eIiAiNHz/ebPfll19q5MiRKlKkiAICApQ/f3799ddf2rp1q959913FxMQoKCjIqu+FCxfKYrGoQ4cOOn36tLy9vZWUlKQePXpo9+7dqlWrltq1a6c7d+7owIED2rBhg7Zv364NGzaoePHiVn316dNHZ8+eVfPmzeXo6Kj169dr2rRpiomJeeAb1HvNmzdPR48eVcuWLdWkSRNt375dU6ZM0YEDBzRr1izzOEZFRenVV1/V6dOnVbduXT377LO6dOmSvvvuO/3www+aO3euateubdX3119/rT/++EMtWrSQr6+vvvvuO82bN09XrlzRzp07VaJECbVr105HjhzRtm3b9Ndff+mbb76Rg4P1n7igoCDlyZNHHTp00Llz57Rp0ybt3LlTc+bMUb169cx2c+bM0eTJk1W4cGG1aNFC+fPn108//aRx48Zp7969CgkJMX8fW9y+fVsdOnTQ8ePH1aBBAzVo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z0o+NuvXr9fo0aN148YNWSwWubu7q0uXLlq+fLnKly+vkydPKioqSr///rvCw8Pl6+urUaNGqXbt2mYwS0hI0MmTJ636tUW+fPlUrlw5lS9fXr1799aNGzc0evRoc/3169e1detWlSpVSlOnTpWfn59VuM/sOtvim2++0Z07dxQcHKxXXnlFTz/9tHnm2R7GB+AuwhkAuxEaGmpOgZPuXhA/d+5c5cmTx7xWolmzZipYsKCWLFmS4s3e+vXrFRISojVr1pjXbdyPi4uLli9frmnTpqV40558AX3p0qX/1T5XrFhh9iXdnWo1Y8YM5ciRw5wSlRzE7v29pbtnDMeNGydJNn3f2L19JV+rk2zPnj3mTSzSch1LWqxdu9a8Rk66O+1vwoQJkmTe/OOpp55SgwYNdOTIES1cuNBq+z///FNjx47V7NmzbZ4umFYhISFW19SsX79eu3fvVtWqVVWtWjVJd6e6SnfPdl26dMlq+ylTpujzzz9XeHh4mvabO3duJSYmpgjv69at07Zt2yRlXl1seQzWqlVLFStW1KZNm8zvKku2f/9+TZgwQQsWLLC6Qcr9JNd64sSJVjfI2b9/v7799lurtvd77MfFxem9994zr89KfvxHRERo2bJlKcLx9evXde3aNeXJk0eFChUypwlGR0dbPXfu3LmjCRMmmGfjbX1e/dMbb7whNzc3/fDDD1q7dq2ku9Nrc+TIoZiYmBQ3Bpo9e7b5XWjp3WdGuN/rw/nz5/Xxxx9LytrxAbiLaY0A7Mbff/+tl156Sc8884wSEhL0/fffKyYmRhMmTFDRokUl3b2G6b///a/69u2rjh07KiAgQOXKldPx48f1448/ysXFRR999JFy5HjwZ085cuTQ8OHDNXjwYLVt21YtWrRQ0aJFderUKW3ZskWFCxc2p3ild58FChRQYGCgWrVqpaSkJG3evFmXL1/WkCFDzO9jatq0qQoWLKjly5frwoULcnd3199//62tW7cqJiZGefPm1Y0bN5SYmJjie7v+qW3btjp48KB69Oih5557Tvnz51dERIR27typQoUKKS4u7qFnFNPL0dFRQUFBatGihQoWLKht27bpzJkzat++vfz9/c12H3zwgTp16qQPP/xQGzdulJeXl65du6bvvvtOt2/f1ogRI8xQnJHy58+v3bt3q127dqpfv75OnDihrVu3qmDBgpo4caLZrlatWurdu7dCQ0PVunVrBQQEqFChQtq7d68OHz6sihUravDgwWnad2BgoD799FO1a9dOLVu2VK5cuXTo0CHt27dPRYoU0d9//51pdbHlMZgjRw5NmjRJXbt2Nb8I3d3dXefPn9emTZtkGIYmTJhgntV6kICAAAUGBmrVqlV68cUX1bRpU129elXff/+9SpUqZZ61ku7eIKR8+fL66aef1KlTJ9WsWVPXr1/Xjz/+qEuXLqlQoUK6evWqrl27JmdnZ73++utat26dPvnkE+3evVuenp6KiYnRpk2bdO3aNb333ntydHRU+fLlVatWLR04cEDt2rVTvXr1lJCQoB07dujkyZNydXXV5cuX033Mc+XKpXHjxqlDhw4aP368GjRoIFdXVz333HNat26d2rZta95xcc+ePTp69KhZZ1vvfpoZWrdurfnz5+uTTz7RkSNHVLZsWZ07d05bt25Vrly5lCtXrkx7HAKwHWfOANiNDz74QE2bNtXGjRu1adMmeXt7a+HChXrppZes2jVp0kQrV65Uy5YtdfDgQS1cuFDHjh3TCy+8oC+//NK8nfrDtGrVSmFhYapVq5Z+/vlnzZ8/X7/99pvatGmjVatWWd2lLD37HDlypNq1a6dNmzbpq6++UsmSJRUSEqKePXuabYoVK6bPP/9cTZs21f/+9z/zy2obN26s1atXq2XLlkpISEhxe/nU/Oc//9H48eP11FNP6ZtvvtHKlSt15coV9e3bVxs2bJCLi4u2b9+e6h3Z/q1XX31V/fv314EDB/Tll1+qQIECGj9+vN5//32rdqVKldLq1avVpUsXRUVFadGiRdq+fbtq1aqlefPm6bXXXsvwsUl3p6UtXrxYhQsX1pIlS7Rv3z61atVKX375pZ5++mmrtgMGDFBoaKg8PT21efNmLV26VLdu3dKbb76pL774Is3XovXr10/BwcHKnz+/Vq5cqbVr1+rOnTt67733zGsKk8+gZTRbHoPS3emIq1ev1iuvvKLIyEh9/vnn2r9/v/z9/fXFF1+kuA3+g4wfP16jRo1Snjx5tHLlSh08eFB9+/ZNcT2bs7Oz5s2bp+eff16nT5/W559/rp07d6p69epaunSp+Vj44YcfJN29Df7SpUvVqVMnnT9/XkuWLNG6detUuXJlzZo1y/yidovFopkzZ6pjx466fv26Fi9erC1b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0fHjx8039i1btlSbNm0kSZMnT9bMmTPVvn17zZ07V++//76uXr2qAQMG6Pbt2/L399dbb70lSZoxY4Z69+6dpnGcO3dOmzZt0scff6yBAweqUKFCmjRpkmbOnKnAwEDNmDFDhQoV0pQpU6y227Ztm/r06aOqVasqNDRU06dPV6lSpfTBBx/owIEDcnBw0Msvv6zNmzdb/ZH77bff9Oeff6pt27b/5vDZHVvraaukpCQNHDhQrVq10uzZs1W7dm1NnjxZO3bsMNd3795d27Zt09tvv62JEyfq4MGD5huBZA97/Dz99NPy8vJKcR3V119/LScnJ7Vo0eJfHJXsLTExMcV/94bvDRs2KFeuXJo5c6Zee+21FNtfvHhRQUFBio6O1qRJkzRgwABNnjxZFy9eNNsYhqFevXrp559/1pAhQxQWFqbevXtr586dGjVqlCTphRdeUO7cuVPU6KuvvlKdOnVUunTpTDoC2cf58+c1e/ZsDRgwQNOmTZNhGOrXr58uX76c5r5mzZqlFi1a6OOPP9YzzzyjOXPmaMmSJerTp4/mzZunjh07au7cufr0008lPZnPxXr16lmFs19++UV37txR/fr11bBhQx0/flznzp2TJJ06dUpRUVFq2LChrly5og4dOujIkSN67733NGXKFCUlJalTp046fvy4JNuPpyRt3LhRW7Zs0ciRI/Xxxx/r77//Vv/+/XXnzh1J0okTJ9ShQwddvnxZH330kcaPH6/Tp0+rY8eO5mPj22+/1cSJE9WpUyeFhYWpT58++vrrrzVu3DhzP8HBwVq+fLl69OihTz75RNHR0VqwYIHVWJYsWaJRo0bpmWee0WeffaZJkyYpV65cCg4O1rlz51SwYEE1a9ZM33zzjdXryJYtW3Tjxg29/PLLGVIbe/XZZ5/pvffeU7169fTpp5+qU6dOmjNnjvk6J909zpGRkRo7dqxmz54tT09PDRs2zAx+vKamX6tWrfTbb7+Zz0tJunnzprZv367nn3/eXGYYht58803NnTtX7dq106effqqWLVvqk08+0ejRo636fNjz78iRI+rWrZvy5s2rkJAQvf766xo8eLBVHzExMXrttdd0/PhxjR49WmFhYQoKCtK6devMDzLatWunuLg4fffdd1bbrlmzRi1btpSLi0uGHquMwLTGbOrVV1/VpUuXFBYWpvfff1+SVKhQ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Va9evSfyuejq6io3NzcdOHBAbm5uOn36tNWdGBs2bKjFixfLMAzt27fPfM2/du2aTp06lepZaenumzpbj6ekFI//5G2S637t2jWtX78+1SmRyX/jWrVqpaSkJC1dulQzZsxQSEiISpUqpSFDhqh169Y2/03866+/NGrUKP3yyy9ycHBQxYoVzVvtJ9c3R44catu2rebPn6/Ro0dr7dq1j3UgSHbt2jVJsjojfa+oqChJ0tSpU/Xpp59qw4YN+u6775QjRw7Vr19fY8aMUZkyZXhN/Zeee+4589q7PHnyaNeuXRo4cKBVm+joaBUqVMjqGjTp/47xvR94Pez5Fx0dneJ54+DgoEKFClktmz9/vj777DNdvXpVRYoUUdWqVeXs7Gy1r1atWunDDz/U2rVr1b17d23YsMH8AMUeEc6yoYsXLyowMFADBgwwT9Em8/T01MCBA9WnTx9FRkaqb9++cnd317p161SpUiXlyJFDP/74ozZu3PjQ/STP+01my0WTyU+ay5cvq2LFiuby5BfXZG+//baOHz+u+fPnq1atWnJ0dFRMTIxWrlxp1a5ly5YaN26cNm7caF4wfu+nXI8DW+uZfBF6euryT4UKFdLVq1d1584dq0+h7q3TzZs31b17d5seP4GBgfrqq6906NAhbdy4McWF3Ei7QoUKmTeKude9Ndq3b5+GDRumoKAgvfHGGypRooSku1Pp9u/fb7azWCxq06aNPv/8c3Xq1EmRkZF2O53DHt0vrN26deuh2+bIkUOdOnVSp06ddPnyZf3444/69NNP1a9fP+3cufOJfS7Wr19fv/32m8qUKaN8+fJZTd1u2LChpk2bpl9++UVnzpwxg1u+fPlUp04dDR06NNU+HR0dbTqetsqXL5/q16+f4g51kqzefCZ/oHbjxg399NNPmjNnjoKDg+Xj42P+Tfz777+t/nbdO56kpCT17NlTuXLl0ooVK+Tp6SkHBwdFRkamuGFF27ZtNXPmTG3fvl3r169Xq1atsnUgeNBzK0+ePJLuTiOU7l53Wb58+RR9JH8gki9fPgUHBys4OFh//vmntmzZotDQUI0dO1Zz587lNfVfaty4sfLly6eNGzcqX758Kl26tKpVq2bVpkCBArp69aoSExOtniPJAfqfwepBChYsmKJehmFY3WDum2++0UcffaQhQ4aoXbt2ZpgbMGCADh8+bLbLkyePWrZsqQ0bNqhKlSq6fv26XV+nybTGbKhIkSJycHDQ0qVLU73j059//qncuXPL0dFR165d02uvvaann37a/FQi+S5kyS+G//yEUbr7CeyFCxeslt17Aff91KxZU05OTikuvPzhhx+sft6/f79atGghPz8/85T1P8cl3f1Eu1WrVlq3bp127NjxWJ41s7We5cqVS3dd/qlevXpKTEzU5s2bzWXx8fHm9JDk/dry+JEkX19flS9fXpMmTdLVq1ft+kUvu/Dz89PBgwetLlaPjIy0ulPcwYMHlZSUpP79+5tvIu7cuWNOubq3RoGBgbpx44YmTJig8uXLW10ngAdLnnpz/vx5c1ny8+NhOnToYN4cwtXVVW3btlWnTp1048YN3bx584l9LtarV0/h4eH65ZdfVL9+fasglXz92bJly5Q/f37zLHSdOnV04sQJVahQQdWrVzf/W7t2rVauXKmcOXPadDxtVadOHUVGRqpKlSrmvqpVq6YFCxZo06ZNkqSBAweqb9++ku6Gg+eee069e/fWnTt3FBUVZV4b9qC/iVevXtWJEyfUrl071ahRw3xTm1p9S5UqpXr16mnRokU6cuRItv+bmNpzKzo62rzBi3R36mGuXLl08eJFq7rnypVLU6ZM0ZkzZ3T27Fk1adLEPM4VK1ZUjx49VL9+ffNvJq+p/46jo6OeeeYZff/999qwYYNat26dok2dOnV0586dFGebkz9kSMsxqlevnrZv325Oc5TufuXGvdMV9+/fr3z58qlnz55mMLt165b279+fIvC3a9dOx44d07x58+Tn52fXH/Rz5iwbypkzp8aMGaM+ffooMDBQnTp1UqVKlRQTE6Off/5ZS5Ys0YABA1SxYkXlzZtXn376qRwcHOTg4KCNGzfqyy+/lPR/83qTP5XatGmTGjdurEqVKqlp06b67LPP9Omnn8rb21vbtm0zb9n8IHny5FHv3r31ySefyNnZWX5+fvrxxx9ThLMaNWrom2++UdWqVVWiRAkdPHhQn332mSwWi9UTUbr7hGrfvr3y5s2rZ599NiMOoV2xtZ4FChRQ06ZNtXXrVo0fP17NmjXT/v37U9wq2Bb16tVTw4YNNXLkSF2+fFmlSpXS559/ritXrlhdKG3L4ydZYGCgpkyZogYNGqT4okqk3euvv64vv/xSb7zxhvr166c7d+7ok08+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\n",
      "text/plain": [
       "<Figure size 1000x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(10, 5))\n",
    "\n",
    "colors = [\"#D3D3D3\", \"#D3D3D3\",\"#D3D3D3\", \"#D3D3D3\",\"#D3D3D3\", \"#D3D3D3\", \"#800000\"]\n",
    "\n",
    "sns.barplot( \n",
    "    x=\"hari_pembelian\",\n",
    "    y=\"total_orders\",\n",
    "    data=df_hari.sort_values(by=\"total_orders\"),\n",
    "    palette=colors\n",
    ")\n",
    "plt.title(\"persebaran pembelian berdasarkan hari\", loc=\"center\", fontsize=15)\n",
    "plt.ylabel(\"total order\")\n",
    "plt.xlabel(None)\n",
    "plt.tick_params(axis='x', labelsize=12)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2e6da7d8",
   "metadata": {
    "papermill": {
     "duration": 0.038555,
     "end_time": "2023-10-18T10:08:38.867816",
     "exception": false,
     "start_time": "2023-10-18T10:08:38.829261",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "Hari senin adalah hari yang paling banyak digunakan oleh konsumen untuk belanja dan umumnya konsumen melakukan transaksi pada siang hari."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2e4701bf",
   "metadata": {
    "papermill": {
     "duration": 0.0377,
     "end_time": "2023-10-18T10:08:38.944776",
     "exception": false,
     "start_time": "2023-10-18T10:08:38.907076",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# Conclusion\n",
    "1. **Category barang yang paling banyak dibeli dan paling sedikit diminati?**\n",
    "> Category yang paling diminati adalah bed_bath_table sebaliknya security dan service adalah kategori yang paling sedikit dibeli.\n",
    "\n",
    "2. **Berapa lama rata-rata pengiriman paket pengiriman paket terlama ? dari mana ke mana?**\n",
    "> setelah dilakukan pembersihan outlier, pengiriman terlama antarkota adalah 24.3 hari yaitu dari kota sao jose dos campos ke kota belem. Untuk pengiriman antarstate yang paling lama dikirimkan adalah 27.69 hari yaitu dari state SP ke state RR.\n",
    "\n",
    "3. **Berapa rata-rata payment value dari tiap tipe transaksi? dan transaksi tipe apa yang paling sering digunakan?**\n",
    "> 75% konsumen menggunakan tipe transaksi creditkan dengan rata-rata payment value sebesar 163.022616.\n",
    "\n",
    "4. **Bagaimana perbandingan penjualan tahun 2017 dan 2018?**\n",
    "> pada tahun 2018, terjadi peningkatan pembelian secara signifikan dibandingkan tahun 2017 yaitu meningkat sebanyak 140.87%.\n",
    "\n",
    "5. **Bulan apa yang terjadi peningkatan penjualan tertinggi?**\n",
    "> November 2017 adalah bulan dengan penjualan tertinggi, terutama di tanggal 24/11/2017.\n",
    "\n",
    "6. **Bagian hari apa yang sering digunakan oleh pembeli untuk melakukan transaksi?**\n",
    "> Hari senin adalah hari yang paling banyak digunakan oleh konsumen untuk belanja dan waktu paling aktif untuk berbelanja ada di siang hari."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  },
  "papermill": {
   "default_parameters": {},
   "duration": 31.245794,
   "end_time": "2023-10-18T10:08:42.642806",
   "environment_variables": {},
   "exception": null,
   "input_path": "__notebook__.ipynb",
   "output_path": "__notebook__.ipynb",
   "parameters": {},
   "start_time": "2023-10-18T10:08:11.397012",
   "version": "2.4.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

# 🏠 Prediksi Harga Rumah dengan Streamlit

Aplikasi ini dibuat menggunakan Streamlit untuk memprediksi harga rumah berdasarkan beberapa fitur seperti luas bangunan, luas tanah, jumlah kamar tidur, kamar mandi, dan garasi. Model yang digunakan adalah **Linear Regression** dari scikit-learn.

---

## 🚀 Fitur
- Prediksi harga rumah secara real-time
- Input interaktif langsung dari halaman web
- Evaluasi model menggunakan Mean Absolute Error (MAE)

---

## 🧠 Model yang Digunakan
- Linear Regression
- Dataset dibagi menjadi training dan testing (80:20)
- Evaluasi menggunakan MAE

---

---

## ⚙️ Cara Menjalankan Aplikasi (Local)

1.Clone repo
git clone https://github.com/ridhotegar16/PrediksiHargaRumah.git
cd PrediksiHargaRumah
2.Buat Virtual Environment
python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # macOS/Linux
3.Install Dependencies
pip install -r requirements.txt
4.Jalankan Streamlit
streamlit run app.py

import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Load dataset
def load_data():
    data = pd.read_excel('DATA RUMAH.xlsx') 
    return data

data = load_data()

# Preprocess data
X = data[['LB', 'LT', 'KT', 'KM', 'GRS']]
y = data['HARGA']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate model
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)

# Streamlit app
st.title('Prediksi Harga Rumah')

st.write("### Evaluasi Model")
st.write(f"Mean Absolute Error: {mae}")

st.write("### Prediksi Harga Rumah")

# Input features
lb = st.number_input("Luas Bangunan (LB)(m\u00B2)", value=0)
lt = st.number_input("Luas Tanah (LT)(m\u00B2)", value=0)
kt = st.number_input("Kamar Tidur (KT)", value=0)
km = st.number_input("Kamar Mandi (KM)", value=0)
gr = st.number_input("Garasi (GRS)", value=0)

# Predict button
def predict_price(lb, lt, kt, km, gr):
    input_df = pd.DataFrame([[lb, lt, kt, km, gr]], columns=['LB', 'LT', 'KT', 'KM', 'GRS'])
    prediction = model.predict(input_df)
    return prediction[0]

if st.button('Prediksi'):
    price = predict_price(lb, lt, kt, km, gr)
    st.write(f"Prediksi Harga Rumah: Rp {price:,.2f}")

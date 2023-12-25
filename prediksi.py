import pickle
import streamlit as st

# Load the pre-trained model
model = pickle.load(open('prediksi.pkl', 'rb'))

# Set the title and add an image
st.title("Prediksi Harga Taksi")
st.image("taxi.jpg", width=400, caption="Taxi Image")

# Create input widgets in a single column
st.sidebar.title("Input Data Pemesanan")
hour = st.sidebar.number_input('Jam Pemesanan', min_value=0, max_value=23)
day = st.sidebar.number_input('Hari Pemesanan', min_value=1, max_value=7)
distance = st.sidebar.number_input('Jarak Perjalanan', min_value=0.0)
cab_type = st.sidebar.number_input('Jenis Taksi', min_value=0)
surge_multiplier = st.sidebar.number_input('Pengganda Tarif', min_value=1.0)
short_summary = st.sidebar.number_input('Cuaca saat Pemesanan', min_value=0)
name = st.sidebar.number_input('Jenis Mobil', min_value=0)

# Add a button to trigger the prediction
if st.sidebar.button("Prediksi Harga"):
    # Perform prediction using the model
    predict = model.predict([[hour, day, distance, short_summary, cab_type, name, surge_multiplier]])

    # Display the prediction result in the main column
    st.title("Hasil Prediksi")
    st.write("Prediksi Harga Taksi dalam USD:", predict[0])

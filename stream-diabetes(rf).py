import pickle
import streamlit as st
import numpy as np

# Membaca model
diabetes_model = pickle.load(open('diabetes_model(rf).sav', 'rb'))

# Membaca scaler
scaler = pickle.load(open('robust(rf).pkl', 'rb'))

# Judul web
st.title('Prediksi Pasien Terkena Diabetes')

# Membagi kolom
col1, col2 = st.columns(2)
with col1:
    Age = st.text_input('Input Usia Pasien (Tahun)')
with col2:
    Blood_Glucose_Level = st.text_input('Input Kadar Gula Darah Pasien (mg/dl)')
with col1:
    Diastolic_Blood_Pressure = st.text_input('Input Tekanan Darah Diastolik Pasien (mmHg)')
with col2:
    Systolic_Blood_Pressure = st.text_input('Input Tekanan Darah Sistolik Pasien (mmHg)')
with col1:
    Heart_Rate = st.text_input('Input Detak Jantung Pasien (bpm)')
with col2:
    Body_Temperature = st.text_input('Input Suhu Tubuh Pasien (Fahrenheit)')
with col1:
    SPO2 = st.text_input('Input SP02 Pasien (%)')
with col2:
    Sweating = st.text_input('Apakah Pasien Mengalami Kondisi Tubuh Berkeringat? (0=Tidak, 1=Ya)')
with col1:
    Shivering = st.text_input('Apakah Pasien Mengalami Kondisi Tubuh Gemetaran? (0=Tidak, 1=Ya)')

# Code untuk prediksi
diab_diagnosis = ''

# Membuat tombol untuk prediksi
if st.button('Test Prediksi Diabetes'):
    try:
        # Pastikan input dikonversi ke tipe data yang sesuai
        input_data = np.array([[int(Age), int(Blood_Glucose_Level), int(Diastolic_Blood_Pressure),
                                int(Systolic_Blood_Pressure), int(Heart_Rate), float(Body_Temperature),
                                int(SPO2), int(Sweating), int(Shivering)]])

        # Terapkan scaler hanya pada fitur yang sesuai
        features_to_scale = input_data[:, :7]
        scaled_features = scaler.transform(features_to_scale)

        # Gabungkan fitur yang sudah di-scaling dengan fitur yang tidak di-scaling
        combined_input_data = np.hstack((scaled_features, input_data[:, 7:]))

        # Lakukan prediksi
        diab_prediction = diabetes_model.predict(combined_input_data)

        # Pastikan hasil prediksi diubah menjadi nilai tunggal sebelum dibandingkan
        if (diab_prediction[0] == [1, 0]).all():
            diab_diagnosis = 'Pasien Terkena Diabetes'
        else:
            diab_diagnosis = 'Pasien Tidak Terkena Diabetes'

        st.success(diab_diagnosis)
    except ValueError as e:
        st.error(f'Error dalam konversi input: {e}')

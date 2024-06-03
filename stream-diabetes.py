import pickle
import streamlit as st

#membaca model
diabetes_model=pickle.load(open('C:/Users/ACER/Downloads/Big Project SSD/diabetes_model.sav','rb'))

#judul web
st.title('Prediksi Pasien Terkena Diabetes')

Age = st.text_input('Input Usia Pasien (Tahun)')
Blood_Glucose_Level = st.text_input('Input Kadar Gula Darah Pasien (mg/dl)')
Diastolic_Blood_Pressure = st.text_input('Input Tekanan Darah Diastolik Pasien (mmHg)')
Systolic_Blood_Pressure = st.text_input('Input Tekanan Darah Sistolik Pasien (mmHg)')
Heart_Rate = st.text_input('Input Detak Jantung Pasien (bpm)')
Body_Temperature = st.text_input('Input Suhu Tubuh Pasien (Fahrenheit)')
SPO2 = st.text_input('Input SP02 Pasien (%)')
Sweating = st.text_input('Apakah Pasien Mengalami Kondisi Tubuh Berkeringat? (0=Tidak, 1=Ya)')
Shivering = st.text_input('Apakah Pasien Mengalami Kondisi Tubuh Gemetaran? (0=Tidak, 1=Ya)')

#code untuk prediksi
diab_diagnosis = ''

#membuat tombol untuk prediksi
if st.button('Test Prediksi Diabetes'):
  diab_diagnosis = diabetes_model.predict([[Age, Blood_Glucose_Level(BGL), Diastolic_Blood_Pressure, Systolic_Blood_Pressure, Heart_Rate, Body_Temperature, SPO2, Sweating_(Y/N), Shivering_(Y/N)]])

  if(diab_prediction[0]==1):
    diab_diagnosis='Pasien Terkena Diabetes'
  else:
    diab_diagnosis='Pasien Tidak Terkena Diabetes'

  st.success(diab_diagnosis)

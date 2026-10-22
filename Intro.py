import streamlit as st
from PIL import Image
st.title("Portafolio II Jeremy Villa Patiño.")

with st.sidebar:
  st.subheader("Aplicaciones Streamlit y GitHub.")
  parrafo = (
    "Streamlit es una pagina que permite construir, compartir y visualizar "
    "aplicaciones creados con script, lo que facilita la creación de las mismas "
    "y permite el uso de diferentes contenidos que se observaron en el primer portafolio, "
    "pero aquí veremos compatibilidad con otros medios y sistemas. "
  )
  st.write(parrafo)

st.subheader("En esta aplicación se encuentran ordenados varios ejercicios de clase.")
col1, col2, col3 = st.columns(3)

with col1:
 
 st.subheader("Dígitos escritos")
 image = Image.open('OIG5.jpg')
 st.image(image, width=190)
 st.write("Aplicación de detección de Dígitos Escritos a mano.") 
 url = "https://mnistjv-cacvnsxcjgusijvux7nr6v.streamlit.app/"
 st.write(f"[Enlace]({url})")

 st.subheader("Receptor MQTT")
 image = Image.open('txt_to_audio.png')
 st.image(image, width=200)
 st.write("Conexión de Streamlit a datos ") 
 url = "https://recepmqttj-gn2cougliwe4cjmyg4kp5g.streamlit.app//"
 st.write(f"[Enlace]({url})")

with col2: 
 st.subheader("Tablero de dibujo")
 image = Image.open('data_analisis.png')
 st.image(image, width=200)
 st.write("Tablero personalizable para realizar dibujos y trazos.") 
 url = "https://recondibujo-pz8epec3ekpjbva7knvwae.streamlit.app/"
 st.write(f"[Enlace]({url})")

 st.subheader("Sensor TQTT")
 image = Image.open('OIG4.jpg')
 st.image(image, width=190)
 st.write("Transmite valores de streamlit a Wokwi TQTT.") 
 url = "https://sendcmqttjv-mgu8xsydqkuxgosedmzb5g.streamlit.app/"
 st.write(f"[Enlace]({url})")


with col3: 
 st.subheader("Modelos de visión")
 image = Image.open('OIG3.jpg')
 st.image(image, width=190)
 st.write("Parrafo descriptivo de dibujos en tablero.") 
 url = "https://drawrecojv-edznqimfwpx3ngauvknclq.streamlit.app/"
 st.write(f"[Enlace]({url})")

 st.subheader("Streamlit voz")
 image = Image.open('audio_to_txt.png')
 st.image(image, width=200)
 st.write("Trasmite tu voz desde esta app a través de un canal.") 
 url = "https://ctrlvoicejv-mdsp4ujkmtwmgwcunzq5e8.streamlit.app/"
 st.write(f"[Enlace]({url})")

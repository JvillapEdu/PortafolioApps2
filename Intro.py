import streamlit as st
from PIL import Image
st.title("Portafolio II Jeremy Villa Patiño.")

with st.sidebar:
  st.subheader("Aplicaciones Streamlit y GitHub.")
  parrafo = (
    "Streamlit es una pagina que permite construir, compartir y visualizar "
    "aplicaciones creados con script, lo que facilita la creación de las mismas "
    "y permite el uso de diferentes contenidos, como texto, botones, compatibilidad "
    "con la cámara del dispositivo, entre muchas otras."
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

 st.subheader("Caracteres en fotos")
 image = Image.open('OIG2.jpg')
 st.image(image, width=200)
 st.write("Una aplicación básica de reconocimiento de caracteres en fotos.") 
 url = "https://gusunhfubjleh3wzmffwwh.streamlit.app/"
 st.write(f"[Enlace]({url})")

 st.subheader("Entrenando Modelos")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("Aquí se encuentra una aplicación donde se usa Teachable Machine.") 
 url = "https://f88d6cyzd5vrbetcdnz4we.streamlit.app/"
 st.write(f"[Enlace]({url})")

with col2: 
 st.subheader("Tablero de dibujo")
 image = Image.open('data_analisis.png')
 st.image(image, width=200)
 st.write("Tablero personalizable para realizar dibujos y trazos.") 
 url = "https://recondibujo-pz8epec3ekpjbva7knvwae.streamlit.app/"
 st.write(f"[Enlace]({url})")

 st.subheader("TF-IDF")
 image = Image.open('txt_to_audio.png')
 st.image(image, width=190)
 st.write("La siguiente aplicación usa esta medida para evaluar relevancia entre 3 preguntas.") 
 url = "https://tfidfj-mv4mppkzxsnc2bko4ysjfn.streamlit.app/"
 st.write(f"[Enlace]({url})")

 st.subheader("Reconocimiento Óptico de Caracteres")
 image = Image.open('OIG3.jpg')
 st.image(image, width=200)
 st.write("El siguiente enlace reconoce caracteres de fotos y procesa a texto.") 
 url = "https://ocr-audioc-3ejf7gktxq2ebkyt5nzwoa.streamlit.app/"
 st.write(f"[Enlace]({url})")


with col3: 
 st.subheader("Modelos de visión")
 image = Image.open('OIG3.jpg')
 st.image(image, width=190)
 st.write("Parrafo descriptivo de dibujos en tablero.") 
 url = "https://drawrecojv-edznqimfwpx3ngauvknclq.streamlit.app/"
 st.write(f"[Enlace]({url})")

 st.subheader("Análisis de Sentimientos")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("El siguiente enlace asigna valores de subjetividad y polaridad.") 
 url = "https://sentimentab-4nxap93hsdrh57cihepe6q.streamlit.app//"
 st.write(f"[Enlace]({url})")
 
 st.subheader("WordCloud")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("Se presenta aquí una aplicación para crear Nube de ideas de textos.") 
 url = "https://wordcloudj-mahtq7qurccxdqrbtxdzxd.streamlit.app/"
 st.write(f"[Enlace]({url})")



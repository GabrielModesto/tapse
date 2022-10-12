import streamlit as st
import pyautogui

st.set_page_config(page_title="Relación TAPSE/sPAP")

# hide_default_format = """
#        <style>
#        #MainMenu {visibility: hidden; }
#        footer {visibility: hidden;}
#        </style>
#        """
# st.markdown(hide_default_format, unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: blue;'>Relación TAPSE/sPSP</h2>", unsafe_allow_html=True)

from PIL import Image
import streamlit as st 

col1, col2, col3 = st.columns(3) 
with col1:st.write(' ') 
with col2:st.image("htp.png") 
with col3:st.write(' ')

st.warning('Valor pronóstico de la relación ecocardiográfica de excursión sistólica del plano anular tricuspídeo/presión sistólica de la arteria pulmonar (TAPSE/sPAP) para la evaluación del riesgo de HAP no invasiva.')


tapse= st.selectbox('TAPSE/sPAP >0.33 mm/mmHg',("Escoja valor", "Si", "No"), key = "1")
   
 
nyha = st.selectbox("NYHA I-II", ("Escoja valor","Si", "No"), key = "2")
    

bnp = st.selectbox("NTproBNP <300 ng/L o BNP <50 ng/L", ("Escoja valor","Si", "No"), key = "3")

if tapse=="Escoja valor" and nyha=="Escoja valor" and bnp=="Escoja valor":
    pass
elif tapse=="Si" and nyha=="Si" and bnp=="Si":
    st.info('TAPSE/sPAP >0,33 mm/mmHg, NYHA I-II y NTproBNP <300 ng/L o BNP <50 ng/L permiten identificar pacientes con HAP de bajo riesgo en el seguimiento')
else:
    st.info('Evalue variables cínicas, de laboratorio y ecocardiografícas para determinar si su paciente está en riesgo intermedio o alto')
    
primary_clr = st.get_option("theme.primaryColor")
txt_clr = st.get_option("theme.textColor")
    
      
col1, col2, col3 = st.columns(3) 
with col1:st.write(' ') 
if st.button('Reiniciar'):
     pyautogui.hotkey('f5') #Simulates F5 key press = page refresh
with col3:st.write(' ')
    
    
    


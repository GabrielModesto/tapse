import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(page_title="Relación TAPSE/sPAP",  page_icon=":")

# st.set_page_config(page_title="Relación TAPSE/sPAP",  page_icon=":", layout="wide" )

  hide_default_format = """
         <style>
          MainMenu {visibility: hidden; }
         footer {visibility: hidden;}
         </style>
         """
  st.markdown(hide_default_format, unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: blue;'>Relación TAPSE/sPSP</h2>", unsafe_allow_html=True)

from PIL import Image
import streamlit as st 

col1, col2, col3 = st.columns(3) 
with col1:st.write(' ') 
with col2:st.image("htp.png") 
with col3:st.write(' ')

def main():

 st.warning('Valor pronóstico de la relación ecocardiográfica de excursión sistólica del plano anular tricuspídeo/presión sistólica de la arteria pulmonar (TAPSE/sPAP) para la evaluación del riesgo de HAP no invasiva.')


 with st.form(key='myform',clear_on_submit=True):

          
    tapse= st.selectbox('TAPSE/sPAP >0.33 mm/mmHg',("Escoja valor", "Si", "No"), key = "1")
    
    nyha = st.selectbox("NYHA I-II", ("Escoja valor","Si", "No"), key = "2")
    
    bnp = st.selectbox("NTproBNP <300 ng/L o BNP <50 ng/L", ("Escoja valor","Si", "No"), key = "3")

    submit_button =st.form_submit_button("Evaluar")
    
    st.write("[Ampliar información](https://www.sciencedirect.com/science/article/abs/pii/S1053249822021143)")

    if submit_button:
   
      if tapse=="Escoja valor" and nyha=="Escoja valor" and bnp=="Escoja valor":
         pass
     
      elif tapse=="Si" and nyha=="Si" and bnp=="Si":
          st.write('TAPSE/sPAP >0,33 mm/mmHg, NYHA I-II y NTproBNP <300 ng/L o BNP <50 ng/L permiten identificar pacientes con HAP de bajo riesgo en el seguimiento')
    
      elif  tapse=="No" or nyha=="No" or bnp=="No":
          st.write('Evalue variables cínicas, de laboratorio y ecocardiografícas para determinar si su paciente está en riesgo intermedio o alto')
    
if __name__ == '__main__':
    # This code won't run if this file is imported.
    main()


components.html(
    """
<script>
const elements = window.parent.document.querySelectorAll('.stButton button')
elements[0].style.backgroundColor = 'lightblue'
</script>
""",
    height=0,
    width=0,
)
    
      
col1, col2 = st.columns(2) 
with col1:st.write(' ') 

# if st.button("Reset"):
  
  

    
    
    


    
    
    
    


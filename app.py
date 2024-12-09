import streamlit as st
import base64
from mistralai import Mistral


MISTRAL_API_KEY=st.secrets["MISTRAL_API_KEY"]
model = "pixtral-large-latest"



st.set_page_config(
    page_title="Prueba de susos de Mixtral",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="auto"
)

st.header(f"Aplicación para evaluar las capacidades de {model}")

columna_izquierda, columna_derecha = st.columns([2,8])

with columna_izquierda:
    imagen = st.file_uploader("Elige una imagen", type=["jpg","png"])

    # ''' 
    # Cuando se usa st.file_uploader en Streamlit, el archivo subido se recibe como un objeto de tipo UploadedFile, que es una clase propia de Streamlit. Los datos de la imagen están en binario (bytes). Este objeto tiene estos metodos utiles
   
    #     getvalue(): Devuelve el contenido completo del archivo como una secuencia de bytes.
    #     read(): Similar a getvalue(), pero se usa más para manejar streams.
    #     name: Devuelve el nombre del archivo original.
    #     type: Devuelve el tipo MIME del archivo (como image/jpeg o image/png).
    # '''

    if imagen:
        imagen_base64 = base64.b64encode(imagen.getvalue()).decode("utf-8")

        with st.expander("Imagen cargada", expanded=True):
            st.image(imagen)

with columna_derecha:

    prompt = st.text_area("Que deseas hacer con la imagen ?")
    btnEjecutarAnalisis = st.button("Generar", type="primary")

    if btnEjecutarAnalisis:

        cliente = Mistral(api_key=MISTRAL_API_KEY)

        mensajes = [
                        {
                            "role": "user",
                            "content": [

                                {
                                    "type": "text",
                                    "text": prompt
                                 },
                                 {
                                    "type": "image_url",
                                    "image_url": f"data:image/jpeg;base64,{imagen_base64}"
                                 },

                            ]
                        },

                    ]

        st.subheader("Resultado")
    
        chat_response = cliente.chat.complete(
            model= model,
            messages = mensajes
        )

        st.write(chat_response.choices[0].message.content)


# ''' 
# ### **¿Por qué convertir binarios a Base64 si ambos son `bytes`?**

# Aunque ambos son `bytes`, el contenido es muy diferente:

# 1. **Bytes originales (`imagen.getvalue()`):**
    
#     - Son los datos puros del archivo. Pueden contener cualquier byte (valores de 0 a 255).
#     - No son seguros para ser enviados o almacenados en formatos de texto (como JSON o HTML), ya que pueden contener caracteres no imprimibles o incompatibles.
# 2. **Bytes codificados en Base64 (`base64.b64encode()`):**
    
#     - Estos representan los datos originales en un formato seguro de texto que usa solo caracteres imprimibles como letras, números, y símbolos como `+`, `/`, `=`. Esto hace que sean ideales para:
#         - Enviar datos en protocolos de texto (como JSON, XML, o HTTP).
#         - Incrustar imágenes en HTML (`<img src="data:image/png;base64,...">`).
#         - Almacenar datos en bases de datos como texto.

# ---

# ### **Flujo Completo**

# Cuando haces esto:

# python

# Copiar código

# `imagen_base64 = base64.b64encode(imagen.getvalue()).decode("utf-8")`

# estás haciendo lo siguiente:

# 1. **`imagen.getvalue()`**: Obtiene los datos binarios originales del archivo cargado.
    
# 2. **`base64.b64encode(imagen.getvalue())`**: Convierte los datos binarios originales en una representación Base64, que es segura para texto. El resultado sigue siendo de tipo `bytes`.
    
# 3. **`.decode("utf-8")`**: Convierte los `bytes` Base64 en una cadena de texto (`str`) para que sea fácil de usar en formatos como JSON, HTML, etc.
    

# ---

# ### **¿Por qué no salteamos `b64encode`?**

# Si simplemente intentas usar los bytes originales (`imagen.getvalue()`), estos pueden ser ilegibles o incompatibles en ciertos contextos porque no están en un formato textual seguro. Por eso usamos Base64, que es específicamente diseñado para este propósito.

# ### **Conclusión**

# Aunque `imagen.getvalue()` ya devuelve bytes, esos bytes no están en Base64. `base64.b64encode()` es necesario para transformarlos en una representación textual segura (aunque sigue siendo un objeto `bytes` por diseño). Luego, `.decode("utf-8")` lo convierte en texto para un uso más práctico.
# '''
# Procesador de Imágenes con Prompts usando Mistral AI

**Descripción:**

Esta aplicación de Streamlit permite a los usuarios cargar una imagen y proporcionar un prompt de texto. La aplicación envía la imagen y el prompt al modelo de IA de Mistral, que genera una respuesta basada en la entrada proporcionada.

**Características:**

*   **Carga de Imágenes:** Soporta formatos JPEG y PNG.
*   **Prompt de Texto:** Prompt personalizable para especificar la tarea deseada.
*   **Integración con Mistral AI:** Utiliza el modelo de IA de Mistral para el procesamiento de imágenes y la generación de texto.
*   **Codificación Base64:** Convierte las imágenes cargadas a formato Base64 para una transmisión eficiente.

**Cómo usar:**

1.  **Clonar el Repositorio:**
    ```bash
    git clone [se quitó una URL no válida]
    ```
2.  **Instalar Requisitos:**
    ```bash
    pip install -r requirements.txt
    ```
    Asegúrate de tener un archivo `requirements.txt` en tu repositorio con las dependencias necesarias (streamlit, mistralai, etc.). Puedes generarlo con `pip freeze > requirements.txt`.
3.  **Configurar Variables de Entorno:**
    *   Crea un archivo `.env` en el directorio del proyecto y añade la siguiente línea, reemplazando `TU_API_KEY` con tu clave API de Mistral AI:
        ```
        MISTRAL_API_KEY=TU_API_KEY
        ```
        Recuerda que no debes commitear este archivo `.env`. Añádelo a `.gitignore`.
4.  **Ejecutar la Aplicación:**
    ```bash
    streamlit run app.py
    ```
5.  **Interactuar con la Aplicación:**
    *   Carga una imagen.
    *   Introduce un prompt de texto.
    *   Haz clic en el botón "Generar" para ver la respuesta del modelo.

**Detalles Técnicos:**

*   **Librerías:** Streamlit, Mistral AI, base64, dotenv (para cargar las variables de entorno)
*   **Funcionalidad:**
    *   Carga de imágenes y conversión a Base64.
    *   Entrada de prompt de texto.
    *   Integración con la API de Mistral AI.
    *   Visualización de las respuestas generadas por el modelo.
*   **Despliegue:** Streamlit facilita el despliegue de esta aplicación en la nube o localmente.

**Personalización:**

*   **Modelo:** Experimenta con diferentes modelos de Mistral AI para obtener diferentes resultados.
*   **Ingeniería de Prompts:** Refina el prompt para obtener respuestas más específicas o creativas.
*   **Post-procesamiento:** Implementa pasos de procesamiento adicionales para mejorar la salida, como filtrado, formateo o visualización.

**Casos de Uso Potenciales:**

*   **Subtitulado de Imágenes:** Generar subtítulos descriptivos para imágenes.
*   **Preguntas y Respuestas sobre Imágenes:** Responder preguntas sobre el contenido de una imagen.
*   **Transferencia de Estilo de Imagen:** Transformar una imagen a un estilo diferente.
*   **Generación de Imágenes:** Crear nuevas imágenes basadas en descripciones de texto.

**Notas Adicionales:**

*   El código incluye comentarios que explican el propósito de las diferentes secciones del código.
*   La codificación Base64 es necesaria para representar los datos de la imagen como una cadena para la transmisión a la API de Mistral AI.
*   Se utiliza `st.secrets["MISTRAL_API_KEY"]` para almacenar de forma segura la clave API en la gestión de secretos de Streamlit (lo ideal es usar un archivo .env y la librería python-dotenv).


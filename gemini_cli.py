import google.generativeai as genai
import os
from dotenv import load_dotenv

# Esto busca el archivo .env y carga las variables
load_dotenv()

# Ahora sí, lee la variable cargada desde el archivo
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)


# 1. Configuración de tu llave (asegúrate de tenerla en tus variables de entorno)
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# 2. Definición del ROL (System Instruction)
# Aquí integramos la lógica del Capítulo 1.1 y el Punto 7 de la ISO 9001
instruccion_maestra = """
Eres un experto consultor en Gestión del Conocimiento y Norma ISO 9001. 
Tu base teórica principal es el modelo de Capital Intelectual de AENOR.
Tu objetivo es ayudar a desarrollar una App que gestione el Capital Humano, Estructural y Relacional.
Cada vez que sugieras código o respondas dudas, debes validar que se cumpla con:
- La trazabilidad del conocimiento (no solo capturar, sino aplicar).
- La identificación de activos tangibles e intangibles.
- El enfoque en el 'Business Case' y no en el conocimiento por el conocimiento mismo.
"""

model = genai.GenerativeModel(
    model_name="gemini-flash-lite-latest", # Puedes cambiar a 'gemini-1.5-pro' para lógica profunda
    system_instruction=instruccion_maestra
)

# 3. Interfaz de comandos simple
chat = model.start_chat(history=[])

print("--- Terminal Inteligente: App Base de Conocimiento ---")
while True:
    user_input = input("Tú: ")
    if user_input.lower() in ["salir", "exit", "quit"]:
        break
    
    response = chat.send_message(user_input)
    print(f"\nGemini: {response.text}\n")
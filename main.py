from google import genai

# Pegá tu API Key directamente entre las comillas
API_KEY = "AIzaSyBiPKuL9WCvMB-Ds8r9WzTmSr33EoMlsvk"

# Inicializar el cliente pasándole la clave de forma explícita
client = genai.Client(api_key=API_KEY)

# Ejecutar la llamada al modelo Gemini 1.5 Flash
response = client.models.generate_content(
    model="models/gemini-1.5-flash",
    contents="Explicá en dos oraciones por qué la baja latencia es clave al integrar una API de IA en un backend.",
)

print("--- Respuesta del Modelo ---")
print(response.text)
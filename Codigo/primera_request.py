# ============================================
# Mi primera request a Claude API
# SaaS de Facturas - Cali, Colombia
# ============================================

from anthropic import Anthropic
from dotenv import load_dotenv
import os

# Cargar API key desde .env
load_dotenv()

# Crear cliente
client = Anthropic()
modelo = "claude-haiku-4-5-20251001"

# ============================================
# Función principal
# ============================================
def preguntar_sobre_factura(pregunta):
    respuesta = client.messages.create(
        model=modelo,
        max_tokens=1000,
        messages=[
            {
                "role": "user",
                "content": pregunta
            }
        ]
    )
    return respuesta.content[0].text

# ============================================
# Prueba
# ============================================
resultado = preguntar_sobre_factura(
    "¿Cuáles son los campos obligatorios en una factura electrónica DIAN de Colombia?"
)

print("=== RESPUESTA DE CLAUDE ===")
print(resultado)
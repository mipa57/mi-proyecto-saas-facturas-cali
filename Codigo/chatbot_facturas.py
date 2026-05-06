# ============================================
# Chatbot Multi-turno para SaaS de Facturas
# Cali, Colombia - Miguel Bejarano
# ============================================

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic()
modelo = "claude-haiku-4-5-20251001"

# ============================================
# Funciones helper
# ============================================

def add_user_message(messages, texto):
    messages.append({
        "role": "user",
        "content": texto
    })
    return messages

def add_assistant_message(messages, texto):
    messages.append({
        "role": "assistant",
        "content": texto
    })
    return messages

def chat(messages):
    respuesta = client.messages.create(
        model=modelo,
        max_tokens=1000,
        messages=messages
    )
    return respuesta.content[0].text

# ============================================
# Chatbot interactivo para el cliente PyME
# ============================================

def iniciar_chatbot():
    print("=" * 50)
    print("   Bienvenido al Asistente de Facturas")
    print("   SaaS Facturas Cali - Soporte 24/7")
    print("=" * 50)
    print("Escribe 'salir' para terminar\n")

    # Historial de conversación
    messages = []

    # Primera pregunta para conocer al cliente
    print("Asistente: ¡Hola! Soy tu asistente de")
    print("facturación electrónica. ¿Cuál es el")
    print("nombre de tu negocio y a qué se dedica?\n")

    while True:
        # Recibir mensaje del usuario
        entrada = input("Tú: ").strip()

        if entrada.lower() == "salir":
            print("\nAsistente: ¡Hasta luego! Recuerda")
            print("que estamos disponibles 24/7. 😊")
            break

        if not entrada:
            continue

        # Agregar mensaje del usuario al historial
        add_user_message(messages, entrada)

        # Obtener respuesta de Claude
        print("\nAsistente: ", end="")
        respuesta = chat(messages)
        print(respuesta)
        print()

        # Guardar respuesta en el historial
        add_assistant_message(messages, respuesta)

# ============================================
# Ejemplo simulado (sin input del usuario)
# ============================================

def ejemplo_simulado():
    print("=" * 50)
    print("   EJEMPLO: Conversación con PyME")
    print("=" * 50)

    messages = []
    conversacion = [
        "Hola, tengo un restaurante en el centro de Cali llamado El Buen Sabor",
        "Necesito saber cómo emitir facturas electrónicas para mis clientes",
        "¿Qué pasa si mi cliente no quiere factura?",
        "¿Cuánto me puede multar la DIAN si no facturo?"
    ]

    for pregunta in conversacion:
        print(f"\nCliente: {pregunta}")
        add_user_message(messages, pregunta)

        respuesta = chat(messages)
        print(f"Asistente: {respuesta}")
        add_assistant_message(messages, respuesta)
        print("-" * 40)

# ============================================
# EJECUTAR
# ============================================

if __name__ == "__main__":
    # Descomenta la que quieras usar:

    # OPCIÓN 1: Chatbot interactivo real
    # iniciar_chatbot()

    # OPCIÓN 2: Ejemplo simulado
    ejemplo_simulado()
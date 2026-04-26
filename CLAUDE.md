# SaaS de Facturas - Cali, Colombia

## Descripción del Proyecto
Automatización de procesamiento de facturas electrónicas 
para PyMEs colombianas en Cali, Valle del Cauca.

## Desarrollador
- Nombre: Miguel Gustavo Bejarano Patiño
- Nivel: Principiante en Python
- Sistema: Windows 8.1 (próximamente Windows 10)
- GitHub: github.com/mipa57/mi-proyecto-saas-facturas-cali

## Stack Tecnológico
- Lenguaje: Python 3.10
- Lectura PDFs: pdfplumber
- IA: Claude API (Anthropic)
- Base de datos: MySQL
- API: FastAPI
- Interfaz: HTML + Bootstrap

## Comandos del Proyecto
- Instalar dependencias: `pip install -r requirements.txt`
- Ejecutar app: `python main.py`
- Pruebas: `python -m pytest tests/`

## Estructura de Carpetas
```
MiSaaS/
├── Artefactos/     → Interfaces web HTML
├── Notas/          → Apuntes del curso
├── Recursos/       → Investigación de mercado
├── Codigo/         → Scripts Python
└── CLAUDE.md       → Este archivo
```

## Convenciones de Código
- Idioma: Todo en español (variables, funciones, comentarios)
- Indentación: 4 espacios
- Funciones: snake_case en español (extraer_nit, leer_factura)
- Siempre validar NIT colombiano (formato: XXXXXXXXX-X)
- Manejo de errores con try/except en todas las funciones

## Mercado Objetivo
- PyMEs en Cali, Colombia
- Sectores: comercio (41.759 emp.) y gastronomía (10.028 emp.)
- Precio objetivo: $35.000 - $180.000 COP/mes
- Competencia: Alegra ($17.900+), Siigo ($145.993+)
- Diferenciador: soporte presencial + IA + precio bajo

## Lo que ya está implementado
- ✅ Portal web de subida de facturas (invoice-upload.html)
- ✅ Investigación de mercado Cali 2026
- ✅ Repositorio GitHub configurado

## Próximas Funciones a Implementar
- ⏳ Módulo lectura PDF con pdfplumber
- ⏳ Extracción de NIT y total con Claude API
- ⏳ Guardado en MySQL
- ⏳ Validación formato DIAN
- ⏳ Panel de administración web

## Reglas Importantes
- NUNCA usar tecnologías muy avanzadas sin explicación
- SIEMPRE explicar el código paso a paso
- SIEMPRE sugerir alternativas gratuitas antes que de pago
- Validar siempre el formato NIT colombiano
- Compatible con Windows 8.1 por ahora

## Documentación de Referencia
- Investigación de mercado: @Recursos/investigacion-mercado-cali-2026.txt
- Notas del curso: @Notas/claude-101.txt

## Correcciones Frecuentes
- Usar pip install --break-system-packages en Windows 8.1
- No usar Docker ni AWS (muy avanzado para el nivel actual)
- Preferir SQLite antes que PostgreSQL para empezar

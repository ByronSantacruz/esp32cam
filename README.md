# ESP32-CAM con YOLO y Flask

Esta aplicación permite detectar objetos en tiempo real utilizando una cámara ESP32-CAM y el modelo YOLO, con una interfaz web desarrollada en Flask.

## Características

- Detección de objetos en tiempo real con YOLO
- Interfaz web para visualizar la cámara y los resultados
- Posibilidad de cambiar la dirección IP de la cámara ESP32-CAM
- Detección automática o manual
- Notificaciones por voz de los objetos detectados

## Requisitos

- Python 3.8 o superior
- ESP32-CAM configurada para transmitir imágenes
- Dependencias listadas en `requirements.txt`

## Instalación local

1. Clona este repositorio
2. Instala las dependencias: `pip install -r requirements.txt`
3. Ejecuta la aplicación: `python app.py`
4. Abre un navegador y visita: `http://localhost:5000`

## Despliegue en Render

1. Crea una cuenta en [Render](https://render.com/)
2. Conecta tu repositorio de GitHub
3. Crea un nuevo servicio web
4. Selecciona el repositorio
5. Configura el servicio:
   - Tipo: Web Service
   - Entorno: Python
   - Comando de construcción: `pip install -r requirements.txt`
   - Comando de inicio: `gunicorn app:app`

## Uso

1. Asegúrate de que tu ESP32-CAM esté encendida y transmitiendo
2. Ingresa la dirección IP correcta de tu ESP32-CAM en la interfaz
3. Haz clic en "Detectar ahora" para una detección única o "Iniciar detección automática" para detección continua

## Notas

- La aplicación está configurada para usar el modelo YOLOv8n por defecto
- Asegúrate de que la ESP32-CAM esté configurada para servir imágenes en la ruta `/cam-lo.jpg`
- Si despliegas en Render, necesitarás asegurarte de que la ESP32-CAM sea accesible desde internet
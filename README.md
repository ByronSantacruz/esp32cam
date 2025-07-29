# ESP32-CAM con YOLO y Flask

Esta aplicación permite detectar objetos en tiempo real utilizando una cámara ESP32-CAM y el modelo YOLO, con una interfaz web desarrollada en Flask.

## Características

- Detección de objetos en tiempo real con YOLO
- Interfaz web para visualizar la cámara y los resultados
- Posibilidad de cambiar la dirección IP de la cámara ESP32-CAM
- Detección automática o manual
- Notificaciones por voz de los objetos detectados

## Requisitos

- Python 3.11.6 o superior (recomendado para compatibilidad con las dependencias)
- ESP32-CAM configurada para transmitir imágenes
- Dependencias listadas en `requirements.txt`
- Suficiente memoria RAM para cargar el modelo YOLO (mínimo 512MB recomendado)

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
   - Comando de inicio: `gunicorn --config gunicorn_config.py app:app`

### Solución de problemas comunes

#### Error 502 Bad Gateway

Si encuentras un error 502 Bad Gateway, puede deberse a:

1. **Tiempo de carga del modelo YOLO**: El modelo puede tardar en cargarse, especialmente en el plan gratuito de Render. La configuración de Gunicorn se ha ajustado para permitir tiempos de carga más largos.

2. **Problemas de memoria**: Los modelos YOLO requieren bastante memoria. Si el servicio se queda sin memoria, puede generar un error 502. Considera actualizar a un plan con más recursos si esto ocurre frecuentemente.

3. **Compatibilidad de versiones**: Asegúrate de que las versiones de las dependencias sean compatibles con la versión de Python utilizada.

#### Verificar logs

Para diagnosticar problemas, revisa los logs de Render:

1. Ve al panel de control de Render
2. Selecciona tu servicio
3. Haz clic en "Logs" para ver los mensajes de error detallados

## Uso

1. Asegúrate de que tu ESP32-CAM esté encendida y transmitiendo
2. Ingresa la dirección IP correcta de tu ESP32-CAM en la interfaz
3. Haz clic en "Detectar ahora" para una detección única o "Iniciar detección automática" para detección continua

## Notas

- La aplicación está configurada para usar el modelo YOLOv8n por defecto
- Asegúrate de que la ESP32-CAM esté configurada para servir imágenes en la ruta `/cam-lo.jpg`
- Si despliegas en Render, necesitarás asegurarte de que la ESP32-CAM sea accesible desde internet
- Se ha incluido un archivo `gunicorn_config.py` con configuraciones optimizadas para el despliegue:
  - Timeout aumentado a 120 segundos para permitir la carga del modelo YOLO
  - 2 workers con 4 hilos cada uno para balancear rendimiento y uso de memoria
  - Configuración para evitar problemas de memoria en el plan gratuito de Render
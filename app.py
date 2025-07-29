from flask import Flask, render_template, send_from_directory, request, jsonify
import cv2
import requests
import numpy as np
from ultralytics import YOLO
import os

app = Flask(__name__)
ESP32_URL = "http://10.42.3.143/cam-lo.jpg"
model = YOLO("yolov8n.pt")  # O el modelo que estés usando

# Ruta para página principal
@app.route("/")
def index():
    # Extraer la IP actual para mostrarla en la interfaz
    current_ip = ESP32_URL.split("http://")[1].split("/")[0]
    return render_template("index.html", current_ip=current_ip)

# Ruta para imagen
@app.route("/imagen")
def get_image():
    return send_from_directory("static", "ultima.jpg", mimetype="image/jpeg")

# Ruta para texto de clase
@app.route("/clase")
def get_class():
    try:
        with open("static/clase.txt", "r", encoding="utf-8") as f:
            return f.read()
    except:
        return "Sin detección"

# Ruta para actualizar la IP del ESP32
@app.route("/actualizar_ip", methods=["POST"])
def actualizar_ip():
    global ESP32_URL
    nueva_ip = request.json.get("ip")
    if nueva_ip:
        ESP32_URL = f"http://{nueva_ip}/cam-lo.jpg"
        return jsonify({"success": True, "message": f"IP actualizada a {nueva_ip}"})
    return jsonify({"success": False, "message": "IP no válida"})

# Ruta para procesar imagen
@app.route("/detectar")
def detectar():
    try:
        # Reducir el timeout para respuestas más rápidas
        response = requests.get(ESP32_URL, timeout=0.5)
        img_array = np.frombuffer(response.content, np.uint8)
        frame = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        if frame is None:
            raise ValueError("No se pudo decodificar la imagen.")

        # Configurar el modelo para ser más rápido (menor confianza)
        results = model(frame, conf=0.25)[0]
        annotated = results.plot()
        
        # Optimizar la calidad de la imagen para transmisión más rápida
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 85]
        cv2.imwrite("static/ultima.jpg", annotated, encode_param)

        with open("static/clase.txt", "w", encoding="utf-8") as f:
            if results.names and results.boxes:
                clases = [results.names[int(cls)] for cls in results.boxes.cls]
                f.write(", ".join(clases))
            else:
                f.write("Sin detección")

        return "Procesado correctamente"
    except Exception as e:
        print("Error:", e)
        return "Error al detectar"

if __name__ == "__main__":
    if not os.path.exists("static"):
        os.makedirs("static")
    if not os.path.exists("static/ultima.jpg"):
        # Imagen temporal vacía (negra)
        negro = np.zeros((480, 640, 1), dtype=np.uint8)
        cv2.imwrite("static/ultima.jpg", negro)
    if not os.path.exists("static/clase.txt"):
        with open("static/clase.txt", "w", encoding="utf-8") as f:
            f.write("Sin detección")

    app.run(host="0.0.0.0", port=5000, debug=True)

# Configuración de Gunicorn para aplicación Flask con YOLO

# Tiempo de espera para los workers (en segundos)
# Aumentado significativamente para permitir que el modelo YOLO cargue y procese imágenes
# Especialmente importante en entornos con recursos limitados como el plan gratuito de Render
timeout = 300

# Número de workers - ajustar según los recursos disponibles
# Para aplicaciones con modelos ML, menos workers pero con más memoria cada uno
workers = 2

# Hilos por worker - permite manejar múltiples solicitudes sin crear nuevos procesos
threads = 4

# Tiempo de espera para el cierre graceful de workers
graceful_timeout = 300

# Mantener conexiones vivas
keepalive = 65

# Configuración de worker para evitar problemas de memoria
worker_class = 'sync'
worker_connections = 1000

# Configuración de logging
loglevel = 'info'

# Configuración para evitar problemas de memoria
max_requests = 1000
max_requests_jitter = 50

# Precarga de la aplicación para evitar que cada worker cargue el modelo por separado
preload_app = True

# Configuración de memoria para PyTorch
import os
os.environ['PYTORCH_CUDA_ALLOC_CONF'] = 'max_split_size_mb:128'

# Configuración para reducir el uso de memoria
import torch
torch.set_num_threads(1)  # Limitar el número de hilos de PyTorch
# Configuración de Gunicorn para aplicación Flask con YOLO

# Tiempo de espera para los workers (en segundos)
# Aumentado para permitir que el modelo YOLO cargue y procese imágenes
timeout = 120

# Número de workers - ajustar según los recursos disponibles
# Para aplicaciones con modelos ML, menos workers pero con más memoria cada uno
workers = 2

# Hilos por worker - permite manejar múltiples solicitudes sin crear nuevos procesos
threads = 4

# Tiempo de espera para el cierre graceful de workers
graceful_timeout = 120

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
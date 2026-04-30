import subprocess
import os
import time
import http.server
import socketserver
import threading
import sys

def run_reflex():
    print("🚀 Arrancando el motor de Reflex...")
    # Ejecutamos el backend en el puerto 8000 (interno)
    subprocess.run(["reflex", "run", "--env", "prod", "--backend-only", "--backend-port", "8001"])

def serve_frontend():
    port = int(os.environ.get("PORT", 8080))
    print(f"🌐 Sirviendo la web en el puerto {port}...")
    
    # Esperamos a que Reflex exporte los archivos si no están
    static_dir = os.path.join(os.getcwd(), ".web", "_static")
    while not os.path.exists(static_dir):
        print("⏳ Esperando a que Reflex termine de preparar la web...")
        time.sleep(5)
    
    os.chdir(static_dir)
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        httpd.serve_forever()

if __name__ == "__main__":
    # Primero inicializamos y exportamos para tener los archivos listos
    print("🛠 Preparando archivos de producción...")
    subprocess.run(["reflex", "init"])
    subprocess.run(["reflex", "export", "--frontend-only", "--no-zip"])
    
    # Lanzamos el backend en un hilo separado
    threading.Thread(target=run_reflex, daemon=True).start()
    
    # Lanzamos el servidor de archivos en el hilo principal
    serve_frontend()

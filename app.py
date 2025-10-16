from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

PORT = 8000

# Устанавливаем текущую папку как корневую
web_dir = os.path.dirname(__file__)
os.chdir(web_dir)

# Создаём сервер
handler = SimpleHTTPRequestHandler
httpd = HTTPServer(("", PORT), handler)

print(f"🚀 Сервер запущен на http://localhost:{PORT}")
httpd.serve_forever()

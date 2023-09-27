import http.server
import socketserver
import cgi

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST'}
        )

        if 'submit' in form and form['submit'].value == 'Registrarse':
            first_name = form['first-name'].value
            last_name = form['last-name'].value
            user = form['user'].value
            email = form['email'].value
            password = form['new-password'].value 

            response_message = '¡Registro exitoso!'
        else:
            response_message = 'Acción de formulario desconocida'

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(response_message.encode('utf-8'))

# Configura el puerto 8000
with socketserver.TCPServer(("", 8000), MyHandler) as httpd:
    print("Servidor en el puerto 8000")
    httpd.serve_forever()

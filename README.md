# ProyectoFinalPython2

## Instalación
**Esta sección muestra como instalar el paquete.**

Para instalar el paquete es necesario crear un entorno virtual:
```terminal
python -m venv venv
env\Scripts\activate
pip install -r python -m venv venv
```

Para utilizarlo solo debe importar las funciones al inicio de su módulo.

```python
from src.proyectoFinalJoseph.images import showImageFromURL,downloadImageFromUrl,grayScaleImage
from src.proyectoFinalJoseph.mymail import sendQuickMail,sendAttachEmail
```

## Usos
### Paquete Images
El paquete Images posee 3 funciones:

**showImageFromURL:** Se encarga de mostrar una imagen desde una URL dada.
```python
from src.proyectoFinalJoseph.images import showImageFromURL

url_imagen = "https://images.pexels.com/photos/5372613/pexels-photo-5372613.jpeg"
showImageFromURL(ruta)
```
**downloadImageFromUrl:** Se encarga de descargar una imagen desde una URL dada y guardarla en la ruta indicada.
```python
from src.proyectoFinalJoseph.images import downloadImageFromUrl

url_imagen = "https://images.pexels.com/photos/5372613/pexels-photo-5372613.jpeg"
ruta = "/"
downloadImageFromUrl(url_imagen,ruta)
```
**grayScaleImage:** Se encarga de pasar una imagen especificada por medio de una ruta a una escala de grises.
```python
from src.proyectoFinalJoseph.images import grayScaleImage

ruta = "imageToGray.jpeg"
grayScaleImage(ruta)
```

### Paquete Mymail
El paquete Mymail posee 2 funciones:

**sendQuickMail:** Por medio de un asunto, mensaje y destinatario especificado, envía un correo simple.
```python
from src.proyectoFinalJoseph.mymail import sendQuickMail

asunto = "El asunto del correo"
msg = "Este es el msg del correo"
dest = "account@mail.com"

sendQuickMail(asunto,msg,dest)
```
**sendAttachEmail:** Por medio de un asunto, mensaje, destinatario especificado y un una ruta de un adjunto, envía un correo.
```python
from src.proyectoFinalJoseph.mymail import sendAttachEmail

asunto = "El asunto del correo"
msg = "Este es el msg del correo"
dest = "account@mail.com"
attach = "test_attach.jpeg"

sendAttachEmail(asunto,msg,dest,attach)
```
## Referencias

Para ver el código fuenta, diríjase al repositorio: [GitHub](https://github.com/joseph-rb/proyecto_final)

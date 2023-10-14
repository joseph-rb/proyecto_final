from src.proyectoFinalJoseph.mymail import sendQuickMail,sendAttachEmail
from src.proyectoFinalJoseph.images import downloadImageFromUrl,showImageFromURL,grayScaleImage

def main():
    url = input("Iniciarndo prueba de images showImageFromURL, digitar URL: ")
    showImageFromURL(url)
    
    path=input("Iniciando prueba de images downloadImageFromUrl, digitar path: ")
    downloadImageFromUrl(url,path)
    
    archivo=input("Iniciando prueba de images grayScaleImage, digitar archivo: ")
    grayScaleImage(archivo)
    #***************************************************************************************
    #***************************************************************************************
    
    asunto = "El asunto del correo"
    msg = "Este es el msg del correo"
    dest = "jose.rodriguezblanco@ucr.ac.cr"
    
    sendQuickMail(asunto,msg,dest)
    
    archivo = input("Path del archivo a adjuntar: ")
    sendAttachEmail(asunto,msg,dest,archivo)
    
    pass
    
if __name__ == "__main__":
    main()
    
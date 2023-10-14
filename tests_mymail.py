import unittest

from src.proyectoFinalJoseph.mymail import sendQuickMail,sendAttachEmail


class TestImages(unittest.TestCase):
    
    def test_sendQuickMail(self):
        '''
        Se encarga de hacer la prueba unitaria de la función sendQuickMail del módulo src.mymail.
        '''
        
        asunto = "El asunto del correo sendQuickMail"
        msg = "Este es el msg del correo sendQuickMail"
        dest = "jose.rodriguezblanco@ucr.ac.cr"

        self.assertTrue(sendQuickMail(asunto,msg,dest))
    
    def test_sendAttachEmail(self):
        '''
        Se encarga de hacer la prueba unitaria de la función sendAttachEmail del módulo src.mymail.
        '''
        asunto = "El asunto del correo sendAttachEmail"
        msg = "Este es el msg del correo sendAttachEmail"
        dest = "jose.rodriguezblanco@ucr.ac.cr"
        path = "test_attach.jpeg"

        self.assertTrue(sendAttachEmail(asunto,msg,dest,path))

if __name__ == "__main__":
    unittest.main()
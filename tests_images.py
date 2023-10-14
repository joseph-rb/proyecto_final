import unittest
import os

from src.proyectoFinalJoseph.images import showImageFromURL,downloadImageFromUrl,grayScaleImage


class TestImages(unittest.TestCase):
    
    def test_showImageFromURL(self):
        '''
        Se encarga de hacer la prueba unitaria de la función showImageFromURL del módulo src.images
        '''
        
        url = "https://images.pexels.com/photos/5372613/pexels-photo-5372613.jpeg"        
        img = showImageFromURL(url)
                
        self.assertIsNotNone(img)
    
    def test_downloadImageFromUrl(self):
        '''
        Se encarga de hacer la prueba unitaria de la función downloadImageFromUrl del módulo src.images
        '''
        url = "https://images.pexels.com/photos/5372613/pexels-photo-5372613.jpeg"        
        img = downloadImageFromUrl(url,".")
        
        self.assertTrue(os.path.exists(img))
        
    def test_grayScaleImage(self):
        '''
        Se encarga de hacer la prueba unitaria de la función grayScaleImage del módulo src.images
        '''
        path = "imageToGray.jpeg"
        
        self.assertTrue(grayScaleImage(path))

if __name__ == "__main__":
    unittest.main()
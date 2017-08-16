import PIL
from PIL import Image
class GENERALFUNCTIONS:
    'redimenciona una imagen, en este caso particular 300px x 300px y lo guarda'
    @staticmethod
    def save_resize_image(_name,_base64):
        maxsize = (300,300)
        try:
            dir = 'app/images/'
            filename = dir + _name
            with open(filename, "wb") as fh:
                fh.write(_base64)
                with open(filename, "r+b") as fh:
                    with Image.open(fh) as image:
                        image.thumbnail(maxsize, PIL.Image.ANTIALIAS)
                        image.save(filename)
            data = {"success": True}
        except Exception as e:
            data = {"success": False, "message": str(e)}
            print (e)
        return data
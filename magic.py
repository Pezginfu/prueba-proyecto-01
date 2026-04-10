# Este archivo se crea intencionalmente para sobreescribir la librería 'python-magic'
# en Vercel. Vercel no tiene la librería C 'libmagic' requerida por python-magic, 
# lo que causa un Error 500 al hacer importaciones. Al tener este archivo, 
# evitamos que el proyecto colapse (ya que usamos Cloudinary para imagenes y no videos).

class Magic:
    def __init__(self, *args, **kwargs):
        pass
        
    def from_buffer(self, content, *args, **kwargs):
        return 'image/jpeg'

def from_buffer(content, mime=True, *args, **kwargs):
    return 'image/jpeg'

from PIL import ImageTk, Image

def LeeImagen(path, size):
    return ImageTk.PhotoImagen(Image.open(path).resize(size, Image.ANTIALIAS))
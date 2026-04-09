from PIL import Image
import imageio.v3 as iio
import numpy as np
import sys

input_path = r"C:\Users\elliot alderson\.gemini\antigravity\brain\ab56faab-f3b8-4ddf-b8d6-592c7ac18f52\local_store_checkout_test_1775523299917.webp"
output_path = r"c:\Users\elliot alderson\Desktop\Nueva carpeta (2)\demo_tienda.mp4"

try:
    print("Abriendo archivo WebP...")
    img = Image.open(input_path)
    frames = []
    
    num_frames = getattr(img, "n_frames", 1)
    print(f"Fotogramas detectados: {num_frames}")
    
    if num_frames == 1:
        print("Cuidado: Pillow solo detecta 1 frame!")
    
    for i in range(num_frames):
        img.seek(i)
        frame_rgb = img.convert("RGB")
        frames.append(np.array(frame_rgb))
        
    print(f"Extraídos {len(frames)} fotogramas reales.")
    
    print("Codificando a MP4 (esto tomará unos segundos)...")
    iio.imwrite(output_path, frames, fps=5, extension=".mp4")
    print("¡Transformado exitosamente!")
except Exception as e:
    print(f"Error fatal: {e}")
    sys.exit(1)

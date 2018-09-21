from PIL import Image
import numpy as np
#import ImageEnhance
#import ImageFilter
 
def scale_image(input_image_path,
                output_image_path,
                width=None,
                height=None
                ):
    original_image = Image.open(input_image_path)
    w, h = original_image.size
    print('The original image size is {wide} wide x {height} '
          'high'.format(wide=w, height=h))
 
    if width and height:
        max_size = (width, height)
    elif width:
        max_size = (width, h)
    elif height:
        max_size = (w, height)
    else:
        # No width or height specified
        raise RuntimeError('Width or height required!')
 
    original_image.thumbnail(max_size, Image.ANTIALIAS)
    original_image.save(output_image_path)
 
    scaled_image = Image.open(output_image_path)
    width, height = scaled_image.size
    print('The scaled image size is {wide} wide x {height} '
          'high'.format(wide=width, height=height))

    mono_image=scaled_image.convert('L')    
    mono_image.save(output_image_path)
    arr = np.asarray(mono_image)
    print(arr)

    arr2=arr/255
    print(arr2)
    	

if __name__ == '__main__':
    scale_image(input_image_path='4.jpg',
                output_image_path='4_scaled.jpg',
                width=10)
    input("End...")
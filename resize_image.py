from PIL import Image
import numpy as np

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
    
    return scaled_image

def conver_to_mono(input_image):
    
    #mono_image=input_image.convert('L')
    #output_image_path='mono_'+str(input_image)    
    #mono_image.save(output_image_path)
    return input_image.convert('L')

def get_image_matrix(input_image):

    arr = np.asarray(input_image)/255
    print(arr)
    	

if __name__ == '__main__':
    scaled_img=scale_image(input_image_path='4.jpg',
                output_image_path='4_scaled.jpg',
                width=10)
    mono_img = conver_to_mono(scaled_img)

    get_image_matrix(mono_img)

    input("End...")
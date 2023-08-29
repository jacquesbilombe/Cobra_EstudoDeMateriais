import sys

from Functions import *


def processing(ROI_NOT):

    global images_to_analyze
    images_to_analyze = list()

    # Execute all pre processing code
    _ , processed_img, image_names = read_images()

    if ROI_NOT in(['Y','y','N','n']):
        if ROI_NOT == 'Y' or ROI_NOT == 'y':
            images_to_analyze = processed_img
        elif ROI_NOT == 'N' or ROI_NOT == 'n':
            flag = True if input('\nSelecione D para Default or C para ROI Personalizado: ') == 'D' else False
            images_to_analyze = ROI(processed_img, flag)
    else:
        print('\nErro: Selecione a combinação certa!')
        sys.exit()
    
    # Get the result of the entire analyze
    material_teor(images_to_analyze, image_names)

if __name__ == '__main__':
    processing()

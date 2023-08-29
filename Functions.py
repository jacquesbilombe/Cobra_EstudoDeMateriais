import os
import cv2
import csv
import numpy as np


"""
In the future, it'll be more accurate to put all these functions in a class
structure for better performance of the entire code.
"""


# -------------------------------------------------- PRE PROCESSING ----------------------------------------------------
def display_image(image):
    cv2.imshow(image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def convert_to_grayscale(image):
  """
  Converts an image to grayscale.
  If the image has 3 channels then it means
  the image is RGB.
  """
  if len(image.shape) == 3:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  else:
    gray_image = image.copy()

  return gray_image

def segment_image_based_on_color(img):
  """Segments an image based on the color."""
  gray = convert_to_grayscale(img)

  thresh = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)[1]
  # the lowest value of the threshold has to remain under 10 (Recomendation)
  return thresh # Binary image

def read_images():
    # Directory containing the images
    image_directory = 'Images/'

    # Get a list of all files in the directory
    all_files = os.listdir(image_directory)

    # Filter out only image files (e.g., .jpg, .png, etc.)
    image_files = [file for file in all_files if file.lower().endswith((".jpg", ".jpeg", ".png","tif"))]

    # Initialize a list to store the images
    images = []
    image_names = []
    processed_img = []

    # Iterate through the image files
    for image_file in image_files:
        image_names.append(image_file)
        image_path = os.path.join(image_directory, image_file)
        img = cv2.imread(image_path)

        if img is not None:
            # Store the image in the 'images' list and Convert it to a Binary Image
            processed_img.append(segment_image_based_on_color(img))
            images.append(img)
        else:
            print(f"Failed to read image: {image_file}")

    return images, processed_img, image_names

# ------------------------------------------------------------ REGION OF INTEREST (ROI)---------------------------------------

def ROI(imgs, flag):

  global images_to_analyze
  images_to_analyze = list()

  def default_mode(target):
    # Extract the ROI from the image (Circle from the image center)

    # Get image dimensions
    height, width = target.shape

    # Center coordinates
    center_x = width // 2
    center_y = height // 2

    # Create a mask of the same size as the image
    mask = np.zeros_like(target)

    # Draw a white filled circle on the mask
    cv2.circle(mask, (center_x, center_y), radius, (255, 255, 255), thickness=-1)

    # Bitwise AND operation to extract the circular region
    result = cv2.bitwise_and(target, mask)

    return result

  def customize_mode(target):
    # The user defines the region of interest
    result = input('okay')
    return result

  if flag:
    # Radius of the circle
    radius = int(input('\nEntre com o valor de raio para extrair a região de interesse: '))  # You can adjust this radius as needed
    for img in imgs:
      images_to_analyze.append(default_mode(img))
    return images_to_analyze
  else:
    for img in imgs:
      images_to_analyze.append(customize_mode(img))
    return images_to_analyze

# ----------------------------------------------------------- MATERIAL CONCENTRATION ------------------------------------------------

def material_teor(images_to_analyze, image_names):

  # Create a CSV writer object
  csv_writer = csv.writer(open("carbon_content.csv", "w"))

  # Write the header row
  csv_writer.writerow(["Imagem", "Concentração do Material (%)", "Teor do Material"])


  for roi_image, img_name in zip(images_to_analyze, image_names):
    # Count the number of white pixels (representing carbon)
    white_pixels = np.sum(roi_image == 255)  # Assuming white is represented as intensity 255

    # Calculate the total number of pixels in the image
    total_pixels = roi_image.shape[0] * roi_image.shape[1]

    # Calculate the concentration (percentage of white pixels)
    concentration_area = np.round((white_pixels / total_pixels) * 100, 2)

    # Get the Carbon Content
    content = np.round(concentration_area * (0.77/100),4)

    # Write the data row to the CSV file
    csv_writer.writerow([img_name, concentration_area, content])

    '''
    print(f"A concentração do Carbono por Área é de: {concentration_area} %")
    print(f"Teor de carbono na imagem é {content}\n")
    '''

  new_file_name = input("Enter the new file name: ")

  #csv_writer.close()

  # Rename the CSV file
  os.rename("carbon_content.csv", new_file_name)
  print('\n > DONE')

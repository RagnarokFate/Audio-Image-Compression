import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import math
import cv2
import random

clown_image_path = "Assignment_2/Clown256B.bmp"
barbara_image_path = "Assignment_2/Barbara.bmp"

def read_bmp(filename):
    # Open the image file
    img = Image.open(filename)
    # Convert the image data to a numpy array
    img_data = np.array(img)
    return img_data

def getSymbleAndProb(vector):
    sorted_vector = sorted(vector.ravel())
    symble_table = [sorted_vector[0]]
    prob_by_symble = [1]
    index = 0
    for i in range(1, len(sorted_vector)):
        if sorted_vector[i-1] == sorted_vector[i]:
            prob_by_symble[index] += 1
        else:
            index += 1
            symble_table.append(sorted_vector[i])
            prob_by_symble.append(1)
    prob_by_symble = [p / len(vector) for p in prob_by_symble]
    return symble_table, prob_by_symble


def entropy_length(vector):
    _, prob = getSymbleAndProb(vector)
    entropy = 0
    for p in prob:
        entropy -= p * np.log2(p)
    entropy *= len(vector)
    return entropy


def plot_prediction_models(image_name, mode1_bitrates, mode1_psnr, mode2_bitrates, mode2_psnr):
    plt.figure(figsize=(8, 6))

    # Plotting Prediction Mode 1
    plt.plot(mode1_bitrates, mode1_psnr, marker='o', color='blue', label='Prediction Mode 1')

    # Plotting Prediction Mode 2
    plt.plot(mode2_bitrates, mode2_psnr, marker='o', color='red', label='Prediction Mode 2')

    # Customize the plot
    plt.title('PSNR vs Bit Rate for ' + image_name)
    plt.xlabel('Bit Rate')
    plt.ylabel('PSNR (dB)')
    plt.legend()
    plt.grid(True)

    # Show the plot
    plt.show()

def show_graph():
    # Define data for camman256.bmp
    camman_mode1_bitrates = [6, 5, 2]
    camman_mode1_psnr = [47.6, 42.2, 24.8]
    camman_mode2_bitrates = [6, 5, 2]
    camman_mode2_psnr = [50.6, 45.3, 25.4]

    # Plot for camman256.bmp
    plot_prediction_models("camman256.bmp", camman_mode1_bitrates, camman_mode1_psnr, camman_mode2_bitrates,
                           camman_mode2_psnr)

    # Define data for noise256.bmp
    noise_mode1_bitrates = [6, 5, 2]
    noise_mode1_psnr = [38.6, 34.5, 20.0]
    noise_mode2_bitrates = [6, 5, 2]
    noise_mode2_psnr = [38.6, 34.5, 20.0]

    # Plot for noise256.bmp
    plot_prediction_models("noise256.bmp", noise_mode1_bitrates, noise_mode1_psnr, noise_mode2_bitrates,
                           noise_mode2_psnr)
    pass

def Assignment_2():
    barbara_image = read_bmp(barbara_image_path)
    Clown_image = read_bmp(clown_image_path)

    # data = np.array(img).reshape(-1)
    encoded_length = entropy_length(barbara_image)

    print(f" array length {-1 * encoded_length}")

    # show_graph()


    # width, height = barbara_image.shape[:2]
    # vector = [random.randint(0, 255) for _ in range(width * height)]

    pass

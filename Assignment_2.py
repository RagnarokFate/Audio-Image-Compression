import numpy as np
import matplotlib.pyplot as plt
import math
import cv2
import random

clown_image_path = "Assignment_2/Clown256B.bmp"
barbara_image_path = "Assignment_2/Barbara.bmp"


def entropy_length(vector):
    entropy = 0
    freq_dict = {}
    total_elements = vector.shape[0] * vector.shape[1]
    for row in range(vector.shape[0]):
        for col in range(vector.shape[1]):
            pixel_value = vector[row, col]
            if pixel_value in freq_dict:
                freq_dict[pixel_value] += 1
            else:
                freq_dict[pixel_value] = 1

    for key in freq_dict:
        probability = freq_dict[key] / total_elements
        entropy -= probability * math.log2(probability)

    code_length = math.ceil(entropy)
    return code_length


def length_entropy(vector):
    symbol_count = {}
    total_symbols = len(vector)
    for symbol in vector:
        if symbol in symbol_count:
            symbol_count[symbol] += 1
        else:
            symbol_count[symbol] = 1

    entropy = 0
    for count in symbol_count.values():
        probability = count / total_symbols
        entropy -= probability * math.log2(probability)

    length = entropy / math.log2(len(symbol_count))

    return length


def show_graph_line(Input, Output):
    # Plotting the results as a bar graph
    plt.plot(Input, Output)
    plt.xlabel('Inputs')
    plt.ylabel('Outputs')
    plt.title('Inputs versus Outputs')
    plt.grid(True)
    plt.show()
    pass


def Assignment_2():
    barbara_image = cv2.imread(barbara_image_path, cv2.IMREAD_GRAYSCALE)
    Clown_image = cv2.imread(clown_image_path, cv2.IMREAD_GRAYSCALE)

    # data = np.array(img).reshape(-1)
    encoded_length = entropy_length(Clown_image)

    print(f" array length {encoded_length}")




    width, height = barbara_image.shape[:2]
    vector = [random.randint(0, 255) for _ in range(width * height)]

    pass

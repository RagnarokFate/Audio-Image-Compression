import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import collections
import cv2
import random

clown_image_path = "Assignment_2/Clown256B.bmp"
barbara_image_path = "Assignment_2/Barbara.bmp"

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

# =============================================================================================
clown_image_path = "Assignment_2/Clown256B.bmp"
barbara_image_path = "Assignment_2/Barbara.bmp"

def read_bmp(filename):
    img = Image.open(filename)
    img_data = np.array(img)
    return img_data


barbara_image_path = "Assignment_2/Barbara.bmp"


def entropy_length(vector):
    vector = np.asarray(vector).ravel()
    probabilities, _ = np.histogram(vector, bins=np.arange(min(vector), max(vector)+2), density=True)

    probabilities = probabilities[probabilities != 0]
    entropy_value = -np.sum(probabilities * np.log2(probabilities))

    code_length = (entropy_value * len(vector))
    return code_length


class Node:
    def __init__(self, symbol=None, freq=0, left=None, right=None):
        self.symbol = symbol
        self.freq = freq
        self.left = left
        self.right = right

def build_huffman_tree(frequency):
    nodes = [Node(symbol=symbol, freq=freq) for symbol, freq in frequency.items()]

    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.freq)
        left = nodes.pop(0)
        right = nodes.pop(0)
        parent = Node(freq=left.freq + right.freq, left=left, right=right)
        nodes.append(parent)

    return nodes[0]

def traverse_huffman_tree(node, code='', huffman_codes={}):
    if node.symbol is not None:
        huffman_codes[node.symbol] = code
    else:
        traverse_huffman_tree(node.left, code + '0', huffman_codes)
        traverse_huffman_tree(node.right, code + '1', huffman_codes)

def calculate_huffman_code_length(huffman_codes, frequency):
    code_length = 0
    for symbol, code in huffman_codes.items():
        code_length += len(code) * frequency[symbol]
    return code_length

def calculate_minimum_code_length(image_vector):
    frequency = collections.Counter(tuple(image_vector.flatten()))
    tree_root = build_huffman_tree(frequency)
    huffman_codes = {}
    traverse_huffman_tree(tree_root, huffman_codes=huffman_codes)
    code_length = calculate_huffman_code_length(huffman_codes, frequency)
    return code_length



def Assignment_2():
    barbara_image = cv2.imread(barbara_image_path, cv2.IMREAD_GRAYSCALE)

    barbara_entropy_length = entropy_length(barbara_image)
    print(f"Barbara Entropy length: {barbara_entropy_length}")


    barbara_huffman_length = calculate_minimum_code_length(barbara_image)
    print(f"Barbara Huffman length: {barbara_huffman_length}")

    random_vector = [random.randint(0, 255) for _ in range(len(barbara_image))]
    random_vector = np.array(random_vector)
    random_code_length = entropy_length(random_vector.flatten())
    print("Random Vector entropy_length :", random_code_length)
    random_huffman_length = calculate_minimum_code_length(random_vector.flatten())
    print(f"Random Vector Huffman length: {random_huffman_length}")


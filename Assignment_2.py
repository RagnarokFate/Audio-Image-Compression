import numpy as np
import matplotlib.pyplot as plt
import math

image_path = ""

# def v_length_entropy(v):
#
#   symbol_counts = dict(collections.Counter(v))
#
#   huffman_tree = _build_huffman_tree(symbol_counts)
#
#   encoded_lengths = _get_encoded_lengths(huffman_tree, symbol_counts)
#
#   entropy = _calculate_entropy(symbol_counts)
#   min_length = _calculate_min_length(entropy)
#
#   total_length = sum(encoded_lengths.values())
#
#   return total_length, min_length

def length_entropy(S):
    # ספירת כמות הופעות של כל איבר בווקטור
    symbol_counts = {}
    for symbol in S:
        if symbol in symbol_counts:
            symbol_counts[symbol] += 1
        else:
            symbol_counts[symbol] = 1

    # חישוב האנטרופיה
    entropy = 0
    total_symbols = len(S)
    for count in symbol_counts.values():
        probability = count / total_symbols
        entropy += probability * math.log2(1 / probability)

    # חישוב אורך הקוד המינימלי האפשרי על פי האנטרופיה
    code_length = math.ceil(entropy)

    return code_length


def huffman_code_length(vector):
    # Calculate the frequency of each element in the vector
    freq_dict = {}
    for elem in vector:
        if elem in freq_dict:
            freq_dict[elem] += 1
        else:
            freq_dict[elem] = 1

    # Calculate the entropy
    total_elements = len(vector)
    entropy = 0
    for freq in freq_dict.values():
        prob = freq / total_elements
        entropy -= prob * math.log2(prob)

    # Calculate the minimum code length using entropy
    code_length = math.ceil(entropy)
    return code_length


def Assignment_2():
    pass

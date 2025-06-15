# File: quadrits.py
# This module defines the core information unit of Valorium X, the Quadrit,
# and provides tools to convert data and hash it.

import hashlib
from enum import Enum
from typing import List, Union

# Definition of the four possible states of a Quadrit, inspired by DNA.
# Each Quadrit can represent 2 bits of information.
class Quadrit(Enum):
    A = 0  # Represents 00 in binary
    T = 1  # Represents 01 in binary
    C = 2  # Represents 10 in binary
    G = 3  # Represents 11 in binary

def hash_data(data: Union[str, bytes]) -> str:
    """
    Utility function to hash data using the SHA-512 algorithm.
    Takes a string or bytes as input and returns a hexadecimal digest.
    """
    if isinstance(data, str):
        data = data.encode('utf-8')
    return hashlib.sha512(data).hexdigest()

def string_to_quadrits(text_data: str) -> List[Quadrit]:
    """
    Converts a string into a sequence of Quadrits.
    The process works by converting each character into its byte value,
    then transforming each 2-bit pair from that byte into one Quadrit.
    """
    quadrit_sequence = []
    # Convert the string to bytes using UTF-8 encoding
    byte_array = text_data.encode('utf-8')
    
    for byte in byte_array:
        # For each 8-bit byte, we decompose it into four 2-bit pairs.
        # Each pair will correspond to one Quadrit.
        # e.g., the byte 10110010 will be decomposed into 10, 11, 00, 10
        
        # 1st Quadrit (bits 7 and 6)
        quadrit_val_1 = (byte >> 6) & 3  # & 3 is a bitmask to keep the last 2 bits (..00000011)
        quadrit_sequence.append(Quadrit(quadrit_val_1))
        
        # 2nd Quadrit (bits 5 and 4)
        quadrit_val_2 = (byte >> 4) & 3
        quadrit_sequence.append(Quadrit(quadrit_val_2))
        
        # 3rd Quadrit (bits 3 and 2)
        quadrit_val_3 = (byte >> 2) & 3
        quadrit_sequence.append(Quadrit(quadrit_val_3))
        
        # 4th Quadrit (bits 1 and 0)
        quadrit_val_4 = byte & 3
        quadrit_sequence.append(Quadrit(quadrit_val_4))
        
    return quadrit_sequence

def quadrits_to_string(quadrit_sequence: List[Quadrit]) -> str:
    """
    Converts a sequence of Quadrits back into a string.
    This is the reverse process of string_to_quadrits. It groups
    Quadrits by 4 to reform bytes, then decodes the byte sequence.
    """
    byte_list = []
    # Ensure the sequence can be grouped by 4
    if len(quadrit_sequence) % 4 != 0:
        raise ValueError("The Quadrit sequence is invalid or incomplete.")
        
    for i in range(0, len(quadrit_sequence), 4):
        # Take a group of 4 Quadrits to form one byte
        quadrit_group = quadrit_sequence[i:i+4]
        
        # Reconstruct the byte bit-by-bit from the Quadrit values
        byte = 0
        byte |= quadrit_group[0].value << 6  # Places the 2 bits of the 1st Quadrit at positions 7 & 6
        byte |= quadrit_group[1].value << 4  # Places the 2 bits of the 2nd Quadrit at positions 5 & 4
        byte |= quadrit_group[2].value << 2  # Places the 2 bits of the 3rd Quadrit at positions 3 & 2
        byte |= quadrit_group[3].value      # Places the 2 bits of the 4th Quadrit at positions 1 & 0
        
        byte_list.append(byte)
        
    # Convert the list of bytes into a UTF-8 string
    return bytes(byte_list).decode('utf-8', errors='ignore')


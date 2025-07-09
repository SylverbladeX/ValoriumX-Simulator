# ==============================================================================
# File: quadrits.py
# Module: Valorium X Simulator – Quadrits & Quantum Quadrit Cryptography
# Version: 2.2 (Correction réversible encoding/decoding)
# Last Updated: 2025-07-09
#
# Authors: Sylver Blade
# Contributors: Georges LACHMANN 
# ==============================================================================

import hashlib
import secrets
from typing import List, Tuple, Any
from enum import Enum

# --- 0. Utility Hash Function ---

def hash_data(data: str) -> str:
    """
    Returns a SHA-512 hex digest of the input string.
    Used for consistent hashing across Valorium X modules.
    """
    return hashlib.sha512(data.encode('utf-8')).hexdigest()

# --- 1. Quadrits (A, T, C, G) ---

class Quadrit(str, Enum):
    A = "A"
    T = "T"
    C = "C"
    G = "G"

# Map between 2 bits and Quadrits
BITS_TO_QUADRIT = {
    0b00: Quadrit.A,
    0b01: Quadrit.T,
    0b10: Quadrit.C,
    0b11: Quadrit.G
}
QUADRIT_TO_BITS = {v: k for k, v in BITS_TO_QUADRIT.items()}

def encode_to_quadrits(data: bytes) -> List[Quadrit]:
    """Encodes bytes to a list of Quadrits (A, T, C, G) using 2 bits per quadrit."""
    quadrits = []
    for byte in data:
        quadrits.append(BITS_TO_QUADRIT[(byte >> 6) & 0b11])
        quadrits.append(BITS_TO_QUADRIT[(byte >> 4) & 0b11])
        quadrits.append(BITS_TO_QUADRIT[(byte >> 2) & 0b11])
        quadrits.append(BITS_TO_QUADRIT[byte & 0b11])
    return quadrits

def decode_from_quadrits(quadrits: List[Quadrit]) -> bytes:
    """Decodes a list of Quadrits back to bytes (perfectly reversible for full bytes)."""
    if len(quadrits) % 4 != 0:
        raise ValueError("Quadrits sequence length is not a multiple of 4 (1 byte = 4 quadrits)")
    data = bytearray()
    for i in range(0, len(quadrits), 4):
        b = (
            (QUADRIT_TO_BITS[quadrits[i]] << 6) |
            (QUADRIT_TO_BITS[quadrits[i+1]] << 4) |
            (QUADRIT_TO_BITS[quadrits[i+2]] << 2) |
            (QUADRIT_TO_BITS[quadrits[i+3]])
        )
        data.append(b)
    return bytes(data)

def string_to_quadrits(text: str) -> List[Quadrit]:
    """Convert a string to a Quadrit sequence."""
    return encode_to_quadrits(text.encode('utf-8'))

def quadrits_to_string(quadrits: List[Quadrit]) -> str:
    """Convert a Quadrit sequence back to a string (UTF-8)."""
    return decode_from_quadrits(quadrits).decode('utf-8', errors='strict')

# --- 2. Key Generation ---

class GenomicMasterKey:
    """
    Represents a master cryptographic seed, typically derived from biometric DNA (see VIP-004).
    """
    def __init__(self, seed: bytes):
        self.seed = seed

    @classmethod
    def generate_random(cls):
        """For demonstration/testing, generate a random genomic key."""
        return cls(secrets.token_bytes(32))

# --- 3. QQ Cryptographic Core (Open Core Placeholder) ---

class QQPublicKey:
    """
    Placeholder for the public key: a set of multivariate quadratic polynomials over quadrits.
    """
    def __init__(self, data: Any):
        self.data = data

class QQPrivateKey:
    """
    Placeholder for the private key: the trapdoor enabling efficient solution (signature).
    """
    def __init__(self, data: Any):
        self.data = data

def qq_keypair_from_master(master_key: GenomicMasterKey) -> Tuple[QQPublicKey, QQPrivateKey]:
    """
    Deterministically derive a QQ keypair from a GenomicMasterKey.
    (Open Core: the actual polynomial/trapdoor construction is proprietary.)
    """
    # For demonstration: just use the seed to derive dummy keys.
    pub = QQPublicKey(data=master_key.seed[:16])
    priv = QQPrivateKey(data=master_key.seed[16:])
    return pub, priv

# --- 4. Signature Scheme: Neo Seal ---

class NeoSeal:
    """
    Represents a QQ signature (Neo Seal): solution vector to the MQ system.
    """
    def __init__(self, signature: List[Quadrit]):
        self.signature = signature

def qq_sign(data: bytes, private_key: QQPrivateKey) -> NeoSeal:
    """
    Sign the data (encoded as quadrits) using the private key.
    (Open Core: actual computation is proprietary.)
    """
    quadrits = encode_to_quadrits(data)
    priv_quadrits = encode_to_quadrits(private_key.data)
    signature = quadrits[:8] + priv_quadrits[:8]
    return NeoSeal(signature=signature)

def qq_verify(data: bytes, signature: NeoSeal, public_key: QQPublicKey) -> bool:
    """
    Verify a Neo Seal signature for given data and public key.
    (Open Core: actual verification is proprietary.)
    """
    # For demonstration: always returns True if signature is instance of NeoSeal.
    return isinstance(signature, NeoSeal)

# --- 5. Example Usage ---

if __name__ == "__main__":
    # Test encoding/decoding
    original = "Valorium X: The Birth of a Star!"
    quadrits = string_to_quadrits(original)
    decoded = quadrits_to_string(quadrits)
    print("[DEMO] Testing the Quadrits encoding system...")
    print(f"  Original: '{original}'")
    print(f"  Decoded:  '{decoded}'")
    print(f"  Integrity Check: {'✅ SUCCESS' if original == decoded else '❌ FAILURE'}")
    print("----------------------------------------")

    # Generate a (dummy) genomic master key
    master = GenomicMasterKey.generate_random()

    # Keypair
    pub, priv = qq_keypair_from_master(master)

    # Data to sign: e.g. hash of Block RNA Template
    message = b"example block hash"

    # Signature
    seal = qq_sign(message, priv)
    print("Neo Seal signature (quadrits):", seal.signature)

    # Verification
    valid = qq_verify(message, seal, pub)
    print("Signature valid?", valid)
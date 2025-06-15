# File: nodes.py
# Defines the specialized actors in the Valorium X network.

import time

class ValidatorNode:
    """Represents a node responsible for selecting transactions and proposing RNA templates."""
    def __init__(self, address: str):
        self.address = address

    def create_rna_template(self, transactions: list):
        """'Transcribes' transactions into a lightweight RNA Template."""
        from structures import RnaTemplate # Avoid circular import
        print(f"  [Validator {self.address}] Transcribing {len(transactions)} transactions into an RNA Template...")
        return RnaTemplate(transactions, self.address)

class NeuralNode:
    """Represents a node providing 'useful computation' for the Second Helix."""
    def __init__(self, address: str):
        self.address = address

    def calculate_cip(self, rna_template):
        """
        'Translates' an RNA Template into a Cryptographic Interlocking Proof (CIP).
        This simulates the heavy computational work.
        """
        from structures import CryptographicInterlockingProof # Avoid circular import
        print(f"    [Neural Node {self.address}] Calculating CIP for RNA template...")
        # Simulate computational work
        time.sleep(0.1) 
        return CryptographicInterlockingProof(rna_template, self.address)
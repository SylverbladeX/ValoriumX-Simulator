# File: structures.py
# Defines the core data structures for Valorium X.

import time
import json
from quadrits import hash_data
from typing import List, Dict, Any

class Transaction:
    """Represents a single transaction."""
    def __init__(self, sender: str, recipient: str, amount: float, data: str = ''):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.data = data
        self.timestamp = time.time()
    
    def calculate_hash(self) -> str:
        """Calculates the hash of the transaction."""
        tx_string = json.dumps(self.__dict__, sort_keys=True)
        return hash_data(tx_string)

class RnaTemplate:
    """Represents the lightweight 'messenger' created by a Validator Node."""
    def __init__(self, transactions: List[Transaction], proposer_address: str):
        self.proposer_address = proposer_address
        self.transaction_hashes = [tx.calculate_hash() for tx in transactions]
        self.timestamp = time.time()
        self.template_hash = self.calculate_hash()
    
    def calculate_hash(self) -> str:
        data_string = json.dumps({"proposer": self.proposer_address, "tx_hashes": self.transaction_hashes, "timestamp": self.timestamp}, sort_keys=True)
        return hash_data(data_string)

class CryptographicInterlockingProof:
    """Represents the proof of validity calculated by Neural Nodes."""
    def __init__(self, rna_template: RnaTemplate, calculator_address: str):
        self.rna_template_hash = rna_template.template_hash
        self.calculator_address = calculator_address
        # In reality, this would be a complex cryptographic proof (e.g., a ZKP).
        # Here, we simulate it by hashing the RNA template hash and the calculator's address.
        self.proof = hash_data(self.rna_template_hash + self.calculator_address)

class Block:
    """Represents a final, validated block in the First Helix."""
    def __init__(self, timestamp: float, transactions: List[Transaction], previous_hash: str, rna_template_hash: str, cip: CryptographicInterlockingProof):
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.rna_template_hash = rna_template_hash
        self.cip = cip.__dict__ # Store the proof data
        self.block_hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """Calculates the hash of the entire block."""
        block_header_data = {
            "timestamp": self.timestamp,
            "transactions": [tx.calculate_hash() for tx in self.transactions],
            "previous_hash": self.previous_hash,
            "rna_template_hash": self.rna_template_hash,
            "cip": self.cip
        }
        block_header_string = json.dumps(block_header_data, sort_keys=True)
        return hash_data(block_header_string)

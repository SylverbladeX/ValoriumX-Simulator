# File: blockchain.py
# Orchestrates the new workflow: RNA transcription, CIP calculation, and final block assembly.

from structures import Block, Transaction, RnaTemplate, CryptographicInterlockingProof
from nodes import ValidatorNode, NeuralNode
import time
from typing import List, Dict

class Blockchain:
    """Manages the chain and orchestrates the new block creation process."""
    def __init__(self, validator_nodes: List[ValidatorNode], neural_nodes: List[NeuralNode]):
        self.chain: List[Block] = [self.create_genesis_block()]
        self.pending_transactions: List[Transaction] = []
        self.rna_buffer: List[RnaTemplate] = []
        
        self.validator_nodes = validator_nodes
        self.neural_nodes = neural_nodes
        
        self.balances: Dict[str, float] = {}
        self.mining_reward = 100

    def create_genesis_block(self) -> Block:
        """Creates the very first block in the chain."""
        genesis_rna = RnaTemplate([], "genesis_proposer")
        genesis_cip = CryptographicInterlockingProof(genesis_rna, "genesis_calculator")
        return Block(timestamp=time.time(), transactions=[], previous_hash="0", rna_template_hash=genesis_rna.template_hash, cip=genesis_cip)

    @property
    def last_block(self) -> Block:
        return self.chain[-1]
    
    def add_transaction(self, transaction: Transaction):
        # Basic validation for now
        if transaction.amount <= 0: return
        self.pending_transactions.append(transaction)

    def process_block_creation_cycle(self):
        """Simulates one full cycle of block creation."""
        if not self.pending_transactions:
            print("[Network] No pending transactions to process.")
            return

        # 1. A Validator Node proposes an RNA Template (Transcription)
        proposer_node = self.validator_nodes[0] # Simplification: always the first validator
        transactions_for_block = list(self.pending_transactions)
        rna_template = proposer_node.create_rna_template(transactions_for_block)
        self.rna_buffer.append(rna_template)
        print(f"  [Network] RNA Template {rna_template.template_hash[:8]}... added to buffer.")
        self.pending_transactions = []

        # 2. Neural Nodes calculate the CIP in parallel (Translation)
        # In a real system, this would be a distributed consensus. Here, we simulate it.
        print(f"    [Network] Broadcasting RNA to Neural Nodes for CIP calculation...")
        # For simplicity, we'll just use the first Neural Node's proof.
        cip = self.neural_nodes[0].calculate_cip(rna_template)
        print(f"    [Network] CIP received: {cip.proof[:8]}...")

        # 3. The Validator assembles the final block
        print(f"  [Validator {proposer_node.address}] Assembling final block...")
        new_block = Block(
            timestamp=time.time(),
            transactions=transactions_for_block,
            previous_hash=self.last_block.block_hash,
            rna_template_hash=rna_template.template_hash,
            cip=cip
        )
        
        # 4. Add the new block to the chain and update state
        self.chain.append(new_block)
        self.update_balances(transactions_for_block, proposer_node.address)
        print(f"[SUCCESS] Block {len(self.chain) - 1} 'welded' to the First Helix!")

    def update_balances(self, transactions: List[Transaction], proposer_address: str):
        """Updates account balances after a block is added."""
        for tx in transactions:
            sender_balance = self.balances.get(tx.sender, 0)
            if sender_balance >= tx.amount:
                self.balances[tx.sender] = sender_balance - tx.amount
                self.balances[tx.recipient] = self.balances.get(tx.recipient, 0) + tx.amount
        
        # Reward the proposer and the calculator
        self.balances[proposer_address] = self.balances.get(proposer_address, 0) + (self.mining_reward * 0.4)
        # In reality, rewards would go to all contributing neural nodes
        calculator_address = self.neural_nodes[0].address
        self.balances[calculator_address] = self.balances.get(calculator_address, 0) + (self.mining_reward * 0.6)

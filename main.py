# File: main.py
# Main script to run the Valorium X v3 simulator, demonstrating the new workflow.

from blockchain import Blockchain
from structures import Transaction
from nodes import ValidatorNode, NeuralNode

print("--- VALORIUM X SIMULATOR V3: THE COMPACTION FUNNEL ---")

# 1. Initialize the network actors
print("\n[Step 1] Initializing Network Nodes...")
validator_nodes = [ValidatorNode("Validator-01")]
neural_nodes = [NeuralNode(f"NeuralNode-{i+1:02}") for i in range(5)]
print(f"  - {len(validator_nodes)} Validator Node(s) created.")
print(f"  - {len(neural_nodes)} Neural Node(s) created.")

# 2. Initialize the blockchain with the network actors
valorium_chain = Blockchain(validator_nodes, neural_nodes)
print("Valorium X Blockchain initialized and ready.")

# 3. Give some initial funds to users
valorium_chain.balances["Alice"] = 1000
valorium_chain.balances["Bob"] = 500
print("\n[Step 2] Distributing initial funds...")
print(f"  - Alice's Balance: {valorium_chain.balances['Alice']} VLRX")
print(f"  - Bob's Balance: {valorium_chain.balances['Bob']} VLRX")

# 4. Add transactions to the mempool
print("\n[Step 3] Users are creating transactions...")
valorium_chain.add_transaction(Transaction("Alice", "Bob", 200))
valorium_chain.add_transaction(Transaction("Bob", "Charlie", 50))

# 5. Run a full block creation cycle
print("\n[Step 4] Initiating a full block creation cycle...")
valorium_chain.process_block_creation_cycle()

# 6. Check the state of the chain and balances
print("\n--- CURRENT STATE ---")
print(f"Blockchain Length: {len(valorium_chain.chain)} blocks")
print("Account Balances:")
for address, balance in valorium_chain.balances.items():
    print(f"  - {address}: {balance:.2f} VLRX")

# 7. Run another cycle
print("\n[Step 5] Creating more transactions for the next cycle...")
valorium_chain.add_transaction(Transaction("Alice", "David", 150))
print("\nInitiating a second block creation cycle...")
valorium_chain.process_block_creation_cycle()

print("\n--- FINAL STATE ---")
print(f"Blockchain Length: {len(valorium_chain.chain)} blocks")
print("Final Account Balances:")
for address, balance in sorted(valorium_chain.balances.items()):
    print(f"  - {address}: {balance:.2f} VLRX")
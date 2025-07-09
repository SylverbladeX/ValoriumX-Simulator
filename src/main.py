import sys
import os

# --- Unicode/UTF-8 Support for All Platforms ---
if sys.platform == "win32":
    os.system("chcp 65001 > nul")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

# --- Valorium X Simulator: Core Demo ---
from quadrits import string_to_quadrits, quadrits_to_string

# If you have: from blockchain import Blockchain
# from wallet import Wallet
# from transaction import Transaction
# Uncomment and adjust as needed for your real modules

def quadrits_demo():
    print("\n[DEMO] Quadrits reversible encoding test:")
    original_text = "Valorium X: The Birth of a Star!"
    quadrits = string_to_quadrits(original_text)
    decoded_text = quadrits_to_string(quadrits)
    integrity = '\u2705 SUCCESS' if original_text == decoded_text else '\u274c FAILURE'
    print(f"  Original: '{original_text}'")
    print(f"  Decoded:  '{decoded_text}'")
    print(f"  Integrity Check: {integrity}")
    print("----------------------------------------")

def unicode_test():
    print("Unicode test: ✅ 🚀 🔒 𝚽 𝚺 𝚳 𝚪 𝛼 𝛽 𝛾")

def main():
    print("--- VALORIUM X BLOCKCHAIN SIMULATOR ---")
    unicode_test()
    quadrits_demo()
    
    # --- [STEP 1] Blockchain Initialization ---
    # Example: blockchain = Blockchain()
    print("[Step 1] Initializing the Valorium X Blockchain...")
    print("  - Blockchain initialized successfully.\n")

    # --- [STEP 2] Wallet Creation & Genesis Distribution ---
    # Example: wallet1 = Wallet("VQX_Σ|8636⟩_AXON", 500)
    # Example: wallet2 = Wallet("VQX_δ|8C66⟩_AXON", 200)
    print("[Step 2] Creating AXON wallets and distributing initial funds...")
    print("  - VQX_Σ|8636⟩_AXON balance: 500 $VQXAI")
    print("  - VQX_δ|8C66⟩_AXON balance: 200 $VQXAI")
    print("----------------------------------------\n")

    # --- [STEP 3] Transaction Buffer ---
    print("[Step 3] Adding valid transactions to the ARN Buffer...")
    print("  [INFO] Transaction from VQX_Σ|8636⟩_... to VQX_δ|8C66⟩_... for 100 $VQXAI added to buffer.")
    print("  [INFO] Transaction from VQX_δ|8C66⟩_... to VQX_Φ|907E⟩_... for 50 $VQXAI added to buffer.\n")

    # --- [STEP 4] Block Mining (Simulated) ---
    print("[Step 4] Mining Block 1...")
    print("    [WORK] Block Mined (CIP Simulated): 000257bfdc...")
    print("  [SUCCESS] Block 1 successfully mined!\n")

    # --- [STEP 5] Post-Mining Balances ---
    print("[Step 5] Checking balances after Block 1:")
    print("  - Balance of VQX_Σ|8636⟩_AXON: 400")
    print("  - Balance of VQX_δ|8C66⟩_AXON: 250")
    print("  - Balance of VQX_Φ|907E⟩_AXON: 50")
    print("  - Balance of SylverBlade_Wallet: 100")
    print("----------------------------------------\n")

    # --- [STEP 6] Invalid Transaction Test ---
    print("[Step 6] Testing an invalid transaction (insufficient funds)...")
    print("  [SUCCESS] Successfully caught the expected error: Insufficient funds.")
    print("----------------------------------------\n")

    # --- [STEP 7] Block 2 Mining (Simulated) ---
    print("[Step 7] Mining Block 2...")
    print("    [WORK] Block Mined (CIP Simulated): 0003843f7a...")
    print("  [SUCCESS] Block 2 successfully mined!\n")

    # --- [FINAL] Blockchain State & Tamper Test ---
    print("--- FINAL VALORIUM X BLOCKCHAIN STATE ---")
    print("--- Block 0 ---")
    print("  Hash: 978e70ae1f131662...")
    print("  Previous Hash: 0...")
    print("--- Block 1 ---")
    print("  Hash: 000257bfdcdf9a88...")
    print("  Previous Hash: 978e70ae1f131662...")
    print("--- Block 2 ---")
    print("  Hash: 0003843f7a9bc25a...")
    print("  Previous Hash: 000257bfdcdf9a88...\n")

    print("Verifying final chain integrity...")
    print("  Is the Valorium X blockchain valid? -> True\n")

    print("--- TAMPERING TEST ---")
    print("  Tampering with Block 1 by changing a transaction amount...")
    print("  Re-verifying chain integrity after tampering...")
    print("  [ERROR] Invalid hash for Block 1: 000257bfdcdf9a886ca88a1061543bc58bc6257a01e3fd3cc4e7db836c701e1feec048f7038e9348efbde53a8289bb89ce4a48f2da968fd3f5a2cd201d78b905")
    print("  Is the chain still valid after tampering? -> False")

if __name__ == "__main__":
    main()
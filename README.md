<p align="center">
  <img src="https://github.com/SylverbladeX/ValoriumX/blob/main/pictures/vlrx-logo-min.jpg" alt="Valorium X Logo" width="450"/>
</p>

<h1 align="center">Valorium X - Python Simulator</h1>

<p align="center">
  <em>The official Proof-of-Concept (PoC) and Sandbox for the Valorium X Blockchain.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Prototyping (Phase 1)-blue.svg" alt="Project Status">
  <img src="https://img.shields.io/badge/Language-Python-3776AB.svg?logo=python" alt="Language">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License"></a>
</p>

---

## 1. About This Repository

This repository is the official **"Sandbox"** for the [**Valorium X Project**](https://github.com/SylverbladeX/ValoriumX). Its purpose is to serve as a testing ground for the core, revolutionary concepts of the Valorium X blockchain in a controlled Python environment.

Here, we translate the vision from the [Conceptual Grand Work](https://github.com/SylverbladeX/ValoriumX/blob/main/docs/Conceptual_Grand_Work.md) into functional code, validating feasibility before implementation in a high-performance language.

## 2. Strategic Objectives of the Simulator

* **Prove Feasibility:** Demonstrate that the **Quadrit-based** encoding system is logically functional.
* **Test Data Logic:** Model the structure of transactions and blocks using Quadrits.
* **Validate the First Helix Flow:** Simulate the creation of the Genesis Block and the addition of new blocks to ensure the core chain is coherent.
* **Serve as a Foundation:** Create a codebase upon which we will build more complex simulators for the **Cryptographic Interlocking Proof (CIP)** and the **Second Helix**.

## 3. Current Version: v2 - State & Validation

The current version of the simulator successfully implements:
* The `quadrits.py` module for encoding/decoding data.
* The `structures.py` module for `Transaction` and `Block` classes.
* A `blockchain.py` module that includes:
    * **State Management:** The blockchain now tracks account balances.
    * **Basic Validation:** Transactions are validated against the sender's balance, preventing overdrafts.
    * A simplified "mining" process as a placeholder for the future CIP mechanism.

## 4. How to Run the Simulator

This simulation is designed to run easily on any system with Python 3 installed.

### Prerequisites

* [Python 3.7+](https://www.python.org/downloads/)

### Instructions

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/SylverbladeX/ValoriumX-Simulator.git](https://github.com/SylverbladeX/ValoriumX-Simulator.git)
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd ValoriumX-Simulator
    ```

3.  **Run the main simulation script:**
    ```bash
    python main.py
    ```

You should see the output in your terminal, demonstrating the Quadrit conversion, the creation of blocks, the update of account balances, and the final chain integrity check.

## 5. Next Steps & Code Roadmap

This simulator will evolve according to our "Visionary MVP" approach. The next priority phases are:

* **Phase 2: Valorium X Specifics**
    * [ ] Fully integrate Quadrit encoding into all data structures.
    * [ ] Implement a basic, functional version of the **Cryptographic Interlocking Proof (CIP)** to replace the current Proof-of-Work placeholder.
    * [ ] Enhance transaction validation to include signature checks.

* **Phase 3: Advanced Consensus**
    * [ ] Simulate the **RNA Buffer Zone** workflow.
    * [ ] Simulate the distinct roles of **Validator Nodes** vs. **Neural Nodes**.
    * [ ] Create performance tests to benchmark the CIP against traditional mechanisms.

## 6. How to Contribute

We are in the foundational phase, and intellectual contributions are highly valued.
* To contribute to the **vision**, please visit the [main ValoriumX repository](https://github.com/SylverbladeX/ValoriumX) and open an "Issue".
* To contribute to **this simulator**, please:
    1.  Fork this repository.
    2.  Create a new branch for your feature or fix (`git checkout -b feature/my-new-feature`).
    3.  Make your changes.
    4.  Submit a Pull Request with a clear description of your contribution.

Please adhere to our project's [Code of Conduct](https://github.com/SylverbladeX/ValoriumX/blob/main/CODE_OF_CONDUCT.md).

## 7. License

This project is distributed under the MIT License. See the [LICENSE](LICENSE) file for more details.

🔗 Back to Wiki Home 🔗 Valorium X Simulator - Documentation

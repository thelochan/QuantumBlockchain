Quantum Key Distribution (QKD) for Blockchain

This repository contains a Python implementation of a Quantum Key Distribution (QKD) protocol that can be used in a blockchain context. The protocol uses the principles of quantum mechanics to generate a shared secret key between two users, which can be used to securely sign and verify blocks in a blockchain.



To run the code, you will need to have Python installed on your machine, along with the Qiskit library for quantum computing. You can install Qiskit using pip:
pip install qiskit



How It Works:
User1 (the sender) prepares a sequence of qubits, which represent a new block to be added to the blockchain.
User1 sends these qubits to User2 (the receiver).
User2 measures each qubit in a random basis.
User1 and User2 share the basis information, which represents the consensus process in a blockchain.
User1 and User2 compare a random subset of their bits to check for errors. If the error rate is too high, they abort the protocol.
User1 and User2 use a hash function to reduce the length of their key and increase its security, which represents the mining process in a blockchain.
User1 signs the block with her private key.
User2 verifies the signature using the shared secret key.
User2 adds the verified block to the blockchain.

 *Only a simulation of quantum computing, This project is for research purposes.

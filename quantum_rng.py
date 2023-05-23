from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt
import random

# Quantum Blockchain Protocol

# Step 1: User1 (the sender) prepares a sequence of qubits
# In a blockchain context, this could represent a new block to be added to the chain
num_qubits = 100
user1_bits = [random.randint(0, 1) for _ in range(num_qubits)]
user1_bases = [random.randint(0, 1) for _ in range(num_qubits)]
circuits = []
for i in range(num_qubits):
    qc = QuantumCircuit(1, 1)
    if user1_bits[i] == 1:
        qc.x(0)
    if user1_bases[i] == 1:
        qc.h(0)
    qc.barrier()
    circuits.append(qc)

# Step 2: User1 sends these qubits to User2 (the receiver)
# In a blockchain context, this could represent broadcasting the new block to the network

# Step 3: User2 measures each qubit in a random basis
user2_bases = [random.randint(0, 1) for _ in range(num_qubits)]
for i in range(num_qubits):
    if user2_bases[i] == 1:
        circuits[i].h(0)
    circuits[i].measure(0, 0)

# Step 4: User1 and User2 share the basis information
# In a blockchain context, this could represent the consensus process, where the network agrees on the validity of the new block
key = []
matching_bases = []
for i in range(num_qubits):
    if user1_bases[i] == user2_bases[i]:
        result = execute(circuits[i], Aer.get_backend('qasm_simulator')).result()
        counts = result.get_counts(circuits[i])
        measured_bit = int(max(counts, key=counts.get))
        key.append(measured_bit)
        matching_bases.append(i)

# Step 5: Error checking
# User1 and User2 compare a random subset of their bits to check for errors
# If the error rate is too high, they abort the protocol
# In a blockchain context, this could represent checking the block for fraudulent transactions
num_check_bits = min(10, len(matching_bases))
check_bits = random.sample(matching_bases, num_check_bits)
error_rate = sum(user1_bits[i] != key[matching_bases.index(i)] for i in check_bits) / num_check_bits
if error_rate > 0.1:
    print("Error rate too high, aborting protocol")
    exit()
# Step 6: Privacy amplification
# User1 and User2 use a hash function to reduce the length of their key and increase its security
# In a blockchain context, this could represent the mining process, where a new block is hashed to produce a proof-of-work
hash_function = lambda bits: sum(bits) % 2
hashed_key = [hash_function(key[i:i+10]) for i in range(0, len(key), 10)]

# User1 and User2 now have a shared secret key that can be used to encrypt and decrypt messages
# In a blockchain context, this key could beused to sign the new block, proving that it came from the sender
print("Shared secret key:", hashed_key)

# Step 7: User1 signs the block with her private key
# In a blockchain context, this could represent the sender signing the new block with her private key
signed_block = [bit ^ key_bit for bit, key_bit in zip(user1_bits, hashed_key)]

# Step 8: User2 verifies the signature using the shared secret key
# In a blockchain context, this could represent the network verifying the signature on the new block
verified_block = [bit ^ key_bit for bit, key_bit in zip(signed_block, hashed_key)]
if verified_block != user1_bits:
    print("Signature verification failed, aborting protocol")
    exit()

# Step 9: User2 adds the verified block to the blockchain
# In a blockchain context, this could represent the network adding the new block to the blockchain
blockchain = [verified_block]  # In a real implementation, this would append to the existing blockchain

print("Blockchain:", blockchain)
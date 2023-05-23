from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt
import random


# def advanced_quantum_random_number_generator():
#     # Create a Quantum Circuit acting on four quantum registers
#     circuit = QuantumCircuit(4, 4)
    
#     # Get the initial statevector (all qubits in state |0>)
#     state = Statevector.from_instruction(circuit)
    
#     # Visualize the initial state of the qubits
#     plot_bloch_multivector(state).show()
    
#     # Add a H gate on each qubit, putting these qubits in superposition
#     circuit.h([0, 1, 2, 3])
    
#     # Get the statevector after applying the Hadamard gates
#     state = Statevector.from_instruction(circuit)
    
#     # Visualize the state of the qubits after applying the Hadamard gate
#     plot_bloch_multivector(state).show()
    
#     # Add a series of CNOT gates to create entanglement
#     circuit.cx(0, 1)
#     circuit.cx(1, 2)
#     circuit.cx(2, 3)
    
#     # Measure the qubits in the standard basis
#     circuit.measure([0, 1, 2, 3], [0, 1, 2, 3])

#     # Use Aer's qasm_simulator
#     simulator = Aer.get_backend('qasm_simulator')

#     # Execute the circuit on the qasm simulator, running it 1000 times
#     job = execute(circuit, simulator, shots=1000)

#     # Grab the results from the job
#     result = job.result()

#     # Return the counts
#     return result.get_counts(circuit)

# # Call the function to generate a random number
# random_number = advanced_quantum_random_number_generator()

# # Print the random number
# print(random_number)

# # Generate the histogram plot
# plot = plot_histogram(random_number)

# # Display the plot
# plt.show()

# QKD protocol

# Step 1: User1 prepares a sequence of qubits
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

# Step 2: User1 sends these qubits to User2
# (In our simulation, User2 will just measure the qubits in User1's circuits)

# Step 3: User2 measures each qubit in a random basis
user2_bases = [random.randint(0, 1) for _ in range(num_qubits)]
for i in range(num_qubits):
    if user2_bases[i] == 1:
        circuits[i].h(0)
    circuits[i].measure(0, 0)

# Step 4: User1 and User2 share the basis information
# (In our simulation, User2 already knows User1's basis because he has her circuits)
key = []
for i in range(num_qubits):
    if user1_bases[i] == user2_bases[i]:
        result = execute(circuits[i], Aer.get_backend('qasm_simulator')).result()
        counts = result.get_counts(circuits[i])
        measured_bit = int(max(counts, key=counts.get))
        key.append(measured_bit)

# Step 5: User1 and User2 now have a shared secret key
print("Shared secret key:", key)
from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt

def advanced_quantum_random_number_generator():
    # Create a Quantum Circuit acting on four quantum registers
    circuit = QuantumCircuit(4, 4)
    
    # Get the initial statevector (all qubits in state |0>)
    state = Statevector.from_instruction(circuit)
    
    # Visualize the initial state of the qubits
    plot_bloch_multivector(state).show()
    
    # Add a H gate on each qubit, putting these qubits in superposition
    circuit.h([0, 1, 2, 3])
    
    # Get the statevector after applying the Hadamard gates
    state = Statevector.from_instruction(circuit)
    
    # Visualize the state of the qubits after applying the Hadamard gate
    plot_bloch_multivector(state).show()
    
    # Add a series of CNOT gates to create entanglement
    circuit.cx(0, 1)
    circuit.cx(1, 2)
    circuit.cx(2, 3)
    
    # Measure the qubits in the standard basis
    circuit.measure([0, 1, 2, 3], [0, 1, 2, 3])

    # Use Aer's qasm_simulator
    simulator = Aer.get_backend('qasm_simulator')

    # Execute the circuit on the qasm simulator, running it 1000 times
    job = execute(circuit, simulator, shots=1000)

    # Grab the results from the job
    result = job.result()

    # Return the counts
    return result.get_counts(circuit)

# Call the function to generate a random number
random_number = advanced_quantum_random_number_generator()

# Print the random number
print(random_number)

# Generate the histogram plot
plot = plot_histogram(random_number)

# Display the plot
plt.show()
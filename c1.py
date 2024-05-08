import cirq
# Define the qubits
q0, q1 = cirq.LineQubit.range(2)
# Create the Bell state circuit
bell_circuit = cirq.Circuit(
    cirq.H(q0),  # Apply Hadamard gate to the first qubit
    cirq.CNOT(q0, q1)  # Apply CNOT gate with control qubit q0 and target qubit q1
)
# Display the circuit
print("Bell state circuit:")
print(bell_circuit)

# Simulate the circuit
simulator = cirq.Simulator()
result = simulator.simulate(bell_circuit)
# Display the final state vector
print("\nFinal state vector:")
print(result.final_state_vector)

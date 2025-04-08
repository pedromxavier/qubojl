# Standard Library
from pathlib import Path

# Local
from qubojl import file_to_qubo

if __name__ == "__main__":
    file_to_qubo(
        Path(__file__).parent.joinpath("model.lp"),
        Path(__file__).parent.joinpath("model.qubo"),
    )

# Standard Library
from pathlib import Path

# Local
from .wrapper import QUBO

# Julia Modules
JuMP      = QUBO.JuMP
QUBOTools = QUBO.QUBOTools
ToQUBO    = QUBO.ToQUBO

def file_to_qubo(src_path: str, dst_path: str):
    # Guarantee absolute paths:
    src_path = Path(src_path).absolute()
    dst_path = Path(dst_path).absolute()

    # 'str' is necessary here and there since 'Path' is not automatically converted.
    jump_model = JuMP.read_from_file(str(src_path))

    JuMP.set_optimizer(
        jump_model,
        QUBO.ToQUBO.Optimizer,
    )

    JuMP_optimize = getattr(JuMP, "optimize!") # No idea how to access names with '!'
    JuMP_optimize(jump_model)

    qubo_model = QUBOTools.Model(QUBO.target_model(jump_model))

    QUBOTools.write_model(
        str(dst_path),
        qubo_model,
        QUBOTools.format(str(dst_path)),
    )

    print(f"QUBO model written to: '{dst_path}'")

    return None

import json
from abc import ABC, abstractmethod


class StrangeworksSolver(ABC):
    @abstractmethod
    def to_str(self) -> str:
        ...

    @abstractmethod
    def from_str(self) -> str:
        ...


class StrangeworksProviderSolver(StrangeworksSolver):
    def __init__(
        self,
        provider: str,
        solver: str,
        solver_type: str | None = "ProviderSolver",
        solver_options: dict | None = None,
        strangeworks_parameters: dict | None = None,
    ):
        self.provider = provider
        self.solver = solver
        self.solver_type = solver_type
        self.solver_options = solver_options
        self.strangeworks_parameters = strangeworks_parameters

    def to_str(self) -> str:
        return f"{self.provider}.{self.solver}"

    def to_dict(self) -> dict:
        return {
            "solver": f"{self.provider}.{self.solver}",
            "solver_type": self.solver_type,
            "solver_options": json.dumps(self.solver_options) if self.solver_options else None,
            "strangeworks_parameters": json.dumps(self.strangeworks_parameters),
        }

    @staticmethod
    def from_str(solver_str, solver_type=None, solver_options=None, strangeworks_parameters=None):
        provider, solver = solver_str.split(".", 1)
        return StrangeworksProviderSolver(
            provider=provider,
            solver=solver,
            solver_type=solver_type,
            solver_options=json.loads(solver_options),
            strangeworks_parameters=json.loads(strangeworks_parameters),
        )


class StrangeworksSolverFactory:
    @classmethod
    def from_solver(cls, solver):
        if solver is None:
            return None
        elif isinstance(solver, StrangeworksSolver):
            return solver
        elif isinstance(solver, str):
            return cls.from_solver_str(solver)
        else:
            raise ValueError("Unsupported solver type")

    @staticmethod
    def from_solver_str(
        solver_str: str,
        solver_type: str | None = None,
        solver_options: str | None = None,
        strangeworks_parameters: str | None = None,
    ):
        if len(solver_str.split(".", 1)) == 2:
            return StrangeworksProviderSolver(
                provider=solver_str.split(".", 1)[0],
                solver=solver_str.split(".", 1)[1],
                solver_type=solver_type,
                solver_options=json.loads(solver_options) if solver_options else None,
                strangeworks_parameters=json.loads(strangeworks_parameters) if strangeworks_parameters else None,
            )
        else:
            raise ValueError("Unprocessable solver string. Solver string must be in the format provider.solver")

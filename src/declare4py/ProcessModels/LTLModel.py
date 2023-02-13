from abc import ABC

from src.declare4py.ProcessModels.AbstractModel import ProcessModel


class LTLModel(ProcessModel, ABC):

    def __init__(self):
        super().__init__()
        self.formula: str = ""
        self.parsed_formula = None

    def parse_from_string(self, content: str, new_line_ctrl: str = "\n"):
        if type(content) is not str:
            raise RuntimeError("You must specify a string as input formula.")
        # Diell, usare il parsing in logaut
        # ma prima devi sostituire i numeri con lettere e mettere tutto in lowercase
        self.formula = content
        self.parsed_formula = None

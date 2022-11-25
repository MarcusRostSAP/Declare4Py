try:
    from future import annotations
except:
    pass

from src.declare4py.core.pm_task import PMTask

"""
Initializes class Discovery, inheriting from class PMTask

Parameters
-------
    PMTask
        inheriting from PMTask
Attributes
-------
    consider_vacuity : bool
        True means that vacuously satisfied traces are considered as satisfied, violated otherwise.
        
    support : float
        the support that a discovered constraint needs to have to be included in the filtered result.

    max_declare_cardinality : int, optional
        the maximum cardinality that the algorithm checks for DECLARE templates supporting it (default 3).
"""


class Discovery(PMTask):

    def __init__(self, log, ltl_model):
        self.consider_vacuity: bool = None
        self.support: str = None
        self.max_declare_cardinality: int = None
        super().__init__(log, ltl_model)


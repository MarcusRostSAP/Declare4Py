from __future__ import annotations

from abc import ABC
from src.declare4py.d4py_event_log import D4PyEventLog
from src.declare4py.ProcessMiningTasks.pm_task import PMTask
from src.declare4py.ProcessModels.ltl_model import LTLModel

"""
Initializes class QueryChecking, inheriting from class PMTask


Attributes
-------
    consider_vacuity : bool
        True means that vacuously satisfied traces are considered as satisfied, violated otherwise.

    template_str : str, optional
        if specified, the query checking is restricted on this DECLARE template. If not, the query checking is
        performed over the whole set of supported templates.

    max_declare_cardinality : int, optional
        the maximum cardinality that the algorithm checks for DECLARE templates supporting it (default 1).

    activation : str, optional
        if specified, the query checking is restricted on this activation activity. If not, the query checking
        considers in turn each activity of the log as activation.

    target : str, optional
        if specified, the query checking is restricted on this target activity. If not, the query checking
        considers in turn each activity of the log as target.

    act_cond : str, optional
        activation condition to evaluate. It has to be written by following the DECLARE standard format.

    trg_cond : str, optional
        target condition to evaluate. It has to be written by following the DECLARE standard format.

    time_cond : str, optional
        time condition to evaluate. It has to be written by following the DECLARE standard format.

    min_support : float, optional
        the minimum support that a constraint needs to have to be included in the result (default 1).
"""


class QueryChecking(PMTask, ABC):

    def __init__(self, consider_vacuity: bool,
                 log: D4PyEventLog, ltl_model: LTLModel):
        super().__init__(log, ltl_model)
        self.consider_vacuity = consider_vacuity


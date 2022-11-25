try:
    from future import annotations
except:
    pass
from .log_utils.ltl_model import LTLModel

from src.declare4py.existence import *
from src.declare4py.choice import *
from src.declare4py.negative_relation import *
from src.declare4py.relation import *


def check_trace_conformance(trace: int, model: LTLModel, consider_vacuity: bool):
    rules = {"vacuous_satisfaction": consider_vacuity}

    # Set containing all constraints that raised SyntaxError in checker functions
    error_constraint_set = set()

    trace_results = {}

    for idx, constraint in enumerate(model.constraints):
        constraint_str = model.serialized_constraints[idx]
        rules["activation"] = constraint['condition'][0]

        if constraint['template'].supports_cardinality:
            rules["n"] = constraint['n']
        if constraint['template'].is_binary:
            rules["correlation"] = constraint['condition'][1]

        rules["time"] = constraint['condition'][-1]  # time condition is always at last position

        try:
            if constraint['template'] is Template.EXISTENCE:
                trace_results[constraint_str] = mp_existence(trace, True, constraint['activities'][0], rules)

            elif constraint['template'] is Template.ABSENCE:
                trace_results[constraint_str] = mp_absence(trace, True, constraint['activities'][0], rules)

            elif constraint['template'] is Template.INIT:
                trace_results[constraint_str] = mp_init(trace, True, constraint['activities'][0], rules)

            elif constraint['template'] is Template.EXACTLY:
                trace_results[constraint_str] = mp_exactly(trace, True, constraint['activities'][0], rules)

            elif constraint['template'] is Template.CHOICE:
                trace_results[constraint_str] = mp_choice(trace, True, constraint['activities'][0],
                                                          constraint['activities'][1], rules)

            elif constraint['template'] is Template.EXCLUSIVE_CHOICE:
                trace_results[constraint_str] = mp_exclusive_choice(trace, True,
                                                                    constraint['activities'][0],
                                                                    constraint['activities'][1], rules)

            elif constraint['template'] is Template.RESPONDED_EXISTENCE:
                trace_results[constraint_str] = mp_responded_existence(trace, True,
                                                                       constraint['activities'][0],
                                                                       constraint['activities'][1], rules)

            elif constraint['template'] is Template.RESPONSE:
                trace_results[constraint_str] = mp_response(trace, True, constraint['activities'][0],
                                                            constraint['activities'][1], rules)

            elif constraint['template'] is Template.ALTERNATE_RESPONSE:
                trace_results[constraint_str] = mp_alternate_response(trace, True,
                                                                      constraint['activities'][0],
                                                                      constraint['activities'][1], rules)

            elif constraint['template'] is Template.CHAIN_RESPONSE:
                trace_results[constraint_str] = mp_chain_response(trace, True,
                                                                  constraint['activities'][0],
                                                                  constraint['activities'][1], rules)

            elif constraint['template'] is Template.PRECEDENCE:
                trace_results[constraint_str] = mp_precedence(trace, True, constraint['activities'][0],
                                                              constraint['activities'][1], rules)

            elif constraint['template'] is Template.ALTERNATE_PRECEDENCE:
                trace_results[constraint_str] = mp_alternate_precedence(trace, True,
                                                                        constraint['activities'][0],
                                                                        constraint['activities'][1], rules)

            elif constraint['template'] is Template.CHAIN_PRECEDENCE:
                trace_results[constraint_str] = mp_chain_precedence(trace, True,
                                                                    constraint['activities'][0],
                                                                    constraint['activities'][1], rules)

            elif constraint['template'] is Template.NOT_RESPONDED_EXISTENCE:
                trace_results[constraint_str] = mp_not_responded_existence(trace, True,
                                                                           constraint['activities'][0],
                                                                           constraint['activities'][1],
                                                                           rules)

            elif constraint['template'] is Template.NOT_RESPONSE:
                trace_results[constraint_str] = mp_not_response(trace, True, constraint['activities'][0],
                                                                constraint['activities'][1], rules)

            elif constraint['template'] is Template.NOT_CHAIN_RESPONSE:
                trace_results[constraint_str] = mp_not_chain_response(trace, True,
                                                                      constraint['activities'][0],
                                                                      constraint['activities'][1], rules)

            elif constraint['template'] is Template.NOT_PRECEDENCE:
                trace_results[constraint_str] = mp_not_precedence(trace, True,
                                                                  constraint['activities'][0],
                                                                  constraint['activities'][1], rules)

            elif constraint['template'] is Template.NOT_CHAIN_PRECEDENCE:
                trace_results[constraint_str] = mp_not_chain_precedence(trace, True,
                                                                        constraint['activities'][0],
                                                                        constraint['activities'][1], rules)

        except SyntaxError:
            if constraint_str not in error_constraint_set:
                error_constraint_set.add(constraint_str)
                print('Condition not properly formatted for constraint "' + constraint_str + '".')

    return trace_results


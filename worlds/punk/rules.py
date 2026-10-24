import json

from rule_builder.rules import *
from .options import PunkOptions

def get_power_rule(power: int, options: PunkOptions)\
        -> Rule:
    if power == 1:
        required_modules = int(options.power1_requirements)
    elif power == 2:
        required_modules = int(options.power2_requirements)
    else:
        required_modules = int(options.power3_requirements)

    return HasGroup("Module", required_modules)

def get_boss_rule(boss_type: str, num: int)\
        -> Rule:
    return Has(f"Completed {boss_type}", num)
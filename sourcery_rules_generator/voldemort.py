from typing import Optional

from sourcery_rules_generator import yaml_converter
from sourcery_rules_generator.models import SourceryCustomRule, PathsConfig


def create_yaml_rules(name_to_avoid: str):

    custom_rules = create_sourcery_custom_rules(name_to_avoid)

    rules_dict = {"rules": [rule.dict(exclude_unset=True) for rule in custom_rules]}
    return yaml_converter.dumps(rules_dict)


def create_sourcery_custom_rules(name_to_avoid: str) -> str:
    description = f"Don't use the name {name_to_avoid}"

    function_name_rule = SourceryCustomRule(
        id=f"no-{name_to_avoid}-function-name",
        description=description,
        tags=["naming", f"no-{name_to_avoid}"],
        pattern="""
def ${function_name}(...):
  ...
""",
        condition=f'function_name.contains("{name_to_avoid}")',
    )

    function_arg_rule = SourceryCustomRule(
        id=f"no-{name_to_avoid}-function-arg",
        description=description,
        tags=["naming", f"no-{name_to_avoid}"],
        pattern="""
def ...(...,${arg_name}: ${type?} = ${default_value?},...):
  ...
""",
        condition=f'arg_name.contains("{name_to_avoid}")',
    )

    class_name_rule = SourceryCustomRule(
        id=f"no-{name_to_avoid}-class-name",
        description=description,
        tags=["naming", f"no-{name_to_avoid}"],
        pattern="""
class ${class_name}(...):
  ...
""",
        condition=f'class_name.contains("{name_to_avoid}")',
    )

    variable_declaration_rule = SourceryCustomRule(
        id=f"no-{name_to_avoid}-property",
        description=description,
        tags=["naming", f"no-{name_to_avoid}"],
        pattern="${var}: ${type}",
        condition=f'var.contains("{name_to_avoid}")',
    )

    variable_assignment_rule = SourceryCustomRule(
        id=f"no-{name_to_avoid}-variable",
        description=description,
        tags=["naming", f"no-{name_to_avoid}"],
        pattern="${var} = ${value}",
        condition=f'var.contains("{name_to_avoid}")',
    )

    return (
        function_name_rule,
        function_arg_rule,
        class_name_rule,
        variable_declaration_rule,
        variable_assignment_rule,
    )

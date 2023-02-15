from sourcery_rules_generator import yaml_converter
from sourcery_rules_generator.models import SourceryCustomRule


def create_yaml_rules(function_name: str):

    custom_rules = create_sourcery_custom_rules(function_name)

    rules_dict = {"rules": [rule.dict(exclude_unset=True) for rule in custom_rules]}
    return yaml_converter.dumps(rules_dict)


def create_sourcery_custom_rules(function_name: str) -> str:
    description = f"Don't call `{function_name}()` in loops."
    function_slug = function_name.replace(".", "-")
    tag = f"no-{function_slug}-in-loops"

    for_rule = SourceryCustomRule(
        id=f"no-{function_slug}-for",
        description=description,
        tags=["performance", tag],
        pattern=f"""
for ... in ... : 
    ...
    {function_name}(...)
    ...
""",
    )
    while_rule = SourceryCustomRule(
        id=f"no-{function_slug}-while",
        description=description,
        tags=["performance", tag],
        pattern=f"""
while ... :
    ...
    {function_name}(...)
    ...
""",
    )

    return (
        for_rule,
        while_rule,
    )

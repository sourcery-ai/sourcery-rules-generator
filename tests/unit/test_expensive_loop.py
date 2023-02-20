from sourcery_rules_generator import expensive_loop
from sourcery_rules_generator.models import SourceryCustomRule


def test_fully_qualified_function_name():
    result = expensive_loop.create_sourcery_custom_rules("custom_lib.api.create_item")

    expected = (
        SourceryCustomRule(
            id="no-custom_lib-api-create_item-for",
            description="Don't call `custom_lib.api.create_item()` in loops.",
            tags=["performance", "no-custom_lib-api-create_item-in-loops"],
            pattern="""
for ... in ... : 
    ...
    custom_lib.api.create_item(...)
    ...
""",
        ),
        SourceryCustomRule(
            id="no-custom_lib-api-create_item-while",
            description="Don't call `custom_lib.api.create_item()` in loops.",
            tags=["performance", "no-custom_lib-api-create_item-in-loops"],
            pattern="""
while ... :
    ...
    custom_lib.api.create_item(...)
    ...
""",
        ),
    )

    assert result == expected

from sourcery_rules_generator import voldemort
from sourcery_rules_generator.models import SourceryCustomRule


def test_do_not_allow_util():
    result = voldemort.create_sourcery_custom_rules("util")

    expected = (
        SourceryCustomRule(
            id="no-util-function-name",
            description="Don't use the name util",
            tags=["naming", "no-util"],
            pattern="""
def ${function_name}(...):
  ...
""",
            condition='function_name.contains("util")',
        ),
        SourceryCustomRule(
            id="no-util-function-arg",
            description="Don't use the name util",
            tags=["naming", "no-util"],
            pattern="""
def ...(...,${arg_name}: ${type?} = ${default_value?},...):
  ...
""",
            condition='arg_name.contains("util")',
        ),
        SourceryCustomRule(
            id="no-util-class-name",
            description="Don't use the name util",
            tags=["naming", "no-util"],
            pattern="""
class ${class_name}(...):
  ...
""",
            condition='class_name.contains("util")',
        ),
        SourceryCustomRule(
            id="no-util-property",
            description="Don't use the name util",
            tags=["naming", "no-util"],
            pattern="${var}: ${type}",
            condition='var.contains("util")',
        ),
        SourceryCustomRule(
            id="no-util-variable",
            description="Don't use the name util",
            tags=["naming", "no-util"],
            pattern="${var} = ${value}",
            condition='var.contains("util")',
        ),
    )

    assert result == expected

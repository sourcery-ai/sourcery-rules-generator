from typer.testing import CliRunner

from sourcery_rules_generator.cli import app

runner = CliRunner()


def test_create_dependency_rule_with_1_importer(yaml_rules_only_api_imports_core):
    result = runner.invoke(
        app, ["create", "--package", "core", "--importer", "api", "--plain"]
    )

    assert result.stdout == yaml_rules_only_api_imports_core

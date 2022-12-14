from typer.testing import CliRunner

from sourcery_rules_generator.cli.cli import app

runner = CliRunner(mix_stderr=False)


def test_create_dependency_rule_with_1_importer(yaml_rules_only_api_imports_core):
    result = runner.invoke(
        app,
        ["dependencies", "create", "--package", "core", "--importer", "api", "--plain"],
    )

    assert result.exit_code == 0
    assert "Generated YAML Rules" in result.stderr
    assert result.stdout == yaml_rules_only_api_imports_core

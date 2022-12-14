from typer.testing import CliRunner

from sourcery_rules_generator.cli.cli import app

runner = CliRunner(mix_stderr=False)


def test_create_dependency_rule_quiet():
    result = runner.invoke(
        app, ["dependencies", "create", "--quiet", "--package", "example"]
    )

    assert result.exit_code == 0
    assert '"Dependencies" Template' not in result.stderr
    assert "Generated YAML Rules" in result.stderr


def test_create_dependency_rule_missing_package():
    result = runner.invoke(app, ["dependencies", "create"])

    assert result.exit_code == 1
    assert "No package provided." in result.stderr

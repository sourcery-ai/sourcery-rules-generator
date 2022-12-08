from typer.testing import CliRunner

from sourcery_rules_generator.cli import app

runner = CliRunner()


def test_start_command():
    result = runner.invoke(app, ["start"])

    assert result.exit_code == 0
    assert result.stdout == "Sourcery Rules Generator started\n"


def test_answer_command(mocker):
    m = mocker.patch(
        "sourcery_rules_generator.sourcery_rules_generator.answer_everything",
        return_value=5,
    )

    result = runner.invoke(app, ["answer"])

    m.assert_called_once()
    assert result.exit_code == 0
    assert result.stdout == "5\n"

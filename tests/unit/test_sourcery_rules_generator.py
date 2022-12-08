from sourcery_rules_generator import sourcery_rules_generator


def test_answer_everything():
    result = sourcery_rules_generator.answer_everything()

    assert result == 42

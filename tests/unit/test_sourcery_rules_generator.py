from sourcery_rules_generator import sourcery_rules_generator


def test_create():
    result = sourcery_rules_generator.create("core", "api")

    assert result.count("id:") == 2

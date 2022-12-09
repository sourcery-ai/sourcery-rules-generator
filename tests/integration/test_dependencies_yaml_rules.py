from sourcery_rules_generator import dependencies


def test_create_yaml_rules():
    result = dependencies.create_yaml_rules("core", "api")

    assert result.count("id:") == 2

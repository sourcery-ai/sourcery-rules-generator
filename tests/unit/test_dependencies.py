from sourcery_rules_generator import dependencies
from sourcery_rules_generator.models import SourceryCustomRule, PathsConfig


def test_1_allowed_importer():
    result = dependencies.create_sourcery_custom_rules("core", "api")

    expected = (
        SourceryCustomRule(
            id="dependency-rules-core-import",
            description="Only `api` should import `core`",
            tags=["architecture", "dependencies"],
            pattern="import ..., ${module}, ...",
            condition='module.matches_regex(r"^core")',
            paths=PathsConfig(exclude=["core/", "tests/", "api/"]),
        ),
        SourceryCustomRule(
            id="dependency-rules-core-from",
            description="Only `api` should import `core`",
            tags=["architecture", "dependencies"],
            pattern="from ${module} import ...",
            condition='module.matches_regex(r"^core")',
            paths=PathsConfig(exclude=["core/", "tests/", "api/"]),
        ),
    )

    assert expected == result


def test_0_allowed_importer():
    result = dependencies.create_sourcery_custom_rules("api", "")

    expected = (
        SourceryCustomRule(
            id="dependency-rules-api-import",
            description="Do not import `api` in other packages",
            tags=["architecture", "dependencies"],
            pattern="import ..., ${module}, ...",
            condition='module.matches_regex(r"^api")',
            paths=PathsConfig(exclude=["api/", "tests/"]),
        ),
        SourceryCustomRule(
            id="dependency-rules-api-from",
            description="Do not import `api` in other packages",
            tags=["architecture", "dependencies"],
            pattern="from ${module} import ...",
            condition='module.matches_regex(r"^api")',
            paths=PathsConfig(exclude=["api/", "tests/"]),
        ),
    )

    assert expected == result

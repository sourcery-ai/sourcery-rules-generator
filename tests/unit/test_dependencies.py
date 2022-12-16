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
            condition='module.matches_regex(r"^core\\b")',
            paths=PathsConfig(exclude=["core/", "tests/", "api/"]),
        ),
        SourceryCustomRule(
            id="dependency-rules-core-from",
            description="Only `api` should import `core`",
            tags=["architecture", "dependencies"],
            pattern="from ${module} import ...",
            condition='module.matches_regex(r"^core\\b")',
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
            condition='module.matches_regex(r"^api\\b")',
            paths=PathsConfig(exclude=["api/", "tests/"]),
        ),
        SourceryCustomRule(
            id="dependency-rules-api-from",
            description="Do not import `api` in other packages",
            tags=["architecture", "dependencies"],
            pattern="from ${module} import ...",
            condition='module.matches_regex(r"^api\\b")',
            paths=PathsConfig(exclude=["api/", "tests/"]),
        ),
    )

    assert expected == result


def test_1_allowed_importer_package_name_incl_dot():
    result = dependencies.create_sourcery_custom_rules("app.core", "app.api")

    expected = (
        SourceryCustomRule(
            id="dependency-rules-app-core-import",
            description="Only `app.api` should import `app.core`",
            tags=["architecture", "dependencies"],
            pattern="import ..., ${module}, ...",
            condition='module.matches_regex(r"^app\.core\\b")',
            paths=PathsConfig(exclude=["app/core/", "tests/", "app/api/"]),
        ),
        SourceryCustomRule(
            id="dependency-rules-app-core-from",
            description="Only `app.api` should import `app.core`",
            tags=["architecture", "dependencies"],
            pattern="from ${module} import ...",
            condition='module.matches_regex(r"^app\.core\\b")',
            paths=PathsConfig(exclude=["app/core/", "tests/", "app/api/"]),
        ),
    )

    assert expected == result


def test_0_allowed_importer_package_name_with_dot():
    result = dependencies.create_sourcery_custom_rules("app.api", "")

    expected = (
        SourceryCustomRule(
            id="dependency-rules-app-api-import",
            description="Do not import `app.api` in other packages",
            tags=["architecture", "dependencies"],
            pattern="import ..., ${module}, ...",
            condition='module.matches_regex(r"^app\.api\\b")',
            paths=PathsConfig(exclude=["app/api/", "tests/"]),
        ),
        SourceryCustomRule(
            id="dependency-rules-app-api-from",
            description="Do not import `app.api` in other packages",
            tags=["architecture", "dependencies"],
            pattern="from ${module} import ...",
            condition='module.matches_regex(r"^app\.api\\b")',
            paths=PathsConfig(exclude=["app/api/", "tests/"]),
        ),
    )

    assert expected == result

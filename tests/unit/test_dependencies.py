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


def test_1_allowed_importer_package_name_incl_dot_and_underscore():
    result = dependencies.create_sourcery_custom_rules("app.view_util", "app.views")

    expected = (
        SourceryCustomRule(
            id="dependency-rules-app-view_util-import",
            description="Only `app.views` should import `app.view_util`",
            tags=["architecture", "dependencies"],
            pattern="import ..., ${module}, ...",
            condition='module.matches_regex(r"^app\.view_util\\b")',
            paths=PathsConfig(exclude=["app/view_util/", "tests/", "app/views/"]),
        ),
        SourceryCustomRule(
            id="dependency-rules-app-view_util-from",
            description="Only `app.views` should import `app.view_util`",
            tags=["architecture", "dependencies"],
            pattern="from ${module} import ...",
            condition='module.matches_regex(r"^app\.view_util\\b")',
            paths=PathsConfig(exclude=["app/view_util/", "tests/", "app/views/"]),
        ),
    )

    assert expected == result


def test_2_allowed_importers_package_name_incl_dot():
    result = dependencies.create_sourcery_custom_rules("app.util", "app.core,app.other")

    expected = (
        SourceryCustomRule(
            id="dependency-rules-app-util-import",
            description="Only `app.core`, `app.other` should import `app.util`",
            tags=["architecture", "dependencies"],
            pattern="import ..., ${module}, ...",
            condition='module.matches_regex(r"^app\.util\\b")',
            paths=PathsConfig(
                exclude=["app/util/", "tests/", "app/core/", "app/other/"]
            ),
        ),
        SourceryCustomRule(
            id="dependency-rules-app-util-from",
            description="Only `app.core`, `app.other` should import `app.util`",
            tags=["architecture", "dependencies"],
            pattern="from ${module} import ...",
            condition='module.matches_regex(r"^app\.util\\b")',
            paths=PathsConfig(
                exclude=["app/util/", "tests/", "app/core/", "app/other/"]
            ),
        ),
    )

    assert expected == result

from typing import Optional

from sourcery_rules_generator import yaml_converter
from sourcery_rules_generator.models import SourceryCustomRule, PathsConfig


def create_yaml_rules(package: str, allowed_importer: Optional[str]) -> str:

    custom_rules = create_sourcery_custom_rules(package, allowed_importer)

    rules_dict = {"rules": [rule.dict(exclude_unset=True) for rule in custom_rules]}
    return yaml_converter.dumps(rules_dict)


def create_sourcery_custom_rules(
    package: str, allowed_importer_text: Optional[str]
) -> str:
    # Dots aren't allowed in the rule ID.
    package_slug = package.replace(".", "-")

    # The dot in the package's fully qualified name
    # needs to be escaped in the regex used for the condition.
    package_in_regex = package.replace(".", "\.")

    exclude_paths = [_path_for_package(package), "tests/"]

    if allowed_importer_text:
        if "," in allowed_importer_text:
            allowed_importers = allowed_importer_text.split(",")
            description = _description_for_multiple_importers(
                package, allowed_importers
            )
            exclude_paths.extend(_path_for_package(impo) for impo in allowed_importers)
        else:
            description = _description_for_1_importer(package, allowed_importer_text)
            exclude_paths.append(_path_for_package(allowed_importer_text))
    else:
        description = _description_for_0_importer(package)

    import_rule = SourceryCustomRule(
        id=f"dependency-rules-{package_slug}-import",
        description=description,
        tags=["architecture", "dependencies"],
        pattern="import ..., ${module}, ...",
        condition=f'module.matches_regex(r"^{package_in_regex}\\b")',
        paths=PathsConfig(exclude=exclude_paths),
    )

    from_rule = SourceryCustomRule(
        id=f"dependency-rules-{package_slug}-from",
        description=description,
        tags=["architecture", "dependencies"],
        pattern="from ${module} import ...",
        condition=f'module.matches_regex(r"^{package_in_regex}\\b")',
        paths=PathsConfig(exclude=exclude_paths),
    )

    return (import_rule, from_rule)


def _description_for_0_importer(package: str):
    return f"Do not import `{package}` in other packages"


def _description_for_1_importer(package: str, allowed_importer: str):
    return f"Only `{allowed_importer}` should import `{package}`"


def _description_for_multiple_importers(package: str, allowed_importers: list[str]):
    quoted = [f"`{impo}`" for impo in allowed_importers]
    return f"Only {', '.join(quoted)} should import `{package}`"


def _path_for_package(package: str) -> str:
    return package.replace(".", "/") + "/"

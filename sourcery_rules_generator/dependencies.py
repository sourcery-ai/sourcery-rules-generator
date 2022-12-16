from typing import Optional

from sourcery_rules_generator import yaml_converter
from sourcery_rules_generator.models import SourceryCustomRule, PathsConfig


def create_yaml_rules(package: str, allowed_importer: Optional[str]) -> str:

    custom_rules = create_sourcery_custom_rules(package, allowed_importer)

    rules_dict = {"rules": [rule.dict(exclude_unset=True) for rule in custom_rules]}
    return yaml_converter.dumps(rules_dict)


def create_sourcery_custom_rules(package: str, allowed_importer: Optional[str]) -> str:
    # Dots aren't allowed in the rule ID.
    package_slug = package.replace(".", "-")

    package_in_regex = package.replace(".", "\.")
    package_path = package.replace(".", "/")

    exclude_paths = [f"{package_path}/", "tests/"]
    description = f"Do not import `{package}` in other packages"
    if allowed_importer:
        description = f"Only `{allowed_importer}` should import `{package}`"
        allowed_importer_path = allowed_importer.replace(".", "/")
        exclude_paths.append(f"{allowed_importer_path}/")

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

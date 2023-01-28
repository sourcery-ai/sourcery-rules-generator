# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.5.0] - 2023-01-29

* Dependencies rules: Allow multiple importer packages

### Added

## [0.4.0] - 2023-01-05

### Added

* "voldemort" rule template and command: names to avoid in your code

## [0.3.3] - 2022-12-21

### Added

* Tests with tox [GH-1](https://github.com/sourcery-ai/sourcery-rules-generator/issues/1)
* Support Python 3.9 [GH-2](https://github.com/sourcery-ai/sourcery-rules-generator/issues/2)
 
## [0.3.2] - 2022-12-16

### Fixed

* Dependencies rules: Detect only the package and its subpackages. Don't detect imports that are only a text match. [GH-10](https://github.com/sourcery-ai/sourcery-rules-generator/issues/10)

## [0.3.1] - 2022-12-15

### Added

* README: Dependencies use cases

## [0.3.0] - 2022-12-14

### Added

* `dependencies create` command: More detailed explanation of the "Dependencies" template.
* `dependencies create` command: `--quiet` option

## [0.2.1] - 2022-12-14

### Fixed

* Support fully qualified package names incl. dot [GH-7](https://github.com/sourcery-ai/sourcery-rules-generator/issues/7) 

## [0.2.0] - 2022-12-13

### Added

* Prepare for public release: README, project metadata

## [0.1.0] - 2022-12-08

### Added

* Command to generate dependencies rules
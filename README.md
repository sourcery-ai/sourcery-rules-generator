# Sourcery Rules Generator 

**This is an experimental project. It might become a part of the [Sourcery CLI](https://docs.sourcery.ai/Overview/Products/Command-Line/).**

Sourcery Rules Generator creates architecture rules for your project.

The generated rules can be used by Sourcery to review your project's architecture.

Currently, the project can create dependency rules.

## Usage

You can create Sourcery rules based on a template with the command:

```
sourcery-rules <TEMPLATE-NAME> create
```

Supported templates:

* dependencies
* naming (coming soon)

For example:

```
sourcery-rules dependencies create
```

![gif sourcery-rules dependencies create](https://raw.githubusercontent.com/sourcery-ai/sourcery-rules-generator/main/sourcery-rules_dependencies_create.gif)

### Create Dependencies Rules

With the dependencies template, you can create rules to check the dependencies:

* between the packages of your application
* to external packages.

Let's say your project has an architecture like this:

![dependencies overview](https://raw.githubusercontent.com/sourcery-ai/sourcery-rules-generator/main/dependencies.png)

You can create rules to ensure:

* no other package imports `api`
* only `api` imports `core`
* only `db` import `SQLAlchemy`
* etc.

Run the command:

```
sourcery-rules dependencies create
```

You'll be prompted to provide:

* a package name
* the packages that are allowed to import the package above

The 2nd parameter is optional.  
E.g. it makes sense to say that no other package should import the `api` or `cli` package of your project.

=>

2 rules will be generated:

* 1 for `import` statements
* 1 for `from ... import` statements


### Using the Generated Rules

The generated rules can be used by Sourcery to review your project.
If you copy the generated rules into your project's `.sourcery.yaml`, Sourcery will use them automatically.

All the generated rules have the tag `architecture`. Once you've copied them to your `.sourcery.yaml`, you can run them with:

```
sourcery review --enable architecture .
```
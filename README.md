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

* [dependencies](#create-dependencies-rules)
* [naming / voldemort](#create-voldemort-rules): avoid some names
* naming / name vs type mismatch (coming soon)

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

The 1st parameter is the fully qualified name of a package or module.  
It can be a package within your project or an external dependency.

The 2nd parameter is optional.  
You have the following possibilities:

* 0 allowed importer (e.g. for packages like `api`, `cli`). Leave this parameter empty.
* 1 allowed importer. Provide the importer package's fully qualified name.
* Multiple allowed importers. Provide multiple fully qualified package names separated by a comma `,`

=>

2 rules will be generated:

* 1 for `import` statements
* 1 for `from ... import` statements

Every generated rule allows imports:

* within the package itself
* in tests

## Dependencies Use Cases

### Internal Dependencies Between the Packages of a Project

* [Law of Demeter](https://en.wikipedia.org/wiki/Law_of_Demeter): Packages should talk only to their "direct neighbors".
* A mature package shouldn't depend on a less mature package
* A core package shouldn't depend on a customer-specific package

Thanks to [w_t_payne](https://news.ycombinator.com/user?id=w_t_payne) and [hbrn](https://news.ycombinator.com/user?id=hbrn) for their input in this [HackerNews discussion](https://news.ycombinator.com/item?id=33999191#34001608) 😃

### External Dependencies

* [Gateway pattern](https://martinfowler.com/articles/gateway-pattern.html): Ensure that only a dedicated package of your software communicates with an external dependency.
* Ensure that a deprecated library isn't used

This [blog post](https://sourcery.ai/blog/dependency-rules/) shows a 3-step method of defining dependency rules:

1. Draw a diagram showing the optimal dependencies between your packages.
2. Phrase some rules in a human language based on the diagram: Which package should depend on which?
3. Translate the rules into code with Sourcery Rules Generator.

## Create Voldemort Rules

With a "voldemort" template, you can create rules that ensure that a specific name isn't used in your code.

For example:

* The word `annual` shouldn't be used, because the preferred term is `yearly`.
* The word `util` shouldn't be used, because it's overly general.

You can create a "voldemort" rule with the command:

```
sourcery-rules voldemort create
```

![screenshot sourcery-rules voldemort create](https://raw.githubusercontent.com/sourcery-ai/sourcery-rules-generator/main/voldemort_create.png)

You'll be prompted to provide:

* the name that you want to avoid

=>

5 rules will be generated:

* function names
* function arguments
* class names
* variable declarations
* variable assignments

## Using the Generated Rules

The generated rules can be used by Sourcery to review your project.
If you copy the generated rules into your project's `.sourcery.yaml`, Sourcery will use them automatically.

All the generated rules have the tag `architecture`. Once you've copied them to your `.sourcery.yaml`, you can run them with:

```
sourcery review --enable architecture .
```
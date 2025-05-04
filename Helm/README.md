# Helm

A helm Chart involves 3 basics:

1. The `Chart.yaml` - declared metadata about the chart like name and version and its dependencies
2. The `values.yaml` - defines values to use in the template
3. The `templates/` directory - The files containing the templates that are based on the values
4. The `tests/` directory - Contains test suite files for running unit-tests

## Running

To check the chart - run this:

```shell
cd chart && helm template .
```

This will show the generated configuration based on the template and values.

The example here is not a valid Kubernetes configuration so you can template it but cannot install it on an actual Kubernetes cluster.

## Testing

The easiest way to test a template is using [helm unittest](https://github.com/helm-unittest/helm-unittest).

There is a simple docker image for using it available [here](https://hub.docker.com/r/helmunittest/helm-unittest).

To run the tests, simply run:

```shell
make test
```

To run tests in a loop during a development - use this command:

```shell
make test-watch
```

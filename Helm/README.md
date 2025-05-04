# Helm

A helm Chart involves 3 basics:

1. The `Chart.yaml` - declared metadata about the chart like name and version and its dependencies
2. The `values.yaml` - defines values to use in the template
3. The `templates/` directory - The files containing the templates that are based on the values

## Running

To check the chart - run this:

```shell
cd chart
helm template .
```

This will show the generated configuration based on the template and values.

The example here is not a valid Kubernetes configuration so you can template it but cannot install it on an actual Kubernetes cluster.

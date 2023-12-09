# Pipenv

## 1. Creating a new virutal environment

```bash
pipenv shell
```

## 2. Installing Packages

This updates the `Pipfile` and `Pipfile.lock` files.

### 2.1. Prod + Dev Packages

```bash
pipenv install <package-name>
```

### 2.2. Dev ONLY Packages

```bash
pipenv install -d <package-name>
```

## 3. Exiting a virtual environment

```bash
deactivate
```

## 4. Opening a virutal environment

```bash
pipenv shell
```

## 5. Running a command in the virtual environment from the outside

```bash
pipenv run <command to run in the virtual env>
```

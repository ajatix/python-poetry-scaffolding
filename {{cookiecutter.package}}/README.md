# {{cookiecutter.package}}

## Development

- Initialize venv with required python version
- Run `make` to setup the project for the first time

### Makefile commands

| command       | comments                                                 | 
| ------------- | -------------------------------------------------------- |
| update        | install dependencies defined in pyproject.toml           |
| requirements  | generate requirements.txt for publishing package         |
| build         | generate sdist package                                   |
| install       | publishes the package to venv to allow testing           |
| test          | runs pytests on package                                  |
| notebook      | starts jupyter notebook server with package dependencies |

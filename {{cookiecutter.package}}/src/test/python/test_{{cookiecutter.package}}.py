from {{cookiecutter.package}} import __version__, __python_version__


def test_{{cookiecutter.package}}():
    assert __version__ == '{{cookiecutter.version}}'
    assert __python_version__ == '{{cookiecutter.python_version}}'
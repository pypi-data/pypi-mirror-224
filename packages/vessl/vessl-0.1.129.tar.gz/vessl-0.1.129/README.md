# `vessl-python-sdk`

## Basic usage

```python
import vessl

vessl.init(organization_name="my-organization")
vessl.create_experiment(...)
```

## Keras

- Use ExperimentCallback

```python
import vessl
from vessl.integration.keras import ExperimentCallback

vessl.init()

# Keras training code
model = Model()
model.compile(...)

# Add integration
model.fit(x, y, epochs=5, callbacks=[ExperimentCallback()])
```

- Run experiment on Vessl using Web UI or SDK

## For M1

```bash
docker context create remote --docker "host=ssh://ec2-user@10.110.3.24"
docker context use remote
docker build . -t vessl-python-sdk
docker run vessl-python-sdk
```

# Development Setting

## Poetry

### Install poetry

[Documentation](https://python-poetry.org/docs/#installation)

### Add & Install new package

Write Package and it's version to pyproject.toml

```
poetry lock
poetry install
```

### Enter the virtual environment

```
poetry shell
```

### Set python version environment

1. Install each python distribution package to your local environment (you can use [pyenv](https://github.com/pyenv/pyenv))
1. [Follow instructions](https://python-poetry.org/docs/managing-environments/#switching-between-environments)

## For faster development

### `VESSL_ENV` constant

`VESSL_ENV` envvar is default set to `prod`.

You can override this with `dev` by setting envvar `VESSL_ENV=dev`

If you set `VESSL_ENV` to `dev`, it automatically sets `WEB_HOST` and `API_HOST` to dev server.

- `WEB_HOST`: `https://dev.vssl.ai`
- `API_HOST`: `https://api.dev.vssl.ai`

It also switches off the sentry configuration on `vessl/cli/_main.py:L55`.

But also, you can override these automatically set variables(`WEB_HOST`, `API_HOST`, etc..) with `.env` file.

### `.env` file

You can use `.env` file to set environment variables for your development.

You should put `.env` file on the root of this project.

See [python-dotenv](https://github.com/theskumar/python-dotenv).

e.g.

```bash
ENABLE_SENTRY=false             # disables sentry configuration, added in order to disable while VESSL_ENV=dev
VESSL_ENV=dev                   # this automatically sets dev api
VESSL_LOG=DEBUG                 # you don't have to pass it through shell command
# API_HOST=http://localhost     # Set freely when attaching to local devenv
# WEB_HOST=http://localhost
```

### Set alias for local CLI run

You can run your local code as cli with `python -m vessl.cli._main`.

But for convienience, you can set alias for that and put in your .zshrc or .bashrc

e.g.

```sh
alias vessldev="python -m vessl.cli._main"
```

### Disable sentry for local development

Set envvar `ENABLE_SENTRY=false` on your shell or on `.env`.

### (TEMPORARY GUIDE) How to update dependencies?

_will be resolved in [PR#210](https://github.com/vessl-ai/vessl-python-sdk/pull/210)_

1. pyproject.toml 업데이트를 한 후,

- `poetry export --with dev --without-hashes > requirements.txt`로 requirements.txt 업데이트

- `poetry export --only test --without-hashes > requirements_test.txt`로 업데이트

2. setup.py에도 업데이트

- 이쪽 의존성은 pyproject.toml쪽 내용이랑 다르기 때문에(ㅠㅠㅠ) 적당히 눈치 보면서 업데이트

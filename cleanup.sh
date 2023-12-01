#!/bin/bash

poetry run black .
poetry run isort .
poetry run ruff check .
poetry run pyright .
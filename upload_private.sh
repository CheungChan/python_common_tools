#!/usr/bin/env bash

rm -rf dist/*
python setup.py sdist
twine upload dist/* -r privatepypi

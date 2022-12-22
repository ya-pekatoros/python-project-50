# Tests and linter status:
[![Actions Status](https://github.com/ya-pekatoros/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/ya-pekatoros/python-project-50/actions)
[![Python CI](https://github.com/ya-pekatoros/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/ya-pekatoros/python-project-50/actions/workflows/pyci.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/24e1c9e1a3d7156eb81c/maintainability)](https://codeclimate.com/github/ya-pekatoros/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/24e1c9e1a3d7156eb81c/test_coverage)](https://codeclimate.com/github/ya-pekatoros/python-project-50/test_coverage)

# Description

Hello!

This package consists second project.

# Requirenments

* Linux OS
* python = "^3.10"
* pip "22.3.1"

# Installation

### You can use pip and install package from git:

    pip install --user git+https://github.com/ya-pekatoros/python-project-50

### Or you can clone rep and use poetry (python package management tool). Some shortcats to do it:

    git clone https://github.com/ya-pekatoros/python-project-50.git
    cd python-project-50
    make install
    make build
    package-install

# Commands and demonstrations

gendiff file-1-path file-2-path
    gendiff --h

[![asciicast](https://asciinema.org/a/nwp85W7BFsW8ybmsRJZCXibrt.svg)](https://asciinema.org/a/nwp85W7BFsW8ybmsRJZCXibrt)

It works with two file formats: JASIN (file.json) and YAML( file.yml or file.yaml)

There are two formats of output: stylish, plain and json (generate JSON file with results). Below you can find some demonstations of how it looks like. You can chose the format using '-f' or '--format' and writing 'stylish' of 'plain' after it. The default format is 'stylish' (if you don't write any of format)

### Stylish format

###### Demonstration of works with flat JSON files:

[![asciicast](https://asciinema.org/a/mIKPz61JM2dsScTsPyr8GEK7p.svg)](https://asciinema.org/a/mIKPz61JM2dsScTsPyr8GEK7p)

###### Demonstration of works with flat YAML files:

[![asciicast](https://asciinema.org/a/MRS0b80RK5t1NL0k5DQtPNAgJ.svg)](https://asciinema.org/a/MRS0b80RK5t1NL0k5DQtPNAgJ)

###### Demonstration of works with nested JSON files:

[![asciicast](https://asciinema.org/a/XgyKOJQAjMYkA6brZF4q2e7eM.svg)](https://asciinema.org/a/XgyKOJQAjMYkA6brZF4q2e7eM)

###### Demonstration of works with nested YAML files:

[![asciicast](https://asciinema.org/a/7P9asGZj8flZVKLfib7Xx5cgw.svg)](https://asciinema.org/a/7P9asGZj8flZVKLfib7Xx5cgw)

### Plain format

###### Demonstration of works with nested JSON files:

[![asciicast](https://asciinema.org/a/kTjeMUJ2vP4PuO42I7EFoIII4.svg)](https://asciinema.org/a/kTjeMUJ2vP4PuO42I7EFoIII4)

### JSON format

###### Demonstration of works with nested JSON files:

[![asciicast](https://asciinema.org/a/4ysoHgXxFUzgIW8bC6imGLr2o.svg)](https://asciinema.org/a/4ysoHgXxFUzgIW8bC6imGLr2o)
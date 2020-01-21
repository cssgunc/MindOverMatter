# MindOverMatter

# Installation

1. Install [Python 3](https://www.python.org/downloads/)
2. Install [VSCode](https://code.visualstudio.com/Download)
3. `. venv/bin/activate`
4. `pip install -r requirements.txt`

# Resources

Installation: https://flask.palletsprojects.com/en/1.1.x/installation/#installation
Quickstart: https://flask.palletsprojects.com/en/1.1.x/quickstart/

## Running

`. venv/bin/activate`
`export FLASK_APP=app.py`
`export FLASK_ENV=development`
`flask run`

## Logging

`app.logger.debug('A value for debugging')`
`app.logger.warning('A warning occurred (%d apples)', 42)`
`app.logger.error('An error occurred')`

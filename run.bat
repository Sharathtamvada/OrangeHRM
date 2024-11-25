coverage erase
coverage run -m pytest --junitxml=junit-{envname}.xml
coverage report
coverage xml -i -o coverage-{envname}.xml

init:
    pip install -r requirements.txt

generate:
    pip3 freeze > requirements.txt

test:
    pytest

.PHONY: init generate test

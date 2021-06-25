.PHONY: setup
setup: virtualenv -p python3 venv && source venv/bin/activate && pip3 install pytest

.PHONY: test
test: setup
      pytest



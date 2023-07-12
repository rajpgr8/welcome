.PHONY: setup
setup: 
	python -m venv . && . ./venv/bin/activate && pip3 install pytest
	
.PHONY: test
test: setup
	pytest

.PHONY: run
run: setup
	docker-compose up




RUN=uvicorn app.main:app --reload

.PHONY: all setup run


setup:
	uv venv && source .venv/bin/activate && uv sync

all: setup

run:
	$(RUN)

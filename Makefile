.PHONY: run help

help:
	@echo "make run2025-<day>    # runs the code for the 2025 AoC Day <day>"

run2025:
	@echo "Please specify the day in a %dd format, e.g. make run2025-03"

run2025-%:
	python3 -m 2025.$*

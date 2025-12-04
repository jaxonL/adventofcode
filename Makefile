.PHONY: run help

YEAR=25

help:
	@echo "make run-<day>        # runs the code for the latest AoC Day <day>"
	@echo "make run2025-<day>    # runs the code for the 2025 AoC Day <day>"

run:
	@echo "Please specify the day in a %dd format, e.g.: make run-03"
	@echo "To specify the year, use the YEAR=YY parameter, e.g.: make run-10 YEAR=18"

run-%:
	python3 -m 20$(YEAR).$*

run2025:
	@echo "Please specify the day in a %dd format, e.g.: make run2025-03"

run2025-%:
	python3 -m 2025.$*

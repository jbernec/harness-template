.PHONY: help test lint format memory-status

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# --- Quality ---
test: ## Run harness invariant tests + your project tests
	python3 -m pytest tests/ -q
	@echo "TODO: Add your project's test command (e.g., uv run pytest)"

memory-status: ## Show memory size and whether a dream (curation) is due
	@python3 scripts/memory_status.py

lint: ## Lint code
	@echo "TODO: Add your lint command (e.g., uv run ruff check .)"

format: ## Format code
	@echo "TODO: Add your format command (e.g., uv run ruff format .)"

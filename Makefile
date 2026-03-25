.PHONY: help test lint format

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# --- Quality ---
test: ## Run test suite
	@echo "TODO: Add your test command (e.g., uv run pytest)"

lint: ## Lint code
	@echo "TODO: Add your lint command (e.g., uv run ruff check .)"

format: ## Format code
	@echo "TODO: Add your format command (e.g., uv run ruff format .)"

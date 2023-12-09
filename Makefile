help: # show command description
	@cat Makefile | sed '/^$$/d' | sed '/^\t/d' | sed '/:=/d' | sed '/^_/d' | sed 's/:.*#/\t/g' | expand -t 25

install:
	@rye sync

jira_token:
	@rye run python tools/gen_jira_token.py

run:
	@rye run python src/main.py | expand -t 50

format: # [develop] format
	@rye run black .
	@rye run ruff check . --fix --show-fixes

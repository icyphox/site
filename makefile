build:
	@vite build

serve:
	@./bin/serve.sh

ci:
	@./bin/build.sh

.PHONY: build serve ci

build:
	@vite build

serve:
	@./bin/serve.sh

ci:
	@./bin/build.sh

deploy:
	aws s3 sync build s3://site/

.PHONY: build serve ci

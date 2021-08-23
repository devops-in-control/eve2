cwd := $(shell pwd)
datetime := $(shell date +"%Y%m%dT%H%M%S")
report_dir := $(cwd)/e2e/reports/$(datetime)
tests_dir := $(cwd)/e2e


test-unit:
	python3 manage.py test

test-e2e:
	mkdir -p $(report_dir)
	Xvfb :69 -screen 0 1024x768x24 &
	export DISPLAY=:69; \
	cd $(report_dir); \
	robot $(tests_dir)/*.robot
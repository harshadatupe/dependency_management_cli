PACKAGE_NAME = deps-manager

.PHONY: all clean build publish

all: build

clean:
	rm -rf dist build *.egg-info

build:
	python3 setup.py sdist bdist_wheel

publish: build
	twine upload dist/*
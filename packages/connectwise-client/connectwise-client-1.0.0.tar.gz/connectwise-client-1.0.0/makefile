# Type:
#    `make help` 
# for a list of all commands and what they do.


# ************************************************************************************
# ********************* Set the variables used in this make file *********************
# ********** Use: `make test-variables` to see them **********************************
# ************************************************************************************
# Identify OS
LOCAL_OS := unknown
ifeq ($(OS),Windows_NT) # Windows
	LOCAL_OS := Windows_NT
endif
ifeq ($(shell uname -s),Darwin) # Mac
	LOCAL_OS := Darwin
endif
ifeq ($(shell uname -s),Linux) # Linux
	LOCAL_OS := Linux
endif

# Base or Root Directory Setup
BASEDIR := .

# Cache Directories
PROJ_CACHE_HOME := $(BASEDIR)/.cache
MYPY_CACHE_DIR := $(PROJ_CACHE_HOME)/.mypy_cache
PYTEST_CACHE_DIR := $(PROJ_CACHE_HOME)/.pytest_cache

# Virtual Folder
VENV := $(BASEDIR)/venv

# Requirements directory and files
REQUIREMENTS_BASEDIR := $(BASEDIR)/requirements
REQUIREMENTS_INPUT := $(wildcard $(REQUIREMENTS_BASEDIR)/*.in)

# Versions
PYTHON_VERSION := $(shell cat .python-version)
APP_VERSION := $(shell git describe --tags --abbrev=0 | sed -Ee 's/^v|-.*//')
VERMAJMIN      := $(subst ., ,$(APP_VERSION))
VERSION        := $(word 1,$(VERMAJMIN))
MAJOR          := $(word 2,$(VERMAJMIN))
MINOR          := $(word 3,$(VERMAJMIN))
NEW_MINOR      := $(shell expr "$(MINOR)" + 1)
NEXT_APP_VERSION := $(VERSION).$(MAJOR).$(NEW_MINOR)


DOCKER_PYTHON_VERSION := $(shell cat .python-version | cut -d"." -f1,2)

# Python Installation Commands
INSTALL_PY_ENV_COMMAND := pyenv install $(PYTHON_VERSION) --skip-existing
ACTIVATE_PY_ENV_COMMAND := pyenv local

# Bin Setup (This will be different for Windows, Mac, and Unix)
ifeq ($(LOCAL_OS),Windows_NT)
	BIN :=$(VENV)/Scripts
endif
ifeq ($(LOCAL_OS),Darwin)
	BIN :=$(VENV)/bin
endif
ifeq ($(LOCAL_OS),Linux)
	BIN :=$(VENV)/bin
endif

# Get Local Machine Name
LOCALHOST := $$($(BIN)/python -c "import socket; s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM); s.connect(('8.8.8.8', 80)); print(s.getsockname()[0]);")

# Package information
PACKAGE_NAME := $$($(BIN)/python -c "import toml; config_dict = toml.load(open('pyproject.toml')); print(config_dict['project']['name'].replace('-', '_'));")
DOCKER_PACKAGE_NAME := $$($(BIN)/python -c "import toml; config_dict = toml.load(open('pyproject.toml')); print(config_dict['project']['name'].replace('_', '-'));")
# Command to figure out the version of each pypi package.
PIP_COMPILE := $(BIN)/python -m piptools compile -q --no-header --allow-unsafe --resolver=backtracking --no-emit-index-url

# Command to get local dev version for the wheel
SCM_VERSION := $$($(BIN)/python -m setuptools_scm)

# **************************************************************************************************************************
# **** NOTE:
#     Targets 
#        If they are preceeded by .PHONY then you can call the target with the syntax:
#           make <target>
#        If target name followed with a double hash (##), then any text after the double hash is for the `make help` output.
# **************************************************************************************************************************

.PHONY: build 
build: install-python clean localenv install-deps full  ## ** Required ** | Setup a new environment after cloning the repo. (Performs `full` target) 

.PHONY: rebuild 
rebuild: install-python clean localenv update-deps full ## Rebuild the current environment including updating dependencies. (Performs `full` target)

.PHONY: full
full: check_code_quality test ## Perform a code quality, build the wheel, and build and refresh docker container

.PHONY: check_code_quality 
check_code_quality: black pylint mypy pydocstyle test ## Check the code quality before checkin (black, pylint, mypy, pydocstyle, and test)

# Install pyenv
.PHONY: install-python
install-python: ## Install the python version indicated by .python-version
	@echo Install Python Version: $(PYTHON_VERSION)
	$(INSTALL_PY_ENV_COMMAND)
	@echo Activate Python Version: $(PYTHON_VERSION)
	$(ACTIVATE_PY_ENV_COMMAND)

.PHONY: clean 
clean: ## Clean up local environment.
	@echo "Clean up old environment"
	rm -rf "$(VENV)"
	rm -rf "$(PROJ_CACHE_HOME)"
	rm -rf "$(BASEDIR)/build"
	rm -rf "$(BASEDIR)/cov_html"
	# Remove all pycache
	find . | grep '__pycache__' | xargs rm -rf
	# Remove egg-info
	find . -type d | grep '.egg-info' | xargs rm -rf

.PHONY: format_code
format_code: ## Run actually reformat the files using black.
	@echo "-------- Format Code with Black --------- "
	@$(BIN)/python -m black --version
	@$(BIN)/python -m black .

.PHONY: black
black: ## Perform Black formatter check and show diff.
	@echo "-------- Running Black --------- "
	@$(BIN)/python -m black --version
	@$(BIN)/python -m black --check --diff .

.PHONY: mypy
mypy: ## Perform MyPy.
	@echo "-------- Running mypy --------- "
	@$(BIN)/python -m mypy --version
	@$(BIN)/python -m mypy .

.PHONY: pylint
pylint: ## Perform PyLint.
	@echo "-------- Running pylint --------- "
	@$(BIN)/python -m pylint --version
	@$(BIN)/python -m pylint .

.PHONY: pydocstyle
pydocstyle: ## Perform PyDocStyle.
	@echo "-------- Running pydocstyle --------- "
	@$(BIN)/python -m pydocstyle --version
	@$(BIN)/python -m pydocstyle --verbose .

.PHONY: test
test: ## Run PyTest.
	@echo "-------- Running tests --------- "
	rm -rf "$(BASEDIR)/cov_html"
	$(BIN)/python -m pytest --version
	$(BIN)/python -m pytest .

.PHONY: deploy
deploy: update-app-version pypack ## Deploy package to pypi.org

.PHONY: pypack
pypack: ## Build the wheel
	@echo "-------- Python Package (sdist and wheel) --------- "
	@rm -rf "$(BASEDIR)/dist"
	@. "$(BIN)/activate"; \
	update-toml --path project.requires-python --value ">=${DOCKER_PYTHON_VERSION}" pyproject.toml;
	$(BIN)/python -m pip install --upgrade build
	$(BIN)/python -m build --skip-dependency-check

.PHONY: to_pypi_org
to_pypi_org: ## Upload to pypi.org
	$(BIN)/python -m pip install twine
	$(BIN)/python -m twine upload --verbose --repository pypi dist/* 

.PHONY: scm-version
scm-version: ## Version that will be released.
	@echo "Version we expect to deploy"
	@echo "$(SCM_VERSION)"

.PHONY: update-app-version	
update-app-version: ## Update the build version of the app.
	@echo "Update the build version of the app."
	@echo "Current Version: $(APP_VERSION)"
	@echo "Next Version: $(NEXT_APP_VERSION)"
	$(shell git tag v$(NEXT_APP_VERSION))
	

# ---------- Environment management targets ----------
# ************************************************************************************
# ********************* Build the venv and install basic packages ********************
# ************************************************************************************
# Creates or updates a virtual ennviroment with base tools
localenv:
	@echo "-------- Set up basic virtual environment --------"
	python -m venv $(VENV)
	$(BIN)/python -m pip install pip pip-tools keyring --upgrade

# ************************************************************************************
# ********************* Dependency Stuff *********************************************
# ************************************************************************************

# Installs dependencies from txt files into venv
.PHONY: install-deps
install-deps: ## Install the dependencies
	@echo "-------- Install dependencies into virtual environment --------"
	$(BIN)/python -m pip install '.[development]' 
	$(BIN)/python -m pip install -e . 

# Forces all requirements .txt files to be rebuilt from scratch and installed into the venv.
# venv will be created if it doesn't exist. A basic venv is needed to make sure we have updated versions
# of core tooling installed, like pip and pip-tools.
.PHONY: update-deps
update-deps: clean-deps resolve-all-deps install-deps ## Perform clean the requirements dir, resolve the deps, and install them.

# Rebuild the constraints file from all *.in files in the Requirements dir
# $@ is target name, @^ is the prerequisites (the *.in files).
$(REQUIREMENTS_BASEDIR)/constraints.txt: $(REQUIREMENTS_INPUT)
	@echo "-------- Rebuild the constraints file from *.in files --------"
	CONSTRAINTS=/dev/null $(PIP_COMPILE) --strip-extras -o $@ $^

# Rebuild the requirements files from all *.in files in the Requirements dir, taking constraints into account
# $@ is target name, @< is the first prerequisite (the *.in files).
# For each *.in file, create an additional *.in-no-args file that doesn't include any arguments (-c).
# This is used to include softer-pinned dependencies in pyproject.toml (only for libraries).
$(REQUIREMENTS_BASEDIR)/%.txt: $(REQUIREMENTS_BASEDIR)/%.in $(REQUIREMENTS_BASEDIR)/constraints.txt
	@echo "-------- Resolve dependencies across all files, incorporating layered constraints --------"
	CONSTRAINTS=constraints.txt $(PIP_COMPILE) --no-annotate -o $@ $<
	@grep -v -E '^-.*' $< > $(addsuffix .in-no-args, $(basename $<))

.PHONY: clean-deps
clean-deps: ## Remove the deps from requirements dir. Leave the *.in files.
	@echo "-------- Clean dependency directory --------"
	rm -rf $(REQUIREMENTS_BASEDIR)/constraints.txt $(REQUIREMENTS_INPUT:in=txt) $(REQUIREMENTS_INPUT:in=in-no-args)

# Alias to collect all .txt files, including constraints
resolve-all-deps: $(REQUIREMENTS_BASEDIR)/constraints.txt $(REQUIREMENTS_INPUT:in=txt)


# ************************************************************************************
# ********************* Show all the variables used in this make file ****************
# ************************************************************************************
.PHONY: test-variables 
test-variables: ## Test the variables used in this make file
	@echo "List of variables used in this make file are:"
	@echo "  LOCAL_OS: $(LOCAL_OS)"
	@echo "  LOCALHOST: $(LOCALHOST)"
	@echo "  BASEDIR: $(BASEDIR)"
	@echo "  PROJ_CACHE_HOME: $(PROJ_CACHE_HOME)"
	@echo "  MYPY_CACHE_DIR: $(MYPY_CACHE_DIR)"
	@echo "  PYTEST_CACHE_DIR: $(PYTEST_CACHE_DIR)"
	@echo "  VENV: $(VENV)"
	@echo "  REQUIREMENTS_BASEDIR: $(REQUIREMENTS_BASEDIR)"
	@echo "  REQUIREMENTS_INPUT: $(REQUIREMENTS_INPUT)"
	@echo "  PYTHON_VERSION: $(PYTHON_VERSION)"
	@echo "  INSTALL_PY_ENV_COMMAND: $(INSTALL_PY_ENV_COMMAND)"
	@echo "  ACTIVATE_PY_ENV_COMMAND: $(ACTIVATE_PY_ENV_COMMAND)"
	@echo "  BIN: $(BIN)"
	@echo "  USER: $(USER)"
	@echo "  PACKAGE_NAME: $(PACKAGE_NAME)"
	@echo "  PIP_COMPILE: $(PIP_COMPILE)"
	@echo "  SCM_VERSION: $(SCM_VERSION)"
	@echo "  APP_VERSION: $(APP_VERSION)"

# ************************************************************************************
# ********************* Help Menu ****************************************************
# ************************************************************************************
.PHONY: help
help: ## Display this help
	@printf "\nusage : make <commands> \n\nthe following commands are available : \n"
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  \033[36m\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-25s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)
	@printf "\n"

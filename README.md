# Countdown with API


## Python Library Installation 
- Run the command prompt with admin privilege and install the Python package Poetry as follow: 
```bash
pip install poetry
```
- Restart the command prompt and cd to the repo directory 
- Install the required libraries by invoking poetry 
```bash
poetry install 
```  

## Test


### Static code analysis - lint

This step verifies the code style of the project and makes sure that common inconsistencies are avoided. You can
easily check for common bugs and also improve the readability of the code.

```bash
poetry run flake8
``` 
Autoformatting: 
```bash
poetry run black {directory or folder}
``` 

### Unit and functional testing - test

Testing verifies the functional requirements of the application. Pytest is used but this is configurable by the developer
in case a different framework is needed.

```bash
poetry run pytest
``` 

## Credit 
Countdown clock credit to this [project] (https://github.com/szimek/final-countdown)
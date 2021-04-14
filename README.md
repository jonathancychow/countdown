# Countdown Application with API Backend
There are two parts to this project:
 1. Display
    - [Countdown Clock](https://jonathancychow.github.io/countdown/?time=35&alert=30)
    - [Message](https://jonathancychow.github.io/countdown/?message=helloworld)
2. Flask server that control the content for the html above.

# Prereq
- If you are runing the flast server on a raspberry pi, please see instruction below for chromedriver installation, see this [link](https://ivanderevianko.com/2020/01/selenium-chromedriver-for-raspberrypi).

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
## Environment
Environment variables for Flask
```bash
cp .env.copy .env
```
Start up script
```bash
chmod +x start_clock.sh
```
# Test
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
# Get Going
Start the flask server with the following command:
```bash
./start_clock.sh
``` 

# Credit 
Countdown clock credit to this [project](https://github.com/szimek/final-countdown).
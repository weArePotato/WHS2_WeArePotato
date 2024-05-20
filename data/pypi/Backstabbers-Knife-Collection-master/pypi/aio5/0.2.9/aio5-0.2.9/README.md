# scrapper-boilerplate


Scrapping functions and for making easy for further scrapping

## instalation

### (Optional) install enviroment

make sure that you have python installed

then install:

```python
pip install virtualenv
```

then install the enviroment and activate:

```python
python -m venv venv
.\venv\scripts\activate
```

### Install the dependêncies:

Install chromedriver [click here](https://chromedriver.chromium.org/downloads), and get the path location.

Create .env file with:

- chromedriver location
- token of telegram bot (if you use telegram function)

Example provided in ".env.example"

install the packages:

```python
pip install -r requirements.txt
```
and activate:
 
```python
python index.py
```

### setup enviroment

create ".env" file with following lines:

```env
CHROMEDRIVER_PATH="Insert your chromedriver path"
TELEGRAM_TOKEN="Insert your telegram token..."
```

## Usage 

```python
from time import sleep
from utils.setup import setSelenium
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def main():
    # import selenium initialization and browser it
    driver = setSelenium()
    driver.get('https://www.google.com')
    sleep(10)
    driver.quit()

if __name__ == "__main__":
    main()

```
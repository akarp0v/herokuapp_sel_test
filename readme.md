## Frontend test automation mini framework
> #### Python | Pytest | Selenium

This is a mini frontend test automation framework for [Web-Herokuapp](http://the-internet.herokuapp.com/)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies

```
pip install -r requirements.txt 
```

## Usage
> Tests use Chrome browser by default

Run
```bash
pytest -vs
```

Headless mode
```bash
pytest -vs --headless=yes
```

Run Docker container
```bash
docker run -it sen10rqa/congenica-sel-py
```
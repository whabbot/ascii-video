# ASCII Video

**Takes live video from your webcam and displays an ASCII art version.**

## Installation and Usage

First make sure [Python 3.8](https://www.python.org/) and [Pipenv](https://pipenv.pypa.io/en/latest/) are installed.

Clone the repository and enter the root directory:
```
git clone https://github.com/whabbot/ascii-video.git
cd ascii-video
```
Install dependencies using Pipenv:
```
pipenv install
``` 
Run ASCII Video from inside root directory:
```
pipenv run python ascii-video.py
```

### To install dev dependencies and run tests
Install dev dependencies using Pipenv:
```
pipenv install --dev
```
This installs [pytest](https://docs.pytest.org) which is used for testing. Tests are located in the tests directory.

Run tests using pytest:
```
pytest
```
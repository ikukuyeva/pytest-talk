# Writing your First Testing Suite with *pytest*

## Overview
Repository contains sample testing suite to illustrate how to write your first
testing suite and how to do so with `pytest`.

We've all heard that we should be testing our Machine Learning models in
production and getting good test coverage. This repository and referenced talk
will give an overview of 4 types of tests: unit, integration, regression and
parametrized test, via examples in `pytest`, to help you write more robust code
in no-time, no prior testing experience necessary.

## Associated Slide Decks
- [IDEAS webinar](http://bit.ly/2ZgDavA) (2019-07-20) slide [deck](http://bit.ly/2JGHOJR)
- [PyLadies Los Angeles meetup](https://www.meetup.com/Pyladies-LA/events/254903299/) (2018-11-08)
slide [deck](http://bit.ly/2LSZeoe)


## Prerequisites to Running the Code/Tests
1. Prerequisites: Install Python 3.6+

2. Clone (or download) this repository

3. (Optionally) Start a virtual environment for the project

4. Install required package `pytest` (to run tests) and `pytest-cov` (to get code coverage)
```
pip3 install -r requirements.txt 
```

## Run the Code
From root of the folder, run:
```
python3 main.py 100 .10 -.2
```

## Run the Tests
From root of the folder, run:
```
pytest tests/. -x --pdb
```

## Check code coverage
From root of the folder, run:
```
pytest tests/. --cov --cov-report=html
open htmlcov/index.html 
```

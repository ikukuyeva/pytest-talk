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
- [IDEAS webinar](http://bit.ly/2YUw0sO) (2019-07-20) slide [deck](http://bit.ly/2XHTFLu)
- [PyLadies Los Angeles meetup](https://www.meetup.com/Pyladies-LA/events/254903299/) (2018-11-08)
slide [deck](http://bit.ly/2LSZeoe)


## Running the Code
1. Prerequisites: Install Python 3.6+

2. (Optionally) Start a virtual environment for the project

3. Clone (or download) this repository

4. Navigate to `price_adjustment` folder on your computer
```
cd  price_adjustment
```

5. Install required package `pytest` (to run tests) and `pytest-cov` (to get code coverage)
```
pip install -r requirements.txt 
```

6. Run tests:
```
pytest tests/. -x --pdb
```

7. To check code coverage, run:
```
pytest tests/. --cov --cov-report=html
open htmlcov/index.html 
```

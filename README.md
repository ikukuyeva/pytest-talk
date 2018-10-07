# *pytest*-ing for Everyone

## Overview
- Repo contains code for [PyLadies Los Angeles meetup](https://www.meetup.com/Pyladies-LA/events/254903299/) on November 7, 2018
- Slide [deck](https://goo.gl/VXPFpb)

## Running the Code
1. Prerequisites: install Python 3.6+ and required package `pytest` (to run tests)
and `pytest-cov` (to get code coverage)

2. Clone this repository

3. Navigate to `price_adjustment folder` on your computer.

4. Run tests:
```
pytest tests/. -x --pdb
```

5. To check code coverage, run:
```
pytest tests/. --cov --cov-report=html
open htmlcov/index.html 
```

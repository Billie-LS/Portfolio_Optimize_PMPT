# Portfolio Analysis and Optimization using Post-Modern Portfolio Theory (PMPT)

## IN DEVELOPMENT

This project is about **Post-Modern Portfolio Theory (PMPT)** based analysis and optimization of a given portfolio’s returns based on individual risk tolerance. It is the continuation and natural evolution of the original project referenced in contributions section below.

The project tries to solve a typical business problem of a Portfolio Manager to find an optimal construction of an investment portfolio.

The post-modern portfolio theory (PMPT) is a portfolio optimization methodology that uses the downside risk of returns instead of the mean variance of investment returns used by the modern portfolio theory (MPT). 
[Investopedia](https://www.investopedia.com/terms/p/pmpt.asp#:~:text=What%20Is%20the%20Post%2DModern,modern%20portfolio%20theory%20(MPT).)

The **Post-Modern Portfolio Theory** :



key concepts:



---

## Technologies

This project leverages python 3.7.* with the following additional packages:
* [Jupyter Notebook](https://jupyter.org/) - The main module of the Financial Planner is written in Jupyter Notebook.
* [Conda](https://docs.conda.io/projects/conda/en/latest/) - Conda environment is recommended to have Pandas library and other dependencies pre-installed.

**Required Libraries:**

You may need the following libraries to work with the application.

- [Pandas](https://pandas.pydata.org/docs/reference/index.html) - pandas is a Python package providing fast, flexible, and expressive data structures designed to make working with “relational” or “labeled” data both easy and intuitive.
- [NumPy](https://numpy.org/doc/stable/user/absolute_beginners.html) - NumPy is the fundamental package for scientific computing in Python.
- [yfinance](https://pypi.org/project/yfinance/) - Download market data from Yahoo! Finance's API
- [SQLAlchemy](https://www.sqlalchemy.org/) - SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.








import pandas as pd
import sqlalchemy as sql
import numpy as np
import scipy as sci
import matplotlib.pyplot as plt
import scipy.optimize as sco

# https://pypi.org/project/yfinance/
import yfinance as yf

import hvplot.pandas
import holoviews as hv
import seaborn as sns
import copy


from pathlib import Path

# https://pandas-datareader.readthedocs.io/en/latest/
from pandas_datareader import data as pdr
from pandas import Timestamp as tstamp
from pandas import read_csv as rcsv
from pandas import read_sql_query as rsqq
from sqlalchemy import (
    create_engine as ce,
    inspect
)

# Import date and timedelta class
from datetime import date
from datetime import timedelta
from scipy import stats

from MCForecastTools import MCSimulation
from calculations import MPTCalculations as mpt
from metrics import QuantMetrics as qm
from dataset import DataCollection as ds

import warnings



---
## **Technologies**
---
### **Dependencies**

This project leverages Jupyter Lab v3.4.4 and python v3.7 with the following packages:


import os


* [pandas](https://pandas.pydata.org/docs/) - Software library written for the python programming language for data manipulation and analysis.



* [read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html) - From 'pandas', reads a comma-separated values (csv) file into DataFrame.

* [concat](https://pandas.pydata.org/docs/reference/api/pandas.concat.html) - From 'pandas', concatenate pandas objects along a particular axis, allows optional set logic along the other axes.

* [numpy](https://numpy.org/doc/stable/) - Software library, NumPy is the fundamental package for scientific computing in Python, provides vast functionality.

* [Path](https://docs.python.org/3/library/pathlib.html) - From pathlib - Object-oriented filesystem paths, Path instantiates a concrete path for the platform the code is running on.

* [hvplot](https://hvplot.holoviz.org/user_guide/Introduction.html) - provides a high-level plotting API built on HoloViews that provides a general and consistent API for plotting data into numerous formats listed within linked documentation.



### **Hardware used for development**

MacBook Pro (16-inch, 2021)

    Chip Appple M1 Max
    macOS Monterey version 12.6

### **Development Software**

Homebrew 3.5.10

    Homebrew/homebrew-core (git revision 0b6b6d9004e; last commit 2022-08-30)
    Homebrew/homebrew-cask (git revision 63ae652861; last commit 2022-08-30)

anaconda Command line client 1.10.0

    conda 4.13.0
    Python 3.9

pip 22.1.2 from /opt/anaconda3/envs/dev/lib/python3.7/site-packages/pip (python 3.7)


git version 2.37.2

---
## *Installation of application (i.e. github clone)*

 In the terminal, navigate to directory where you want to install this application from the repository and enter the following command

```python
git clone git@github.com:Billie-LS/Portfolio_Optimize_PMPT.git
```

---
## **Usage**

From terminal, the installed application is run through jupyter lab web-based interactive development environment (IDE) interface by typing at prompt:

```python
  > jupyter lab
```

The file you will run is:

```python
  nmpt.ipynb
```


## Contributors

Skylizard, Loki 'billie' [GitHub](https://github.com/Billie-LS) [LinkedIn](https://www.linkedin.com/in/l-s-6a0316244/)

Conyea, Will [GitHub](https://github.com/willkanye) [LinkedIn](https://www.linkedin.com/in/william-conyea-3666a7172/)


### Original Project Contributors
[Modern Portfolio Theory Based Portfolio Analysis and Optimization](https://github.com/FintechBTC/mpt)

Peers of FinTech Blended Boot Camp, Columbia Engineering (2022-23 Batch)

- [Skylizard, Loki 'billie'](https://github.com/Billie-LS)

- [Conyea, Will](https://github.com/willkanye)
- [Gavnoudias, Stratis](https://github.com/sgavnoudias)
- [Huang, Yan](https://github.com/Shiroyana)
- [Mandal, Dinesh](https://github.com/dinesh-m)


---

## License

MIT License

Copyright (c) [2022] [Loki 'billie' Skylizard]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
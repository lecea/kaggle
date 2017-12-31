# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import

import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

# %matplotlib inline
# 观察前几行的源数据：

train_data = pd.read_csv('data/train.csv')
test_data = pd.read_csv('data/test.csv')

sns.set_style('whitegrid')
train_data.head()

# 数据信息总览：
train_data.info()
print("-" * 40)
test_data.info()
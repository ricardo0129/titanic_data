import pandas as pd
import numpy as np
import random
import math
path = './train.csv'
titanic_data = pd.read_csv(path)
titanic_data["Sex"] = np.where(titanic_data["Sex"] == "female", 1, 0)
titanic_data['Age'] = titanic_data['Age'].fillna(round(random.uniform(16,32),2))
titanic_data['Fare'] = titanic_data['Fare'].fillna(round(random.uniform(0,50),2))
titanic_data.to_csv("train_better.csv",index=False)

path = './test.csv'
test_data = pd.read_csv(path)
test_data["Sex"] = np.where(test_data["Sex"] == "female", 1, 0)
test_data['Age'] = test_data['Age'].fillna(round(random.uniform(16,32),2))
test_data['Fare'] = test_data['Fare'].fillna(round(random.uniform(0,50),2))
test_data.to_csv("test_better.csv",index=False)

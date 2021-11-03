import numpy as np
import pandas as pd

def isNaN(num):
    return num != num


def findIfColumnsWithConstantValues(dataFrame: pd.core.frame.DataFrame) -> dict:
    """ This will return if there is any column with constant value present in all rows"""

    constantValues = {}
    for i in dataFrame.columns:
        uniqueValues = list(dataFrame[i].unique())
        if len(uniqueValues) == 1 and uniqueValues[0] not in [np.NAN,None,''] and not isNaN(uniqueValues[0]):
            constantValues.update({i: uniqueValues[0]})

    return constantValues


def findIfColumnsWithHighCardinality(dataFrame: pd.core.frame.DataFrame) -> dict:
    """ This will return if there is any column with High Cardinality.
    High-cardinality refers to columns with values that are very uncommon or unique"""

    cardinalityValues = {}
    for i in dataFrame.columns:
        uniqueValues = list(dataFrame[i].unique())
        if len(uniqueValues) > 100 and not len(uniqueValues) == len(dataFrame):
            cardinalityValues.update({i:str(len(uniqueValues))})

    return cardinalityValues


def findIfColumnsWithUniqueIDs(dataFrame: pd.core.frame.DataFrame) -> list:
    """ This will return if there is any column with UniqueIDs"""

    IdColumns = []
    for i in dataFrame.columns:
        uniqueValues = list(dataFrame[i].unique())
        if len(uniqueValues) == len(dataFrame):
            IdColumns.append(i)

    return IdColumns


def findMissingValuesPercentage(dataFrame: pd.core.frame.DataFrame) -> dict:
    """ This will return the percentage of missing values in each columns"""

    all_data_na = (dataFrame.isnull().sum() / len(dataFrame)) * 100
    all_data_na = all_data_na.drop(all_data_na[all_data_na == 0].index).sort_values(ascending=False)
    missing_data = pd.DataFrame({'Missing Ratio': all_data_na.apply(lambda x: str(round(x,2)))}).to_dict()
    return missing_data['Missing Ratio']


def findBinaryColumns(dataFrame: pd.core.frame.DataFrame) -> list:
    """ This will return the list of columns with Binary Values"""

    bool_cols = [col for col in dataFrame
                 if np.isin(dataFrame[col].unique(), [0, 1]).all()]
    return bool_cols

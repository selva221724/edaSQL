from IPython.core.display import display, HTML
import pyodbc
import numpy as np
import seaborn as sb
from matplotlib import pyplot as plt
import missingno
import warnings
import pandas as pd

warnings.filterwarnings('ignore')

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


class SQL:

    def __init__(self, printAll=True):
        self.printAll = printAll
        self.server = self.database = self.user = self.password = self.sqlDriver = None
        self.cursor = self.dbConnection = None, None
        pass

    def connectToDataBase(self, server: str, user: str, password: str, database: str,
                          sqlDriver='ODBC Driver 17 for SQL Server'):
        self.server = server
        self.database = database
        self.user = user
        self.password = password
        self.sqlDriver = sqlDriver

        self.dbConnection = pyodbc.connect(
            'DRIVER={' + self.sqlDriver + '};SERVER='
            + self.server +
            ';DATABASE=' + self.database +
            ';UID=' + self.user +
            ';PWD=' + self.password)

        display(HTML('<img src="sql_logo.jpg" width="50%" height="50%">'))

        if self.printAll:
            print('========== Connected to DataBase Successfully ===========')
            print('Server: ', self.server)
            print('DataBase: ', self.database)
            print('User : ', self.user)
            print('Password : ', self.password)

        self.cursor = self.dbConnection.cursor()


class EDA:

    def __init__(self, dataFrame, HTMLDisplay=True):
        self.dataFrame = dataFrame
        self.HTMLDisplay = HTMLDisplay
        pass

    def getInfo(self):
        pass

    def dataInsights(self, printAll=True) -> dict:
        dataOverview = {
            'Dataset Overview':
                {
                    'Number of Columns': str(len(self.dataFrame.columns)),
                    'Number of Rows': str(len(self.dataFrame)),
                    'Overall Missing cells': str(self.dataFrame.isnull().sum().sum()),
                    'Overall Missing cells (%)': str(
                        round((self.dataFrame.isnull().sum().sum() / self.dataFrame.notnull().sum().sum()) * 100, 2)),
                    'Duplicate rows': str(self.dataFrame.duplicated().sum()),
                    'Duplicate rows (%)': str(round(self.dataFrame.duplicated().sum() / len(self.dataFrame) * 100, 2)),
                },
            'Types of Columns':
                {
                    'Numeric': str(len(self.dataFrame.select_dtypes("number").columns)),
                    'Categorical': str(len(self.dataFrame.select_dtypes("object").columns)),
                    'Date and Time': str(len(self.dataFrame.select_dtypes("datetime64").columns))
                }
        }

        if self.HTMLDisplay and printAll:
            displayContent = """"""
            for parent, child in dataOverview.items():
                tempDisplay = ''
                tempDisplay += '<!DOCTYPE html>\n<html>\n<head>\n<style>\ntable {\n  border-collapse: collapse;\n  ' \
                               '\n}\n\ntd, ' \
                               'th {\n  border: 1px solid #dddddd;\n  text-align: left;\n  padding: ' \
                               '18px;\n}\n\ntr:nth-child(even) {\n  background-color: ' \
                               '#dddddd;\n}\n</style>\n</head>\n<body>\n\n<h1 style=font-size:15px>' + parent + '</h1><table>'
                for cat, value in child.items():
                    tempDisplay += '<tr><th>' + cat + ' :</th><td> ' + value + '</td></tr>'

                tempDisplay += '</table></body></html><br>'
                displayContent += tempDisplay

            display(HTML(displayContent))

        else:
            printer = []
            for parent, child in dataOverview.items():
                printer.append(parent + '\n')
                for cat, value in child.items():
                    printer.append('    ' + cat + ': ' + value + '\n')

            for pr in printer:
                print(pr)

        return dataOverview

    def deepInsights(self, printAll=True) -> dict:
        deepInsights = {
            "Columns with Constant Values": insights.findIfColumnsWithConstantValues(self.dataFrame),
            "Columns with High Cardinality": insights.findIfColumnsWithHighCardinality(self.dataFrame),
            "Columns with  with Unique ID's": insights.findIfColumnsWithUniqueIDs(self.dataFrame),
            "Columns with Missing Values Percentage": insights.findMissingValuesPercentage(self.dataFrame),
            "Columns with Binary Values": insights.findBinaryColumns(self.dataFrame)
        }

        mapper = {
            "Columns with Constant Values": ['Column', 'Value'],
            "Columns with High Cardinality": ['Column', 'No of Unique Values'],
            "Columns with Missing Values Percentage": ['Column', 'Percentage']
        }

        if self.HTMLDisplay and printAll:
            displayContent = """"""
            for parent, child in deepInsights.items():
                tempDisplay = ''
                tempDisplay += '<!DOCTYPE html>\n<html>\n<head>\n<style>\ntable {\n  ' \
                               '\n}\n\ntd,' \
                               'th {\n  border: 1px solid #dddddd;\n  text-align: centre;\n  padding: ' \
                               '8px\n}\n\ntr:nth-child(even) {\n  background-color: ' \
                               '#dddddd;\n}\n</style>\n</head>\n<body>\n\n<h1 style=font-size:15px>' + parent + '</h1><table>'
                if type(child) == dict:
                    tempDisplay += '<tr><th>' + mapper[parent][0] + '</th><th>' + mapper[parent][1] + '</th>'
                    for cat, value in child.items():
                        tempDisplay += '<tr><td>' + cat + '</td><td> ' + value + '</td></tr>'
                else:
                    for cols in child:
                        tempDisplay += '<tr><td > ' + cols + '</td></tr>'

                tempDisplay += '</table></body></html><br>'
                displayContent += tempDisplay

            display(HTML(displayContent))

        else:
            printer = []
            for parent, child in deepInsights.items():
                printer.append(parent + '\n')
                if type(child) == dict:
                    for cat, value in child.items():
                        printer.append('    ' + cat + ': ' + value + '\n')
                else:
                    for cols in child:
                        printer.append('    ' + cols + '\n')
            for pr in printer:
                print(pr)

        return deepInsights

    def pearsonCorrelation(self, columns: list = None):
        """The Pearson correlation is also known as the “product moment correlation coefficient” (PMCC) or
        simply “correlation”. This will generate the Heat Map of Correlation between the Numerical Columns"""

        pearsonDataFrame = self.dataFrame.select_dtypes("number")

        corr = pearsonDataFrame.corr()
        sb.heatmap(corr, cmap="Blues", annot=True)
        plt.title("Pearson's correlation Heat Map")

    def spearmanCorrelation(self, columns: list = None):
        """In statistics, Spearman's rank correlation rank correlation coefficient or Spearman's ρ, named after Charles Spearman and
        often denoted by the Greek letter \rho or as r_{s}, is a nonparametric measure of rank correlation. It
        assesses how well the relationship between two variables can be described using a monotonic function. This
        will generate the Heat Map of Correlation between the Numerical Columns """

        spearmanDataFrame = self.dataFrame.select_dtypes("number")

        corr = spearmanDataFrame.corr(method='spearman')
        sb.heatmap(corr, annot=True)
        plt.title("Spearman's correlation Heat Map")

    def kendallCorrelation(self, columns: list = None):
        """Kendall's rank correlation provides a distribution free test of independence and a measure of the
        strength of dependence between two variables. This
        will generate the Heat Map of Correlation between the Numerical Columns """

        kendallDataFrame = self.dataFrame.select_dtypes("number")

        corr = kendallDataFrame.corr(method='kendall')
        sb.heatmap(corr, annot=True)
        plt.title("Kendall's correlation Heat Map")

    def missingValuesPlot(self, plot='matrix', color=(13, 87, 161)):
        color = (color[0] / 255, color[1] / 255, color[2] / 255)
        if plot == 'matrix':
            missingno.matrix(df=self.dataFrame, color=color, labels=True, sparkline=False)
            plt.title('Missing Values Plot - Matrix')
        if plot == 'bar':
            missingno.bar(df=self.dataFrame, color=color, labels=True)
            plt.title('Missing Values Plot - Count Bar')
        if plot == 'heatmap':
            missingno.heatmap(df=self.dataFrame, labels=True)
            plt.title('Missing Values Plot - HeatMap')
        if plot == 'dendrogram':
            missingno.dendrogram(df=self.dataFrame)
            plt.title('Missing Values Plot - Dendrogram')

    def outliersVisualization(self, plot='box'):
        if plot == 'box':
            for i in list(self.dataFrame.select_dtypes("number").columns):
                plt.figure()
                sb.boxplot(self.dataFrame[i])
                plt.title('Outlier Visualization - ' + str(i))

        if plot == 'scatter':
            for i in list(self.dataFrame.select_dtypes("number").columns):
                plt.figure()
                plt.scatter(range(len(self.dataFrame)), self.dataFrame[i])
                plt.title('Outlier Visualization - ' + str(i))
                plt.xlabel('Index')
                plt.ylabel('Values')

    def getOutliers(self, printAll=True) -> dict:
        outliersDict = {}
        for i in list(self.dataFrame.select_dtypes("number").columns):
            q_low = self.dataFrame[i].quantile(0.01)
            q_hi = self.dataFrame[i].quantile(0.99)
            filteredDf = self.dataFrame[(self.dataFrame[i] < q_hi) & (self.dataFrame[i] > q_low)]
            filteredDf1 = self.dataFrame.merge(filteredDf, indicator=True, how='outer').query(
                '_merge != "both"').drop('_merge', 1)
            outliers = filteredDf1[[i]]
            outliersDict.update({i: outliers})
            if printAll:
                display(HTML('<h1 style="background-color:powderblue;font-size:16px;">' + i + '</h1>'))
                display(outliers)

        return outliersDict

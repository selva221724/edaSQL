<p align="center">
  <img src="https://raw.githubusercontent.com/selva221724/edaSQL/main/readme_src/sql_logo_smaller.png" width="70%" height="70%" >
  <br><br>
</p>

[<img src="https://img.shields.io/static/v1?label=pypi&message=passing&color=green">](https://pypi.org/project/edaSQL/)
[<img src="https://img.shields.io/static/v1?label=docs&message=passing&color=green">](https://edasql.readthedocs.io/en/latest/)
[<img src="https://img.shields.io/static/v1?label=license&message=MIT&color=green">](https://opensource.org/licenses/MIT)
## SQL Bridge Tool to Exploratory Data Analysis  


**edaSQL** is a library to link SQL to **Exploratory Data Analysis** and further more in the Data Engineering. This will solve many limitations in the SQL studios available in the market. Use the SQL Query language to get your Table Results. 

## Installation
Install using pip . [Offical Python Package Here!!](https://pypi.org/project/edaSQL/)
```shell
pip install edaSQL
```

(OR)

Clone this Repository. Run this from the root directory to install

```shell
python setup.py install
```

## Documentation

<img src="https://blog.readthedocs.com/_static/logo-opengraph.png"  width="20%" height="20%">

[Read the detailed documentation in readthedocs.io](https://edasql.readthedocs.io/en/latest/)


## edaSQL Code Sample

### Import Packages
```python
import edaSQL
import pandas as pd
```

### 1. Connect to the DataBase
```python
edasql = edaSQL.SQL()
edasql.connectToDataBase(server='your server name', 
                         database='your database', 
                         user='username', 
                         password='password')
```

### 2. Query Data 
```python
sampleQuery = "select  * from INX"
data = pd.read_sql(sampleQuery, edasql.dbConnection)
```

### 3. Data Overview
```python
insights =  edaSQL.EDA(dataFrame=data,HTMLDisplay=True)
dataInsights =insights.dataInsights()
deepInsights = insights.deepInsights()
```

### 4.Correlation
```python
eda = edaSQL.EDA(dataFrame=data)
eda.pearsonCorrelation()
eda.spearmanCorrelation()
eda.kendallCorrelation()
```

### 5. Missing Values
```python
eda.missingValuesPlot(plot ='matrix')
eda.missingValuesPlot(plot ='bar')
eda.missingValuesPlot(plot ='heatmap')
eda.missingValuesPlot(plot ='dendrogram')
```

### 6. Outliers 
```python
eda.outliersVisualization(plot = 'box')
eda.outliersVisualization(plot = 'scatter')
outliers = eda.getOutliers()
```

## Jupyter NoteBook Tutorial

<img src="https://raw.githubusercontent.com/selva221724/edaSQL/main/readme_src/notebook.png">

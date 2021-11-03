<p align="center">
  <img src="readme_src/sql_logo_smaller.png" width="70%" height="70%" >
  <br><br>
</p>

## SQL Bridge to Exploratory Data Analysis Tool   


**edaSQL** is a library to link SQL to **Exploratory Data Analysis** and further more in the Data Engineering. This will solve many limitations in the SQL studios available in the market. 

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
<img src="readme_src/notebook.png">

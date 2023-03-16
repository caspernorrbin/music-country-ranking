# Music Country Ranking Analysis

This project aims to evaluate and rank countries based on their musical contributions, utilizing the comprehensive [Million Song Dataset](http://millionsongdataset.com/). The primary objective is to discern and quantify the "hotness" of different countries in comparison to one another.

## Dataset
The original HDF format of the dataset has been converted into a more accessible CSV format, which is available within the `csv/` directory. Furthermore, a 'countries' column has been added to the dataset, where applicable. This was done through the mapping of geographical coordinates to their respective countries, using data from the `geojson/` files.

## Running the Analysis
To commence with the analysis, a Spark cluster and a HDFS environment needs to be configured. These measures ensure the readiness and efficiency of the infrastructure for processing the dataset. The application can scale with larger datasets and more processing nodes. Here are the essential steps:

1. **Data Storage**: Ensure that the CSV files are stored in a location that is accessible by Spark.

2. **Notebook Customization**: Modify the provided notebooks to specify the connection details of your Spark cluster and the precise location of the HDFS file.

Once the configuration of your cluster and environment is in place, the subsequent step is to initiate the analysis. This can be accomplished by executing the cells within the provided notebooks.

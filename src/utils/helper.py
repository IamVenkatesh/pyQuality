from pyspark.sql import SparkSession


class Helper:

    def __init__(self, spark: SparkSession):
        self.spark = spark

    def create_hive_table_df(self, database_name, table_name):
        """
        Summary: This function is helper to read the hive database table to spark dataframe

        Parameters: Database Name & Table Name

        Output: Returns a spark dataframe
        """
        return self.spark.table("{0}.{1}".format(database_name, table_name))

    def create_hdfs_files_df(self, format_type, hdfs_location, infer_schema=True):
        """
        Summary: This function is helper to read the hdfs files to spark dataframe

        Parameters: HDFS File Format, HDFS File Location, True or False for inferSchema. By Default the values is
        set to true.

        Output: Returns a spark dataframe
        """
        return self.spark.read.format(format_type).option("header", True) \
            .option("inferSchema", infer_schema).load(hdfs_location)

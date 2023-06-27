from pyspark.sql import SparkSession

def get_spark_session(env, app_name):

    if env == 'local':
        spark = SparkSession.builder.appName(app_name).master('local[*]').getOrCreate()

    spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
    
    return spark





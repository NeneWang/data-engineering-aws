import sys, os
from util import get_spark_session
# need to import for session creation
from pyspark.sql import SparkSession

# creating the session
spark = SparkSession.builder.getOrCreate()


def main():
    
    print(type(os.environ))

    env = os.environ.get('ENVIRON')
    spark = get_spark_session(env, 'SparkByExamples.com')
    spark.sql('SELECT current_date').show()
    



if __name__ == '__main__':
    main()





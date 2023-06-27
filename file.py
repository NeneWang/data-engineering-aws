from pyspark.sql.functions import year, month, dayofmonth

df.withColumn('year', year(df['date'])).show()




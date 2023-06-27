
def to_files(df, tgt_dir, file_format):
    # Write the data to the target directory
    # df.coalesce(1).write.format(file_format).save(tgt_dir)
    # pass
    df.coalesce(16).write.partitionBy('year', 'month', 'day').mode('append').format(file_format).save(tgt_dir) # 16 is the number of partitions





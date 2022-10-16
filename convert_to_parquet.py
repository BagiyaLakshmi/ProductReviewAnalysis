import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd


df = pd.read_csv("datasets/data_1.csv")
table = pa.Table.from_pandas(df)
pq.write_table(table, 'datasets/data_1.parquet')

df1 = pd.read_csv("datasets/reviews_1.csv")
table = pa.Table.from_pandas(df1)
pq.write_table(table, 'datasets/review_1.parquet')

print(pd.read_parquet('datasets/data_1.parquet'))
print(pd.read_parquet('datasets/review_1.parquet'))

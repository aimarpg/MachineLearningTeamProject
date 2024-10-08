#PROCESS BANK MARKETING DATASET TO CSV FOR EASIER MANAGEABILITY

from scipy.io import arff
import pandas as pd

with open('../resources/raw_datasets/phpkIxskf.arff', 'r') as f:
    data, meta = arff.loadarff(f)

column_names = [
    'age', 'job', 'marital', 'education', 'default', 'balance', 'housing',
    'loan', 'contact', 'day', 'month', 'duration', 'campaign', 'pdays',
    'previous', 'poutcome', 'deposit'
]

df = pd.DataFrame(data)
df.columns = column_names

df.to_csv('../resources/processed_datasets/Bank_Marketing.csv', index=False)

print("Bank Marketing dataset processed and saved as CSV")


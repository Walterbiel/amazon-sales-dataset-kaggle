import pandas as pd
import kaggle

kaggle.api.authenticate()
kaggle.api.dataset_download_files('karkavelrajaj/amazon-sales-dataset', path='.',unzip=True)

df = pd.read_csv(r'C:\Users\walte\Documents\Aquivos_Walter\Universidade dos dados\Python + Power BI\Amazon_kaggle_dataset\amazon.csv')

lista = [1,2,3,4,5,6,7,8,9]

df.head()

df.to_csv(r'C:\Users\walte\Documents\Aquivos_Walter\amazonteste.csv')
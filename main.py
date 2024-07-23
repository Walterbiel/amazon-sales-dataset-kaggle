import kaggle
kaggle.api.authenticate()
kaggle.api.dataset_download_files('karkavelrajaj/amazon-sales-dataset', path='.',unzip=True)
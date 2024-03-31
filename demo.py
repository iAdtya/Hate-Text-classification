from text_classification.logger import logging
from text_classification.exception import CustomException
import sys
from text_classification.configuration.gcloud_syncer import GCloudSync

# logging.info("Welcome to Logging!! ")

# try:
#     a = 2 / "0"

# except Exception as e:
#     raise CustomException(e, sys) from e

obj = GCloudSync()
obj.sync_folder_from_gcloud("hate-classification", "dataset.zip", "Download/dataset.zip")

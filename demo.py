# from text_classification.logger import logging
# from text_classification.exception import CustomException
# import sys
# from text_classification.configuration.gcloud_syncer import GCloudSync

# # logging.info("Welcome to Logging!! ")

# # try:
# #     a = 2 / "0"

# # except Exception as e:
# #     raise CustomException(e, sys) from e

# obj = GCloudSync()
# obj.sync_folder_from_gcloud("hate-classification", "dataset.zip", "Download/dataset.zip")


# from fastbook import *
# urls = search_images_ddg('grizzly bear', max_images=100)
# len(urls),urls[0]

# dest = Path('grizzly.jpg')
# if not dest.exists(): download_url(urls[0], dest, show_progress=False)

# im = Image.open(dest)
# im.to_thumb(256,256)

# searches ='forest', 'grizzly'
# path = Path('bird_or_not')

# if not path.exists():
#   for o in searches:
#     dest = (path/o)
#     dest.mkdir(exist_ok=True)
#     results = search_images_ddg(f'{o} photo')
#     download_images (dest, urls=results[:200])
#     resize_images (dest, max_size=400, dest=dest)

# failed = verify_images(get_image_files(path))
# failed.map(Path.unlink)

# dls = DataBlock(
#     blocks=(ImageBlock, CategoryBlock),
#     get_items=get_image_files,
#     splitter=RandomSplitter(valid_pct=0.2, seed=42),
#     get_y=parent_label,
#     item_tfms=[Resize(192,method='squish')]
# ).dataloaders(path)

# dls.show_batch(max_n=6)

# learn = cnn_learner(dls,resnet18,metrics=error_rate)
# learn.fine_tune(3)

import keras
print(keras.__version__)

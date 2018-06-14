
import json
import random

from kaggle import api


# TODO: Figure this out dynamically. Used command line:
#
#     $ kaggle datasets list --page 383
#
# mixed with divide and conquer technique to land on this number.
MAX_PAGES = 383


def get_random_dataset():
    """Choose a random dataset based on a random paging to the API and random
    selection.
    """
    page = random.randint(1, MAX_PAGES)
    response = api.datasets_list_with_http_info(page=page)
    # Response is a tuple of size 3 containing:
    #   - <list(<dict>, ...)> the data
    #   - <int> ?
    #   - <HTTPHeaderDict> headers
    data, something, headers = response
    dataset = random.choice(data)
    # Note: in the kaggle api lib, it casts the dataset to an instance of
    # <kaggle.models.kaggle_models_extended.Dataset>, but we can just use the
    # dict here.
    return dataset


if __name__ == '__main__':
    print json.dumps(get_random_dataset())

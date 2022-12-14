import os

from surprise import BaselineOnly, Dataset, Reader
from surprise.model_selection import cross_validate

# path to dataset file
file_path = os.path.expanduser("BX-Book-Ratings.csv")

print(file_path)

# As we're loading a custom dataset, we need to define a reader. In the
# movielens-100k dataset, each line has the following format:
# 'user item rating timestamp', separated by '\t' characters.
reader = Reader(line_format="user item rating", sep=";", skip_lines=1)

data = Dataset.load_from_file('./BX-Book-Ratings.csv', reader)

# We can now use this dataset as we please, e.g. calling cross_validate
cross_validate(BaselineOnly(), data, verbose=True)
from surprise import Dataset, SlopeOne, accuracy
from surprise.model_selection import train_test_split

data = Dataset.load_builtin('ml-100k')

trainset, testset = train_test_split(data, test_size=.25)

algo = SlopeOne()
algo.fit(trainset)

print(testset.n_users)
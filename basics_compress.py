import pickle

filename = 'basics'
outfile = open(filename, 'wb')

pickle.dump('title.basics.tsv.gz', outfile)
outfile.close()

filename2 = 'ratings'
outfile = open(filename2, 'wb')

pickle.dump('title.ratings.tsv.gz', outfile)
outfile.close()
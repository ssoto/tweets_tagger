import argparse

import pandas as pd
from tweet_tagger import settings
from pandas.core.common import maybe_box_datetimelike
from pymongo.errors import BulkWriteError


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv-path',
                        help='CSV twets file path',
                        type=str)
    args = parser.parse_args()
    return args


def main():
    args = get_arguments()
    df = pd.read_csv(args.csv_path)
    df = df.rename(columns={'id': '_id'})
    save_data = [
        dict((k, maybe_box_datetimelike(v))
             for k, v in zip(df.columns, row) if v is not None and v == v)
        for row in df.values]
    try:
        settings.TWEETS_COL.insert_many(save_data,
                                        ordered=True)
    except BulkWriteError:
        print('Batch warnings appeared, but documents has been inserted.')


if __name__ == '__main__':
    main()

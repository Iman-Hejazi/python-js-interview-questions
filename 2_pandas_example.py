'''
1) read the 'pandas_example.csv' file into a dataframe
2) change the "inc" column value for the first 5 rows to 0
3) change the "inc" column, for all of the rows with "bit_depth" more than 5000, to 90
4) iterate through all rows and print "bit_depth"
5) find the count of all unique values in "inc" column
6) using logging library, after each of the above steps log that the step has finished.
'''

import pandas as pd
import logging


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


FIlE_NAME = 'pandas_example.csv'


logging.info(
    "1.change the 'inc' column, for all of the rows with 'bit_depth' more than 5000, to 90")
df = pd.read_csv(FIlE_NAME)
logging.info(df.head())


logging.info(
    "2.change the 'inc' column, for all of the rows with 'bit_depth' more than 5000, to 90")
df.iloc[0:5, 1] = 0
logging.info(df.head())


logging.info(
    "3.change the 'inc' column, for all of the rows with 'bit_depth' more than 5000, to 90")
df.loc[df['bit_depth'] > 5000, 'inc'] = 90
\
logging.info(df.tail())


logging.info("4.iterate through all rows and print 'bit_depth' ")
for index, row in df.iterrows():
    logging.info(row['bit_depth'])


# 5.find the count of all unique values in "inc" column
logging.info("5 .find the count of all unique values in 'inc' column ")
logging.info(df['inc'].value_counts())

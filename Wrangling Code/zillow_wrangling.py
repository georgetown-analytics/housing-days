__author__ = 'Will'

import csv
import datetime
import glob
import os
import pandas


# the glob is set to search for the pattern '*.csv'
files = [f for f in glob.glob('zillow/*.csv')]
print(files)
# get zip codes from file names
for f in files:
        base = os.path.basename(f)
        df = pandas.read_csv(f, sep=',', delimiter=None, header='infer', names=None, index_col=False, usecols=None, squeeze=False, prefix=None, mangle_dupe_cols=True, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skipinitialspace=False, skiprows=None, skipfooter=None, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=False, skip_blank_lines=True, parse_dates=False, infer_datetime_format=False, keep_date_col=False, date_parser=None, dayfirst=False, iterator=False, chunksize=None, compression='infer', thousands=None, decimal='.', lineterminator=None, quotechar='"', quoting=0, escapechar=None, comment=None, encoding=None, dialect=None, tupleize_cols=False, error_bad_lines=True, warn_bad_lines=True, skip_footer=0, doublequote=True, delim_whitespace=False, as_recarray=False, compact_ints=False, use_unsigned=False, low_memory=True, buffer_lines=None, memory_map=False, float_precision=None)
        df['Index Month'] = pandas.to_datetime(df['Month'], format='%Y-%m')
        df['Index Month'] = df['Index Month'].map(lambda t: t.replace(day=1))
        df.to_csv('zillow/zillow_wrangled/'+base+'.csv')

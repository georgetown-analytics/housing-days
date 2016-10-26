__author__ = 'Will'

from ingestionhelpers import *


# This file will run the necessary scripts to pull and prepare data for storage

# We start with CSVs of MLS data. They will need to be broken down to comply with API limits.

# The current setup below uses one CSV

csv = 'test.csv'
df = pandas.read_csv(csv, sep=',', delimiter=None, header='infer', names=None, index_col=None, usecols=None, squeeze=False, prefix=None, mangle_dupe_cols=True, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skipinitialspace=False, skiprows=None, skipfooter=None, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=False, skip_blank_lines=True, parse_dates=False, infer_datetime_format=False, keep_date_col=False, date_parser=None, dayfirst=False, iterator=False, chunksize=None, compression='infer', thousands=None, decimal='.', lineterminator=None, quotechar='"', quoting=0, escapechar=None, comment=None, encoding=None, dialect=None, tupleize_cols=False, error_bad_lines=True, warn_bad_lines=True, skip_footer=0, doublequote=True, delim_whitespace=False, as_recarray=False, compact_ints=False, use_unsigned=False, low_memory=True, buffer_lines=None, memory_map=False, float_precision=None)

# Create an address-neighborhood data file. Start by taking addresses from the MLS CSV file
neighborhoods = pandas.concat([df['Address']], axis=1, keys=['Address'])


neighborhoods['Neighborhood'] = neighborhoods['Address'].apply(lambda col: zillow_hood_lookup(col))
neighborhoods.to_csv('test_output.csv')
import csv
import datetime
import glob
import os
import pandas

# merges all csv files in a directory, with headers and zip codes

# the glob is set to search for the pattern '*.csv'
files = [f for f in glob.glob('*.csv')]

# get zip codes from file names
for f in files:
        base = os.path.basename(f)
        zip = base[:5]
        print(zip)
        df = pandas.read_csv(f, sep=',', delimiter=None, header='infer', names=None, index_col=False, usecols=None, squeeze=False, prefix=None, mangle_dupe_cols=True, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skipinitialspace=False, skiprows=None, skipfooter=None, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=False, skip_blank_lines=True, parse_dates=False, infer_datetime_format=False, keep_date_col=False, date_parser=None, dayfirst=False, iterator=False, chunksize=None, compression='infer', thousands=None, decimal='.', lineterminator=None, quotechar='"', quoting=0, escapechar=None, comment=None, encoding=None, dialect=None, tupleize_cols=False, error_bad_lines=True, warn_bad_lines=True, skip_footer=0, doublequote=True, delim_whitespace=False, as_recarray=False, compact_ints=False, use_unsigned=False, low_memory=True, buffer_lines=None, memory_map=False, float_precision=None)

        df['Zip'] = zip
        df.to_csv('with_zip/'+str(zip)+'.csv')


# output file looks like '20161001-merged.csv'
outfile = '{:%Y%m%d}-merged.csv'.format(datetime.datetime.now())

files = [f for f in glob.glob('with_zip/*.csv')]

# write merged file to same folder
with open(outfile, 'w') as f_out:
    dict_writer = None
    for f in files:
        print(f)
        with open(f, 'r') as f_in:
            dict_reader = csv.DictReader(f_in)
            if not dict_writer:
                dict_writer = csv.DictWriter(f_out, lineterminator='\n', fieldnames=dict_reader.fieldnames)
                dict_writer.writeheader()
            for row in dict_reader:
                dict_writer.writerow(row)


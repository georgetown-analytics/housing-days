__author__ = 'Will'
import pandas

f = 'All_Sales.csv'
df = pandas.read_csv(f, sep=',', delimiter=None, header='infer', names=None, index_col=False, usecols=None, squeeze=False, prefix=None, mangle_dupe_cols=True, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skipinitialspace=False, skiprows=None, skipfooter=None, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=False, skip_blank_lines=True, parse_dates=False, infer_datetime_format=False, keep_date_col=False, date_parser=None, dayfirst=False, iterator=False, chunksize=None, compression='infer', thousands=None, decimal='.', lineterminator=None, quotechar='"', quoting=0, escapechar=None, comment=None, encoding=None, dialect=None, tupleize_cols=False, error_bad_lines=True, warn_bad_lines=True, skip_footer=0, doublequote=True, delim_whitespace=False, as_recarray=False, compact_ints=False, use_unsigned=False, low_memory=True, buffer_lines=None, memory_map=False, float_precision=None)
df = df.drop_duplicates(subset=['Address', 'Close Date'])
df = df[(df['DOMP'] != 0)]

addresses = df[['Address']]
addresses = addresses.drop_duplicates()
addresses.to_csv('addresses.csv')

latest_sale_bool = df.groupby(['Address'], sort=False)['Close Date'].transform(max) == df['Close Date']
latest_sales = df[latest_sale_bool]

latest_sales.to_csv('latest_sales.csv')

sale_counts = df.groupby('Address').size().reset_index()
sale_counts.columns = ['Address', 'Sale Count']
sale_counts.to_csv('sales_counts.csv')


merged = pandas.merge(latest_sales, sale_counts, how='left', on='Address', left_on=None, right_on=None, left_index=False, right_index=False, sort=True, suffixes=('_x', '_y'), copy=True, indicator=False)


merged['Close Date'] = pandas.to_datetime(merged['Close Date'], format='%d-%b-%y')
merged['Index Month'] = merged['Close Date'].map(lambda t: t.replace(day=1))


merged.to_csv('output.csv')
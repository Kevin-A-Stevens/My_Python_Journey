"""
Reading a CSV file
"""
import csv

csv_filename = 'OlympicMedals_2020.csv'

with open(csv_filename, encoding='utf-8', newline='') as csv_file:
    headers = csv_file.readline().strip('\n').split(',')
    print(f'Column head: {headers}')
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)

print("-" * 80)

csv_filename = 'cereal_grains.csv'

# changing number string values to floats (if csv file contains non quoted numbers)
with open(csv_filename, encoding='utf-8', newline='') as csv_file:
    reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        print(row)

"""
Sniffer and Dialect
Sniffer class examines the file for things such as the delimiter used
The sniffer then creates a dialect
"""

input_filename = 'country_info.txt'

with open(input_filename, encoding='utf-8', newline='') as countries_data:
    sample = ""
    for line in range(3):
        sample += countries_data.readline()
    country_dialect = csv.Sniffer().sniff(sample)
    country_dialect.skipinitialspace = True  # if a starting space needs skipped
    countries_data.seek(0)  # set file pointer at start of file
    country_reader = csv.reader(countries_data, dialect=country_dialect)
    for row in country_reader:
        print(row)

print("-" * 80)

# printing the dialect
attributes = ['delimiter',
              'doublequote',
              'escapechar',
              'lineterminator',
              'quotechar',
              'quoting',
              'skipinitialspace',
              ]

for attribute in attributes:
    print(f'{attribute}: {repr(getattr(country_dialect, attribute))}')

# Use repr above if you suspect garbled characters in strings
# do not need it in the above statement though

"""
writing to a csv file
"""

cereals = [
    ["Barley", 556, 1.7, 32.9, 10.1, 13.8],
    ["Durum", 339, 5, 27.4, 4.09, 9.7],
    ["Fonio", 240, 1, 4, 1.7, 0.05],
    ["Maize", 442, 7.4, 37.45, 6.15, 11.03],
    ["Millet", 484, 2, 37.9, 13.4, 9.15],
    ["Oats", 231, 9.2, 35.1, 10.3, 3.73],
    ["Rice (Brown)", 346, 2.8, 38.1, 9.9, 0.8],
    ["Rice, (White)", 345, 3.6, 37.6, 5.4, 0.1],
    ["Rye", 422, 2, 31.4, 18.2, 21.2],
    ["Sorghum", 316, 3, 37.8, 9.92, 9.15],
    ["Triticale", 338, 1.81, 36.6, 19, 0.9],
    ["Wheat", 407, 1.2, 27.8, 12.9, 13.8],
]

column_headings = ["Cereal", "Calories", "Fat", "Protein", "Fibre", "Vitamin E"]

output_filename = 'my_cereals.csv'

with open(output_filename, 'w', encoding='utf-8', newline='') as output_file:
    writer = csv.writer(output_file, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(column_headings)
    writer.writerows(cereals)

"""
csv DictReader
"""
print("-" * 80)
cereals_filename = 'cereal_grains.csv'

with open(cereals_filename, encoding='utf-8', newline='') as cereals_file:
    reader = csv.DictReader(cereals_file)
    for row in reader:
        print(row)

ordering = ['Country', 'Gold', 'Silver', 'Bronze', 'Rank']
# Note the lack of 'Total' in `ordering`

with open('OlympicMedals_2020.csv', encoding='utf-8', newline='') as data, open('medals_dict.py', 'w', encoding='utf-8') as output_file:
    # Write the first part of the code (excluding the actual data)
    print('import csv', file=output_file)
    print(file=output_file)
    print('medals_table = [', file=output_file)

    reader = csv.DictReader(data)
    # Read each row from the CSV file, as a dictionary,
    # and produce a new dictionary containing the key/value
    # pairs we want, in the order we want.
    for row_dict in reader:
        new_dict = {}
        # Only print the values for the keys we want
        # (in the order we want them).
        for key in ordering:
            value = row_dict[key]
            if value.isnumeric():
                value = int(value)
            new_dict[key.casefold()] = value

        # print the dictionary to the output file
        # (indented by 4 spaces, with a trailing comma).
        print(f'    {new_dict},', file=output_file)

    # All the data rows have been written, print the terminating ]
    print(']', file=output_file)
    print(file=output_file)  # and finish with a blank line.

"""
zip function
"""
print("-" * 80)
albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Imelda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]

keys = ['album', 'artist', 'year']

filename = 'albums.csv'
with open(filename, 'w', encoding='utf-8', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=keys)
    writer.writeheader()
    for row in albums:
        zip_object = zip(keys, row)
        # print(zip_object)
        # for thing in zip(keys, row):
        #     print("\t", thing)
        albums_dict = dict(zip_object)
        print(albums_dict)
        writer.writerow(albums_dict)

"""
reading and writing to the same text file
"""
import datetime
from os import SEEK_SET
from typing import TextIO, Tuple


def get_year() -> int:
    """Return the current year as an integer."""
    return datetime.datetime.now().year


def parse_invoice_number(invoice_number: str) -> Tuple[int, int]:
    """Split a well-formed invoice "number" into its component parts.

    :param invoice_number: A string of the form YYYY-NNNN
        YYYY is the 4 digit year.
        NNNN is a 4 digit invoice number, left padded with zeros.
        The 2 parts are separated with a "-" character.
    :return: The returned tuple will contain:
        the 4 digit year as an integer,
        the invoice number as an integer.
    """
    year, number = invoice_number.split('-')
    return int(year), int(number)

def next_invoice_number(invoice_number: str) -> str:
    """ Produce the next invoice "number" in sequence.

    The format of `invoice_number` is described in `parse_invoice_number`.

    :param invoice_number: A string representing an invoice number.
    :return: A string representing the next invoice number.
        The numerical part will be incremented, unless the current year
        isn't the same as the year in `invoice_number`. In that case,
        the new invoice number will contain the current year, and the
        numerical part will be set to "0001".
    """
    invoice_year, number = parse_invoice_number(invoice_number)
    year = get_year()
    if year == invoice_year:
        number += 1
    else:
        invoice_year = year
        number = 1
    new_invoice_number = f'{invoice_year}-{number:04d}'
    return new_invoice_number


def record_invoice(invoice_file: TextIO,
                   company: str,
                   amount: float,
                   last_line_ptr: int = 0) -> int:
    """Create a new invoice number, and write it to a file on disk.

    :param invoice_file: An open text file, opened using r+.
    :param company: The name of the company being invoiced.
    :param amount: The amount of the invoice.
    :param last_line_ptr: The position of the start of the last line
    in the file. This will be obtained by the previous call to
    record_invoice
    :return: The position of the start of the last line in the file.
    This can be used to subsequent calls to record_invoice.
    """
    invoice_file.seek(last_line_ptr, SEEK_SET)
    last_row = ''
    for line in invoice_file:
        print('*', end='')  # TODO delete after testing
        last_row = line
    if last_row:
        # invoice_number, _, _ = last_row.split('\t')
        invoice_number = last_row.split('\t')[0]
        new_invoice_number = next_invoice_number(invoice_number)
    else:
        # If the file is empty, we'll start numbering from 1
        year = get_year()
        new_invoice_number = f'{year}-{1:04d}'

    last_line_ptr = invoice_file.tell()
    print(f'{new_invoice_number}\t{company}\t{amount}', file=invoice_file)
    return last_line_ptr

data_file = 'invoices.csv'

with open(data_file, 'r+') as invoices:
    last_line = record_invoice(invoices, 'ACME Roadrunner', 18.40)
    last_line = record_invoice(invoices, 'Squirrel Storage', 320.55, last_line)


# Test code:
# current_year = get_year()
# test_data = [
#     ('2019-0005', (2019, 5), f'{current_year}-0001'),
#     (f'{current_year}-8514', (current_year, 8514), f'{current_year}-8515'),
#     (f'{current_year}-0001', (current_year, 1), f'{current_year}-0002'),
#     (f'{current_year}-0023', (current_year, 23), f'{current_year}-0024'),
# ]
#
# for test_string, result, next_number in test_data:
#     parts = parse_invoice_number(test_string)
#     if parts == result:
#         print(f'{test_string} parsed successfully')
#     else:
#         print(f'{test_string} failed to parse. Expected {result} got {parts}')
#
#     new_number = next_invoice_number(test_string)
#     if next_number == new_number:
#         print(f'New number {new_number} generated correctly for {test_string}')
#     else:
#         print(f'New number {new_number} is not correct for {test_string}')
#
#     print('-' * 80)


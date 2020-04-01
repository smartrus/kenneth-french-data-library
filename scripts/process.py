import re
import csv
import zipfile
import urllib.request
import string
from datetime import datetime
from io import StringIO

url = "http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/5_Industry_Portfolios_CSV.zip"
urllib.request.urlretrieve(url, "../archive/source.zip")

with zipfile.ZipFile("../archive/source.zip", 'r') as zip_ref:
    zip_ref.extractall("../data/")

input_name = "../data/5_Industry_Portfolios.CSV"
output_name = "../data/avg_value_weighted_returns.csv"

with open(input_name, 'r') as f_input, open(output_name, 'w') as f_output:
    # Read whole file in
    all_input = f_input.read()  

    # Extract interesting lines
    ab_input = re.findall(r'  Average Value Weighted Returns -- Monthly(.*?)  Average Equal Weighted Returns -- Monthly', all_input, re.DOTALL)[0]

    # Convert into a file object and parse using the CSV reader
    fab_input = StringIO(ab_input)
    csv_input = csv.reader(fab_input)
    csv_output = csv.writer(f_output)

    # Iterate a row at a time from the input
    next(csv_input)  # skip the first row from the reader, the old header
    next(csv_input)  # skip the first row from the reader, the old header
    # write new header
    csv_output.writerow(['Date', 'Cnsmr', 'Manuf', 'HiTec', 'Hlth', 'Other'])

    for input_row in csv_input:
        # Skip any empty rows
        if input_row:
            # Write row at a time to the output
            csv_output.writerow(map(str.strip, input_row))
Detail for 5 Industry Portfolios

## Data

Dataset contains 5 Industry Portfolios monthly returns from July 1926 till February 2020.

Industry portfolios:

 * Cnsmr  Consumer Durables, Nondurables, Wholesale, Retail, and Some Services (Laundries, Repair Shops)
 * Manuf  Manufacturing, Energy, and Utilities
 * HiTec  Business Equipment, Telephone and Television Transmission
 * Hlth   Healthcare, Medical Equipment, and Drugs
 * Other  Other -- Mines, Constr, BldMt, Trans, Hotels, Bus Serv, Entertainment, Finance


The data is fetched from [Kenneth French Data Library](http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html)

## Preparation

To update the data run the process script locally:
```bash
python scripts/process.py
```

Several steps will be done to get the final data.

* It first hits the URL and download the XLS file to the archive directory
* It applies parsing on a sheet named 'Data' in the downloaded file.
* After cleaning and parsing, final output is genertated in a CSV file that is contained under 'data' directory and is named 'united_states_historical_house_prices.csv'.

## License

Copyright 2020 Kenneth R. French
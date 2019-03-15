import pandas as pd


# Test 3 inline
# define Function, easy solution with pandas
def calc_stat(p):
    p_dat = pd.read_csv(p, delim_whitespace=True)
    pmax = p_dat.loc[:, 'rre150d0'].max()
    pmin = p_dat.loc[:, 'rre150d0'].min()
    pmean = p_dat.loc[:, 'rre150d0'].mean()
    return [pmax, pmin, pmean]  # returns a list

path = r'C:\Users\Jan Liechti\Google Drive\UNI\FS19\Geographie\Gedatenanalyse_u_Modellierung\02 Intro Python\precip_data.txt'  # path to Textfile
results = calc_stat(path)
print('maximum precipitation: {} \nminimum precipitation: {}\nmean precipitation: {}'.format(results[0], results[1], round(results[2], 1)))

# Erweiterung Test

# Test 2 für Kraken
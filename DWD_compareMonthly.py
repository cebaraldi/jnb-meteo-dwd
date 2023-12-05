#!/usr/bin/env python
# coding: utf-8

get_ipython().run_line_magic('reset', '-sf')
import pandas as pd
import numpy as np
from datetime import datetime, date
from IPython.display import Markdown as md
from iteration_utilities import flatten # can be probably removed from conda environment


url = "https://opendata.dwd.de/"
path = 'climate_environment/CDC/observations_germany/climate/daily/kl/'
recent_path = path + 'recent/'
historical_path = path + 'historical/'
filename = 'KL_Tageswerte_Beschreibung_Stationen.txt' 
ws = pd.read_csv(url + recent_path + filename, sep="\t", header=0, skiprows = 0, encoding = "ISO-8859-1").dropna()
ws.drop(0, inplace=True)

# save original column names
colnames = ws.columns[0].split(' ')

# rename column for instance to 'dummy'
ws.columns = ['dummy']

# split string up to 6th column
ws = ws['dummy'].str.split('\s+', n=6, expand=True)

# convert 1:6 to numeric
for col in  ws.iloc[:,1:6]:
    ws[col] = pd.to_numeric(ws[col], errors='coerce') 
    
# concat columns back to a type consistent dataframe
wst = pd.concat([ws.iloc[:,0:6], ws[6].str.slice(0,41), ws[6].str.slice(41,)], axis=1)  
wst.columns = colnames
wst.head()


# Convert von_datum and bis_datum to a date type
wst["von"] = pd.to_datetime(wst["von_datum"], format="%Y%m%d", errors="coerce")
wst["bis"] = pd.to_datetime(wst["bis_datum"], format="%Y%m%d", errors="coerce")
# print(wst.loc[:,['Stations_id','von','bis']])

# Function to extract stations Climatic Standard Normal periods, s. WMO-No. 1203
def dwd_extratCSN(df, yyyy, wmo1203=30):
    first = str(yyyy-wmo1203+1) + '-1-1'
    last = str(yyyy)+ '-12-31'
    fv = pd.to_datetime(first, format='%Y-%m-%d', errors="coerce").date()
    lv = pd.to_datetime(last, format='%Y-%m-%d', errors="coerce").date()
    return df[(df['von'] <= first) & (df['bis'] >= last)], (lv - fv).days

# Select stations having data for the Standard Reference Period and some Climatic Standard Normal periods
wmo_yyyy = 1990
CSN, CSN_days = dwd_extratCSN(wst.drop(['von_datum','bis_datum'], axis=1), wmo_yyyy)  # Standard Ref. Period
# print(CSN.loc[:,['Stations_id','von','bis']])
# print(CSN.describe())
# print(len(CSN.index))
# print(CSN_days)


# ### DWD Compare Each Month vs. Climatic Norm

md(f"{len(wst.index)} available weather stations {len(CSN.index)} of which contribute to the Climatic Standard Normal ending in {wmo_yyyy}. This period contains {CSN_days} days.")


# CSN.drop(['Stationshoehe','geoBreite','geoLaenge'], axis=1)
# print(CSN.loc[:,['Stations_id','Stationsname']].head())
# print(CSN.loc[:,['Stations_id','Stationsname']].tail(11).to_markdown())
CSN


# Display number of weather stations by Bundesland:

print(CSN.groupby(['Bundesland'])['Bundesland'].count().to_markdown())


# Download zip file from URL
# [howto](https://pythonguides.com/download-zip-file-from-url-using-python/)

# Loop zip files in zip_url and extract observations

from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile
from re import compile

def collectRecords(zfile): 
    with BytesIO(zfile.read()) as b, ZipFile(b) as datafile: 
        r = compile("^produkt_klima_tag_.*\.txt$")
        dfound = list(filter(r.match, datafile.namelist()))
        number = len(dfound)
        assert number == 1, f"WARN: exactly one element expected, got {number} instead"
        # print(dfound[0])
        rf = datafile.open(dfound[0])
        lines = rf.readlines()
        rf.close()
        header = True
        for bline in lines:
            line = bline.decode('unicode-escape').rstrip('\r\n').split(';')
            del line[-1] # remove last column containing only string 'eor'
            #print(line)
            if header: # initialize list of lists
                header = not(header)
                record = [line]
            else:
                record.append(line)
    return record

# Function to extract data for Climatic Standard Period
# See WMO Guidelines on the Calculation of Climate Normals: WMO-No. 1203
def dwd_extratCSNData(df, yyyy, wmo1203=30):
    first = str(yyyy-wmo1203+1) + '-1-1'
    last = str(yyyy)+ '-12-31'
    fv = pd.to_datetime(first, format='%Y-%m-%d', errors="coerce").date()
    lv = pd.to_datetime(last, format='%Y-%m-%d', errors="coerce").date()
    return df[(df['DATUM'] >= fv) & (df['DATUM'] <= lv)], (lv - fv).days

get_ipython().run_line_magic('time', '')
csn_lst = CSN['Stations_id'].to_list()


get_ipython().run_cell_magic('time', '', '\n# zip_url = url + recent_path \n# tw_regex = compile(r\'tageswerte_KL_[0-9]{5}_akt.zip\')\n\nzip_url = url + historical_path \ntw_regex = compile(r\'tageswerte_KL_[0-9]{5}_[0-9]{8}_[0-9]{8}_hist.zip\')\n\nonce = True\ncurrent_year = date.today().year # to end the csn_period loop\ncsn_dict = {}\nwith urlopen(zip_url) as f:\n    for bline in f.readlines():\n        zfound = tw_regex.search(bline.decode(\'utf-8\'))\n        # print(zfound)\n        if zfound:\n            zfilename = zfound.string[zfound.start():zfound.end()]\n            sid = zfilename[14:19] # extracted weather station id\n            \n            # if sid in csn_lst[:3]:\n            if sid in csn_lst:\n                # print(sid)\n                csn_dict[sid] = {}\n                with urlopen(zip_url + zfilename) as z:\n                    record = collectRecords(z) # <-- function call   \n                    df = pd.DataFrame(record[1:], columns=record[0])\n\n                    # Remove leading and trailing blanks from column names\n                    trimmed = [s.strip() for s in list(df)]\n                    df.columns = trimmed\n                    df = df.apply(pd.to_numeric)\n \n                    # Extract overall summary statistics\n                    # print(df.describe())\n                    csn_dict[sid][\'all\'] = {\'summary\': df.describe()}\n                    \n                    df["DATUM"] = pd.to_datetime(df["MESS_DATUM"], format="%Y%m%d", errors="coerce").dt.date\n                    df["DAY"] = pd.to_datetime(df["MESS_DATUM"], format="%Y%m%d", errors="coerce").dt.day\n                    df["MONTH"] = pd.to_datetime(df["MESS_DATUM"], format="%Y%m%d", errors="coerce").dt.month\n                    df.drop([\'MESS_DATUM\'], axis=\'columns\',inplace=True)\n                    df.replace(-999, np.NaN, inplace=True)  \n                    df[\'STATIONS_ID\'] = df[\'STATIONS_ID\'].astype(\'str\').apply(lambda x: \'{0:0>5}\'.format(x))\n\n                    for csn_period in range(1990, current_year, 10):\n                        CSN_df, CSN_days = dwd_extratCSNData(df, csn_period)\n                        season = df.groupby([\'MONTH\', \'DAY\'])[[\'VPM\', \'PM\', \'RSK\', \'TMK\', \'UPM\']].describe()\n                        # season = df.groupby([\'MONTH\', \'DAY\'])[\'TMK\'].describe()\n                        csn_dict[sid][csn_period] = {\'days\': CSN_days, \'summary\': CSN_df.describe(), \'season\': season}\n\nmd(f"{len(csn_dict)} DWD weather stations have been processed at URL {zip_url}.")\n# print(zip_url)\n')


# import pickle
# dump_fn = 'dwd_csn.pickle'

# with open(dump_fn, 'wb') as f:
#     # Pickle the dictionary using the highest protocol available.
#     pickle.dump(csn_dict, f, pickle.HIGHEST_PROTOCOL)

# with open(dump_fn, 'rb') as f:
#     # The protocol version used is detected automatically, so we do not
#     # have to specify it.
#     csn_dict = pickle.load(f)


csn_dict.keys() # STATIONS_ID


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = [ {
        "Year": 1974,
        "Electricity Supplied[GW.h]": 947.5,
        "Reference Unit Power[MW]": 319,
        "Annual Time On Line[h]": 4458,
        "Operation Factor[%]": 66.0,
        "Energy Availability Factor[%]_Annual": 50.3,
        "Energy Availability Factor[%]_Cumulative": 50.3,
        "Load Factor[%]_Annual": 50.3,
        "Load Factor[%]_Cumulative": 50.3
    },
    {
        "Year": 1975,
        "Electricity Supplied[GW.h]": 2357.8,
        "Reference Unit Power[MW]": 319,
        "Annual Time On Line[h]": 7730,
        "Operation Factor[%]": 88.2,
        "Energy Availability Factor[%]_Annual": 85.6,
        "Energy Availability Factor[%]_Cumulative": 73.8,
        "Load Factor[%]_Annual": 84.4,
        "Load Factor[%]_Cumulative": 73.0
    },
    {
        "Year": 1976,
        "Electricity Supplied[GW.h]": 2408.6,
        "Reference Unit Power[MW]": 319,
        "Annual Time On Line[h]": 7808,
        "Operation Factor[%]": 88.9,
        "Energy Availability Factor[%]_Annual": 86.9,
        "Energy Availability Factor[%]_Cumulative": 79.0,
        "Load Factor[%]_Annual": 86.0,
        "Load Factor[%]_Cumulative": 78.2
    },
    {
        "Year": 1977,
        "Electricity Supplied[GW.h]": 1537.0,
        "Reference Unit Power[MW]": 345,
        "Annual Time On Line[h]": 4650,
        "Operation Factor[%]": 53.1,
        "Energy Availability Factor[%]_Annual": 53.0,
        "Energy Availability Factor[%]_Cumulative": 71.3,
        "Load Factor[%]_Annual": 52.2,
        "Load Factor[%]_Cumulative": 70.4
    },
    {
        "Year": 1978,
        "Electricity Supplied[GW.h]": 2711.81,
        "Reference Unit Power[MW]": 345,
        "Annual Time On Line[h]": 8026,
        "Operation Factor[%]": 91.6,
        "Energy Availability Factor[%]_Annual": 90.9,
        "Energy Availability Factor[%]_Cumulative": 75.9,
        "Load Factor[%]_Annual": 89.7,
        "Load Factor[%]_Cumulative": 74.9
    },
    {
        "Year": 1979,
        "Electricity Supplied[GW.h]": 2503.7,
        "Reference Unit Power[MW]": 335,
        "Annual Time On Line[h]": 7551,
        "Operation Factor[%]": 86.2,
        "Energy Availability Factor[%]_Annual": 84.1,
        "Energy Availability Factor[%]_Cumulative": 77.4,
        "Load Factor[%]_Annual": 85.3,
        "Load Factor[%]_Cumulative": 76.9
    },
    {
        "Year": 1980,
        "Electricity Supplied[GW.h]": 2180.5,
        "Reference Unit Power[MW]": 335,
        "Annual Time On Line[h]": 6947,
        "Operation Factor[%]": 79.1,
        "Energy Availability Factor[%]_Annual": 73.5,
        "Energy Availability Factor[%]_Cumulative": 76.8,
        "Load Factor[%]_Annual": 74.1,
        "Load Factor[%]_Cumulative": 76.4
    },
    {
        "Year": 1981,
        "Electricity Supplied[GW.h]": 2647.6,
        "Reference Unit Power[MW]": 335,
        "Annual Time On Line[h]": 8120,
        "Operation Factor[%]": 92.7,
        "Energy Availability Factor[%]_Annual": 89.7,
        "Energy Availability Factor[%]_Cumulative": 78.5,
        "Load Factor[%]_Annual": 90.2,
        "Load Factor[%]_Cumulative": 78.3
    },
    {
        "Year": 1982,
        "Electricity Supplied[GW.h]": 1753.6,
        "Reference Unit Power[MW]": 335,
        "Annual Time On Line[h]": 5600,
        "Operation Factor[%]": 63.9,
        "Energy Availability Factor[%]_Annual": 59.2,
        "Energy Availability Factor[%]_Cumulative": 76.2,
        "Load Factor[%]_Annual": 59.8,
        "Load Factor[%]_Cumulative": 76.1
    },
    {
        "Year": 1983,
        "Electricity Supplied[GW.h]": 2356.0,
        "Reference Unit Power[MW]": 335,
        "Annual Time On Line[h]": 8101,
        "Operation Factor[%]": 92.5,
        "Energy Availability Factor[%]_Annual": 78.4,
        "Energy Availability Factor[%]_Cumulative": 76.5,
        "Load Factor[%]_Annual": 80.3,
        "Load Factor[%]_Cumulative": 76.5
    },
    {
        "Year": 1984,
        "Electricity Supplied[GW.h]": 1706.12,
        "Reference Unit Power[MW]": 335,
        "Annual Time On Line[h]": 8678,
        "Operation Factor[%]": 98.8,
        "Energy Availability Factor[%]_Annual": 98.7,
        "Energy Availability Factor[%]_Cumulative": 78.6,
        "Load Factor[%]_Annual": 58.0,
        "Load Factor[%]_Cumulative": 74.8
    },
    {
        "Year": 1985,
        "Electricity Supplied[GW.h]": 1470.45,
        "Reference Unit Power[MW]": 335,
        "Annual Time On Line[h]": 7159,
        "Operation Factor[%]": 81.7,
        "Energy Availability Factor[%]_Annual": 91.6,
        "Energy Availability Factor[%]_Cumulative": 79.7,
        "Load Factor[%]_Annual": 50.1,
        "Load Factor[%]_Cumulative": 72.6
    },
    {
        "Year": 1986,
        "Electricity Supplied[GW.h]": 2204.96,
        "Reference Unit Power[MW]": 335,
        "Annual Time On Line[h]": 7532,
        "Operation Factor[%]": 86.0,
        "Energy Availability Factor[%]_Annual": 75.8,
        "Energy Availability Factor[%]_Cumulative": 79.4,
        "Load Factor[%]_Annual": 75.1,
        "Load Factor[%]_Cumulative": 72.8
    },
    {
        "Year": 1987,
        "Electricity Supplied[GW.h]": 1405.8,
        "Reference Unit Power[MW]": 335,
        "Annual Time On Line[h]": 4391,
        "Operation Factor[%]": 50.1,
        "Energy Availability Factor[%]_Annual": 49.2,
        "Energy Availability Factor[%]_Cumulative": 77.2,
        "Load Factor[%]_Annual": 47.9,
        "Load Factor[%]_Cumulative": 70.9
    },
    {
        "Year": 1988,
        "Electricity Supplied[GW.h]": 808.1,
        "Reference Unit Power[MW]": 335,
        "Annual Time On Line[h]": 2515,
        "Operation Factor[%]": 28.6,
        "Energy Availability Factor[%]_Annual": 27.1,
        "Energy Availability Factor[%]_Cumulative": 73.7,
        "Load Factor[%]_Annual": 27.5,
        "Load Factor[%]_Cumulative": 67.9
    },
    {
        "Year": 1989,
        "Electricity Supplied[GW.h]": 0.0,
        "Reference Unit Power[MW]": 335,
        "Annual Time On Line[h]": 0,
        "Operation Factor[%]": 0.0,
        "Energy Availability Factor[%]_Annual": 0.0,
        "Energy Availability Factor[%]_Cumulative": 68.9,
        "Load Factor[%]_Annual": 0.0,
        "Load Factor[%]_Cumulative": 63.5
    },
    {
        "Year": 1990,
        "Electricity Supplied[GW.h]": 1722.59,
        "Reference Unit Power[MW]": 335,
        "Annual Time On Line[h]": 7201,
        "Operation Factor[%]": 82.2,
        "Energy Availability Factor[%]_Annual": 58.7,
        "Energy Availability Factor[%]_Cumulative": 68.3,
        "Load Factor[%]_Annual": 58.7,
        "Load Factor[%]_Cumulative": 63.2
    },
    {
        "Year": 1991,
        "Electricity Supplied[GW.h]": 2721.89,
        "Reference Unit Power[MW]": 335,
        "Annual Time On Line[h]": 8390,
        "Operation Factor[%]": 95.8,
        "Energy Availability Factor[%]_Annual": 92.6,
        "Energy Availability Factor[%]_Cumulative": 69.7,
        "Load Factor[%]_Annual": 92.8,
        "Load Factor[%]_Cumulative": 64.9
    },
    {
        "Year": 1992,
        "Electricity Supplied[GW.h]": 2230.24,
        "Reference Unit Power[MW]": 335,
        "Annual Time On Line[h]": 7089,
        "Operation Factor[%]": 80.7,
        "Energy Availability Factor[%]_Annual": 76.3,
        "Energy Availability Factor[%]_Cumulative": 70.0,
        "Load Factor[%]_Annual": 75.8,
        "Load Factor[%]_Cumulative": 65.5
    },
    {
        "Year": 1993,
        "Electricity Supplied[GW.h]": 2403.66,
        "Reference Unit Power[MW]": 335,
        "Annual Time On Line[h]": 7287,
        "Operation Factor[%]": 83.2,
        "Energy Availability Factor[%]_Annual": 82.2,
        "Energy Availability Factor[%]_Cumulative": 70.7,
        "Load Factor[%]_Annual": 81.9,
        "Load Factor[%]_Cumulative": 66.4
    },
    {
        "Year": 1994,
        "Electricity Supplied[GW.h]": 2651.86,
        "Reference Unit Power[MW]": 335,
        "Annual Time On Line[h]": 7916,
        "Operation Factor[%]": 90.4,
        "Energy Availability Factor[%]_Annual": 90.4,
        "Energy Availability Factor[%]_Cumulative": 71.6,
        "Load Factor[%]_Annual": 90.4,
        "Load Factor[%]_Cumulative": 67.5
    },
    {
        "Year": 1995,
        "Electricity Supplied[GW.h]": 2671.71,
        "Reference Unit Power[MW]": 335,
        "Annual Time On Line[h]": 8376,
        "Operation Factor[%]": 95.6,
        "Energy Availability Factor[%]_Annual": 92.3,
        "Energy Availability Factor[%]_Cumulative": 72.6,
        "Load Factor[%]_Annual": 91.0,
        "Load Factor[%]_Cumulative": 68.6
    },
    {
        "Year": 1996,
        "Electricity Supplied[GW.h]": 2038.8,
        "Reference Unit Power[MW]": 335,
        "Annual Time On Line[h]": 6990,
        "Operation Factor[%]": 79.6,
        "Energy Availability Factor[%]_Annual": 70.6,
        "Energy Availability Factor[%]_Cumulative": 72.5,
        "Load Factor[%]_Annual": 69.3,
        "Load Factor[%]_Cumulative": 68.7
    },
    {
        "Year": 1997,
        "Electricity Supplied[GW.h]": 2720.14,
        "Reference Unit Power[MW]": 335,
        "Annual Time On Line[h]": 8329,
        "Operation Factor[%]": 95.1,
        "Energy Availability Factor[%]_Annual": 93.4,
        "Energy Availability Factor[%]_Cumulative": 73.4,
        "Load Factor[%]_Annual": 92.7,
        "Load Factor[%]_Cumulative": 69.7
    },
    {
        "Year": 1998,
        "Electricity Supplied[GW.h]": 2374.36,
        "Reference Unit Power[MW]": 335,
        "Annual Time On Line[h]": 7242,
        "Operation Factor[%]": 82.7,
        "Energy Availability Factor[%]_Annual": 81.3,
        "Energy Availability Factor[%]_Cumulative": 73.7,
        "Load Factor[%]_Annual": 80.9,
        "Load Factor[%]_Cumulative": 70.1
    },
    {
        "Year": 1999,
        "Electricity Supplied[GW.h]": 1395.5,
        "Reference Unit Power[MW]": 335,
        "Annual Time On Line[h]": 4364,
        "Operation Factor[%]": 49.8,
        "Energy Availability Factor[%]_Annual": 47.8,
        "Energy Availability Factor[%]_Cumulative": 72.7,
        "Load Factor[%]_Annual": 47.6,
        "Load Factor[%]_Cumulative": 69.2
    },
    {
        "Year": 2000,
        "Electricity Supplied[GW.h]": 1677.85,
        "Reference Unit Power[MW]": 335,
        "Annual Time On Line[h]": 5038,
        "Operation Factor[%]": 57.4,
        "Energy Availability Factor[%]_Annual": 56.8,
        "Energy Availability Factor[%]_Cumulative": 72.1,
        "Load Factor[%]_Annual": 57.0,
        "Load Factor[%]_Cumulative": 68.8
    },
    {
        "Year": 2001,
        "Electricity Supplied[GW.h]": 1425.96,
        "Reference Unit Power[MW]": 335,
        "Annual Time On Line[h]": 4407,
        "Operation Factor[%]": 50.3,
        "Energy Availability Factor[%]_Annual": 48.7,
        "Energy Availability Factor[%]_Cumulative": 71.2,
        "Load Factor[%]_Annual": 48.6,
        "Load Factor[%]_Cumulative": 68.0
    },
    {
        "Year": 2002,
        "Electricity Supplied[GW.h]": 1011.5,
        "Reference Unit Power[MW]": 335,
        "Annual Time On Line[h]": 3030,
        "Operation Factor[%]": 34.6,
        "Energy Availability Factor[%]_Annual": 34.6,
        "Energy Availability Factor[%]_Cumulative": 70.0,
        "Load Factor[%]_Annual": 34.5,
        "Load Factor[%]_Cumulative": 66.9
    },
    {
        "Year": 2003,
        "Electricity Supplied[GW.h]": 2020.6,
        "Reference Unit Power[MW]": 335,
        "Annual Time On Line[h]": 6094,
        "Operation Factor[%]": 69.6,
        "Energy Availability Factor[%]_Annual": 68.8,
        "Energy Availability Factor[%]_Cumulative": 69.9,
        "Load Factor[%]_Annual": 68.8,
        "Load Factor[%]_Cumulative": 66.9
    },
    {
        "Year": 2004,
        "Electricity Supplied[GW.h]": 2725.01,
        "Reference Unit Power[MW]": 335,
        "Annual Time On Line[h]": 8250,
        "Operation Factor[%]": 93.9,
        "Energy Availability Factor[%]_Annual": 92.2,
        "Energy Availability Factor[%]_Cumulative": 70.6,
        "Load Factor[%]_Annual": 92.6,
        "Load Factor[%]_Cumulative": 67.8
    },
    {
        "Year": 2005,
        "Electricity Supplied[GW.h]": 1997.96,
        "Reference Unit Power[MW]": 335,
        "Annual Time On Line[h]": 7004,
        "Operation Factor[%]": 80.0,
        "Energy Availability Factor[%]_Annual": 68.5,
        "Energy Availability Factor[%]_Cumulative": 70.6,
        "Load Factor[%]_Annual": 68.1,
        "Load Factor[%]_Cumulative": 67.8
    },
    {
        "Year": 2006,
        "Electricity Supplied[GW.h]": 2100.55,
        "Reference Unit Power[MW]": 335,
        "Annual Time On Line[h]": 6403,
        "Operation Factor[%]": 73.1,
        "Energy Availability Factor[%]_Annual": 72.1,
        "Energy Availability Factor[%]_Cumulative": 70.6,
        "Load Factor[%]_Annual": 71.6,
        "Load Factor[%]_Cumulative": 67.9
    },
    {
        "Year": 2007,
        "Electricity Supplied[GW.h]": 2718.74,
        "Reference Unit Power[MW]": 335,
        "Annual Time On Line[h]": 8300,
        "Operation Factor[%]": 94.8,
        "Energy Availability Factor[%]_Annual": 93.8,
        "Energy Availability Factor[%]_Cumulative": 71.3,
        "Load Factor[%]_Annual": 92.6,
        "Load Factor[%]_Cumulative": 68.6
    },
    {
        "Year": 2008,
        "Electricity Supplied[GW.h]": 2481.26,
        "Reference Unit Power[MW]": 335,
        "Annual Time On Line[h]": 7562,
        "Operation Factor[%]": 86.1,
        "Energy Availability Factor[%]_Annual": 85.3,
        "Energy Availability Factor[%]_Cumulative": 71.7,
        "Load Factor[%]_Annual": 84.3,
        "Load Factor[%]_Cumulative": 69.1
    },
    {
        "Year": 2009,
        "Electricity Supplied[GW.h]": 2397.18,
        "Reference Unit Power[MW]": 335,
        "Annual Time On Line[h]": 7296,
        "Operation Factor[%]": 83.3,
        "Energy Availability Factor[%]_Annual": 82.9,
        "Energy Availability Factor[%]_Cumulative": 72.0,
        "Load Factor[%]_Annual": 81.7,
        "Load Factor[%]_Cumulative": 69.5
    },
    {
        "Year": 2010,
        "Electricity Supplied[GW.h]": 2782.75,
        "Reference Unit Power[MW]": 335,
        "Annual Time On Line[h]": 8560,
        "Operation Factor[%]": 97.7,
        "Energy Availability Factor[%]_Annual": 95.5,
        "Energy Availability Factor[%]_Cumulative": 72.7,
        "Load Factor[%]_Annual": 94.8,
        "Load Factor[%]_Cumulative": 70.2
    },
    {
        "Year": 2011,
        "Electricity Supplied[GW.h]": 2334.46,
        "Reference Unit Power[MW]": 335,
        "Annual Time On Line[h]": 7289,
        "Operation Factor[%]": 83.2,
        "Energy Availability Factor[%]_Annual": 79.6,
        "Energy Availability Factor[%]_Cumulative": 72.9,
        "Load Factor[%]_Annual": 79.6,
        "Load Factor[%]_Cumulative": 70.4
    },
    {
        "Year": 2012,
        "Electricity Supplied[GW.h]": 2477.36,
        "Reference Unit Power[MW]": 335,
        "Annual Time On Line[h]": 7521,
        "Operation Factor[%]": 85.6,
        "Energy Availability Factor[%]_Annual": 84.2,
        "Energy Availability Factor[%]_Cumulative": 73.2,
        "Load Factor[%]_Annual": 84.2,
        "Load Factor[%]_Cumulative": 70.8
    },
    {
        "Year": 2013,
        "Electricity Supplied[GW.h]": 2449.53,
        "Reference Unit Power[MW]": 340,
        "Annual Time On Line[h]": 7310,
        "Operation Factor[%]": 83.4,
        "Energy Availability Factor[%]_Annual": 82.6,
        "Energy Availability Factor[%]_Cumulative": 73.4,
        "Load Factor[%]_Annual": 82.8,
        "Load Factor[%]_Cumulative": 71.1
    },
    {
        "Year": 2014,
        "Electricity Supplied[GW.h]": 2631.71,
        "Reference Unit Power[MW]": 340,
        "Annual Time On Line[h]": 7875,
        "Operation Factor[%]": 89.9,
        "Energy Availability Factor[%]_Annual": 88.8,
        "Energy Availability Factor[%]_Cumulative": 73.8,
        "Load Factor[%]_Annual": 88.4,
        "Load Factor[%]_Cumulative": 71.5
    },
    {
        "Year": 2015,
        "Electricity Supplied[GW.h]": 1951.35,
        "Reference Unit Power[MW]": 340,
        "Annual Time On Line[h]": 6109,
        "Operation Factor[%]": 69.7,
        "Energy Availability Factor[%]_Annual": 66.0,
        "Energy Availability Factor[%]_Cumulative": 73.6,
        "Load Factor[%]_Annual": 65.5,
        "Load Factor[%]_Cumulative": 71.4
    },
    {
        "Year": 2016,
        "Electricity Supplied[GW.h]": 2476.82,
        "Reference Unit Power[MW]": 340,
        "Annual Time On Line[h]": 7700,
        "Operation Factor[%]": 87.7,
        "Energy Availability Factor[%]_Annual": 83.3,
        "Energy Availability Factor[%]_Cumulative": 73.8,
        "Load Factor[%]_Annual": 82.9,
        "Load Factor[%]_Cumulative": 71.6
    },
    {
        "Year": 2017,
        "Electricity Supplied[GW.h]": 2359.66,
        "Reference Unit Power[MW]": 340,
        "Annual Time On Line[h]": 7832,
        "Operation Factor[%]": 89.4,
        "Energy Availability Factor[%]_Annual": 79.7,
        "Energy Availability Factor[%]_Cumulative": 74.0,
        "Load Factor[%]_Annual": 79.2,
        "Load Factor[%]_Cumulative": 71.8
    },
    {
        "Year": 2018,
        "Electricity Supplied[GW.h]": 2274.09,
        "Reference Unit Power[MW]": 340,
        "Annual Time On Line[h]": 7393,
        "Operation Factor[%]": 84.4,
        "Energy Availability Factor[%]_Annual": 76.3,
        "Energy Availability Factor[%]_Cumulative": 74.0,
        "Load Factor[%]_Annual": 76.4,
        "Load Factor[%]_Cumulative": 71.9
    },
    {
        "Year": 2019,
        "Electricity Supplied[GW.h]": 2392.4,
        "Reference Unit Power[MW]": 340,
        "Annual Time On Line[h]": 7341,
        "Operation Factor[%]": 83.8,
        "Energy Availability Factor[%]_Annual": 80.3,
        "Energy Availability Factor[%]_Cumulative": 74.2,
        "Load Factor[%]_Annual": 80.3,
        "Load Factor[%]_Cumulative": 72.1
    },
    {
        "Year": 2020,
        "Electricity Supplied[GW.h]": 2680.41,
        "Reference Unit Power[MW]": 340,
        "Annual Time On Line[h]": 8067,
        "Operation Factor[%]": 91.8,
        "Energy Availability Factor[%]_Annual": 89.8,
        "Energy Availability Factor[%]_Cumulative": 74.5,
        "Load Factor[%]_Annual": 89.8,
        "Load Factor[%]_Cumulative": 72.5
    },
    {
        "Year": 2021,
        "Electricity Supplied[GW.h]": 2318.78,
        "Reference Unit Power[MW]": 340,
        "Annual Time On Line[h]": 7243,
        "Operation Factor[%]": 82.7,
        "Energy Availability Factor[%]_Annual": 77.8,
        "Energy Availability Factor[%]_Cumulative": 74.6,
        "Load Factor[%]_Annual": 77.8,
        "Load Factor[%]_Cumulative": 72.6
    },
    {
        "Year": 2022,
        "Electricity Supplied[GW.h]": 2034.01,
        "Reference Unit Power[MW]": 340,
        "Annual Time On Line[h]": 6528,
        "Operation Factor[%]": 74.5,
        "Energy Availability Factor[%]_Annual": 68.3,
        "Energy Availability Factor[%]_Cumulative": 74.4,
        "Load Factor[%]_Annual": 68.3,
        "Load Factor[%]_Cumulative": 72.5
    },
    {
        "Year": 2023,
        "Electricity Supplied[GW.h]": 2197.12,
        "Reference Unit Power[MW]": 340,
        "Annual Time On Line[h]": 6855,
        "Operation Factor[%]": 78.2,
        "Energy Availability Factor[%]_Annual": 73.8,
        "Energy Availability Factor[%]_Cumulative": 74.4,
        "Load Factor[%]_Annual": 73.8,
        "Load Factor[%]_Cumulative": 72.5
    }
]

df = pd.DataFrame(data)

electricity = df['Electricity Supplied[GW.h]'].values
print("Media:", np.mean(electricity))
print("Desviación Estándar:", np.std(electricity))
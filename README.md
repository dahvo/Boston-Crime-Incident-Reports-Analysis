# Crime Incident Reports Analysis

## Dataset Origin
The dataset used in this project is sourced from the Boston Police Department (BPD) and is available on the Boston Data Portal:
- [Crime Incident Reports Dataset](https://data.boston.gov/dataset/crime-incident-reports-august-2015-to-date-source-new-system/resource/b973d8cb-eeb2-4e7e-99da-c92938efc9c0)

Crime incident reports are provided by BPD to document the initial details surrounding an incident to which BPD officers respond. This dataset contains records from the new crime incident report system, which includes a reduced set of fields focused on capturing the type of incident as well as when and where it occurred. Records in the new system begin in June of 2015.

The records used in this project are from 1/1/2020 to 1/11/2025.

## Data Cleaning Strategy

### Processing Files
The following files were processed:
- `2020.csv`
- `2021.csv`
- `2022.csv`
- `2023-to-present.csv`

### Missing Values Summary
#### 2020.csv
```
                    Missing Values  Percentage
OFFENSE_CODE_GROUP           70894  100.000000
UCR_PART                     70894  100.000000
Lat                           1747    2.464242
Location                      1747    2.464242
Long                          1747    2.464242
DISTRICT                       278    0.392135
STREET                           1    0.001411
```

#### 2021.csv
```
                    Missing Values  Percentage
OFFENSE_CODE_GROUP           71721  100.000000
UCR_PART                     71721  100.000000
Lat                           2890    4.029503
Location                      2890    4.029503
Long                          2890    4.029503
DISTRICT                       993    1.384532
STREET                         679    0.946724
```

#### 2022.csv
```
                    Missing Values  Percentage
OFFENSE_CODE_GROUP           73852  100.000000
UCR_PART                     73852  100.000000
Lat                           3808    5.156258
Location                      3808    5.156258
Long                          3808    5.156258
DISTRICT                       171    0.231544
STREET                           1    0.001354
```

#### 2023-to-present.csv
```
                    Missing Values  Percentage
UCR_PART                    157637  100.000000
OFFENSE_CODE_GROUP          157637  100.000000
REPORTING_AREA               30311   19.228354
Long                         10137    6.430597
Lat                          10137    6.430597
Location                     10137    6.430597
DISTRICT                       358    0.227104
```

### Data Cleaning Decisions
- **Columns Removed**: `UCR_PART` and `OFFENSE_CODE_GROUP` (100% missing values)
- **Rows with Missing Location Data**: Excluded from location-specific analysis but included in other analyses.
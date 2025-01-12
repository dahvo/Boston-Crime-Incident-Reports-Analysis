# Crime Incident Reports Dataset - Data Dictionary

## Dataset Origin
The dataset used in this project is sourced from the Boston Police Department (BPD) and is available on the Boston Data Portal:
- [Crime Incident Reports Dataset](https://data.boston.gov/dataset/crime-incident-reports-august-2015-to-date-source-new-system/resource/b973d8cb-eeb2-4e7e-99da-c92938efc9c0)

Crime incident reports are provided by BPD to document the initial details surrounding an incident to which BPD officers respond. This dataset contains records from the new crime incident report system, which includes a reduced set of fields focused on capturing the type of incident as well as when and where it occurred. Records in the new system begin in June of 2015.

The records used in this project are from 1/1/2020 to 1/11/2025.
## Incident Details

| Variable Name | Type    | Description | Possible Values |
|--------------|---------|-------------|-----------------|
| _id | Numerical | Unique identifier for the record | Positive integers |
| INCIDENT_NUMBER | Numerical | Incident number | Positive integers |
| OFFENSE_CODE | Numerical | Code for the offense | Positive integers |
| OFFENSE_CODE_GROUP | Categorical | Group of the offense code | Various offense groups |
| OFFENSE_DESCRIPTION | Categorical | Description of the offense | Various offense descriptions |
| DISTRICT | Categorical | District where the incident occurred | Various district codes |
| REPORTING_AREA | Numerical | Reporting area code | Positive integers |
| SHOOTING | Categorical | Whether the incident involved a shooting | 0, 1 |
| OCCURRED_ON_DATE | DateTime | Date and time when the incident occurred | DateTime format |
| YEAR | Numerical | Year when the incident occurred | Four-digit year |
| MONTH | Numerical | Month when the incident occurred | 1-12 |
| DAY_OF_WEEK | Categorical | Day of the week when the incident occurred | Sunday, Monday, etc. |
| HOUR | Numerical | Hour when the incident occurred | 0-23 |
| UCR_PART | Categorical | Uniform Crime Reporting (UCR) part | Various UCR parts |
| STREET | Categorical | Street where the incident occurred | Various street names |
| Lat | Numerical | Latitude of the incident location | Decimal degrees |
| Long | Numerical | Longitude of the incident location | Decimal degrees |
| Location | String | Combined latitude and longitude | "(Lat, Long)" |

## Additional data

  As you can see above there isn't a categorical datapoint in order to simplify analysis, so I made one.


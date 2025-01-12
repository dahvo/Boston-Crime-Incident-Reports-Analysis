# Crime Incident Reports Dataset - Data Dictionary

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

## Notes

1. **Missing Values**
   - Missing values will be coded as 'NA'
   - Numerical variables: Will be handled using mean or median imputation based on distribution
   - Categorical variables: Will be handled using mode imputation or creating a 'Missing' category

2. **Derived Features**
   - incident_duration = (END_DATE - OCCURRED_ON_DATE).total_seconds() / 3600
   - is_weekend = DAY_OF_WEEK in ['Saturday', 'Sunday']

3. **Data Collection Context**
   - Data collected from crime incident reports
   - Purpose: Analyze crime patterns and trends
   - Scope: Incidents reported in a specific city

4. **Data Quality Considerations**
   - All categorical variables will be encoded appropriately for modeling
   - Numerical variables will be checked for outliers
   - Correlations between incident details will be analyzed
   - Incident reports will be validated for logical consistency
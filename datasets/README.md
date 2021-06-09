# Datasets

**Preprocessed Data**: Contains cleaned data used by ML model for identifying high risk regions.

**Other Data**: Contains sets of data extracted from sources used for visualizations and analysis, with added variable columns and data used in calculation of variables. See readme in Other Data folder for details. These files are intermediate to files in the Preprocessed Data folder. 

2016 Canada Census data is used here. Data was downloaded from the official site and relevant variables were extracted for regions of interest. Data was cleaned and formatted before using for modeling. The hierarchy of regions (e.g. Census subdivision, Census metropolitan areas) for which data is available varies among the datasets and therefore it was a challenge to find datasets with a matching system of regions for comparison. In certain cases, information for some regions was missing.

**Sources**:

Human Trafficking Incidents and Sexual Exploitation Incidents: 
[Statistics Canada. Table 35-10-0177-01  Incident-based crime statistics, by detailed violations, Canada, provinces, territories and Census Metropolitan Areas](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3510017701)

For this proof of concept, we looked at regions in Ontario for which human trafficking data is available.

Income: 
[Statistics Canada, 2016 Census of Population, Statistics Canada Catalogue no. 98-400-X2016133.](https://www12.statcan.gc.ca/census-recensement/2016/dp-pd/dt-td/Rp-eng.cfm?LANG=E&APATH=3&DETAIL=0&DIM=0&FL=A&FREE=0&GC=0&GID=0&GK=0&GRP=1&PID=111873&PRID=10&PTYPE=109445&S=0&SHOWALL=0&SUB=0&Temporal=2016&THEME=119&VID=0&VNAMEE=&VNAMEF=)

Aboriginal Population: [Statistics Canada, 2016 Census of Population, Statistics Canada Catalogue no. 98-400-X2016173.]( https://www12.statcan.gc.ca/census-recensement/2016/dp-pd/dt-td/Rp-eng.cfm?TABID=2&LANG=E&APATH=3&DETAIL=0&DIM=0&FL=A&FREE=0&GC=0&GID=1341753&GK=0&GRP=1&PID=111095&PRID=10&PTYPE=109445&S=0&SHOWALL=0&SUB=0&Temporal=2017&THEME=122&VID=0&VNAMEE=&VNAMEF=&D1=0&D2=0&D3=0&D4=0&D5=0&D6=0)

Employment & Education: [Statistics Canada, 2016 Census of Population, Statistics Canada Catalogue no. 98-400-X2016284.](https://www12.statcan.gc.ca/census-recensement/2016/dp-pd/dt-td/Rp-eng.cfm?TABID=2&LANG=E&APATH=3&DETAIL=0&DIM=0&FL=A&FREE=0&GC=3515&GID=1259598&GK=2&GRP=1&PID=111848&PRID=10&PTYPE=109445&S=0&SHOWALL=0&SUB=0&Temporal=2017&THEME=124&VID=0&VNAMEE=&VNAMEF=&D1=0&D2=0&D3=0&D4=0&D5=0&D6=0)

Latitude-Longitude Coordinates for Ontario Regions: https://developer.mapquest.com/documentation/tools/latitude-longitude-finder/

Latitude-Longitude Coordinates for GO Transit Stops used in Use Case: http://www.metrolinx.com/en/aboutus/opendata/default.aspx

Additional data found for future use:

Origin-Destination of Drivers - Record of Uber Trips: https://movement.uber.com/?lang=en-CA

Detailed Record of Uber Trips: https://www.kaggle.com/fivethirtyeight/uber-pickups-in-new-york-city



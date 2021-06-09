# Data Preprocessing:

For all of the datasets, we extracted Ontario regions for which human trafficking data is available and we removed the features where the whole row or column was empty. Footnotes and extra information were deleted as well. Please see file descriptions below for detailed processing in each dataset:

**File Descriptions**

CLEANhumantrafficking and CLEANaboriginal: <br /> 
St. Catharines-Niagara & Kitchener-Cambridge-Waterloo split up and data copied for each separate region

CLEANaboriginal: <br />
Prevalence of low income: The proportion or percentage of units whose income falls below a specified low-income line <br />
= in low income/ (in low income + not in low income) * 100 <br />
Variable 'prevalence of low income' used for map visualization

CLEANlabor_education: <br /> 
Total - Labour force status (column C) = Refers to whether a person aged 15 years and over was employed, unemployed or not in the labour force during the week of Sunday, May 1 to Saturday, May 7, 2016. <br />
Variable 'Unemployment rate' used for map visualization <br />
For measure of education level: % no postsecondary study = people with no postsecondary study / Total- major field of study * 100

CLEANincome: <br /> 
Prevalence of low income = in low income/ (in low income + not in low income) * 100
Prevalence of low income calculated for 'Total-household type', 'low income measure' = 1 (where 1 = after tax, 2 = before tax)

Lat_Long_Ontario_Cities: <br />
Latitudes and longitudes of center points for each of the selected regions for the proof of concept.

sample_GOtransit_locations: <br />
Latitudes and longitudes of GO transit stops in each of the selected regions for the proof of concept.

             
             


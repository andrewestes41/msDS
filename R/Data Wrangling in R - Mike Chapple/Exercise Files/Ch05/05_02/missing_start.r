# Data Wrangling in R
# 5.2 Missing and Special Values in R
#

# Load the tidyverse and the food inspections dataset
library(tidyverse)

names <- c("ID", "DBAName", "AKAName", "License", "FacilityType", "Risk", "Address", 
           "City", "State", "ZIP", "InspectionDate", "InspectionType", "Results",
           "Violations", "Latitude","Longitude","Location")

inspections <- read_csv('http://594442.youcanlearnit.net/inspections.csv', 
                        col_names=names, skip=1)

# Look at a summary of the data
summary(inspections)


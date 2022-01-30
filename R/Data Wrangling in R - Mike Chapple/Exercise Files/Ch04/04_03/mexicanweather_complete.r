# Data Wrangling in R
# 4.3 Making Long Datasets Wide with Spread

# Load the tidyverse
library(tidyverse)

# Read the dataset
weather <- read_csv("http://594442.youcanlearnit.net//mexicanweather.csv")

# Let's look at what we have
weather

# And use spread() to make it wider
weather.wide <- spread(weather, element, value)

# Where are we now?
weather.wide


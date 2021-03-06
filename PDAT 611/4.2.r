suppressPackageStartupMessages(library(nycflights13))
suppressPackageStartupMessages(library(tidyverse))
tictok

flights <- flights
airlines <- airlines
airports <- airports
planes <- planes
weather <- weather


flights.September <- flights %>%
  filter(month == 9) %>%
  filter(day == 29) %>%
  filter(origin == "EWR")
flights.September <- flights.September


weather.September <- weather %>%
  filter(month == 9) %>%
  filter(day == 29)
view(weather.September)

tib1 <- inner_join(airlines, flights.September)

NewarkSept29 <- tib1 %>%
  select(month, day, hour, name)
view(NewarkSept29)


install.packages("nycflights13")
library(nycflights13)
library(tidyverse)
flights



nycMarch <- filter(flights, month==3)
nycMarch <- subset(nycMarch, select = -c(origin, dest))
nycMarch <- nycMarch %>% arrange(desc(tailnum))
nycMarch

hist(nycMarch$dep_delay,
     xlab="Delayed Arrival", ylab="Delayed Departure",
     main="Delated Arrivals Correlation on Departures")



model <- lm(arr_delay ~ dep_delay, nycMarch)
summary(model)
scatter.smooth(x=nycMarch$arr_delay, y=nycMarch$dep_delay, main="Arrival ~ Departure") 
# Scatter plot
plot(nycMarch$arr_delay, nycMarch$dep_delay,
     xlab="Delayed Arrival", ylab="Delayed Departure",
     main="Delated Arrivals Correlation on Departures",
     pch = 19,
     col = factor(nycMarch$carrier))
legend("bottomright",
       legend = levels(factor(nycMarch$carrier)),
       pch = 19,
       col = factor(levels(factor(nycMarch$carrier))))



plot(flights$arr_delay, flights$dep_delay,
     xlab="Delayed Arrival", ylab="Delayed Departure",
     main="Delated Arrivals Correlation on Departures",
     pch = 19,
     col = factor(flights$carrier))
legend("bottomright",
       legend = levels(factor(flights$carrier)),
       pch = 19,
       col = factor(levels(factor(flights$carrier))))
#It took an extra 18.09 seconds to run the full dataset. 
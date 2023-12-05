library(AmesHousing)
library(tidyverse)
library(ggplot2)
Ames <- make_ames()

Ames.50 <- Ames %>%
  filter(Ames$Year_Built >= 1950)

Ames2 <- Ames %>% 
  mutate(Remodeled = Ames$Year_Built != Ames$Year_Remod_Add)
  

set.seed(248)
t.test(Sale_Price ~ Remodeled, data=Ames2)

#The mean group in TRUE is very different: 176k vs 206k

oneC <- 
  ggplot() +
    geom_point(data=Ames.50, aes(Sale_Price/1000, Year_Remod_Add, color="lightred")) +
    geom_point(data=Ames2, aes(Sale_Price/1000,  Year_Built, color="darkblue"))
oneC + coord_flip()
#A recently remodeled home offers more value than a home that was remodeled 70+ years ago
#New houses are priced similarly to recently remodeld homes


n1 <- 50
n2 <- 50
mu1 <- 15
mu2 <- 17
sigma1 <- 8
sigma2 <- 8

first <- rnorm(n1, mean = mu1, sd = sigma1)
second <- rnorm(n2, mean = mu2, sd = sigma2)
t.test(first, second, alternative = "two.sided", paired = FALSE, var.equal = FALSE)

t.test(first, second, alternative = "two.sided", paired = TRUE, var.equal = FALSE)
#Comparing the two samples, there is a statistically significant difference between the two groups.
#With a p-value of .01485, it is a strongly correlated. 
#Group 1 is not as successful, on average, at reducing the BP as Group 2
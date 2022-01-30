library(AmesHousing)
library(tidyverse)
Ames <- make_ames()

?ggplot
p <- ggplot(Ames, aes(Sale_Price/1000, Overall_Cond))
p + geom_boxplot()
#Typically overall condition correlates to price 
#The Average boxplot is different due to several outliers on the higher end
#This indicates that there is another factor influencing price within the average class

?geom_jitter
d <- p + geom_jitter(aes(colour = Year_Built)) + 
          labs(title="Plot of Price by Condition and Year Built and Lot Size",x="Sale Price in Thousands", y = "Overall Condition Rating") +
          theme(axis.text.x = element_text(angle=90, hjust=1)) +
          scale_x_continuous(breaks=seq(0, 900, by=100))
z <- d + coord_flip()
t <- z + geom_jitter(aes(size = Lot_Area))
t <- t + stat_summary(fun = median, geom="point", shape=18, size=3, color="red")
t


a <- ggplot(data = Ames) +
  geom_boxplot(mapping = aes(x=reorder(Neighborhood, Sale_Price/1000, na.rm = TRUE), y = Sale_Price/1000)) +
  theme(axis.text.x = element_text(angle=90, hjust = 1)) +
  labs(title="Plot of Price by Neighborhood",x="Sale Price in Thousands", y = "Neighborhood")
a <- a + coord_flip()
a

           
           
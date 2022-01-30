install.packages("AmesHousing")
library(AmesHousing)
library(tidyverse)
Ames <- make_ordinal_ames()
head(Ames)
summary(Ames)

AmesNew <- filter(Ames, 'Year Built' > 1980)
AmecAC <- filter(Ames, 'Central Air' == "Y")
AmesPool <- filter(Ames, Pool_QC != "No Pool")
AmesPosh <- filter(Ames, Pool_QC != "No Pool" & Kitchen_Qual == "Excellent")
AmesNiceKitch <- filter(Ames, Kitchen_Qual == "Excellent" | Kitchen_Qual == "Good")

AmesOld <- arrange(Ames, Year_Built)
AmesCheap <- arrange(Ames, Sale_Price)
AmesExpensive <- arrange(Ames, desc(Sale_Price))

AmesSkinny <- select(Ames, Year_Built, Sale_Price, Gr_Liv_Area)
AmesAllButPrice <- select(Ames, -Sale_Price)
AmesSF <- select(Ames, contains("SF"))

AmesThousands <- mutate(Ames, Sale_Price_K = Sale_Price/1000)
AmesAcre <- mutate(Ames, Lot_Size_Acre = Lot_Area/43560)
AmesBig <- mutate(Ames, BigHouse = Gr_Liv_Area > 2500)
head(Ames)

#    %>% is pipe
# pipes send the result from the first line of the code to the second line

AmesChain <- Ames %>%
  mutate(Bath = Full_Bath + Half_Bath/2) %>%
  filter(Bath > 2 &
           Central_Air == "Y" &
           Year_Built > 1990 &
           Sale_Price < 400000) %>%
  arrange(desc(Sale_Price))

AmesGroup <- group_by(Ames, Kitchen_Qual)
AmesGroup <- Ames %>%
  group_by(Kitchen_Qual)

AmesKitchenPrice <- Ames %>%
  group_by(Kitchen_Qual) %>%
  summarize(n=n(), AvgPrice = mean(Sale_Price), MaxPrice = max(Sale_Price))
AmesKitchenPrice
View(AmesKitchenPrice)


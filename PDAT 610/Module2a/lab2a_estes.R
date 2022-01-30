# Importing Datasets
library(ggplot2)
library(dplyr)
abalone.url <-
  "https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data"
abalone.data <- read.csv(abalone.url, header=FALSE) #data does not have variable names
abalone.data

summary(abalone.data)
head(abalone.data)

colnames(abalone.data)[1] <- "sex"
colnames(abalone.data)[2] <- "length"
colnames(abalone.data)[3] <- "diameter"
colnames(abalone.data)[4] <- "height"
colnames(abalone.data)[5] <- "whole_weight"
colnames(abalone.data)[6] <- "shucked_weight"
colnames(abalone.data)[7] <- "viscera_weight"
colnames(abalone.data)[8] <- "shell_weight"
colnames(abalone.data)[9] <- "rings"



#What is the class of the data abalone.data? (Use class() function)
class(abalone.data)
#data frame

#What is the datatype of variable diameter? (Use typeof() function)
typeof(abalone.data$diameter)
#double

#Use the function summary() to find basic description of diameter and age (rings) of abalone.
summary(abalone.data$diameter)
summary(abalone.data$rings)

#Use the function mean() to find the mean of diameter of female abalone.
female.abalone=dplyr::filter(abalone.data,sex=='F')
male.abalone=dplyr::filter(abalone.data,sex=='M')
summary(female.abalone)
mean(female.abalone$diameter)
#https://rstudio-pubs-static.s3.amazonaws.com/408480_f4bdfd9620c84a9598e512f1a59e66f5.html


#	Assume Y: diameter and X: rings. What is???(X^' X)???^(-1) X^' Y ?  
#(Hint: Some matrix concepts are used here. 
#X^'means X transpose and  ???(X^' X)???^(-1) means inverse of (X^' X). 
#You want to find the R functions for transpose and inverse of the matrix. 
#I intentionally left this out so you can practice to find appropriate functions using google.)
library(MASS)
summary(abalone.data)
Y <- (abalone.data$diameter)
typeof(Y)
X <- as.numeric(abalone.data$rings)
typeof(X)

Z <- cbind(X,Y)
typeof(Z)

abalone.matrix <- matrix(Z)

t(abalone.matrix) #transpose
ginv(abalone.matrix) #inverse

#Can you think of an interesting question about Abalone? 
#(For example, do female abalone weigh more than male abalone?) 
#Make your own question and answer it. 
#You can use mean and standard deviation (function sd()) to answer the question. 
#If you wish, you can also use some graphs and even hypothesis test 
#(we have not discussed about these topics yet thus it is not mandatary for this assignment. 
#We will discuss all of these in later modules. 
#Try to figure out as much as you can and as much as you want).

#http://www.sthda.com/english/wiki/correlation-test-between-two-variables-in-r#install-and-load-required-r-packages

install.packages("ggpubr")
library("ggpubr")
summary(abalone.data)
corLengthAge <- cor.test(abalone.data$length, abalone.data$rings)
corWeightAge <- cor.test(abalone.data$whole_weight, abalone.data$rings) 
corHeightAge <- cor.test(abalone.data$height, abalone.data$rings)

sd(abalone.data$rings)

covLengthAge <- cov(abalone.data$length, abalone.data$rings)
covWeighthAge <- cov(abalone.data$whole_weight, abalone.data$rings)
covHeighthAge <- cov(abalone.data$height, abalone.data$rings)

#some further test would be calculating the likelihood the abalone is a M or F based upon length, weight, height
#https://rstudio-pubs-static.s3.amazonaws.com/408480_f4bdfd9620c84a9598e512f1a59e66f5.html
malemodel <- lm(rings~length+diameter+height+whole_weight+viscera_weight+shell_weight,data=male.abalone)
femalemodel <- lm(rings~length+diameter+height+whole_weight+viscera_weight+shell_weight,data=female.abalone)

x <- lm(rings~length,data=male.abalone)
y <- lm(rings~length,data=female.abalone)


#http://www.sthda.com/english/articles/39-regression-model-diagnostics/160-multicollinearity-essentials-and-vif-in-r/
install.packages("caret")
install.packages("car")
install.packages("tidyverse")
library(car)
library(caret)
library(tidyverse)

set.seed(123)
age.samples <- abalone.data$rings %>%
  createDataPartition(p = 0.8, list = FALSE)
train.data <- abalone.data[age.samples, ]
test.data <- abalone.data[-age.samples, ]

model1 <- lm(rings ~., data = train.data)

predictions <- model1 %>% predict(test.data)

data.frame(
  RMSE = RMSE(predictions, test.data$rings),
  R2 = R2(predictions, test.data$rings)
)

car.::vif(model1)

model2 <- lm(rings ~. -whole_weight -viscera_weight -diameter -length, data = train.data)

predictions <- model2 %>% predict(test.data)

data.frame(
  RMSE = RMSE(predictions, test.data$rings),
  R2 = R2(predictions, test.data$rings)
)

car::vif(model2)

hist(abalone.data$rings)
plot(abalone.data$rings, abalone.data$length)

male.bp = abalone.data$Rings[which(abalone.data$sex=='M')] 
female.bp = abalone.data$Rings[which(abalone.data$sex=='F')] 
my.bp <- boxplot(Alive,Dead,
                 main = "Ages Distribution of Abalone by Genders",
                 ylab = "Ages",
                 names = c("Male", "Female"))



#https://github.com/nishitpatel01/predicting-age-of-abalone-using-regression

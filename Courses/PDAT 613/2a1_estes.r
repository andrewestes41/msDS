library(tidyverse)
library(MASS)
library(leaps)
library(car)
insurance <- read.csv("Insurance_A.csv", colClasses=c('numeric', 'factor', 'numeric', 'numeric', 'factor', 'factor', 'numeric'))

#####################################simple linear regression########################################
#checking for a relationship
scatter.smooth(insurance$expenses, insurance$bmi)
cor(insurance$expenses, insurance$bmi)

#checking for distribution (http://r-statistics.co/Linear-Regression.html)
  #divide graph area in 2 columns
par(mfrow=c(1, 2))  

  #density plot for expenses
plot(density(insurance$expenses), main="Density Plot: Expenses", ylab="Cost", sub=paste("Skewness:", round(insurance::skewness(insurance$expenses), 2)))
polygon(density(insurance$expenses), col="red")

  #density plot for bmi
plot(density(insurance$bmi), main="Density Plot: BMI", ylab="Cost", sub=paste("Skewness:", round(insurance::skewness(insurance$bmi), 2)))
polygon(density(insurance$bmi), col="red")


  #Creating a Simple linear model
simpleLR <- lm(expenses ~ bmi, insurance)
summary(simpleLR)
plot(simpleLR)

#analysis
  #The P-Value is well under the .05 threshold. 
  #The F-Statistic also shows a significantly increased model fit. 
  #R-Squared and Adjusted R-Squared are insignificant. 
  #The RSE is 11870. MSE is therefore 11870/142 = 83.59
  #Residuals vs fitted is a poor fit (there is a group or residuals above 2,000 which should be in the negatives to continue the downward sloping pattern)
  #q-q is somewhat flose to the linear line
  #scale location shows nothing obvious
  #cook's distance in residuals vs leverage graph goes from -2 to 4. There are some influenctial poitns, but disregarding them, -1 to 3 is the range which strongly indicates non-linearity

#####################################multiple linear regression########################################
#variable selection (http://www.sthda.com/english/articles/37-model-selection-essentials-in-r/154-stepwise-regression-essentials-in-r/)
  #Fit the full model 
full.model <- lm(expenses ~., data = insurance)
summary(full.model)
  #Forward and Backward variable selection model
step.model <- stepAIC(full.model, direction = "both", trace = FALSE)
summary(step.model)
  #Backward selection only model. 
back.model <- stepAIC(full.model, direction = "backward", trace = FALSE)
summary(back.model)

plot(step.model)
#residual vs fitted shows two distinct groups at the 30,000 amount on the x-axis
#q-q shows a clear deviation from linearity
#scale location shows two distinct groups (10k and 30k)
#residuals vs leverage (cooks distance) goes to -2 and +4. Using the common threshold of 1, this is obviously non-linear

#####################################additional analysis########################################
  #finding the one best predictor 
models <- regsubsets(expenses ~., data = insurance, nvmax = 2, method = "seqrep")
summary(models)
  #indicates "smoker" is the most important factor
smoke <- lm(expenses ~ smoker, insurance)
summary(smoke)
plot(smoke)
  #p value is significant
  #f statistic increased from 54 with BMI to 2178
  #mse decreased to 7470/142 to 52.61
  #r-squared and adjusted r-squared were above .6194
  #just looking at the absolute value of the estimates for the full model, smoker is clearly the largest value
  #the residual vs fitted shows a clear distinction between the two groups
  #the normal q-q plot is predominantly on the line
  #scale-location shows two clear groups
  #cooks distance is less than .003


#backward regression on model excluding smoking
no.smoke <- lm(expenses ~ . -smoker, insurance)
no.smoke.step <- stepAIC(no.smoke, direction = "both", trace = FALSE)
summary(no.smoke.step)
  #age, being a male, bmi, and having children are statistically significant. 
  #being a male is nearly 3x as impactful as the next highest absolute value, which is having children
  #being a male is nearly 5x as impactful as the other two variables, age and bmi

#graphically showing difference in expenses between non-smokers and smokers
boxplot(insurance$smoker, insurance$expenses)

#graphically showing the affect on expense by each individual predictor
avPlots(step.model)
avPlots(no.smoke.step)

smoke <- insurance %>%
  filter(smoker=='yes')
  
no.smoke <- insurance %>%
  filter(smoker=="no")

insurance.male <- insurance %>%
  filter(sex == 'male') %>%
  filter(smoker=='yes')

insurance.female <- insurance %>%
  filter(sex == 'female')
  filter(smoker=='yes')


115/662
159/676
.2352071/.173716
115+159
159/274
.58/.42
676/1338

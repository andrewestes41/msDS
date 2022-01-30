install.packages("titanic")
library(titanic)


###################################step 3##################################
summary(titanic_train)
  

###################################step 4##################################
?table
titanic_table <- table(titanic_train$Survived, titanic_train$Pclass)
titanic_table
#1st class passengers were the only Pclass more likely to survive than not
#there were less 2 Pclass passengers than either 1Pclass or 3Pclass


###################################step 5##################################
hist(titanic_train$Age)  
#younger passengers outlived older passengers
#is that due to age or due to number of passengers within each age group?


###################################step 6##################################
?boxplot
help(bx)
#https://www.programmingr.com/examples/how-to-make-a-side-by-side-boxplot-in-r/
Alive = titanic_train$Age[which(titanic_train$Survived==1)] 
Dead = titanic_train$Age[which(titanic_train$Survived==0)]  
my.bp <- boxplot(Alive,Dead,
          main = "Ages of Survivors vs Non-Survivors",
          ylab = "Ages",
          names = c("Alive", "Dead"))

#there appears to be no difference in the age distribution of who survived


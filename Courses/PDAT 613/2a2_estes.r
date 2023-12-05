library(tidyverse)
library(MASS)
library(leaps)
library(car)
library(caret)
library(rpart)
library(rpart.plot)
library(randomForest)
library(e1071)

insurance <- read.csv("Insurance_A.csv", colClasses=c('numeric', 'factor', 'numeric', 'numeric', 'factor', 'factor', 'numeric'))

#creating training/test datasets
set.seed(8940)
ins <- sample(1:nrow(insurance), 0.70*floor(nrow(insurance)))
ins.train <- insurance[ins, ]
ins.test <- insurance[-ins, ]

#linear model
ins.lm <- lm(expenses ~., data=ins.train)
ins.train.lm.pred <- predict(ins.lm, newdata= ins.train)
RMSE(ins.train$expenses, ins.train.lm.pred)

ins.test.lm.predict <- predict(ins.lm, newdata = ins.test)
RMSE(ins.test$expenses, ins.test.lm.predict)

ins.step <- step(ins.lm, trace=0)
ins.test.step.pred <- predict(ins.step, newdata=ins.test)
RMSE(ins.test$expenses, ins.test.step.pred)

#CART model
ins.rpart <- rpart(expenses ~., data=ins.train)
rpart.plot(rpart(expenses ~., data=ins.train))
ins.test.rpart.pred <- predict(ins.rpart, newdata=ins.test) 
RMSE(ins.test$expenses, ins.test.rpart.pred)    

#random forest model
ins.rf <- randomForest(expenses ~ ., data=ins.train)
ins.test.rf.pred <- predict(ins.rf, newdata=ins.test)
RMSE(ins.test$expenses, ins.test.rf.pred)
ins.rf

RMSEoob <- sqrt(22412374)
RMSEoob

varImpPlot(ins.rf)
#################################################################
drybeans <- read.csv("beans.csv")

set.seed(65489)
beans <- sample(1:nrow(drybeans), 0.70*floor(nrow(drybeans)))
beans.train <- drybeans[beans, ]
beans.test <- drybeans[-beans, ]


#CART model
beans.rpart <- rpart(Class ~., data=beans.train)
rpart.plot(rpart(Class ~., data=beans.train))
beans.test.rpart.pred <- predict(beans.rpart, newdata=beans.test) 
RMSE(beans.test$Class, beans.test.rpart.pred)    

#random forest model
beans.rf <- randomForest(Class ~ ., data=beans.train)
beans.test.rf.pred <- predict(beans.rf, newdata=beans.test)
RMSE(beans.test$Class, beans.test.rf.pred)
beans.rf

#SVM
beans.svm <- svm(Class ~., data=beans.train)
beans.svm.pred <- predict(beans.svm, newdata=beans.test)

confusionMatrix(beans.svm.pred, beans.test$Class, positive="TRUE")

#logistic regression
beans.log <- glm(Class ~ ., data=beans.train, family="binomial")
summary(beans.log)
confusionMatrix(beans.log, beans.test$Class, positive="TRUE")
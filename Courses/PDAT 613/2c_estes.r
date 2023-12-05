#install.packages("pacman", "cvms", "ranger")
pacman::p_load(tidymodels, 
               tidyverse, 
               ggplot2, 
               MASS, 
               leaps, 
               car, 
               caret, 
               rpart, 
               rpart.plot, 
               randomForest, 
               pROC, 
               factoextra, 
               dplyr, 
               hablar, 
               cvms,
               ranger)

#loading the data
df_original <- read.csv("ObesityDataSet_raw_and_data_sinthetic.csv", stringsAsFactors = TRUE)
df <- subset(df_original, select=-c(Height, Weight))

#creating training/test datasets
set.seed(1234)
split <- sample(1:nrow(df), 0.75*floor(nrow(df)))
split.train <- df[split, ]
split.test <- df[-split, ]

################################################################################################################################
#ATTEMPT 1.1 
#untuned random forest
train.rf <- rand_forest(
  mode="classification",
  engine="randomForest") %>%
  fit(NObeyesdad ~ ., data = split.train) 

test1.1 <- predict(train.rf, new_data=split.test)
class(test1.1)
class(split.test$NObeyesdad)
table(test1.1)


rf.1 <- randomForest(NObeyesdad ~ ., data=split.train)
rf.1.pred <- predict(rf.1, newdata=split.test)
table(rf.1.pred)

confusionMatrix(rf.1.pred, split.test$NObeyesdad)

################################################################################################################################
#ATTEMPT 1.2
tree.model.fit <- rand_forest() %>%
  set_engine("randomForest") %>%
  set_mode("classification") %>%
  fit(NObeyesdad ~., data = split.train)

test1.2 <- predict(tree.model.fit, new_data = split.test)
class(test1.2)
class(split.test$NObeyesdad)
table(test1.2)

################################################################################################################################
#ATTEMP 1.3
rf.mod <- 
  rand_forest(trees = 1000) %>%
  set_engine("ranger") %>%
  set_mode("classification")

rf.fit <-
  rf.mod %>%
  fit(NObeyesdad ~., data = split.train)

test1.3 <- predict(rf.fit, split.test) 
class(test1.3)
class(split.test$NObeyesdad)
table(test1.3)

################################################################################################################################
################################################################################################################################
################################################################################################################################
#evaluating untuned random forest
# need to figure out how to make test.rf.pred a factor instead of df so the confusion matrix can be calculated
# or need to figure out how to make the cf df have the same length in the system
#https://cran.r-project.org/web/packages/cvms/vignettes/Creating_a_confusion_matrix.html
cf <- tibble("target" = split.test$NObeyesdad,
             "prediction" = test.rf.pred)

conf_mat <- confusion_matrix(targets = cf$target,
                             predictions = cf$prediction)

################################################################################################################################
#setting up the grid
tree_grid <- grid_regular(cost_complexity(),
                          tree_depth(),
                          levels = 5)
head(tree_grid, 10)

tree_grid2 <- grid_regular(mtry(c(1, 14)),
                           min_n(),
                           levels = 5)
head(tree_grid2, 10)
################################################################################################################################
#re-sampling
rf.wf <-
  workflow() %>%
  add_model(rf.mod) %>%
  add_formula(NObeyesdad ~ .)

folds <- vfold_cv(split.train, v = 10)

rf_fit_rs <-
  rf_wf %>%
  fit_resamples(folds)

rf_fit_rs
collect_metrics(rf_fit_rs)

################################################################################################################################
################################################################################################################################
################################################################################################################################
#ATTEMPT 2.1
tuned.train.rf <- rand_forest(
  mode="classification",
  engine="randomForest",
  mtry = (c(1, 14)),
  min_n = tune(), 
  ) %>%
  fit(NObeyesdad ~ ., data = split.train)

predict(tuned.train.rf, new_data = split.test)

################################################################################################################################
#ATTEMPT 2.2
tuned.tree.model.fit <- rand_forest(
  cost_complexity= tune(),
  tree_depth = tune()
  ) %>%
    set_engine("randomForest") %>%
    set_mode("classification") %>%
    mtry = (c(1, 14)) %>%
    min_n = tune() %>%
    fit(NObeyesdad ~., data = split.train)

predict(tuned.tree.model.fit, new_data = split.test)

################################################################################################################################
#ATTEMPT 2.3
tune_spec <-
  rand_forest() %>%
  set_engine("randomForest") %>%
  set_mode("classification")
tune_spec  

rf.tune.results <-
  tune_spec %>%
  tune_grid(NObeyesdad ~ ., resamples = folds)

rf.tune.results %>% collect_metrics() %>% head()

rf.tune.results %>% collect_metrics() %>%
  filter(.metric == "accuracy") %>%
  mutate(tree_depth = factor(tree_depth)) %>%
  ggplot(aes(x=cost_complexity, y=mean, color=tree_depth)) +
  geom_line() + geom_point() + ylab("Accuracy")

################################################################################################################################
#ATTEMPT 2.4
tune_spec2 <- 
  rand_forest(
    mtry = tune(),
    min_n = tune(),
  ) %>% 
  set_engine("randomForest") %>% 
  set_mode("classification")
tune_spec2

rf.tune2.results <-
  tune_spec2 %>%
  tune_grid(NObeyesdad ~ ., resamples = folds, grid = tree_grid2)

rf.tune2.results %>% collect_metrics() %>% head()

rf.tune2.results %>% collect_metrics() %>%
  filter(.metric == "accuracy") %>%
  mutate(mtry = factor(mtry)) %>%
  ggplot(aes(x=mtry, y=mean)) +
  geom_line() + geom_point() + ylab("Accuracy")

################################################################################################################################
#ATTEMPT 2.5
tune_spec3 <- 
  decision_tree(
    cost_complexity = tune(),
    tree_depth = tune()
  ) %>% 
  set_engine("rpart") %>% 
  set_mode("classification")
tune_spec3

rf.tune3.results <-
  tune_spec3 %>%
  tune_grid(NObeyesdad ~ ., resamples = folds)

rf.tune3.results %>% collect_metrics() %>% head()

rf.tune3.results %>% collect_metrics() %>%
  filter(.metric == "accuracy") %>%
  mutate(tree_depth = factor(tree_depth)) %>%
  ggplot(aes(x=cost_complexity, y=mean, color=tree_depth)) +
  geom_line() + geom_point() + ylab("Accuracy")

################################################################################################################################
#ATTEMPT 3.1
best.params <- rf.tune2.results %>% select_best(metric="accuracy")
best.model <- tune_spec2 %>%
  finalize_model(best.params) %>%
  fit(NObeyesdad ~ ., data=split.train)
best.model  


################################################################################################################################
#ATTEMPT 4.1
untuned <- predict(train.rf, new_data = split.test) %>% bind_cols(split.test)
tuned <- predict(best.model, new_data = split.test) %>% bind_cols(split.test)

a_predicted <- c(untuned$.pred_class)
b_actual <- c(untuned$NObeyesdad)
ab <- data.frame(a_predicted, b_actual)

c_predicted <- c(tuned$.pred_class)
d_actual <- c(tuned$NObeyesdad)
cd <- data.frame(c_predicted, d_actual)

untuned.cf <- confusionMatrix(ab$a_predicted, ab$b_actual)
untuned.cf

tuned.cf <- confusionMatrix(cd$c_predicted, cd$d_actual)
tuned.cf

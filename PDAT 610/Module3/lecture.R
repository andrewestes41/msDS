
test <- function(vector){
  minn <- min(vector)
  maxx <- max(vector)
  summ <- sum(vector)
  meann <- mean(vector)
  return(minn)
}

test(c(1, 3, 5, 7, 9, 6))

multi_return <- function(vector) {
  my_list <- list(min(vector), max(vector), sum(vector), mean(vector))
  return(my_list) 
}

a <- (c(1, 3, 5, 7, 9, 6))
multi_return(a)


a <- 1:5
b <- c(2, 4, 6, 8, 10)

a[1] == 1
a[1] > 2 & b[3] > 3
a[1] > 2 & b[3 > 3

a < 2 & b > 3              
a < 2 | b > 3              
a < 2 && b < 3

library("titanic")
data(titanic_train)
str(titanic_train)
head(titanic_train)
str(titanic_train)    

titanic_train$vect_if <-
  ifelse(titanic_train$Age <= 18, 1, 0)
str(titanic_train)

for(i in 1:nrow(titanic_train))
{
  if(is.na(titanic_train$Age[i])){
    titanic_train$for_if[i] <- NA
  } else if(titanic_train$Age[i] <= 18({
    titanic_train$for_if[i] <- 1
  } else
    titanic_train$for_if[i] <- o
}
  }))
  }
}

age_minor <- function(x){
  if(is.na(x)) return(x)
  else if (x <= 18) return (1)
  else return (0)
}

titanic_train$sap_if <- sapply(titanic_train$Age, age_minor)
str(titanic_train)

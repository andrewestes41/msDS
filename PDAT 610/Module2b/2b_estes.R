
library(tidyr)

kim <- read.csv("C:\\Users\\andre\\OneDrive\\Desktop\\PDAT 610\\Module2b\\Clean-KimData.csv")
head(kim)

#1
  #Determining the number of students who are either first year students or male
  #Results in 229 observations
maleORfirst <- filter(kim, Semester < 2 | Gender == "M" )
count(maleORfirst)

  #Determing the number of students who are both first year students and male
  #Utilizing piping, results in 43 observations
FreshOrMales <-kim %>% 
  filter(Semester < 2 & Gender == "M")
count(FreshOrMales)
  #The difference in observations is due to the difference of | vs. &

#2 
  #Mutating the table to create the BMI variable
kimBMI <- mutate(kim, BMI = 703 *(Weight/(h=Height^2)))

  #Mutating the table to create the Obese variable and viewing the results
kimData <- mutate(kimBMI, Obese = BMI > 30)
head(kimData)

#3
  #calculate average BMI for each year using "group_by and summarize" functions
kimData2 <- kimData %>% 
  mutate(Year = round(Semester/2)+1)
head(kimData2)


df <- kimData2 %>% group_by(Year)
df %>% summarise (
          avg = mean(BMI, na.rm = TRUE)
)


#4
  #calculate the percentage of obese students per year
  #does this show a trend?

  #filtering obesity by year
firstYearObese <- filter(df, Year == 1 & BMI > 30)
secondYearObese <- filter(df, Year == 2 & BMI > 30)
thirdYearObese <- filter(df, Year == 3 & BMI > 30)
fourthYearObese <- filter(df, Year == 4 & BMI > 30)
fifthYearObese <- filter(df, Year == 5 & BMI > 30)
sixthYearObese <- filter(df, Year == 6 & BMI > 30)


  #filtering data by year
firstYear <- filter(df, Year == 1)
secondYear <- filter(df, Year == 2)
thirdYear <- filter(df, Year == 3)
fourthYear <- filter(df, Year == 4)
fifthYear <- filter(df, Year == 5)
sixthYear <- filter(df, Year == 6)

  #dividing total number of obesity/yr by total respondents/yr
obeseFirstYr <- count(firstYearObese)/count(firstYear)
obeseSecondYr <- count(secondYearObese)/count(secondYear)
obeseThirdYr <- count(thirdYearObese)/count(thirdYear)
obeseFourthYr <- count(fourthYearObese)/count(fourthYear)
obeseFifthYr <- count(fifthYearObese)/count(fifthYear)
obeseSixthYr <- count(sixthYearObese)%/%count(sixYear)

  #output of the above division
obeseFirstYr 
obeseSecondYr
obeseThirdYr
obeseFourthYr
obeseFifthYr
obeseSixthYr

#5
  #calculate the average size of men and women's feet using all data points. 
  #calculate the average size of men's and women's feet excluding giant feet

  #removing all observances over 2 standard deviations away this is the result:
  #female average drops from 7.99 to 7.96
  #female SD drops from 1.33 to 1.17
  #male average drops from 11.51 to 10.81
  #male sd drops from 8.19 to 1.31

maleDF <- filter(df, Gender == "M")
mean(maleDF$Shoe.Size, na.rm = TRUE)
sd(maleDF$Shoe.Size, na.rm = TRUE)

maleDF2 <- filter(maleDF, Shoe.Size < 20)
mean(maleDF2$Shoe.Size, na.rm = TRUE)
sd(maleDF2$Shoe.Size, na.rm = TRUE)

maleDF3 <- filter(maleDF2, Shoe.Size > 7.86 & Shoe.Size < 13.9)
mean(maleDF3$Shoe.Size, na.rm = TRUE)
sd(maleDF3$Shoe.Size, na.rm = TRUE)



femaleDF <- filter(df, Gender == "F")
mean(femaleDF$Shoe.Size, na.rm = TRUE)
sd(femaleDF$Shoe.Size, na.rm = TRUE)

femaleDF2 <- filter(femaleDF, Shoe.Size > 5.33 & Shoe.Size < 10.65)
mean(femaleDF2$Shoe.Size, na.rm = TRUE)
sd(femaleDF2$Shoe.Size, na.rm = TRUE)


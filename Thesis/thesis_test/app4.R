#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#


#loading the libraries and setting up the dataframes and variables
#library(shiny)
library(plotly)
library(readxl)
library(tidyverse)
library(magrittr)
library(jpeg)
library(officer)


linebreaks <- function(n){HTML(strrep(br(), n))}

#setwd("C:\\Users\\andre\\OneDrive\\Desktop\\thesis_test")

z.orig.laps <- read.csv("laps.csv")
laps  <- z.orig.laps

z.orig.weather <- read.csv("weather.csv")
weather  <- z.orig.weather

z.orig.messages <- read.csv("messages.csv")
messages  <- z.orig.messages

z.orig.results <- read.csv("results.csv")
results  <- z.orig.results

documentation <- read_docx("documentation.docx")

word1 <- a(href="documentation.docx")


courses <- c(
  "Australia","Austria", "Bahrain","China", "Azerbaijan", "Spain", "Monaco", "Canada",
  "France","Austria","Great Britain","Germany","Hungary","Belgium","Italy",
  "Singapore","Russia","Japan","United States","Mexico","Brazil","United Arab Emirates",
  "Abu Dhabi","Portugal","Turkey","Netherlands","Qatar","Saudi Arabia")

#manipulating the message/flag data
flags <- messages %>%
  subset(Flag == "YELLOW" |
           Flag == "DOUBLE YELLOW" |
           Flag == "RED")


#manipulating the pitstop data
pitInOnly <- laps[complete.cases(laps$PitInTime),]
pitInVariables <- as.list(colnames(pitInOnly))

pit_by <- pitInOnly %>%
  group_by(RACE, Year, Team, Driver) %>%
  summarize()

#maniuplating the results data
points_by <- results %>%
  group_by(RACE, Year, TeamName, TeamColor, FullName, Points) %>%
  summarize() %>%
  mutate(Driver = sub(".* ", "", FullName)) %>%
  mutate(Driver = substr(Driver, 1, 3)) %>%
  mutate(Team = TeamName)

#manipulating the weather data
weatherAir_scale <- scale(weather$AirTemp)
weatherTrack_scale <- scale(weather$TrackTemp)
weatherHumidity_scale <- scale(weather$Humidity)
weatherPressure_scale <- scale(weather$Pressure)
weatherWind_scale <- scale(weather$WindSpeed)

weather_scale <- weather %>%
  mutate(AirScale = weatherAir_scale) %>%
  mutate(TrackScale = weatherTrack_scale) %>%
  mutate(HumidityScale = weatherHumidity_scale) %>%
  mutate(PressureScale = weatherPressure_scale) %>%
  mutate(WindScale = weatherWind_scale)

by_race <- weather_scale %>%
  group_by(RACE, Year) %>%
  summarise(
    meanAir = round(mean(AirTemp), 1),
    minAir = min(AirTemp),
    maxAir = max(AirTemp),
    rangeAir = maxAir - minAir,
    
    meanTrack = round(mean(TrackTemp), 1),
    minTrack = min(TrackTemp),
    maxTrack = max(TrackTemp),
    rangeTrack = maxTrack - minTrack,
    
    meanHumidity = round(mean(Humidity), 1),
    minHumidity = min(Humidity),
    maxHumidity = max(Humidity),
    rangeHumidity = maxHumidity - minHumidity,
    
    meanPressure = round(mean(Pressure), 1),
    minPressure = min(Pressure),
    maxPressure = max(Pressure),
    rangePressure = maxPressure - minPressure,
    
    meanWind = round(mean(WindSpeed), 1),
    minWind = min(WindSpeed),
    maxWind = max(WindSpeed),
    rangeWind = maxWind - minWind
  ) 

by_race_range <- data.frame(
  AirTemperatureMean = round(range(by_race$meanAir), 2),
  AirTemperatureRange = round(range(by_race$rangeAir), 2),
  
  TrackTemperatureMean = round(range(by_race$meanTrack), 2),
  TrackTemperatureRange = round(range(by_race$rangeTrack), 2),
  
  HumidityMean = round(range(by_race$meanHumidity), 2),
  HumidityRange = round(range(by_race$rangeHumidity), 2),
  
  AirPressureMean = round(range(by_race$meanPressure), 2),
  AirPressureRange = round(range(by_race$rangePressure), 2),
  
  WindSpeedMean = round(range(by_race$meanWind), 2),
  WindSpeedRange = round(range(by_race$rangeWind), 2)
)

totalweather <- weather %>%
  mutate(RACE = "RACE") %>%
  mutate(Year = "YEAR") %>%
  mutate(meanAir = round(mean(AirTemp)), 2) %>%
  mutate(meanTemp = round(mean(TrackTemp)), 2) %>%
  mutate(meanHumidity = round(mean(Humidity)), 2) %>%
  mutate(meanWind = round(mean(WindSpeed)), 2) %>%
  mutate(meanPressure = round(mean(Pressure)), 2) %>%
select(RACE, Year, meanAir, meanTemp, meanHumidity, meanWind, meanPressure)

# Define UI for application
ui <- fluidPage(

  sidebarLayout(
    sidebarPanel(
                # radioButtons("Histograms", "Histogram types",
                #              c("Courses" = "courses",
                #                "LapNumber" = "LapNumber",
                #                "Flag" = "Flag")),
      
                  selectInput(inputId = "courses",
                              label = h3("Select a Race"),
                              choices = courses,
                              multiple = FALSE, 
                              selected = "Australia"),
                 
                  sliderInput("Year", "Year:",
                              min = 2018, max = 2022,
                              value = c(2019, 2021),
                              step = 1),
                  
                  # selectInput(inputId =  "var1",
                  #             label = h3("Histogram of Which Lap Number Pit Stops Occur"),
                  #             choices = "LapNumber",
                  #             selected = "LapNumber"),
                  # 
                  # selectInput(inputId =  "var2",
                  #             label = h3("Histogram of Flag Frequency"),
                  #             choices = "Flag",
                  #             selected = "Flag"),
                 
                  selectInput(inputId =  "var4",
                              label = h3("Point Accumulation by Team or Driver"),
                              choices = c("Team", "Driver"),
                              selected = "Team*"),
                  
                  selectInput(inputId =  "var3",
                            label = h3("Pit Stops Frequency by Team or Driver"),
                            choices = c("Team", "Driver"),
                            selected = "Team"),
                  
                  selectInput("dataset", 
                              label = h3("Dataset Preview"),
                              choices = c("results", "messages", "weather", "laps")),
                  
                  linebreaks(0),
                  
                  downloadButton("downloadData", "Download Dataset",
                                 style="color: #fff; background-color: #337ab7; border-color: #2e6da4"),

                  # linebreaks(3),
                  # 
                  # selectInput("documentation",
                  #             label = h3("Documentation"),
                  #             choices = c("documentation")),
                  # 
                  # downloadButton('downloadDocumentation', 'Download Documentation',
                  #                style="color: #fff; background-color: #337ab7; border-color: #2e6da4"),
                  
                  linebreaks(10),
                  
                  word1,
                  a("Download Documentation", href="documentation.docx"),
                  
                  linebreaks(2),
                  
                  fileInput(inputId = "file1", 
                            label = "Attach Feedback")


    ),
  
    mainPanel(
            tabsetPanel(type = "tabs",

                 tabPanel("Course Visualization", fluidRow(
                        column(width=12,
                               imageOutput("img1")))),
                 
                 tabPanel("Lap # When Pit Stop",
                          fluidRow(
                            column(10, plotlyOutput("CoursesPlot")),
                            column(10, plotlyOutput("TotalPlot"))
                            )),
                 
                 tabPanel("Tyre Life When Pit Stop",
                          fluidRow(
                            column(10, plotlyOutput("TyrePlot")),
                            column(10, plotlyOutput("TotalTyrePlot"))
                          )),
                 
                 tabPanel("Weather", 
                          fluidRow(
                            dataTableOutput("weather"),
                            dataTableOutput("totalweather")
                          )),
                          
                 
                 tabPanel("Flag", plotlyOutput("FlagPlot")),
                 
                 tabPanel("Points", plotlyOutput("PointPlot")),
                 
                 tabPanel("Pit", plotlyOutput("PitPlot")),
                 
                 tabPanel("Preview Datasets", tableOutput("dataset")),
                 
                 #tabPanel("Documentation", textOutput("documentation"))
                 
                 
        )
      )
    )
)



# Define server logic
server <- function(input, output) {
 

  
#https://stackoverflow.com/questions/40861908/shiny-r-implement-slider-input

  output$CoursesPlot <- renderPlotly({
    p <- pitInOnly %>%
      subset(LapNumber!=1) %>%
      mutate(
        courses = input$courses) %>%
      filter(
        RACE == courses) %>%
      filter(
        Year >= input$Year[1] & Year <= input$Year[2]
      ) %>%
      ggplot(aes(x = LapNumber)) +
        geom_histogram() +
      ggtitle("Lap Number When Driver Came in for PitStop By Course and Year")
    
      ggplotly(p)
  })
  
  output$TyrePlot <- renderPlotly({
    p1 <- pitInOnly %>%
      subset(LapNumber!=1) %>%
      mutate(
        courses = input$courses) %>%
      filter(
        RACE == courses) %>%
      filter(
        Year >= input$Year[1] & Year <= input$Year[2]
      ) %>%
      ggplot(aes(x = TyreLife)) +
      geom_histogram() +
      ggtitle("Tyre Age When Driver Came in for PitStop By Course and Year")
    
    ggplotly(p1)
  })
  
  output$FlagPlot <- renderPlotly({
    p2 <- flags %>%
      mutate(
        courses = input$courses) %>%
      filter(
        RACE == courses) %>%
      filter(
        Year >= input$Year[1] & Year <= input$Year[2]
      ) %>%
      ggplot(aes(
                 x = Flag,
                 fill = Flag)) +
      geom_histogram(stat="count",
                     position = "dodge",
                     bins = 1) +
      scale_fill_manual(values = c("DOUBLE YELLOW" = "black", 
                                   "RED" = "red",
                                   "YELLOW" = "yellow")) +
      scale_color_manual(values = c("DOUBLE YELLOW" = "yellow", 
                                    "RED" = "red",
                                    "YELLOW" = "yellow")) +
      ggtitle("Quantification of Hazardous Flags by Course and Year")
    
    ggplotly(p2)
  })
  
  output$PitPlot <- renderPlotly({
    p3 <- pit_by %>%
      mutate(
        courses = input$courses) %>%
      filter(
        RACE == courses) %>%
      filter(
        Year >= input$Year[1] & Year <= input$Year[2]
      ) %>%
      ggplot(aes(y = .data[[input$var3]],
                 fill= Team)) +
      geom_bar() +
      ggtitle("Lap Number When Driver Came in for PitStop By Course and Year")
    
    ggplotly(p3)
  })
  
  output$PointPlot <- renderPlotly({
    p4 <- points_by %>%
      mutate(
        courses = input$courses) %>%
      filter(
        RACE == courses) %>%
      filter(
        Year >= input$Year[1] & Year <= input$Year[2]
      ) %>%
      ggplot(aes(x = Points, 
                 y = .data[[input$var4]],
                 fill=TeamName)) +
      geom_col() +
      ggtitle("Points Accumulated by Team or Driver By Course and Year")
    
    ggplotly(p4)
  })

  output$weather <- renderDataTable({by_race %>%
      mutate(
        courses = input$courses) %>%
      filter(
        RACE == courses) %>%
      select(Year, meanAir, meanTrack, meanHumidity, meanWind, meanPressure)
  })
  
  output$totalweather <- renderDataTable({
    head(totalweather, 1)
  })
  
  re1 <- reactive({
    input$file1
    })

  output$Invoice <- renderImage({
    re1()
    })

#  output$img1 <- renderImage({
#    list(src="C:\\Users\\andre\\OneDrive\\Desktop\\F1_Tracks\\Total_noDuplicate\\France.png")
#  })
  
  output$img1 <- renderImage({
    if(input$courses == "Abu Dhabi"){        
      list(src="C:\\Users\\andre\\OneDrive\\Desktop\\F1_Tracks\\Total_noDuplicate\\AbuDhabi.png", height = "500", width="800")
    } else if(input$courses == "Australia"){
      list(src="C:\\Users\\andre\\OneDrive\\Desktop\\F1_Tracks\\Total_noDuplicate\\Australian.png", height = "500", width="800")
    } else if(input$courses == "Austria"){
      list(src="C:\\Users\\andre\\OneDrive\\Desktop\\F1_Tracks\\Total_noDuplicate\\Austria.png",height = "500", width="800")
    } else if(input$courses == "Azerbaijan"){
      list(src="C:\\Users\\andre\\OneDrive\\Desktop\\F1_Tracks\\Total_noDuplicate\\Azerbaijan.png",height = "500", width="800")
    } else if(input$courses == "Bahrain"){
      list(src="C:\\Users\\andre\\OneDrive\\Desktop\\F1_Tracks\\Total_noDuplicate\\Bahrain.png",height = "500", width="800")
    } else if(input$courses == "Belgium"){
      list(src="C:\\Users\\andre\\OneDrive\\Desktop\\F1_Tracks\\Total_noDuplicate\\Belgium.png",height = "500", width="800")
    } else if(input$courses == "Brazil"){
      list(src="C:\\Users\\andre\\OneDrive\\Desktop\\F1_Tracks\\Total_noDuplicate\\Brazil",height = "500", width="800")
    } else if(input$courses == "Canada"){
      list(src="C:\\Users\\andre\\OneDrive\\Desktop\\F1_Tracks\\Total_noDuplicate\\Canada",height = "500", width="800")
    } else if(input$courses == "China"){
      list(src="C:\\Users\\andre\\OneDrive\\Desktop\\F1_Tracks\\Total_noDuplicate\\China.png",height = "500", width="800")
    } else if(input$courses == "France"){
      list(src="C:\\Users\\andre\\OneDrive\\Desktop\\F1_Tracks\\Total_noDuplicate\\France.png",height = "500", width="800")
    } else if(input$courses == "Germany"){
      list(src="C:\\Users\\andre\\OneDrive\\Desktop\\F1_Tracks\\Total_noDuplicate\\Germany.png",height = "500", width="800")
    } else if(input$courses == "Great Britain"){
      list(src="C:\\Users\\andre\\OneDrive\\Desktop\\F1_Tracks\\Total_noDuplicate\\GreatBritain.png",height = "500", width="800")
    } else if(input$courses == "Hungary"){
      list(src="C:\\Users\\andre\\OneDrive\\Desktop\\F1_Tracks\\Total_noDuplicate\\Hungary.png",height = "500", width="800")
    } else if(input$courses == "Italy"){
      list(src="C:\\Users\\andre\\OneDrive\\Desktop\\F1_Tracks\\Total_noDuplicate\\Italy.png",height = "500", width="800")
    } else if(input$courses == "Japan"){
      list(src="C:\\Users\\andre\\OneDrive\\Desktop\\F1_Tracks\\Total_noDuplicate\\Japan.png",height = "500", width="800")
    } else if(input$courses == "Mexico"){
      list(src="C:\\Users\\andre\\OneDrive\\Desktop\\F1_Tracks\\Total_noDuplicate\\Mexico.png",height = "500", width="800")
    } else if(input$courses == "Monaco"){
      list(src="C:\\Users\\andre\\OneDrive\\Desktop\\F1_Tracks\\Total_noDuplicate\\Monaco.png",height = "500", width="800")
    } else if(input$courses == "Netherlands"){
      list(src="C:\\Users\\andre\\OneDrive\\Desktop\\F1_Tracks\\Total_noDuplicate\\Netherlands.png",height = "500", width="800")
    } else if(input$courses == "Portugal"){
      list(src="C:\\Users\\andre\\OneDrive\\Desktop\\F1_Tracks\\Total_noDuplicate\\Portugal.png",height = "500", width="800")
    } else if(input$courses == "Qatar"){
      list(src="C:\\Users\\andre\\OneDrive\\Desktop\\F1_Tracks\\Total_noDuplicate\\Qatar.png",height = "500", width="800")
    } else if(input$courses == "Russia"){
      list(src="C:\\Users\\andre\\OneDrive\\Desktop\\F1_Tracks\\Total_noDuplicate\\Russia.png",height = "500", width="800")
    } else if(input$courses == "SaudiArabia"){
      list(src="C:\\Users\\andre\\OneDrive\\Desktop\\F1_Tracks\\Total_noDuplicate\\SaudiArabia.png",height = "500", width="800")
    } else if(input$courses == "Singapore"){
      list(src="C:\\Users\\andre\\OneDrive\\Desktop\\F1_Tracks\\Total_noDuplicate\\Singapore.png",height = "500", width="800")
    } else if(input$courses == "Spain"){
      list(src="C:\\Users\\andre\\OneDrive\\Desktop\\F1_Tracks\\Total_noDuplicate\\Spain.png",height = "500", width="800")
    } else if(input$courses == "Turkey"){
      list(src="C:\\Users\\andre\\OneDrive\\Desktop\\F1_Tracks\\Total_noDuplicate\\Turkey.png",height = "500", width="800")
    } else if(input$courses == "United Arab Emirates"){
      list(src="C:\\Users\\andre\\OneDrive\\Desktop\\F1_Tracks\\Total_noDuplicate\\UnitedArabEmirates.png",height = "500", width="800")     
    } else {
      list(src="C:\\Users\\andre\\OneDrive\\Desktop\\F1_Tracks\\Total_noDuplicate\\UnitedStates.png", height = "500", width="800")
    }
    
  })

  
  #https://shiny.rstudio.com/gallery/file-download.html
  
  datasetInput <- reactive({
    switch(input$dataset,
           "results" = results,
           "laps" = lap,
           "weather" = weather,
           "messages" = messages)
  })
  output$dataset <- renderTable({
    head(datasetInput())
  })
  output$downloadData <- downloadHandler(
    filename = function() {
      paste(input$dataset, ".csv", sep = "")
    },
    content = function(file) {
      write.csv(datasetInput(), file, row.names = FALSE)
    }
  )

  
  output$TotalPlot <- renderPlotly({
    p5 <- pitInOnly %>%
      subset(LapNumber!=1) %>%
      filter(
        Year >= input$Year[1] & Year <= input$Year[2]
      ) %>%
      ggplot(aes( x = LapNumber
      )) +
      geom_histogram(
        binwidth = 1
      ) +
      ggtitle("Lap Number When Driver Came in for PitStop Across All Courses")
    
  
    ggplotly(p5)
  })
  
  output$TotalTyrePlot <- renderPlotly({
    p6 <- pitInOnly %>%
      subset(LapNumber!=1) %>%
      filter(
        Year >= input$Year[1] & Year <= input$Year[2]
      ) %>%
      ggplot(aes(x = TyreLife)) +
      geom_histogram(       
        binwidth = 1
      ) +
      ggtitle("Lap Number When Driver Came in for PitStop Across All Courses")
    
    ggplotly(p6)
  })
  
#"C:\\Users\\andre\\OneDrive\\Desktop\\thesis_test\\documentation.docx"
#https://www.rdocumentation.org/packages/ReporteRs/versions/0.8.10/topics/writeDoc
#https://stackoverflow.com/questions/59023362/download-existing-docx-object-from-r-shiny-app
  # output$downloadDocumentation <- downloadHandler(
  #   filename = function() {
  #     paste(documentation, ".docx", sep = "")
  #   },
  #   content = function(file) { 
  #     writeDoc(documentation, file) 
  #       print(target = file)
  #   }
  # )
  # 
  # 
  # output$Documentation <- renderText({
  #   'test'
  # })
  # 
}

# Run the application 
shinyApp(ui = ui, server = server)

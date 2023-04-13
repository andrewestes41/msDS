#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)
library(tidyverse)
library(plotly)
#?aes_ 


orig.nba <- read.csv("nba2018.csv")
nba <- orig.nba

nbaTeams <- list("ATL", "BKN", "BOS", "CHA", "CHI", "CLE", 
                 "DAL", "DEN", "DET", "GSW", "HOU", "IND",
                 "LAC", "LAL", "MEM", "MIA", "MIL", "MIN",
                 "NOP", "NYK", "OKC", "ORL", "PHI", "PHX",
                 "POR", "SAC", "SAS", "TOR", "UTA", "WAS")

nbaVariables <- as.list(colnames(nba))
                        

# Define UI for application
ui <- fluidPage(
  titlePanel("My Shiny App"),
  
  sidebarLayout(
    sidebarPanel("Sidebar Panel",
                 selectInput( inputId = "team1",
                              label = h3("Select Team 1"),
                              choices = nbaTeams,
                              selected = "CHA"),
                 selectInput(inputId =  "var1",
                             label = h3("Choose Variable 1"),
                             choices = nbaVariables,
                             selected = "AGE"),
                 selectInput(inputId =  "team2",
                             label = h3("Select Team 2"),
                             choices = nbaTeams,
                             selected = "PHX"),
                 selectInput(inputId =  "var2",
                             label = h3("Choose Variable 2"),
                             choices = nbaVariables,
                             selected = "GP")
                 ),
    mainPanel(
      h2("Main Plot"),
      #dataTableOutput("data"),
      plotlyOutput("NBAplot")
      )
    )
  )




# Define server logic
server <- function(input, output) {
  
  output$data <- renderDataTable({nba %>%
      mutate(
        team1 = input$team1,
        team2 = input$team2) %>%
      filter(
        TEAM == team1 | TEAM == team2
        ) 
  })
  
  output$NBAplot <- renderPlotly({
    p <- nba %>%
      mutate(
        team1 = input$team1,
        team2 = input$team2) %>%
      filter(
        TEAM == team1 | TEAM == team2
      ) %>%
    ggplot(aes(x = .[[input$var1]],
              y = .[[input$var2]],
              color = TEAM,
              text = c(PLAYER))) + #text=paste0(var1, var2, " and some text ", var3)
      geom_point() +
      labs(title = "Comparison of Two User Selected Variables and Teams",
           x = input$var1,
           y = input$var2) 
    ggplotly(p, tooltip = "text")
  })
  
#  output$NBAplot <- renderPlotly({
#    p <- nba %>%
#      mutate(
#        team1 = input$team1,
#        var1 = input$var1,
#        team2 = input$team2,
#        var2 = input$var2) %>%
#      filter(
#        TEAM == team1 | TEAM == team2
#      ) %>%
#      select(
#        TEAM, input$var1, input$var2
#    ) %>%
#      ggplot() +
#        geom_point(aes(x = input$var1,
#                       y = input$var2)) 
#     ggplotly(p)
      
#  })
  
}
# Run the application 
shinyApp(ui = ui, server = server)


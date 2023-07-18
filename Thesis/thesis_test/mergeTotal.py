# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 13:18:51 2022

@author: andre
"""

#%%

#can only go back to 2018 using the API, 2014-2017 leads to error:
#Cannot load laps, telemetry, weather, and message data because  the relevant API is not supported for this session.


#%%
#installing packages
#pip install "fastf1"
#import fastf1
#installing libraries
import numpy as np
import pandas as pd

import fastf1 as ff1
from fastf1.core import Laps
from fastf1 import utils
from fastf1 import plotting
plotting.setup_mpl()

import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib import cm

from timple.timedelta import strftimedelta
#%%
import os
os.getcwd()


#directing to cache folder for data storage
ff1.Cache.enable_cache("C:\\Users\\andre\\OneDrive\\Desktop\\Thesis\\cache")

#%%

schedule18 = ff1.get_event_schedule(2018)
schedule19 = ff1.get_event_schedule(2019)
schedule20 = ff1.get_event_schedule(2020)
schedule21 = ff1.get_event_schedule(2021)
schedule22 = ff1.get_event_schedule(2022)


#%%

australia_race_18 = ff1.get_session(2018, 1, 'R')
australia_race_18.load()
australia_race_18_laps = australia_race_18.laps
australia_race_18_messages = australia_race_18.race_control_messages
australia_race_18_weather = australia_race_18.weather_data
australia_race_18_results = australia_race_18.results

bahrain_race_18 = ff1.get_session(2018, 2, 'R')
bahrain_race_18.load()
bahrain_race_18_laps = bahrain_race_18.laps
bahrain_race_18_messages = bahrain_race_18.race_control_messages
bahrain_race_18_weather = bahrain_race_18.weather_data
bahrain_race_18_results = bahrain_race_18.results

china_race_18 = ff1.get_session(2018, 3, 'R')
china_race_18.load()
china_race_18_laps = china_race_18.laps
china_race_18_messages = china_race_18.race_control_messages
china_race_18_weather = china_race_18.weather_data
china_race_18_results = china_race_18.results

azerbaijan_race_18 = ff1.get_session(2018, 4, 'R')
azerbaijan_race_18.load()
azerbaijan_race_18_laps = azerbaijan_race_18.laps
azerbaijan_race_18_messages = azerbaijan_race_18.race_control_messages
azerbaijan_race_18_weather = azerbaijan_race_18.weather_data
azerbaijan_race_18_results = azerbaijan_race_18.results

spain_race_18 = ff1.get_session(2018, 5, 'R')
spain_race_18.load()
spain_race_18_laps = spain_race_18.laps
spain_race_18_messages = spain_race_18.race_control_messages
spain_race_18_weather = spain_race_18.weather_data
spain_race_18_results = spain_race_18.results

monaco_race_18 = ff1.get_session(2018, 6, 'R')
monaco_race_18.load()
monaco_race_18_laps = monaco_race_18.laps
monaco_race_18_messages = monaco_race_18.race_control_messages
monaco_race_18_weather = monaco_race_18.weather_data
monaco_race_18_results = monaco_race_18.results

canada_race_18 = ff1.get_session(2018, 7, 'R')
canada_race_18.load()
canada_race_18_laps = canada_race_18.laps
canada_race_18_messages = canada_race_18.race_control_messages
canada_race_18_weather = canada_race_18.weather_data
canada_race_18_results = canada_race_18.results

france_race_18 = ff1.get_session(2018, 8, 'R')
france_race_18.load()
france_race_18_laps = france_race_18.laps
france_race_18_messages = france_race_18.race_control_messages
france_race_18_weather = france_race_18.weather_data
france_race_18_results = france_race_18.results

austria_race_18 = ff1.get_session(2018, 9, 'R')
austria_race_18.load()
austria_race_18_laps = austria_race_18.laps
austria_race_18_messages = austria_race_18.race_control_messages
austria_race_18_weather = austria_race_18.weather_data
austria_race_18_results = austria_race_18.results

great_britain_race_18 = ff1.get_session(2018, 10, 'R')
great_britain_race_18.load()
great_britain_race_18_laps = great_britain_race_18.laps
great_britain_race_18_messages = great_britain_race_18.race_control_messages
great_britain_race_18_weather = great_britain_race_18.weather_data
great_britain_race_18_results = great_britain_race_18.results

germany_race_18 = ff1.get_session(2018, 11, 'R')
germany_race_18.load()
germany_race_18_laps = germany_race_18.laps
germany_race_18_messages = germany_race_18.race_control_messages
germany_race_18_weather = germany_race_18.weather_data
germany_race_18_results = germany_race_18.results

hungary_race_18 = ff1.get_session(2018, 12, 'R')
hungary_race_18.load()
hungary_race_18_laps = hungary_race_18.laps
hungary_race_18_messages = hungary_race_18.race_control_messages
hungary_race_18_weather = hungary_race_18.weather_data
hungary_race_18_results = hungary_race_18.results

belgium_race_18 = ff1.get_session(2018, 13, 'R')
belgium_race_18.load()
belgium_race_18_laps = belgium_race_18.laps
belgium_race_18_messages = belgium_race_18.race_control_messages
belgium_race_18_weather = belgium_race_18.weather_data
belgium_race_18_results = belgium_race_18.results

italy_race_18 = ff1.get_session(2018, 14, 'R')
italy_race_18.load()
italy_race_18_laps = italy_race_18.laps
italy_race_18_messages = italy_race_18.race_control_messages
italy_race_18_weather = italy_race_18.weather_data
italy_race_18_results = italy_race_18.results

singapore_race_18 = ff1.get_session(2018, 15, 'R')
singapore_race_18.load()
singapore_race_18_laps = singapore_race_18.laps
singapore_race_18_messages = singapore_race_18.race_control_messages
singapore_race_18_weather = singapore_race_18.weather_data
singapore_race_18_results = singapore_race_18.results

russia_race_18 = ff1.get_session(2018, 16, 'R')
russia_race_18.load()
russia_race_18_laps = russia_race_18.laps
russia_race_18_messages = russia_race_18.race_control_messages
russia_race_18_weather = russia_race_18.weather_data
russia_race_18_results = russia_race_18.results

japan_race_18 = ff1.get_session(2018, 17, 'R')
japan_race_18.load()
japan_race_18_laps = japan_race_18.laps
japan_race_18_messages = japan_race_18.race_control_messages
japan_race_18_weather = japan_race_18.weather_data
japan_race_18_results = japan_race_18.results

united_states_race_18 = ff1.get_session(2018, 18, 'R')
united_states_race_18.load()
united_states_race_18_laps = united_states_race_18.laps
united_states_race_18_messages = united_states_race_18.race_control_messages
united_states_race_18_weather = united_states_race_18.weather_data
united_states_race_18_results = united_states_race_18.results

mexico_race_18 = ff1.get_session(2018, 19, 'R')
mexico_race_18.load()
mexico_race_18_laps = mexico_race_18.laps
mexico_race_18_messages = mexico_race_18.race_control_messages
mexico_race_18_weather = mexico_race_18.weather_data
mexico_race_18_results = mexico_race_18.results

brazil_race_18 = ff1.get_session(2018, 20, 'R')
brazil_race_18.load()
brazil_race_18_laps = brazil_race_18.laps
brazil_race_18_messages = brazil_race_18.race_control_messages
brazil_race_18_weather = brazil_race_18.weather_data
brazil_race_18_results = brazil_race_18.results

united_arab_emirates_race_18 = ff1.get_session(2018, 21, 'R')
united_arab_emirates_race_18.load()
united_arab_emirates_race_18_laps = united_arab_emirates_race_18.laps
united_arab_emirates_race_18_messages = united_arab_emirates_race_18.race_control_messages
united_arab_emirates_race_18_weather = united_arab_emirates_race_18.weather_data
united_arab_emirates_race_18_results = united_arab_emirates_race_18.results


merge2018_laps = pd.concat([
    australia_race_18_laps, 
    bahrain_race_18_laps,
    china_race_18_laps,
    azerbaijan_race_18_laps,
    spain_race_18_laps,
    monaco_race_18_laps,
    canada_race_18_laps,
    france_race_18_laps,
    austria_race_18_laps,
    great_britain_race_18_laps,
    germany_race_18_laps,
    hungary_race_18_laps,
    belgium_race_18_laps,
    italy_race_18_laps,
    singapore_race_18_laps,
    russia_race_18_laps,
    japan_race_18_laps,
    united_states_race_18_laps,
    mexico_race_18_laps,
    brazil_race_18_laps,
    united_arab_emirates_race_18_laps],
    keys = ['Australia', 
            'Bahrain',
            'China',
            'Azerbaijan',
            'Spain',
            'Monaco',
            'Canada',
            'France',
            'Austria',
            'GreatBritain',
            'Germany',
            'Hungary',
            'Belgium',
            'Italy',
            'Singapore',
            'Russia',
            'Japan',
            'UnitedStates',
            'Mexico',
            'Brazil',
            'UnitedArabEmirates'],
    names=['RACE'])

merge2018_messages = pd.concat([
    australia_race_18_messages, 
    bahrain_race_18_messages,
    china_race_18_messages,
    azerbaijan_race_18_messages,
    spain_race_18_messages,
    monaco_race_18_messages,
    canada_race_18_messages,
    france_race_18_messages,
    austria_race_18_messages,
    great_britain_race_18_messages,
    germany_race_18_messages,
    hungary_race_18_messages,
    belgium_race_18_messages,
    italy_race_18_messages,
    singapore_race_18_messages,
    russia_race_18_messages,
    japan_race_18_messages,
    united_states_race_18_messages,
    mexico_race_18_messages,
    brazil_race_18_messages,
    united_arab_emirates_race_18_messages],
    keys = ['Australia', 
            'Bahrain',
            'China',
            'Azerbaijan',
            'Spain',
            'Monaco',
            'Canada',
            'France',
            'Austria',
            'GreatBritain',
            'Germany',
            'Hungary',
            'Belgium',
            'Italy',
            'Singapore',
            'Russia',
            'Japan',
            'UnitedStates',
            'Mexico',
            'Brazil',
            'UnitedArabEmirates'],
    names=['RACE'])

merge2018_weather = pd.concat([
    australia_race_18_weather, 
    bahrain_race_18_weather,
    china_race_18_weather,
    azerbaijan_race_18_weather,
    spain_race_18_weather,
    monaco_race_18_weather,
    canada_race_18_weather,
    france_race_18_weather,
    austria_race_18_weather,
    great_britain_race_18_weather,
    germany_race_18_weather,
    hungary_race_18_weather,
    belgium_race_18_weather,
    italy_race_18_weather,
    singapore_race_18_weather,
    russia_race_18_weather,
    japan_race_18_weather,
    united_states_race_18_weather,
    mexico_race_18_weather,
    brazil_race_18_weather,
    united_arab_emirates_race_18_weather],
    keys = ['Australia', 
            'Bahrain',
            'China',
            'Azerbaijan',
            'Spain',
            'Monaco',
            'Canada',
            'France',
            'Austria',
            'GreatBritain',
            'Germany',
            'Hungary',
            'Belgium',
            'Italy',
            'Singapore',
            'Russia',
            'Japan',
            'UnitedStates',
            'Mexico',
            'Brazil',
            'UnitedArabEmirates'],
    names=['RACE'])

merge2018_results = pd.concat([
    australia_race_18_results, 
    bahrain_race_18_results,
    china_race_18_results,
    azerbaijan_race_18_results,
    spain_race_18_results,
    monaco_race_18_results,
    canada_race_18_results,
    france_race_18_results,
    austria_race_18_results,
    great_britain_race_18_results,
    germany_race_18_results,
    hungary_race_18_results,
    belgium_race_18_results,
    italy_race_18_results,
    singapore_race_18_results,
    russia_race_18_results,
    japan_race_18_results,
    united_states_race_18_results,
    mexico_race_18_results,
    brazil_race_18_results,
    united_arab_emirates_race_18_results],
    keys = ['Australia', 
            'Bahrain',
            'China',
            'Azerbaijan',
            'Spain',
            'Monaco',
            'Canada',
            'France',
            'Austria',
            'GreatBritain',
            'Germany',
            'Hungary',
            'Belgium',
            'Italy',
            'Singapore',
            'Russia',
            'Japan',
            'UnitedStates',
            'Mexico',
            'Brazil',
            'UnitedArabEmirates'],
    names=['RACE'])


merge2018_laps["Year"] = 2018
merge2018_messages["Year"] = 2018
merge2018_weather["Year"] = 2018
merge2018_results["Year"] = 2018

#%%

australia_race_19 = ff1.get_session(2019, 1, 'R')
australia_race_19.load()
australia_race_19_laps = australia_race_19.laps
australia_race_19_messages = australia_race_19.race_control_messages
australia_race_19_weather = australia_race_19.weather_data
australia_race_19_results = australia_race_19.results

bahrain_race_19 = ff1.get_session(2019, 2, 'R')
bahrain_race_19.load()
bahrain_race_19_laps = bahrain_race_19.laps
bahrain_race_19_messages = bahrain_race_19.race_control_messages
bahrain_race_19_weather = bahrain_race_19.weather_data
bahrain_race_19_results = bahrain_race_19.results

china_race_19 = ff1.get_session(2019, 3, 'R')
china_race_19.load()
china_race_19_laps = china_race_19.laps
china_race_19_messages= china_race_19.race_control_messages
china_race_19_weather = china_race_19.weather_data
china_race_19_results = china_race_19.results

azerbaijan_race_19 = ff1.get_session(2019, 4, 'R')
azerbaijan_race_19.load()
azerbaijan_race_19_laps = azerbaijan_race_19.laps
azerbaijan_race_19_messages = azerbaijan_race_19.race_control_messages
azerbaijan_race_19_weather = azerbaijan_race_19.weather_data
azerbaijan_race_19_results = azerbaijan_race_19.results

spain_race_19 = ff1.get_session(2019, 5, 'R')
spain_race_19.load()
spain_race_19_laps = spain_race_19.laps
spain_race_19_messages = spain_race_19.race_control_messages
spain_race_19_weather = spain_race_19.weather_data
spain_race_19_results = spain_race_19.results

monaco_race_19 = ff1.get_session(2019, 6, 'R')
monaco_race_19.load()
monaco_race_19_laps = monaco_race_19.laps
monaco_race_19_messages = monaco_race_19.race_control_messages
monaco_race_19_weather = monaco_race_19.weather_data
monaco_race_19_results = monaco_race_19.results

canada_race_19 = ff1.get_session(2019, 7, 'R')
canada_race_19.load()
canada_race_19_laps = canada_race_19.laps
canada_race_19_messages = canada_race_19.race_control_messages
canada_race_19_weather = canada_race_19.weather_data
canada_race_19_results = canada_race_19.results

france_race_19 = ff1.get_session(2019, 8, 'R')
france_race_19.load()
france_race_19_laps = france_race_19.laps
france_race_19_messages = france_race_19.race_control_messages
france_race_19_weather = france_race_19.weather_data
france_race_19_results = france_race_19.results

austria_race_19 = ff1.get_session(2019, 9, 'R')
austria_race_19.load()
austria_race_19_laps = austria_race_19.laps
austria_race_19_messages = austria_race_19.race_control_messages
austria_race_19_weather = austria_race_19.weather_data
austria_race_19_results = austria_race_19.results

great_britain_race_19 = ff1.get_session(2019, 10, 'R')
great_britain_race_19.load()
great_britain_race_19_laps = great_britain_race_19.laps
great_britain_race_19_messages = great_britain_race_19.race_control_messages
great_britain_race_19_weather = great_britain_race_19.weather_data
great_britain_race_19_results = great_britain_race_19.results

germany_race_19 = ff1.get_session(2019, 11, 'R')
germany_race_19.load()
germany_race_19_laps = germany_race_19.laps
germany_race_19_messages = germany_race_19.race_control_messages
germany_race_19_weather = germany_race_19.weather_data
germany_race_19_results = germany_race_19.results

hungary_race_19 = ff1.get_session(2019, 12, 'R')
hungary_race_19.load()
hungary_race_19_laps = hungary_race_19.laps
hungary_race_19_messages = hungary_race_19.race_control_messages
hungary_race_19_weather = hungary_race_19.weather_data
hungary_race_19_results = hungary_race_19.results

belgium_race_19 = ff1.get_session(2019, 13, 'R')
belgium_race_19.load()
belgium_race_19_laps = belgium_race_19.laps
belgium_race_19_messages = belgium_race_19.race_control_messages
belgium_race_19_weather = belgium_race_19.weather_data
belgium_race_19_results = belgium_race_19.results

italy_race_19 = ff1.get_session(2019, 14, 'R')
italy_race_19.load()
italy_race_19_laps = italy_race_19.laps
italy_race_19_messages = italy_race_19.race_control_messages
italy_race_19_weather = italy_race_19.weather_data
italy_race_19_results = italy_race_19.results

singapore_race_19 = ff1.get_session(2019, 15, 'R')
singapore_race_19.load()
singapore_race_19_laps = singapore_race_19.laps
singapore_race_19_messages = singapore_race_19.race_control_messages
singapore_race_19_weather = singapore_race_19.weather_data
singapore_race_19_results = singapore_race_19.results

russia_race_19 = ff1.get_session(2018, 16, 'R')
russia_race_19.load()
russia_race_19_laps = russia_race_19.laps
russia_race_19_messages = russia_race_19.race_control_messages
russia_race_19_weather = russia_race_19.weather_data
russia_race_19_results = russia_race_19.results

japan_race_19 = ff1.get_session(2019, 17, 'R')
japan_race_19.load()
japan_race_19_laps = japan_race_19.laps
japan_race_19_messages = japan_race_19.race_control_messages
japan_race_19_weather = japan_race_19.weather_data
japan_race_19_results = japan_race_19.results

mexico_race_19 = ff1.get_session(2019, 18, 'R')
mexico_race_19.load()
mexico_race_19_laps = mexico_race_19.laps
mexico_race_19_messages = mexico_race_19.race_control_messages
mexico_race_19_weather = mexico_race_19.weather_data
mexico_race_19_results = mexico_race_19.results

united_states_race_19 = ff1.get_session(2019, 19, 'R')
united_states_race_19.load()
united_states_race_19_laps = united_states_race_19.laps
united_states_race_19_messages = united_states_race_19.race_control_messages
united_states_race_19_weather = united_states_race_19.weather_data
united_states_race_19_results = united_states_race_19.results

brazil_race_19 = ff1.get_session(2019, 20, 'R')
brazil_race_19.load()
brazil_race_19_laps = brazil_race_19.laps
brazil_race_19_messages = brazil_race_19.race_control_messages
brazil_race_19_weather = brazil_race_19.weather_data
brazil_race_19_results = brazil_race_19.results

abu_dhabi_race_19 = ff1.get_session(2019, 21, 'R')
abu_dhabi_race_19.load()
abu_dhabi_race_19_laps = abu_dhabi_race_19.laps
abu_dhabi_race_19_messages = abu_dhabi_race_19.race_control_messages
abu_dhabi_race_19_weather = abu_dhabi_race_19.weather_data
abu_dhabi_race_19_results = abu_dhabi_race_19.results


merge2019_laps = pd.concat([
    australia_race_19_laps, 
    bahrain_race_19_laps,
    china_race_19_laps,
    azerbaijan_race_19_laps,
    spain_race_19_laps,
    monaco_race_19_laps,
    canada_race_19_laps,
    france_race_19_laps,
    austria_race_19_laps,
    great_britain_race_19_laps,
    germany_race_19_laps,
    hungary_race_19_laps,
    belgium_race_19_laps,
    italy_race_19_laps,
    singapore_race_19_laps,
    russia_race_19_laps,
    japan_race_19_laps,
    mexico_race_19_laps,
    united_states_race_19_laps,
    brazil_race_19_laps,
    abu_dhabi_race_19_laps],
    keys = ['Australia', 
            'Bahrain',
            'China',
            'Azerbaijan',
            'Spain',
            'Monaco',
            'Canada',
            'France',
            'Austria',
            'GreatBritain',
            'Germany',
            'Hungary',
            'Belgium',
            'Italy',
            'Singapore',
            'Russia',
            'Japan',
            'Mexico',
            'UnitedStates',
            'Brazil',
            'AbuDhabi'],
    names=['RACE'])

merge2019_messages = pd.concat([
    australia_race_19_messages, 
    bahrain_race_19_messages,
    china_race_19_messages,
    azerbaijan_race_19_messages,
    spain_race_19_messages,
    monaco_race_19_messages,
    canada_race_19_messages,
    france_race_19_messages,
    austria_race_19_messages,
    great_britain_race_19_messages,
    germany_race_19_messages,
    hungary_race_19_messages,
    belgium_race_19_messages,
    italy_race_19_messages,
    singapore_race_19_messages,
    russia_race_19_messages,
    japan_race_19_messages,
    mexico_race_19_messages,
    united_states_race_19_messages,
    brazil_race_19_messages,
    abu_dhabi_race_19_messages],
    keys = ['Australia', 
            'Bahrain',
            'China',
            'Azerbaijan',
            'Spain',
            'Monaco',
            'Canada',
            'France',
            'Austria',
            'GreatBritain',
            'Germany',
            'Hungary',
            'Belgium',
            'Italy',
            'Singapore',
            'Russia',
            'Japan',
            'Mexico',
            'UnitedStates',
            'Brazil',
            'AbuDhabi'],
    names=['RACE'])


merge2019_weather = pd.concat([
    australia_race_19_weather, 
    bahrain_race_19_weather,
    china_race_19_weather,
    azerbaijan_race_19_weather,
    spain_race_19_weather,
    monaco_race_19_weather,
    canada_race_19_weather,
    france_race_19_weather,
    austria_race_19_weather,
    great_britain_race_19_weather,
    germany_race_19_weather,
    hungary_race_19_weather,
    belgium_race_19_weather,
    italy_race_19_weather,
    singapore_race_19_weather,
    russia_race_19_weather,
    japan_race_19_weather,
    mexico_race_19_weather,
    united_states_race_19_weather,
    brazil_race_19_weather,
    abu_dhabi_race_19_weather],
    keys = ['Australia', 
            'Bahrain',
            'China',
            'Azerbaijan',
            'Spain',
            'Monaco',
            'Canada',
            'France',
            'Austria',
            'GreatBritain',
            'Germany',
            'Hungary',
            'Belgium',
            'Italy',
            'Singapore',
            'Russia',
            'Japan',
            'Mexico',
            'UnitedStates',
            'Brazil',
            'AbuDhabi'],
    names=['RACE'])

merge2019_results = pd.concat([
    australia_race_19_results , 
    bahrain_race_19_results ,
    china_race_19_results ,
    azerbaijan_race_19_results ,
    spain_race_19_results ,
    monaco_race_19_results ,
    canada_race_19_results ,
    france_race_19_results ,
    austria_race_19_results ,
    great_britain_race_19_results ,
    germany_race_19_results ,
    hungary_race_19_results ,
    belgium_race_19_results ,
    italy_race_19_results ,
    singapore_race_19_results,
    russia_race_19_results ,
    japan_race_19_results ,
    mexico_race_19_results ,
    united_states_race_19_results ,
    brazil_race_19_results ,
    abu_dhabi_race_19_results],
    keys = ['Australia', 
            'Bahrain',
            'China',
            'Azerbaijan',
            'Spain',
            'Monaco',
            'Canada',
            'France',
            'Austria',
            'GreatBritain',
            'Germany',
            'Hungary',
            'Belgium',
            'Italy',
            'Singapore',
            'Russia',
            'Japan',
            'Mexico',
            'UnitedStates',
            'Brazil',
            'AbuDhabi'],
    names=['RACE'])

merge2019_laps["Year"] = 2019
merge2019_messages["Year"] = 2019
merge2019_weather["Year"] = 2019
merge2019_results["Year"] = 2019

#%%

austria_race_20a = ff1.get_session(2020, 1, 'R')
austria_race_20a.load()
austria_race_20a_laps = austria_race_20a.laps
austria_race_20a_messages = austria_race_20a.race_control_messages
austria_race_20a_weather = austria_race_20a.weather_data
austria_race_20a_results = austria_race_20a.results

austria_race_20b = ff1.get_session(2020, 2, 'R')
austria_race_20b.load()
austria_race_20b_laps = austria_race_20b.laps
austria_race_20b_messages = austria_race_20b.race_control_messages
austria_race_20b_weather = austria_race_20b.weather_data
austria_race_20b_results = austria_race_20b.results

hungary_race_20 = ff1.get_session(2020, 3, 'R')
hungary_race_20.load()
hungary_race_20_laps = hungary_race_20.laps
hungary_race_20_messages = hungary_race_20.race_control_messages
hungary_race_20_weather = hungary_race_20.weather_data
hungary_race_20_results = hungary_race_20.results

great_britain_race_20a = ff1.get_session(2020, 4, 'R')
great_britain_race_20a.load()
great_britain_race_20a_laps = great_britain_race_20a.laps
great_britain_race_20a_messages = great_britain_race_20a.race_control_messages
great_britain_race_20a_weather = great_britain_race_20a.weather_data
great_britain_race_20a_results = great_britain_race_20a.results

great_britain_race_20b = ff1.get_session(2020, 5, 'R')
great_britain_race_20b.load()
great_britain_race_20b_laps = great_britain_race_20b.laps
great_britain_race_20b_messages = great_britain_race_20b.race_control_messages
great_britain_race_20b_weather = great_britain_race_20b.weather_data
great_britain_race_20b_results = great_britain_race_20b.results

spain_race_20 = ff1.get_session(2020, 6, 'R')
spain_race_20.load()
spain_race_20_laps = spain_race_20.laps
spain_race_20_messages = spain_race_20.race_control_messages
spain_race_20_weather = spain_race_20.weather_data
spain_race_20_results = spain_race_20.results

belgium_race_20 = ff1.get_session(2020, 7, 'R')
belgium_race_20.load()
belgium_race_20_laps = belgium_race_20.laps
belgium_race_20_messages = belgium_race_20.race_control_messages
belgium_race_20_weather = belgium_race_20.weather_data
belgium_race_20_results = belgium_race_20.results

italy_race_20a = ff1.get_session(2020, 8, 'R')
italy_race_20a.load()
italy_race_20a_laps = italy_race_20a.laps
italy_race_20a_messages = italy_race_20a.race_control_messages
italy_race_20a_weather = italy_race_20a.weather_data
italy_race_20a_results = italy_race_20a.results

italy_race_20b = ff1.get_session(2020, 9, 'R')
italy_race_20b.load()
italy_race_20b_laps = italy_race_20b.laps
italy_race_20b_messages = italy_race_20b.race_control_messages
italy_race_20b_weather = italy_race_20b.weather_data
italy_race_20b_results = italy_race_20b.results

russia_race_20 = ff1.get_session(2020, 10, 'R')
russia_race_20.load()
russia_race_20_laps = russia_race_20.laps
russia_race_20_messages = russia_race_20.race_control_messages
russia_race_20_weather = russia_race_20.weather_data
russia_race_20_results = russia_race_20.results

germany_race_20 = ff1.get_session(2020, 11, 'R')
germany_race_20.load()
germany_race_20_laps = germany_race_20.laps
germany_race_20_messages = germany_race_20.race_control_messages
germany_race_20_weather = germany_race_20.weather_data
germany_race_20_results = germany_race_20.results

portugal_race_20 = ff1.get_session(2020, 12, 'R')
portugal_race_20.load()
portugal_race_20_laps = portugal_race_20.laps
portugal_race_20_messages = portugal_race_20.race_control_messages
portugal_race_20_weather = portugal_race_20.weather_data
portugal_race_20_results = portugal_race_20.results

italy_race_20c = ff1.get_session(2020, 13, 'R')
italy_race_20c.load()
italy_race_20c_laps = italy_race_20b.laps
italy_race_20c_messages = italy_race_20b.race_control_messages
italy_race_20c_weather = italy_race_20b.weather_data
italy_race_20c_results = italy_race_20b.results

turkey_race_20 = ff1.get_session(2020, 14, 'R')
turkey_race_20.load()
turkey_race_20_laps = turkey_race_20.laps
turkey_race_20_messages = turkey_race_20.race_control_messages
turkey_race_20_weather = turkey_race_20.weather_data
turkey_race_20_results = turkey_race_20.results

bahrain_race_20a = ff1.get_session(2020, 15, 'R')
bahrain_race_20a.load()
bahrain_race_20a_laps = bahrain_race_20a.laps
bahrain_race_20a_messages = bahrain_race_20a.race_control_messages
bahrain_race_20a_weather = bahrain_race_20a.weather_data
bahrain_race_20a_results = bahrain_race_20a.results

bahrain_race_20b = ff1.get_session(2020, 16, 'R')
bahrain_race_20b.load()
bahrain_race_20b_laps = bahrain_race_20b.laps
bahrain_race_20b_messages = bahrain_race_20b.race_control_messages
bahrain_race_20b_weather = bahrain_race_20b.weather_data
bahrain_race_20b_results = bahrain_race_20b.results

abu_dhabi_race_20 = ff1.get_session(2020, 17, 'R')
abu_dhabi_race_20.load()
abu_dhabi_race_20_laps = abu_dhabi_race_20.laps
abu_dhabi_race_20_messages = abu_dhabi_race_20.race_control_messages
abu_dhabi_race_20_weather = abu_dhabi_race_20.weather_data
abu_dhabi_race_20_results = abu_dhabi_race_20.results



merge2020_laps = pd.concat([
    austria_race_20a_laps,
    austria_race_20b_laps,
    hungary_race_20_laps,
    great_britain_race_20a_laps,
    great_britain_race_20b_laps,
    spain_race_20_laps,
    belgium_race_20_laps,
    italy_race_20a_laps,
    italy_race_20b_laps,
    russia_race_20_laps,
    germany_race_20_laps,
    portugal_race_20_laps,
    italy_race_20c_laps,
    turkey_race_20_laps,
    bahrain_race_20a_laps,
    bahrain_race_20b_laps,
    abu_dhabi_race_20_laps],
    keys = ['AustriaA', 
            'AustriaB',
            'Hungary',
            'GreatBritainA',
            'GreatBritainB',
            'Spain',
            'Belgium',
            'ItalyA',
            'ItalyB',
            'Russia',
            'Germany',
            'Portugal',
            'ItalyC',
            'Turkey',
            'BahrainA',
            'BahrainB',
            'AbuDhabi'],
    names=['RACE'])

merge2020_messages = pd.concat([
    austria_race_20a_messages ,
    austria_race_20b_messages,
    hungary_race_20_messages ,
    great_britain_race_20a_messages ,
    great_britain_race_20b_messages ,
    spain_race_20_messages ,
    belgium_race_20_messages ,
    italy_race_20a_messages ,
    italy_race_20b_messages ,
    russia_race_20_messages ,
    germany_race_20_messages ,
    portugal_race_20_messages ,
    italy_race_20c_messages ,
    turkey_race_20_messages ,
    bahrain_race_20a_messages ,
    bahrain_race_20b_messages ,
    abu_dhabi_race_20_messages ],
    keys = ['AustriaA', 
            'AustriaB',
            'Hungary',
            'GreatBritainA',
            'GreatBritainB',
            'Spain',
            'Belgium',
            'ItalyA',
            'ItalyB',
            'Russia',
            'Germany',
            'Portugal',
            'ItalyC',
            'Turkey',
            'BahrainA',
            'BahrainB',
            'AbuDhabi'],
    names=['RACE'])

merge2020_weather = pd.concat([
    austria_race_20a_weather,
    austria_race_20b_weather,
    hungary_race_20_weather,
    great_britain_race_20a_weather,
    great_britain_race_20b_weather,
    spain_race_20_weather,
    belgium_race_20_weather,
    italy_race_20a_weather,
    italy_race_20b_weather,
    russia_race_20_weather,
    germany_race_20_weather,
    portugal_race_20_weather,
    italy_race_20c_weather,
    turkey_race_20_weather,
    bahrain_race_20a_weather,
    bahrain_race_20b_weather,
    abu_dhabi_race_20_weather],
    keys = ['AustriaA', 
            'AustriaB',
            'Hungary',
            'GreatBritainA',
            'GreatBritainB',
            'Spain',
            'Belgium',
            'ItalyA',
            'ItalyB',
            'Russia',
            'Germany',
            'Portugal',
            'ItalyC',
            'Turkey',
            'BahrainA',
            'BahrainB',
            'AbuDhabi'],
    names=['RACE'])

merge2020_results = pd.concat([
    austria_race_20a_results ,
    austria_race_20b_results ,
    hungary_race_20_results ,
    great_britain_race_20a_results ,
    great_britain_race_20b_results ,
    spain_race_20_results ,
    belgium_race_20_results ,
    italy_race_20a_results ,
    italy_race_20b_results ,
    russia_race_20_results ,
    germany_race_20_results ,
    portugal_race_20_results ,
    italy_race_20c_results ,
    turkey_race_20_results ,
    bahrain_race_20a_results ,
    bahrain_race_20b_results ,
    abu_dhabi_race_20_results ],
    keys = ['AustriaA', 
            'AustriaB',
            'Hungary',
            'GreatBritainA',
            'GreatBritainB',
            'Spain',
            'Belgium',
            'ItalyA',
            'ItalyB',
            'Russia',
            'Germany',
            'Portugal',
            'ItalyC',
            'Turkey',
            'BahrainA',
            'BahrainB',
            'AbuDhabi'],
    names=['RACE'])

merge2020_laps["Year"] = 2020
merge2020_messages["Year"] = 2020
merge2020_weather["Year"] = 2020
merge2020_results["Year"] = 2020

#%%

bahrain_race_21 = ff1.get_session(2021, 1, 'R')
bahrain_race_21.load()
bahrain_race_21_laps = bahrain_race_21.laps
bahrain_race_21_messages= bahrain_race_21.race_control_messages
bahrain_race_21_weather= bahrain_race_21.weather_data
bahrain_race_21_results = bahrain_race_21.results

italy_race_21a = ff1.get_session(2021, 2, 'R')
italy_race_21a.load()
italy_race_21a_laps = italy_race_21a.laps
italy_race_21a_messages= italy_race_21a.race_control_messages
italy_race_21a_weather= italy_race_21a.weather_data
italy_race_21a_results= italy_race_21a.results

portugal_race_21 = ff1.get_session(2021, 3, 'R')
portugal_race_21.load()
portugal_race_21_laps = portugal_race_21.laps
portugal_race_21_messages= portugal_race_21.race_control_messages
portugal_race_21_weather= portugal_race_21.weather_data
portugal_race_21_results = portugal_race_21.results

spain_race_21 = ff1.get_session(2021, 4, 'R')
spain_race_21.load()
spain_race_21_laps = spain_race_21.laps
spain_race_21_messages= spain_race_21.race_control_messages
spain_race_21_weather= spain_race_21.weather_data
spain_race_21_results= spain_race_21.results

monaco_race_21 = ff1.get_session(2021, 5, 'R')
monaco_race_21.load()
monaco_race_21_laps = monaco_race_21.laps
monaco_race_21_messages= monaco_race_21.race_control_messages
monaco_race_21_weather= monaco_race_21.weather_data
monaco_race_21_results= monaco_race_21.results

azerbaijan_race_21 = ff1.get_session(2021, 6, 'R')
azerbaijan_race_21.load()
azerbaijan_race_21_laps = azerbaijan_race_21.laps
azerbaijan_race_21_messages= azerbaijan_race_21.race_control_messages
azerbaijan_race_21_weather= azerbaijan_race_21.weather_data
azerbaijan_race_21_results= azerbaijan_race_21.results

france_race_21 = ff1.get_session(2021, 7, 'R')
france_race_21.load()
france_race_21_laps = france_race_21.laps
france_race_21_messages= france_race_21.race_control_messages
france_race_21_weather= france_race_21.weather_data
france_race_21_results = france_race_21.results

austria_race_21a = ff1.get_session(2021, 8, 'R')
austria_race_21a.load()
austria_race_21a_laps = austria_race_21a.laps
austria_race_21a_messages= austria_race_21a.race_control_messages
austria_race_21a_weather= austria_race_21a.weather_data
austria_race_21a_results = austria_race_21a.results

austria_race_21b = ff1.get_session(2021, 9, 'R')
austria_race_21b.load()
austria_race_21b_laps = austria_race_21b.laps
austria_race_21b_messages= austria_race_21b.race_control_messages
austria_race_21b_weather= austria_race_21b.weather_data
austria_race_21b_results = austria_race_21b.results

great_britain_race_21 = ff1.get_session(2021, 10, 'R')
great_britain_race_21.load()
great_britain_race_21_laps = great_britain_race_21.laps
great_britain_race_21_messages= great_britain_race_21.race_control_messages
great_britain_race_21_weather= great_britain_race_21.weather_data
great_britain_race_21_results = great_britain_race_21.results

hungary_race_21 = ff1.get_session(2021, 11, 'R')
hungary_race_21.load()
hungary_race_21_laps = hungary_race_21.laps
hungary_race_21_messages= hungary_race_21.race_control_messages
hungary_race_21_weather= hungary_race_21.weather_data
hungary_race_21_results = hungary_race_21.results

belgium_race_21 = ff1.get_session(2021, 12, 'R')
belgium_race_21.load()
belgium_race_21_laps = belgium_race_21.laps
belgium_race_21_messages= belgium_race_21.race_control_messages
belgium_race_21_weather= belgium_race_21.weather_data
belgium_race_21_results = belgium_race_21.results

netherlands_race_21 = ff1.get_session(2021, 13, 'R')
netherlands_race_21 .load()
netherlands_race_21_laps = netherlands_race_21.laps
netherlands_race_21_messages= netherlands_race_21.race_control_messages
netherlands_race_21_weather= netherlands_race_21.weather_data
netherlands_race_21_results = netherlands_race_21.results

italy_race_21b = ff1.get_session(2021, 14, 'R')
italy_race_21b.load()
italy_race_21b_laps = italy_race_21b.laps
italy_race_21b_messages= italy_race_21b.race_control_messages
italy_race_21b_weather= italy_race_21b.weather_data
italy_race_21b_results = italy_race_21b.results

russia_race_21 = ff1.get_session(2021, 15, 'R')
russia_race_21.load()
russia_race_21_laps = russia_race_21.laps
russia_race_21_messages= russia_race_21.race_control_messages
russia_race_21_weather= russia_race_21.weather_data
russia_race_21_results = russia_race_21.results

turkey_race_21 = ff1.get_session(2021, 16, 'R')
turkey_race_21.load()
turkey_race_21_laps = turkey_race_21.laps
turkey_race_21_messages= turkey_race_21.race_control_messages
turkey_race_21_weather= turkey_race_21.weather_data
turkey_race_21_results = turkey_race_21.results

united_states_race_21 = ff1.get_session(2021, 17, 'R')
united_states_race_21.load()
united_states_race_21_laps = united_states_race_21.laps
united_states_race_21_messages= united_states_race_21.race_control_messages
united_states_race_21_weather= united_states_race_21.weather_data
united_states_race_21_results = united_states_race_21.results

mexico_race_21 = ff1.get_session(2021, 18, 'R')
mexico_race_21.load()
mexico_race_21_laps = mexico_race_21.laps
mexico_race_21_messages= mexico_race_21.race_control_messages
mexico_race_21_weather= mexico_race_21.weather_data
mexico_race_21_results = mexico_race_21.results

brazil_race_21 = ff1.get_session(2021, 19, 'R')
brazil_race_21.load()
brazil_race_21_laps = brazil_race_21.laps
brazil_race_21_messages= brazil_race_21.race_control_messages
brazil_race_21_weather= brazil_race_21.weather_data
brazil_race_21_results = brazil_race_21.results

qatar_race_21 = ff1.get_session(2021, 20, 'R')
qatar_race_21.load()
qatar_race_21_laps = qatar_race_21.laps
qatar_race_21_messages= qatar_race_21.race_control_messages
qatar_race_21_weather= qatar_race_21.weather_data
qatar_race_21_results = qatar_race_21.results

saudi_arabia_race_21 = ff1.get_session(2021, 21, 'R')
saudi_arabia_race_21.load()
saudi_arabia_race_21_laps = saudi_arabia_race_21.laps
saudi_arabia_race_21_messages= saudi_arabia_race_21.race_control_messages
saudi_arabia_race_21_weather= saudi_arabia_race_21.weather_data
saudi_arabia_race_21_results= saudi_arabia_race_21.results

abu_dhabi_race_21 = ff1.get_session(2021, 22, 'R')
abu_dhabi_race_21.load()
abu_dhabi_race_21_laps = abu_dhabi_race_21.laps
abu_dhabi_race_21_messages= abu_dhabi_race_21.race_control_messages
abu_dhabi_race_21_weather= abu_dhabi_race_21.weather_data
abu_dhabi_race_21_results= abu_dhabi_race_21.results

merge2021_laps = pd.concat([
    bahrain_race_21_laps, 
    italy_race_21a_laps,
    portugal_race_21_laps, 
    spain_race_21_laps,
    monaco_race_21_laps, 
    azerbaijan_race_21_laps,
    france_race_21_laps, 
    austria_race_21a_laps, 
    austria_race_21b_laps,
    great_britain_race_21_laps,
    hungary_race_21_laps, 
    belgium_race_21_laps,
    netherlands_race_21_laps, 
    italy_race_21b_laps,
    russia_race_21_laps,
    turkey_race_21_laps,
    united_states_race_21_laps, 
    mexico_race_21_laps,
    brazil_race_21_laps,
    qatar_race_21_laps, 
    saudi_arabia_race_21_laps, 
    abu_dhabi_race_21_laps],
    keys = ['Bahrain', 
            'ItalyA',
            'Portugal',
            'Spain',
            'Monaco',
            'Azerbaijan',
            'France',
            'AustriaA',
            'AustriaB',
            'GreatBritain',
            'Hungary',
            'Belgium',
            'Netherlands',
            'ItalyB',
            'Russia',
            'Turkey',
            'UnitedStates',
            'Mexico',
            'Brazil',
            'Qatar',
            'SaudiArabia',
            'AbuDhabi'],
    names=['RACE'])

merge2021_messages = pd.concat([
    bahrain_race_21_messages, 
    italy_race_21a_messages,
    portugal_race_21_messages, 
    spain_race_21_messages,
    monaco_race_21_messages, 
    azerbaijan_race_21_messages,
    france_race_21_messages, 
    austria_race_21a_messages, 
    austria_race_21b_messages,
    great_britain_race_21_messages,
    hungary_race_21_messages, 
    belgium_race_21_messages,
    netherlands_race_21_messages, 
    italy_race_21b_messages,
    russia_race_21_messages,
    turkey_race_21_messages,
    united_states_race_21_messages, 
    mexico_race_21_messages,
    brazil_race_21_messages,
    qatar_race_21_messages, 
    saudi_arabia_race_21_messages, 
    abu_dhabi_race_21_messages],
    keys = ['Bahrain', 
            'ItalyA',
            'Portugal',
            'Spain',
            'Monaco',
            'Azerbaijan',
            'France',
            'AustriaA',
            'AustriaB',
            'GreatBritain',
            'Hungary',
            'Belgium',
            'Netherlands',
            'ItalyB',
            'Russia',
            'Turkey',
            'UnitedStates',
            'Mexico',
            'Brazil',
            'Qatar',
            'SaudiArabia',
            'AbuDhabi'],
    names=['RACE'])

merge2021_weather = pd.concat([
    bahrain_race_21_weather, 
    italy_race_21a_weather,
    portugal_race_21_weather, 
    spain_race_21_weather,
    monaco_race_21_weather, 
    azerbaijan_race_21_weather,
    france_race_21_weather, 
    austria_race_21a_weather, 
    austria_race_21b_weather,
    great_britain_race_21_weather,
    hungary_race_21_weather, 
    belgium_race_21_weather,
    netherlands_race_21_weather, 
    italy_race_21b_weather,
    russia_race_21_weather,
    turkey_race_21_weather,
    united_states_race_21_weather, 
    mexico_race_21_weather,
    brazil_race_21_weather,
    qatar_race_21_weather, 
    saudi_arabia_race_21_weather, 
    abu_dhabi_race_21_weather],
    keys = ['Bahrain', 
            'ItalyA',
            'Portugal',
            'Spain',
            'Monaco',
            'Azerbaijan',
            'France',
            'AustriaA',
            'AustriaB',
            'GreatBritain',
            'Hungary',
            'Belgium',
            'Netherlands',
            'ItalyB',
            'Russia',
            'Turkey',
            'UnitedStates',
            'Mexico',
            'Brazil',
            'Qatar',
            'SaudiArabia',
            'AbuDhabi'],
    names=['RACE'])

merge2021_results = pd.concat([
    bahrain_race_21_results, 
    italy_race_21a_results,
    portugal_race_21_results, 
    spain_race_21_results,
    monaco_race_21_results, 
    azerbaijan_race_21_results,
    france_race_21_results, 
    austria_race_21a_results, 
    austria_race_21b_results,
    great_britain_race_21_results,
    hungary_race_21_results, 
    belgium_race_21_results,
    netherlands_race_21_results, 
    italy_race_21b_results,
    russia_race_21_results,
    turkey_race_21_results,
    united_states_race_21_results, 
    mexico_race_21_results,
    brazil_race_21_results,
    qatar_race_21_results, 
    saudi_arabia_race_21_results, 
    abu_dhabi_race_21_results],
    keys = ['Bahrain', 
            'ItalyA',
            'Portugal',
            'Spain',
            'Monaco',
            'Azerbaijan',
            'France',
            'AustriaA',
            'AustriaB',
            'GreatBritain',
            'Hungary',
            'Belgium',
            'Netherlands',
            'ItalyB',
            'Russia',
            'Turkey',
            'UnitedStates',
            'Mexico',
            'Brazil',
            'Qatar',
            'SaudiArabia',
            'AbuDhabi'],
    names=['RACE'])

merge2021_laps["Year"] = 2021
merge2021_messages["Year"] = 2021
merge2021_weather["Year"] = 2021
merge2021_results["Year"] = 2021

#%%
bahrain_race_22 = ff1.get_session(2022, 1, 'R')
bahrain_race_22.load()
bahrain_race_22_laps = bahrain_race_22.laps
bahrain_race_22_messages = bahrain_race_22.race_control_messages
bahrain_race_22_weather= bahrain_race_22.weather_data
bahrain_race_22_results= bahrain_race_22.results

saudi_arabia_race_22 = ff1.get_session(2022, 2, 'R')
saudi_arabia_race_22.load()
saudi_arabia_race_22_laps = saudi_arabia_race_22.laps
saudi_arabia_race_22_messages = saudi_arabia_race_22.race_control_messages
saudi_arabia_race_22_weather= saudi_arabia_race_22.weather_data
saudi_arabia_race_22_results= saudi_arabia_race_22.results

australia_race_22 = ff1.get_session(2022, 3, 'R')
australia_race_22.load()
australia_race_22_laps = australia_race_22.laps
australia_race_22_messages = australia_race_22.race_control_messages
australia_race_22_weather= australia_race_22.weather_data
australia_race_22_results= australia_race_22.results

italy_race_22a = ff1.get_session(2022, 4, 'R')
italy_race_22a.load()
italy_race_22a_laps = italy_race_22a.laps
italy_race_22a_messages = italy_race_22a.race_control_messages
italy_race_22a_weather= italy_race_22a.weather_data
italy_race_22a_results= italy_race_22a.results

united_states_race_22a = ff1.get_session(2022, 5, 'R')
united_states_race_22a.load()
united_states_race_22a_laps = united_states_race_22a.laps
united_states_race_22a_messages= united_states_race_22a.race_control_messages
united_states_race_22a_weather= united_states_race_22a.weather_data
united_states_race_22a_results= united_states_race_22a.results

spain_race_22 = ff1.get_session(2022, 6, 'R')
spain_race_22.load()
spain_race_22_laps = spain_race_22.laps
spain_race_22_messages= spain_race_22.race_control_messages
spain_race_22_weather= spain_race_22.weather_data
spain_race_22_results= spain_race_22.results

monaco_race_22 = ff1.get_session(2022, 7, 'R')
monaco_race_22.load()
monaco_race_22_laps = monaco_race_22.laps
monaco_race_22_messages= monaco_race_22.race_control_messages
monaco_race_22_weather= monaco_race_22.weather_data
monaco_race_22_results= monaco_race_22.results

azerbaijan_race_22 = ff1.get_session(2022, 8, 'R')
azerbaijan_race_22.load()
azerbaijan_race_22_laps = azerbaijan_race_22.laps
azerbaijan_race_22_messages= azerbaijan_race_22.race_control_messages
azerbaijan_race_22_weather= azerbaijan_race_22.weather_data
azerbaijan_race_22_results= azerbaijan_race_22.results

canada_race_22 = ff1.get_session(2022, 9, 'R')
canada_race_22.load()
canada_race_22_laps = canada_race_22.laps
canada_race_22_messages= canada_race_22.race_control_messages
canada_race_22_weather= canada_race_22.weather_data
canada_race_22_results= canada_race_22.results

great_britain_race_22 = ff1.get_session(2022, 10, 'R')
great_britain_race_22.load()
great_britain_race_22_laps = azerbaijan_race_22.laps
great_britain_race_22_messages= azerbaijan_race_22.race_control_messages
great_britain_race_22_weather= azerbaijan_race_22.weather_data
great_britain_race_22_results= azerbaijan_race_22.results

austria_race_22 = ff1.get_session(2022, 11, 'R')
austria_race_22.load()
austria_race_22_laps = austria_race_22.laps
austria_race_22_messages= austria_race_22.race_control_messages
austria_race_22_weather= austria_race_22.weather_data
austria_race_22_results= austria_race_22.results

france_race_22 = ff1.get_session(2022, 12, 'R')
france_race_22.load()
france_race_22_laps = france_race_22.laps
france_race_22_messages= france_race_22.race_control_messages
france_race_22_weather= france_race_22.weather_data
france_race_22_results= france_race_22.results

hungary_race_22 = ff1.get_session(2022, 13, 'R')
hungary_race_22.load()
hungary_race_22_laps = hungary_race_22.laps
hungary_race_22_messages= hungary_race_22.race_control_messages
hungary_race_22_weather= hungary_race_22.weather_data
hungary_race_22_results= hungary_race_22.results

belgium_race_22 = ff1.get_session(2022, 14, 'R')
belgium_race_22.load()
belgium_race_22_laps = belgium_race_22.laps
belgium_race_22_messages= belgium_race_22.race_control_messages
belgium_race_22_weather= belgium_race_22.weather_data
belgium_race_22_results= belgium_race_22.results

netherlands_race_22 = ff1.get_session(2022, 15, 'R')
netherlands_race_22.load()
netherlands_race_22_laps = netherlands_race_22.laps
netherlands_race_22_messages= netherlands_race_22.race_control_messages
netherlands_race_22_weather= netherlands_race_22.weather_data
netherlands_race_22_results= netherlands_race_22.results

italy_race_22b = ff1.get_session(2022, 16, 'R')
italy_race_22b.load()
italy_race_22b_laps = italy_race_22b.laps
italy_race_22b_messages= italy_race_22b.race_control_messages
italy_race_22b_weather= italy_race_22b.weather_data
italy_race_22b_results= italy_race_22b.results

singapore_race_22 = ff1.get_session(2022, 17, 'R')
singapore_race_22.load()
singapore_race_22_laps = singapore_race_22.laps
singapore_race_22_messages= singapore_race_22.race_control_messages
singapore_race_22_weather= singapore_race_22.weather_data
singapore_race_22_results= singapore_race_22.results

japan_race_22 = ff1.get_session(2022, 18, 'R')
japan_race_22.load()
japan_race_22_laps = japan_race_22.laps
japan_race_22_messages= japan_race_22.race_control_messages
japan_race_22_weather = japan_race_22.weather_data
japan_race_22_results= japan_race_22.results

united_states_race_22b = ff1.get_session(2022, 19, 'R')
united_states_race_22b.load()
united_states_race_22b_laps = united_states_race_22b.laps
united_states_race_22b_messages= united_states_race_22b.race_control_messages
united_states_race_22b_weather= united_states_race_22b.weather_data
united_states_race_22b_results= united_states_race_22b.results

mexico_race_22 = ff1.get_session(2022, 20, 'R')
mexico_race_22.load()
mexico_race_22_laps = mexico_race_22.laps
mexico_race_22_messages= mexico_race_22.race_control_messages
mexico_race_22_weather = mexico_race_22.weather_data
mexico_race_22_results= mexico_race_22.results

brazil_race_22 = ff1.get_session(2022, 21, 'R')
brazil_race_22.load()
brazil_race_22_laps = brazil_race_22.laps
brazil_race_22_messages= brazil_race_22.race_control_messages
brazil_race_22_weather = brazil_race_22.weather_data
brazil_race_22_results= brazil_race_22.results

abu_dhabi_race_22 = ff1.get_session(2022, 22, 'R')
abu_dhabi_race_22.load()
abu_dhabi_race_22_laps = abu_dhabi_race_22.laps
abu_dhabi_race_22_messages= abu_dhabi_race_22.race_control_messages
abu_dhabi_race_22_weather = abu_dhabi_race_22.weather_data
abu_dhabi_race_22_results= abu_dhabi_race_22.results

merge2022_laps = pd.concat([
    bahrain_race_22_laps,
    saudi_arabia_race_22_laps,
    australia_race_22_laps,
    italy_race_22a_laps,
    united_states_race_22a_laps,
    spain_race_22_laps,
    monaco_race_22_laps,
    azerbaijan_race_22_laps,
    canada_race_22_laps,
    great_britain_race_22_laps,
    austria_race_22_laps,
    france_race_22_laps,
    hungary_race_22_laps,
    belgium_race_22_laps,
    netherlands_race_22_laps,
    italy_race_22b_laps,
    singapore_race_22_laps,
    japan_race_22_laps,
    united_states_race_22b_laps,
    mexico_race_22_laps,
    brazil_race_22_laps,
    abu_dhabi_race_22_laps],
    keys = ['Bahrain', 
            'SaudiArabia',
            'Australia',
            'ItalyA',
            'UnitedStatesA',
            'Spain',
            'Monaco',
            'Azerbaijan',
            'Canada',
            'GreatBritain',
            'Austria',
            'France',
            'Hungary',
            'Belgium',
            'Netherlands',
            'ItalyB',
            'Singapore',
            'Japan',
            'UnitedStatesB',
            'Mexico',
            'Brazil',
            'AbuDhabi'],
    names=['RACE'])

merge2022_messages = pd.concat([
    bahrain_race_22_messages,
    saudi_arabia_race_22_messages,
    australia_race_22_messages,
    italy_race_22a_messages,
    united_states_race_22a_messages,
    spain_race_22_messages,
    monaco_race_22_messages,
    azerbaijan_race_22_messages,
    canada_race_22_messages,
    great_britain_race_22_messages,
    austria_race_22_messages,
    france_race_22_messages,
    hungary_race_22_messages,
    belgium_race_22_messages,
    netherlands_race_22_messages,
    italy_race_22b_messages,
    singapore_race_22_messages,
    japan_race_22_messages,
    united_states_race_22b_messages,
    mexico_race_22_messages,
    brazil_race_22_messages,
    abu_dhabi_race_22_messages],
    keys = ['Bahrain', 
            'SaudiArabia',
            'Australia',
            'ItalyA',
            'UnitedStatesA',
            'Spain',
            'Monaco',
            'Azerbaijan',
            'Canada',
            'GreatBritain',
            'Austria',
            'France',
            'Hungary',
            'Belgium',
            'Netherlands',
            'ItalyB',
            'Singapore',
            'Japan',
            'UnitedStatesB',
            'Mexico',
            'Brazil',
            'Abu Dhabi'],
    names=['RACE'])

merge2022_weather = pd.concat([
    bahrain_race_22_weather,
    saudi_arabia_race_22_weather,
    australia_race_22_weather,
    italy_race_22a_weather,
    united_states_race_22a_weather,
    spain_race_22_weather,
    monaco_race_22_weather,
    azerbaijan_race_22_weather,
    canada_race_22_weather,
    great_britain_race_22_weather,
    austria_race_22_weather,
    france_race_22_weather,
    hungary_race_22_weather,
    belgium_race_22_weather,
    netherlands_race_22_weather,
    italy_race_22b_weather,
    singapore_race_22_weather,
    japan_race_22_weather,
    united_states_race_22b_weather,
    mexico_race_22_weather,
    brazil_race_22_weather,
    abu_dhabi_race_22_weather],
    keys = ['Bahrain', 
            'SaudiArabia',
            'Australia',
            'ItalyA',
            'UnitedStatesA',
            'Spain',
            'Monaco',
            'Azerbaijan',
            'Canada',
            'GreatBritain',
            'Austria',
            'France',
            'Hungary',
            'Belgium',
            'Netherlands',
            'ItalyB',
            'Singapore',
            'Japan',
            'UnitedStatesB',
            'Mexico',
            'Brazil',
            'AbuDhabi'],
    names=['RACE'])

merge2022_results = pd.concat([
    bahrain_race_22_results,
    saudi_arabia_race_22_results,
    australia_race_22_results,
    italy_race_22a_results,
    united_states_race_22a_results,
    spain_race_22_results,
    monaco_race_22_results,
    azerbaijan_race_22_results,
    canada_race_22_results,
    great_britain_race_22_results,
    austria_race_22_results,
    france_race_22_results,
    hungary_race_22_results,
    belgium_race_22_results,
    netherlands_race_22_results,
    italy_race_22b_results,
    singapore_race_22_results,
    japan_race_22_results,
    united_states_race_22b_results,
    mexico_race_22_results,
    brazil_race_22_results,
    abu_dhabi_race_22_results],
    keys = ['Bahrain', 
            'SaudiArabia',
            'Australia',
            'ItalyA',
            'UnitedStatesA',
            'Spain',
            'Monaco',
            'Azerbaijan',
            'Canada',
            'GreatBritain',
            'Austria',
            'France',
            'Hungary',
            'Belgium',
            'Netherlands',
            'ItalyB',
            'Singapore',
            'Japan',
            'UnitedStatesB',
            'Mexico',
            'Brazil',
            'AbuDhabi'],
    names=['RACE'])

merge2022_laps["Year"] = 2022
merge2022_messages["Year"] = 2022
merge2022_weather["Year"] = 2022
merge2022_results["Year"] = 2022
#%%

mergeTotal_laps = pd.concat([
    merge2018_laps,
    merge2019_laps,
    merge2020_laps,
    merge2021_laps,
    merge2022_laps])

mergeTotal_messages = pd.concat([
    merge2018_messages,
    merge2019_messages,
    merge2020_messages,
    merge2021_messages,
    merge2022_messages])

mergeTotal_weather = pd.concat([
    merge2018_weather,
    merge2019_weather,
    merge2020_weather,
    merge2021_weather,
    merge2022_weather])

mergeTotal_results = pd.concat([
    merge2018_results,
    merge2019_results,
    merge2020_results,
    merge2021_results,
    merge2022_results])

mergeTotal_laps.insert(0, "NewID", range(1, 1 + len(mergeTotal_laps)))
mergeTotal_laps.drop(["Year"], axis=1)
mergeTotal_laps.loc[58170:71068, ["Year"]] = 2022

mergeTotal_messages.insert(0, "NewID", range(1, 1 + len(mergeTotal_messages)))
mergeTotal_messages.drop(["Year"], axis=1)
mergeTotal_messages.loc[58170:71068, ["Year"]] = 2022

mergeTotal_weather.insert(0, "NewID", range(1, 1 + len(mergeTotal_weather)))
mergeTotal_weather.drop(["Year"], axis=1)
mergeTotal_weather.loc[58170:71068, ["Year"]] = 2022

mergeTotal_results.insert(0, "NewID", range(1, 1 + len(mergeTotal_results)))
mergeTotal_results.drop(["Year"], axis=1)
mergeTotal_results.loc[58170:71068, ["Year"]] = 2022

#%%

#converting dataframes into csv for ggplot visualizations

mergeTotal_laps.to_csv("C:\\Users\\andre\\OneDrive\\Desktop\\laps.csv", na_rep='NA')
mergeTotal_messages.to_csv("C:\\Users\\andre\\OneDrive\\Desktop\\messages.csv", na_rep='NA')
mergeTotal_weather.to_csv("C:\\Users\\andre\\OneDrive\\Desktop\\weather.csv", na_rep='NA')
mergeTotal_results.to_csv("C:\\Users\\andre\\OneDrive\\Desktop\\results.csv", na_rep='NA')

#%%

#graphing the track, with the gear shifts used by the fastest driver
#not relevant to the thesis, but that was what the example used
#https://theoehrly.github.io/Fast-F1/examples_gallery/plot_gear_shifts_on_track.html#sphx-glr-examples-gallery-plot-gear-shifts-on-track-py
  
#the first two races of 2018 are not available. here is the code for testing
#neither are austria2020b or belgium2021 
    #test = ff1.get_session(2018, 2, 'R')
    #test.load()
    #lap = china_race_18.laps.pick_fastest()
    #tel = lap.get_telemetry()

#China - 2018
lapChina18 = china_race_18.laps.pick_fastest()
tel = lapChina18.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapChina18['Driver']} - {china_race_18.event['EventName']} {china_race_18.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Azerbaijan - 2018
lapAzerbaijan18 = azerbaijan_race_18.laps.pick_fastest()
tel = lapAzerbaijan18.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapAzerbaijan18['Driver']} - {azerbaijan_race_18.event['EventName']} {azerbaijan_race_18.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Spain - 2018
lapSpain18 = spain_race_18.laps.pick_fastest()
tel = lapSpain18.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapSpain18['Driver']} - {spain_race_18.event['EventName']} {spain_race_18.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Monaco - 2018
lapMonaco18 = monaco_race_18.laps.pick_fastest()
tel = lapMonaco18.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapMonaco18['Driver']} - {monaco_race_18.event['EventName']} {monaco_race_18.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Canada - 2018
lapCanada18 = canada_race_18.laps.pick_fastest()
tel = lapCanada18.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapCanada18['Driver']} - {canada_race_18.event['EventName']} {canada_race_18.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#France - 2018
lapFrance18 = france_race_18.laps.pick_fastest()
tel = lapFrance18.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapFrance18['Driver']} - {france_race_18.event['EventName']} {france_race_18.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Austria - 2018
lapAustria18 = austria_race_18.laps.pick_fastest()
tel = lapAustria18.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapAustria18['Driver']} - {austria_race_18.event['EventName']} {austria_race_18.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Great Britain - 2018
lapGB18 = great_britain_race_18.laps.pick_fastest()
tel = lapGB18.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapGB18['Driver']} - {great_britain_race_18.event['EventName']} {great_britain_race_18.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Germany - 2018
lapGermany18 = germany_race_18.laps.pick_fastest()
tel = lapGermany18.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapGermany18['Driver']} - {germany_race_18.event['EventName']} {germany_race_18.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Hungary - 2018
lapHungary18 = hungary_race_18.laps.pick_fastest()
tel = lapHungary18.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapHungary18['Driver']} - {hungary_race_18.event['EventName']} {hungary_race_18.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Belgium - 2018
lapBelgium18 = belgium_race_18.laps.pick_fastest()
tel = lapBelgium18.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapBelgium18['Driver']} - {belgium_race_18.event['EventName']} {belgium_race_18.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Italy - 2018
lapItaly18 = italy_race_18.laps.pick_fastest()
tel = lapItaly18.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapItaly18['Driver']} - {italy_race_18.event['EventName']} {italy_race_18.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Singapore - 2018
lapSingapore18 = singapore_race_18.laps.pick_fastest()
tel = lapSingapore18.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapSingapore18['Driver']} - {singapore_race_18.event['EventName']} {singapore_race_18.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Russia - 2018
lapRussia18 = russia_race_18.laps.pick_fastest()
tel = lapRussia18.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapRussia18['Driver']} - {russia_race_18.event['EventName']} {russia_race_18.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Japan - 2018
lapJapan18 = japan_race_18.laps.pick_fastest()
tel = lapJapan18.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapJapan18['Driver']} - {japan_race_18.event['EventName']} {japan_race_18.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#United States - 2018
lapUS18 = united_states_race_18.laps.pick_fastest()
tel = lapUS18.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapUS18['Driver']} - {united_states_race_18.event['EventName']} {united_states_race_18.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Mexico - 2018
lapMexico18 = mexico_race_18.laps.pick_fastest()
tel = lapMexico18.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapMexico18['Driver']} - {mexico_race_18.event['EventName']} {mexico_race_18.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Brazil - 2018
lapBrazil18 = brazil_race_18.laps.pick_fastest()
tel = lapBrazil18.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapBrazil18['Driver']} - {brazil_race_18.event['EventName']} {brazil_race_18.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#UAE - 2018
lapUAE18 = united_arab_emirates_race_18.laps.pick_fastest()
tel = lapUAE18.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapUAE18['Driver']} - {united_arab_emirates_race_18.event['EventName']} {united_arab_emirates_race_18.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()
#%%

#Australia - 2019
lapAustralia19 = australia_race_19.laps.pick_fastest()
tel = lapAustralia19.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapAustralia19['Driver']} - {australia_race_19.event['EventName']} {australia_race_19.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Bahrain - 2019
lapBahrain19 = bahrain_race_19.laps.pick_fastest()
tel = lapBahrain19.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapBahrain19['Driver']} - {bahrain_race_19.event['EventName']} {bahrain_race_19.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#China - 2019
lapChina19 = china_race_19.laps.pick_fastest()
tel = lapChina19.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapChina19['Driver']} - {china_race_19.event['EventName']} {china_race_19.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Azerbaijan - 2019
lapAzerbaijan19 = azerbaijan_race_19.laps.pick_fastest()
tel = lapAzerbaijan19.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapAzerbaijan19['Driver']} - {azerbaijan_race_19.event['EventName']} {azerbaijan_race_19.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Spain - 2019
lapSpain19 = spain_race_19.laps.pick_fastest()
tel = lapSpain19.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapSpain19['Driver']} - {spain_race_19.event['EventName']} {spain_race_19.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Monaco - 2019
lapMonaco19 = monaco_race_19.laps.pick_fastest()
tel = lapMonaco19.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapMonaco19['Driver']} - {monaco_race_19.event['EventName']} {monaco_race_19.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Canada - 2019
lapCanada19 = canada_race_19.laps.pick_fastest()
tel = lapCanada19.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapCanada19['Driver']} - {canada_race_19.event['EventName']} {canada_race_19.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#France - 2019
lapFrance19 = france_race_19.laps.pick_fastest()
tel = lapFrance19.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapFrance19['Driver']} - {france_race_19.event['EventName']} {france_race_19.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Austria - 2019
lapAustria19 = austria_race_19.laps.pick_fastest()
tel = lapAustria19.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapAustria19['Driver']} - {austria_race_19.event['EventName']} {austria_race_19.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Great Britain - 2019
lapGB19 = great_britain_race_19.laps.pick_fastest()
tel = lapGB19.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapGB19['Driver']} - {great_britain_race_19.event['EventName']} {great_britain_race_19.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Germany - 2019
lapGermany19 = germany_race_19.laps.pick_fastest()
tel = lapGermany19.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapGermany19['Driver']} - {germany_race_19.event['EventName']} {germany_race_19.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Hungary - 2019
lapHungary19 = hungary_race_19.laps.pick_fastest()
tel = lapHungary19.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapHungary19['Driver']} - {hungary_race_19.event['EventName']} {hungary_race_19.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Belgium - 2019
lapBelgium19 = belgium_race_19.laps.pick_fastest()
tel = lapBelgium19.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapBelgium19['Driver']} - {belgium_race_19.event['EventName']} {belgium_race_19.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Italy - 2019
lapItaly19 = italy_race_19.laps.pick_fastest()
tel = lapItaly19.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapItaly19['Driver']} - {italy_race_19.event['EventName']} {italy_race_19.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Singapore - 2019
lapSingapore19 = singapore_race_19.laps.pick_fastest()
tel = lapSingapore19.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapSingapore19['Driver']} - {singapore_race_19.event['EventName']} {singapore_race_19.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Russia - 2019
lapRussia19 = russia_race_19.laps.pick_fastest()
tel = lapRussia19.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapRussia19['Driver']} - {russia_race_19.event['EventName']} {russia_race_19.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Japan - 2019
lapJapan19 = japan_race_19.laps.pick_fastest()
tel = lapJapan19.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapJapan19['Driver']} - {japan_race_19.event['EventName']} {japan_race_19.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()
 
#Mexico - 2019
lapMexico19 = mexico_race_19.laps.pick_fastest()
tel = lapMexico19.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapMexico19['Driver']} - {mexico_race_19.event['EventName']} {mexico_race_19.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#United States - 2019
lapUS19 = united_states_race_19.laps.pick_fastest()
tel = lapUS19.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapUS19['Driver']} - {united_states_race_19.event['EventName']} {united_states_race_19.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Brazil - 2019
lapBrazil19 = brazil_race_19.laps.pick_fastest()
tel = lapBrazil19.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapBrazil19['Driver']} - {brazil_race_19.event['EventName']} {brazil_race_19.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Abu Dhabi - 2019
lapAbu19 = abu_dhabi_race_19.laps.pick_fastest()
tel = lapAbu19.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapAbu19['Driver']} - {abu_dhabi_race_19.event['EventName']} {abu_dhabi_race_19.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()
#%%
#Austria 2020 - First Race
lapAustria20a = austria_race_20a.laps.pick_fastest()
tel = lapAustria20a.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapAustria20a['Driver']} - {austria_race_20a.event['EventName']} {austria_race_20a.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Great Britain 2020 - First Race
lapGB20a = great_britain_race_20a.laps.pick_fastest()
tel = lapGB20a.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapGB20a['Driver']} - {great_britain_race_20a.event['EventName']} {great_britain_race_20a.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Great Britain 2020 - Second Race
lapGB20b = great_britain_race_20b.laps.pick_fastest()
tel = lapGB20b.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapGB20b['Driver']} - {great_britain_race_20b.event['EventName']} {great_britain_race_20b.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Belgium 2020 
lapBelgium20= belgium_race_20.laps.pick_fastest()
tel = lapBelgium20.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapBelgium20['Driver']} - {belgium_race_20.event['EventName']} {belgium_race_20.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Russia 2020 
lapRussia20= russia_race_20.laps.pick_fastest()
tel = lapRussia20.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapRussia20['Driver']} - {russia_race_20.event['EventName']} {russia_race_20.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Gemany 2020 
lapGemany20= germany_race_20.laps.pick_fastest()
tel = lapGemany20.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapGemany20['Driver']} - {germany_race_20.event['EventName']} {germany_race_20.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Portugal 2020 
lapPortugal20= portugal_race_20.laps.pick_fastest()
tel = lapPortugal20.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapPortugal20['Driver']} - {portugal_race_20.event['EventName']} {portugal_race_20.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Italy 2020 - first race
lapItaly20a = italy_race_20a.laps.pick_fastest()
tel = lapItaly20a.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapItaly20a['Driver']} - {italy_race_20a.event['EventName']} {italy_race_20a.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Italy 2020 - second race
lapItaly20b = italy_race_20b.laps.pick_fastest()
tel = lapItaly20b.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapItaly20b['Driver']} - {italy_race_20b.event['EventName']} {italy_race_20b.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Italy 2020 - third race
lapItaly20c = italy_race_20c.laps.pick_fastest()
tel = lapItaly20c.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapItaly20c['Driver']} - {italy_race_20c.event['EventName']} {italy_race_20c.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Turkey 2020
lapTurkey20 = turkey_race_20.laps.pick_fastest()
tel = lapTurkey20.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapTurkey20['Driver']} - {turkey_race_20.event['EventName']} {turkey_race_20.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Bahrain 2020 - first race
lapBahrain20a = bahrain_race_20a.laps.pick_fastest()
tel = lapBahrain20a.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapBahrain20a['Driver']} - {bahrain_race_20a.event['EventName']} {bahrain_race_20a.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Bahrain 2020 - second race
lapBahrain20b = bahrain_race_20b.laps.pick_fastest()
tel = lapBahrain20b.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapBahrain20b['Driver']} - {bahrain_race_20b.event['EventName']} {bahrain_race_20b.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Abu Dhabi 2020
lapAbu20 = abu_dhabi_race_20.laps.pick_fastest()
tel = lapAbu20.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapAbu20['Driver']} - {abu_dhabi_race_20.event['EventName']} {abu_dhabi_race_20.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()
#%%

#Bahrain 2021
lapBahrain21 = bahrain_race_21.laps.pick_fastest()
tel = lapBahrain21.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapBahrain21['Driver']} - {bahrain_race_21.event['EventName']} {bahrain_race_21.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Italy 2021 - first race
lapItaly21a = italy_race_21a.laps.pick_fastest()
tel = lapItaly21a.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapItaly21a['Driver']} - {italy_race_21a.event['EventName']} {italy_race_21a.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Portugal 2021
lapPortugal21 = portugal_race_21.laps.pick_fastest()
tel = lapPortugal21.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapPortugal21['Driver']} - {portugal_race_21.event['EventName']} {portugal_race_21.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Spain 2021
lapSpain21 = spain_race_21.laps.pick_fastest()
tel = lapSpain21.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapSpain21['Driver']} - {spain_race_21.event['EventName']} {spain_race_21.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Monaco 2021
lapMonaco21 = monaco_race_21.laps.pick_fastest()
tel = lapMonaco21.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapMonaco21['Driver']} - {monaco_race_21.event['EventName']} {monaco_race_21.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Azerbaijan 2021
lapAzerbaijan21 = azerbaijan_race_21.laps.pick_fastest()
tel = lapAzerbaijan21.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapAzerbaijan21['Driver']} - {azerbaijan_race_21.event['EventName']} {azerbaijan_race_21.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#France 2021
lapFrance21 = france_race_21.laps.pick_fastest()
tel = lapFrance21.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapFrance21['Driver']} - {france_race_21.event['EventName']} {france_race_21.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Austria 2021 - first race
lapAustria21a = austria_race_21a.laps.pick_fastest()
tel = lapAustria21a.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapAustria21a['Driver']} - {austria_race_21a.event['EventName']} {austria_race_21a.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Austria 2021 - second race
lapAustria21b = austria_race_21b.laps.pick_fastest()
tel = lapAustria21b.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapAustria21b['Driver']} - {austria_race_21b.event['EventName']} {austria_race_21b.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Great Britain 2021 
lapGB21= great_britain_race_21.laps.pick_fastest()
tel = lapGB21.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapGB21['Driver']} - {great_britain_race_21.event['EventName']} {great_britain_race_21.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Hungary 2021 
lapHungary21= hungary_race_21.laps.pick_fastest()
tel = lapHungary21.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapHungary21['Driver']} - {hungary_race_21.event['EventName']} {hungary_race_21.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()


#Netherlands 2021 
lapNetherlands21= netherlands_race_21.laps.pick_fastest()
tel = lapNetherlands21.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapNetherlands21['Driver']} - {netherlands_race_21.event['EventName']} {netherlands_race_21.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Italy 2021 - second race
lapItaly21b= italy_race_21b.laps.pick_fastest()
tel = lapItaly21b.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapItaly21b['Driver']} - {italy_race_21b.event['EventName']} {italy_race_21b.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Russia 2021
lapRussia21= russia_race_21.laps.pick_fastest()
tel = lapRussia21.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapRussia21['Driver']} - {russia_race_21.event['EventName']} {russia_race_21.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Turkey 2021
lapTurkey21= turkey_race_21.laps.pick_fastest()
tel = lapTurkey21.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapTurkey21['Driver']} - {turkey_race_21.event['EventName']} {turkey_race_21.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#United States 2021
lapUS21= united_states_race_21.laps.pick_fastest()
tel = lapUS21.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapUS21['Driver']} - {united_states_race_21.event['EventName']} {united_states_race_21.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Mexico 2021
lapMexico21= mexico_race_21.laps.pick_fastest()
tel = lapMexico21.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapMexico21['Driver']} - {mexico_race_21.event['EventName']} {mexico_race_21.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Brazil 2021
lapBrazil21= brazil_race_21.laps.pick_fastest()
tel = lapBrazil21.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapBrazil21['Driver']} - {brazil_race_21.event['EventName']} {brazil_race_21.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Qatar 2021
lapQatar21= qatar_race_21.laps.pick_fastest()
tel = lapQatar21.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapQatar21['Driver']} - {qatar_race_21.event['EventName']} {qatar_race_21.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Saudi Arabia 2021
lapSaudi21= saudi_arabia_race_21.laps.pick_fastest()
tel = lapSaudi21.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapSaudi21['Driver']} - {saudi_arabia_race_21.event['EventName']} {saudi_arabia_race_21.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()
 
#Abu 2021
lapAbu21= abu_dhabi_race_21.laps.pick_fastest()
tel = lapAbu21.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapAbu21['Driver']} - {abu_dhabi_race_21.event['EventName']} {abu_dhabi_race_21.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#%%

#Bahrain 2022
lapBahrain22 = bahrain_race_22.laps.pick_fastest()
tel = lapBahrain22.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapBahrain22['Driver']} - {bahrain_race_22.event['EventName']} {bahrain_race_22.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Saudi Arabia 2022
lapSaudi22 = saudi_arabia_race_22.laps.pick_fastest()
tel = lapSaudi22.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapSaudi22['Driver']} - {saudi_arabia_race_22.event['EventName']} {saudi_arabia_race_22.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Australia 2022
lapAustralia22 = australia_race_22.laps.pick_fastest()
tel = lapAustralia22.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapAustralia22['Driver']} - {australia_race_22.event['EventName']} {australia_race_22.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Italy 2022
lapItaly22a = italy_race_22a.laps.pick_fastest()
tel = lapItaly22a.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapItaly22a['Driver']} - {italy_race_22a.event['EventName']} {italy_race_22a.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#US 2022 - first race
lapUS22a = united_states_race_22a.laps.pick_fastest()
tel = lapUS22a.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapUS22a['Driver']} - {united_states_race_22a.event['EventName']} {united_states_race_22a.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Spain 2022
lapSpain22 = spain_race_22.laps.pick_fastest()
tel = lapSpain22.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapSpain22['Driver']} - {spain_race_22.event['EventName']} {spain_race_22.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Monaco 2022
lapMonaco22 = monaco_race_22.laps.pick_fastest()
tel = lapMonaco22.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapMonaco22['Driver']} - {monaco_race_22.event['EventName']} {monaco_race_22.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Azerbaijan 2022
lapAzerbaijan22 = azerbaijan_race_22.laps.pick_fastest()
tel = lapAzerbaijan22.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapAzerbaijan22['Driver']} - {azerbaijan_race_22.event['EventName']} {azerbaijan_race_22.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Canada 2022
lapCanada22 = canada_race_22.laps.pick_fastest()
tel = lapCanada22.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapCanada22['Driver']} - {canada_race_22.event['EventName']} {canada_race_22.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Great Britain 2022
lapGB22 = great_britain_race_22.laps.pick_fastest()
tel = lapGB22.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapGB22['Driver']} - {great_britain_race_22.event['EventName']} {great_britain_race_22.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Austria 2022
lapAustria22 = austria_race_22.laps.pick_fastest()
tel = lapAustria22.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapAustria22['Driver']} - {austria_race_22.event['EventName']} {austria_race_22.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#France 2022
lapFrance22 = france_race_22.laps.pick_fastest()
tel = lapFrance22.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapFrance22['Driver']} - {france_race_22.event['EventName']} {france_race_22.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Hungary 2022
lapHungary22 = hungary_race_22.laps.pick_fastest()
tel = lapHungary22.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapHungary22['Driver']} - {hungary_race_22.event['EventName']} {hungary_race_22.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Belgium 2022
lapBelgium22 = belgium_race_22.laps.pick_fastest()
tel = lapBelgium22.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapBelgium22['Driver']} - {belgium_race_22.event['EventName']} {belgium_race_22.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Netherlands 2022
lapNetherlands22 = netherlands_race_22.laps.pick_fastest()
tel = lapNetherlands22.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapNetherlands22['Driver']} - {netherlands_race_22.event['EventName']} {netherlands_race_22.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Italy 2022
lapItaly22b = italy_race_22b.laps.pick_fastest()
tel = lapItaly22b.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapItaly22b['Driver']} - {italy_race_22b.event['EventName']} {italy_race_22b.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Singapore 2022
lapSingapore22 = singapore_race_22.laps.pick_fastest()
tel = lapSingapore22.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapSingapore22['Driver']} - {singapore_race_22.event['EventName']} {singapore_race_22.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()
 
#Japan 2022
lapJapan22 = japan_race_22.laps.pick_fastest()
tel = lapJapan22.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapJapan22['Driver']} - {japan_race_22.event['EventName']} {japan_race_22.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#US 2022 - second race
lapUS22b = united_states_race_22b.laps.pick_fastest()
tel = lapUS22b.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapUS22b['Driver']} - {united_states_race_22b.event['EventName']} {united_states_race_22b.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#Mexico 2022
lapMexico22 = mexico_race_22.laps.pick_fastest()
tel = lapMexico22.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapMexico22['Driver']} - {mexico_race_22.event['EventName']} {mexico_race_22.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#brazil 2022
lapBrazil22 = brazil_race_22.laps.pick_fastest()
tel = lapBrazil22.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapBrazil22['Driver']} - {brazil_race_22.event['EventName']} {brazil_race_22.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()

#abu dhabi 2022
lapAbu22 = abu_dhabi_race_22.laps.pick_fastest()
tel = lapAbu22.get_telemetry()

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lapAbu22['Driver']} - {abu_dhabi_race_22.event['EventName']} {abu_dhabi_race_22.event.year}"
)
     
cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))
plt.show()
#%%

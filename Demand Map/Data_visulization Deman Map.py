import csv
import pandas as pd
from csv import reader
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import numpy as np
import copy
import math


def calculate_Business(filepath, list):
    # Create a dictionary to store startup's name and the number of the business team.
    # First assign 0 to every value.
    Bus_list = {}
    for l in list:
        Bus_list[l] = 0

    # Iterate every element in the list.
    for l in range(0, len(list)):
        # Reload csv file when each iteration begins.
        csvfile = open(filepath, "r")
        csvreader = csv.reader(csvfile)
        # Iterate every column in the file.
        for item in csvreader:
            # Check if the first grid contains the company.
            if list[l] in item[0]:
                # Check if the second grid contains the Business team.
                words = item[1].split(",")
                for w in words:
                    if ('BUSINESS TEAM' in w or 'CUSTOMER TEAM' in w or 'Customer Service Assistant' in w
                            or 'Social Media Marketing' in w or 'Public Relations' in w
                            or 'Sales & Business Development' in w or 'SEO/SEM' in w
                            or 'Customer Service & User Support' in w):
                        # Update the number.
                        Bus_list[list[l]] += 1
    # Print out the dict
    print(Bus_list)

def calculate_Creative(filepath):
    # Create a dictionary to store startup's name and the number of the creative team.
    # First assign 0 to every value.
    Crea_list = {}
    for l in list:
        Crea_list[l] = 0

    # Iterate every element in the list.
    for l in range(0, len(list)):
        # Reload csv file when each iteration begins.
        csvfile = open(filepath, "r")
        csvreader = csv.reader(csvfile)
        # Iterate every column in the file.
        for item in csvreader:
            # Check if the first grid contains the company.
            if list[l] in item[0]:
                # Check if the second grid contains the Business team.
                words = item[1].split(",")
                for w in words:
                    if ('COMMUNICATIONS TEAM' in w or 'CREATIVE TEAM' in w or 'TEAM 2' in w
                            or 'Content Writer/Editor' in w or 'Graphic Designer' in w
                            or 'Design | Content' in w or 'UX Designer' in w):
                        # Update the number.
                        Crea_list[list[l]] += 1
    # Print out the dict
    print(Crea_list)

def 

def calculate_DSA(filepath):
    # Data Science Army(DSA) will be consider a single team.
    # First assign 0 to the key.
    DSA_list = {'Data Science Army': 0}

    # Reload csv file when each iteration begins.
    csvfile = open(filepath, "r")
    csvreader = csv.reader(csvfile)

    # Iterate every row in the file.
    for item in csvreader:
        # Check if the first grid contains the company.
        if 'DATA SCIENCE ARMY' in item[0]:
            DSA_list['Data Science Army'] += 1
    # Print out the dict
    print(DSA_list)


if __name__ == "__main__":
    #  IDData = pd.read_csv('IDEA LAB DATA - Sheet3.csv')
    listAB = ['46andMix', 'A_Connect', 'AA', 'Abstract', 'Adonis', 'Ahonetwo', 'AIID', 'ANAKIN', 'app’arell',
              'Appbooks', 'Augmented', 'Aura App', 'B4Usend', 'Bachicas', 'BAM', 'BANDAI', 'beep beep', 'BKFK',
              'BODUIT', 'BOTDOJO', 'Botligion', 'Budpay']
    listCDE = ['Carousel', 'Centimint', 'ChickStarter', 'CIRCUMPASS',
               'Citric acid', 'Confessional', 'COPYCATZ', 'Covtrace', 'DB9', 'Disruptive Labs', 'DOCS',
               'DR. INTERNET', 'Droney', 'EasyLazy', 'ecamino', 'Edgeucation', 'egoIDPsyche', 'ELEVATE', 'Emojee',
               'ENERGY CANDY', 'Escargot', 'ESCAVE', 'ETM']
    listFGHJ = ['FAM-ESS', 'FASCIA', 'FEEED', 'FIRESTARTER', 'FORWARD',
                'FOVIES', 'funfunfood', 'Game Chip', 'GERMANA', 'GoGoGo', 'GPS PERSONAS', 'Gpstickys', 'Greenlit',
                'Haba Haba', 'HaiR app', 'HEAD GURU', 'Hiergraphics', 'HORREAL', 'HYPE.YOU.UP', 'INAFLASH', 'INSOLAR',
                'IQ BlindSpot', 'Jellyfish Antfarm']
    listKLM = ['Karma Fund', 'Keanu Capital', 'KHOOBASH', 'LANKING', 'LEFTY',
               'Let\'s Play', 'LIFESHOP', 'LIGHT', 'LIVE MEDITATION', 'LivWin', 'LOOP', 'M.O.M', 'Membrain', 'MICRO',
               'MMMWC', 'Mochi Tochi', 'Mochips', 'Moguly', 'momandpop', 'Momentum', 'MONET VENTURES', 'MONKISH',
               'Moonshadows', 'mooVRoom', 'moredata', 'MOVIE ROOM', 'MUSICGRAF', 'NAIM']
    lisrNPQ = ['Nemebeat', 'nextsport',
               'Now Equity', 'OFFDIAL', 'ONE SPOT', 'OnSupply', 'Open Closet', 'OTHERSIDE', 'Paper to Database'
                                                                                            'Paper Worx', 'PARADISIO',
               'PEACH', 'Pegasus', 'Pendulum', 'PIMPMYPIC', 'Pink Algae', 'PLAID',
               'Playbük', 'PockeTeach', 'POMPOM', 'POV', 'POWERCUBE', 'PREVIEW', 'ProCO2', 'ProFashion', 'PRONTO',
               'Protein', 'PSYCARE']
    listRS = ['Raconteur', 'RAVERSE', 'REP REP', 'Result App', 'Resume Survivor', 'RETURNZ',
              'Ricochet', 'Rise Capital', 'RISE HOLDINGS', 'Rockstar Entrepreneur', 'Round Z', 'RUN IT BACK',
              'Sandy Apples', 'Scoot', 'Second Chances', 'semantexts', 'SEMANTISCALE', 'SharperBarber', 'SHAUP',
              'Shi*heads app', 'SHITSTORM MEDIA', 'SIDE HUSTLE', 'Sitterz', 'Slopes', 'Snakeit', 'SoftWear',
              'SOURCEBRICKS', 'soursashimi', 'Sparkles', 'Split', 'Spotterz', 'Spoucey', 'Surf & Solar', 'SVS',
              'SWEAT FACTORY H AF', 'SweetSpots']
    listTVWY = ['TechCards', 'the algorithm project', 'THE AS', 'The Buddy',
                'THE EMERGENCY BACKPACK', 'THE OLIVIA PROJECT', 'Time Machine', 'Tofushi', 'TOLL\'D', 'TORQUE',
                'Toytrader', 'TRANSFORMHR', 'TRENDZ', 'TRILLION TRACK', 'TRUNKSHOW', 'U.GOD', 'UMAMI', 'Vanilla',
                'Veeting', 'VRISING', 'Waterblades', 'webappapp', 'wetlabs', 'Whatyallthink', 'White Compass',
                'Wincy', 'Wingman', 'WWMD', 'XPR', 'Yogilittle']

    #calculate_Business('IDEA LAB DATA - Sheet3.csv', listAB)
    #calculate_Creative('IDEA LAB DATA - Sheet3.csv', listAB)
    #calculate_Data('IDEA LAB DATA - Sheet3.csv', listAB)
    #calculate_Developers('IDEA LAB DATA - Sheet3.csv', listAB)
    #calculate_PM('IDEA LAB DATA - Sheet3.csv', listAB)

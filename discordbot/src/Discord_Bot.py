from bs4 import BeautifulSoup
import json
import urllib3
from pandas.io.html import read_html
import requests
import discord
from lxml import etree
import csv
import re
import pandas as pd 
from discord.ext import commands
from urllib.request import urlopen
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pandas as pd
import io


client = commands.Bot(command_prefix = '.')



@client.event
async def on_ready():
    print('Bot is ready.')

@client.command(aliases=['bothelp'])
async def botDef(ctx):
    await ctx.send(f'Usage is as follows:\n> .elecResult <state|congressional district> <cd|prez>. \n> For congressional districts, put a 0 in the front of singular numbers.\n> Example: CA-05.\n> For states with multiple words, put an underline.\n> Example: North_Carolina')


@client.command(aliases=['elec'])
async def args(ctx, question, arg1, arg2 = None):
    if question == "nevada":
        question = "Nevada"

    def filenameRetrieve(filename1, test1, test2):
        filename = filename1
        fields = []
        rows = []
        with open(filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            fields = next(csvreader)
            for row in csvreader:
                    rows.append(row)

            col = [x[0] for x in rows]
                
            if question in col:
                for x in range(0, len(rows)):
                    if question == rows[x][0]:
                        return [rows[x][test1], rows[x][test2], rows[x][12], rows[x][9], rows[x][2], rows[x][3], rows[x][4], rows[x][5], rows[x][8]]
               
#    await ctx.send(f'{test[0]}\n')
    # if arg2 == "2014":
    #     if arg1 == "senate":
    #         html = urlopen('https://en.wikipedia.org/wiki/2014_United_States_Senate_election_in_' + question)
    #         embed = discord.Embed(title = "2014 Senate Election",description="A description of this state in its 2014 Senate election",colour=random.randint(0, 0xffffff))
    #         bs = BeautifulSoup(html, 'html.parser')
    #         images = bs.find_all('img', {'src':re.compile('.svg')})
    #         for image in images: 
    #             try :  
    #                 result = image['src'].index("Election_Results_by_County")
    #                 test = image['src']
    #                 embed.set_image(url="https:"+test)
    #             except:
    #                 pass
    #         await ctx.send(embed=embed)

    #     if arg1 == "gov":
    #         html = urlopen('https://en.wikipedia.org/wiki/2014_' + question + '_gubernatorial_election')
    #         embed = discord.Embed(title = "2014 Gubernatorial Election",description="A description of this state in its 2014 gubernatorial election",colour=random.randint(0, 0xffffff))
    #         bs = BeautifulSoup(html, 'html.parser')
    #         images = bs.find_all('img', {'src':re.compile('.svg')})
    #         for image in images: 
    #             try :  
    #                 result = image['src'].index("Election_Results_by_County")
    #                 test = image['src']
    #                 embed.set_image(url="https:"+test)
    #             except:
    #                 pass
    #         await ctx.send(embed=embed)
    # if arg2 == "2018":
    #     if arg1 == "senate":
    #         html = urlopen('https://en.wikipedia.org/wiki/2018_United_States_Senate_election_in_' + question)
    #         bs = BeautifulSoup(html, 'html.parser')
    #         embed = discord.Embed(title = "2018 Senate Election",description="A description of this state in its 2018 senate election",colour=random.randint(0, 0xffffff))
    #         images = bs.find_all('img', {'src':re.compile('.svg')})
    #         for image in images: 
    #             try : 
    #                 if question == "California":
    #                     result = image['src'].index("CA_US_Senate_2018")
    #                 else:
    #                     reuslt = image['src'].index("Election_Results_by_County")
    #                 test = image['src']
    #                 embed.set_image(url="https:"+test)
    #             except:
    #                 pass
    #         await ctx.send(embed=embed)
    #     if arg1 == "gov":
    #         html = urlopen('https://en.wikipedia.org/wiki/2018_' + question + '_gubernatorial_election')
    #         bs = BeautifulSoup(html, 'html.parser')
    #         embed = discord.Embed(title = "2018 Gubernatorial Election",description="A description of this state in its 2018 gubernatorial election",colour=random.randint(0, 0xffffff))
    #         images = bs.find_all('img', {'src':re.compile('.svg')})
    #         for image in images: 
    #             try :  
    #                 result = image['src'].index("Election_Results_by_County")
    #                 test = image['src']
    #                 embed.set_image(url="https:"+test)
    #             except:
    #                 pass
    #         await ctx.send(embed=embed)
    # if arg2 == "2012":
    #     if arg1 == "prez":
    #         test = filenameRetrieve("2012prez.csv", 2, 5)
    #         html = urlopen('https://en.wikipedia.org/wiki/2012_United_States_presidential_election_in_' + question)
    #         embed = discord.Embed(title = "2012 Presidential Election",description="A description of this state in the 2012 election",colour=random.randint(0, 0xffffff))
    #         bs = BeautifulSoup(html, 'html.parser')
    #         images = bs.find_all('img', {'src':re.compile('.svg')})
    #         for image in images: 
    #             try :  
    #                 if question == "Rhode_Island":
    #                     question = "Rhode_island"
    #                 if question == "New_York":
    #                     question = "New_york"
    #                 result = image['src'].index(question + "_presidential_election_results_2012")
    #                 test = image['src']
    #                 embed.set_image(url="https:"+test)
    #             except : 
    #                 pass
    #         await ctx.send(embed=embed)
    #     if arg1 == "senate":
    #             html = urlopen('https://en.wikipedia.org/wiki/2012_United_States_Senate_election_in_' + question)
    #             bs = BeautifulSoup(html, 'html.parser')
    #             embed = discord.Embed(title = "2012 Senate Election",description="A description of this state in its 2012 senate election",colour=random.randint(0, 0xffffff))
    #             images = bs.find_all('img', {'src':re.compile('.svg')})
    #             page = 'https://en.wikipedia.org/wiki/2012_United_States_Senate_election_in_' + question
    #             var = 0
    #             for image in images:  
    #                 try :
    #                     result = image['src'].index("2012")
    #                     test = image['src']
    #                     var = var + 1
    #                     if var == 1:
    #                         embed.set_image(url="https:"+test)
    #                     else:
    #                         pass
    #                 except:
    #                     pass
    #             await ctx.send(embed=embed)
    #     if arg1 == "gov":
    #         html = urlopen('https://en.wikipedia.org/wiki/2012_' + question + '_gubernatorial_election')
    #         bs = BeautifulSoup(html, 'html.parser')
    #         embed = discord.Embed(title = "2012 Gubernatorial Election",description="A description of this state in its 2012 gubernatorial election",colour=random.randint(0, 0xffffff))
    #         images = bs.find_all('img', {'src':re.compile('.svg')})
    #         for image in images: 
    #             try :  
    #                 result = image['src'].index("Election_Results_by_County")
    #                 test = image['src']
    #                 await ctx.send(f'https:{test}\n')
    #             except:
    #                 pass

    #         await ctx.send(embed=embed)
    if arg2 == "2016" or arg2 is None or arg2 == "2020":
        if arg1 == "cd" and arg2 is None:
            filename1 = 'StateAbbr.csv'
            fields1 = []
            rows1 = []
            with open(filename1, 'r') as csvfile1:
                csvreader1 = csv.reader(csvfile1)
                fields1 = next(csvreader1)
                for row in csvreader1:
                        rows1.append(row)

                col1 = [d[0] for d in rows1]
                question = question.upper()
                if question[:2] in col1:
                    for d in range(0, len(rows1)):
                        if question[:2] == rows1[d][0]:
                            question1 = rows1[d][1]
            if question[-2:] == "AL":
                html = urlopen("https://en.wikipedia.org/wiki/" + question1 + "%27s__at-large_congressional_district")
                pass
            elif int(question[-2:]) == 10 or int(question[-2:]) == 11 or int (question[-2:]) == 12 or int(question[-2:]) == 13:
                html = urlopen('https://en.wikipedia.org/wiki/' + question1 + "%27s_" + question[-2:] + "th_congressional_district")
            elif int(question[-1]) == 1 or (int(question[-2] == 0) and int(question[-1] == 1)):
                if (question[-2] == '-' or question[-2] == '0'):                
                    html = urlopen('https://en.wikipedia.org/wiki/' + question1 + "%27s_" + question[-1] + "st_congressional_district")
            elif int(question[-1]) == 2 or (int(question[-2] == 0) and int(question[-1] == 2)):
                if (question[-2] == '-' or question[-2] == '0'): 
                    html = urlopen('https://en.wikipedia.org/wiki/' + question1 + "%27s_" + question[-1] + "nd_congressional_district")
                else:
                    html = urlopen('https://en.wikipedia.org/wiki/' + question1 + "%27s_" + question[-2:] + "nd_congressional_district")
            elif int(question[-1]) == 3 or (int(question[-2] == 0) and int(question[-1] == 3)):
                if (question[-2] == '-' or question[-2] == '0'): 
                    html = urlopen('https://en.wikipedia.org/wiki/' + question1 + "%27s_" + question[-1] + "rd_congressional_district")
                else:
                    html = urlopen('https://en.wikipedia.org/wiki/' + question1 + "%27s_" + question[-2:] + "rd_congressional_district")
            elif ((3 < int(question[-1]) <= 9) and ((question[-2]) == '-') or (3 < int(question[-1]) <= 9) and ((question[-2]) == '0')):
                if (question[-2] == '-' or question[-2] == '0'): 
                    html = urlopen('https://en.wikipedia.org/wiki/' + question1 + "%27s_" + question[-1:] + "th_congressional_district")  
            else:
                html = urlopen('https://en.wikipedia.org/wiki/' + question1 + "%27s_" + question[-2:] + "th_congressional_district")  

        
            bs = BeautifulSoup(html, 'html.parser')
            images = bs.find_all('img', {'src':re.compile('.png')})
            var = 0
            tbl = bs.find("table", {"class": "infobox vcard; width=200px;"})
            table_body = tbl.find('tbody')

            rows = table_body.find_all('tr')
            data = []
            descriptor = []
            testing = 0
            str1 = " "
            for row in rows:
                cols = row.find_all('td')
                cols = [ele.text.strip() for ele in cols]
                data.append([ele for ele in cols if ele])
                str1 = ' '.join(cols)
                testing = testing + 1

            testing = 0
            for row in rows:
                cols = row.find_all('th')
                cols = [ele.text.strip() for ele in cols]
                descriptor.append([ele for ele in cols if ele])
                str1 = ' '.join(cols)
                testing = testing + 1

            out = [item for t in data for item in t] 

            labelNames = [item for t in descriptor for item in t]
            
            embed = discord.Embed(title = labelNames[0],description="A general description of this congressional district",colour=random.randint(0, 0xffffff))

            fixedNums = []
            fixedLabels = []
            numRelevant = 0
            otherNumRelevant = 0
            for i in out:
                numRelevant = numRelevant  + 1
                a_string = i
                testing3 = re.sub(r'\[.*?\]', '', a_string)
                testing3 = re.sub(r"(\w)([A-Z])", r"\1 \2", testing3)
                testing3 = re.sub(r'([a-zA-Z])(?=\d)',r'\1 ',testing3)
                if numRelevant > 3:
                    fixedNums.append(testing3)
                    otherNumRelevant = otherNumRelevant + 1
            
            numRelevant = 0
            otherNumRelevant = 0
            for i in labelNames:
                numRelevant = numRelevant  + 1
                a_string = i
                testing3 = re.sub(r'\[.*?\]', '', a_string)
                testing3 = re.sub(r'([a-zA-Z])(?=\d)',r'\1 ',testing3)
                if numRelevant > 1:
                    fixedLabels.append(testing3)
                    otherNumRelevant = otherNumRelevant + 1
            toMoveEthnicity = []

            for labelName, detailName in zip(fixedLabels, fixedNums):
                if labelName == "Ethnicity":
                    toMoveEthnicity.append(detailName)                    
                else:
                    embed.add_field(name=labelName, value=detailName)
            try:
                embed.add_field(name="Ethnicity", value= toMoveEthnicity[0])
            except IndexError:
                pass
           


            test = filenameRetrieve("Education.csv", 3, 4)
            embed.add_field(name="Education: ", value= "Less than High School: " + test[4] + "\nHigh school: " +test[5] + "\nSome College: " + test[6] + "\nCollege or more: " + test[7])

            test = filenameRetrieve("Education.csv", 6, 7)
            embed.add_field(name="Whites by Education", value= "College Educated: " + test[0] + "\nNon-College educated: "+ test[1])


            test = filenameRetrieve("dailykosHouse.csv", 3, 4)
           
          #  float(re.findall(r'"(.*?)"', test[0]))
            if float(test[0]) > float(test[1]):
                embed.add_field(name="**2016 Presidential Election**", value= "**Hillary Clinton: "+test[0] + "%**\nDonald Trump: " + test[1] + "%")
            else:
                embed.add_field(name="**2016 Presidential Election**", value= "Hillary Clinton: "+test[0] + "%**\nDonald Trump: " + test[1] + "%**")

            test = filenameRetrieve("2018-house.csv", 19, 20)
            if test[3] == "No Major Opponent" or test[8] == "No Major Opponent":
                embed.add_field(name="**2018 House Election**", value= "**" + test[2] + ": " + test[0] + "**")
            elif int(test[1]) < int(test[0]):
                embed.add_field(name="**2018 House Election**", value= "**" + test[2] + ": " +test[0] + "%**\n" + test[3] + ": " + test[1] + "%")
            else :
                embed.add_field(name="**2018 House Election**", value= "" + test[2] + ": " +test[0] + "%\n**" + test[3] + ": " + test[1] + "%**")
            
           # test = filenameRetrieve("Education.csv", 3, 4)
           # embed.add_field(name="**College**", value= "**" + test[2] + ": " +test[0] + "**\n**" + test[3] + "**")
            

            for image in images: 
                try : 
                    var = var + 1
                    if var == 1:  
                        if str(question[:2]) == "WA":
                            result = image['src'].index("WA")
                            test = image['src']
                            embed.set_image(url="https:"+test)
                        else:
                            result = image['src'].index("US_Congressional_District")
                            test = image['src']
                            embed.set_image(url="https:"+test)
                    else:
                        pass
                except:
                    pass 
            await ctx.send(embed=embed)

        if arg1 == "prez":
            filename1 = 'StateAbbr.csv'
            fields1 = []
            rows1 = []
            
            if (len(question) == 2):
                question = question.upper()
                with open(filename1, 'r') as csvfile1:
                    csvreader1 = csv.reader(csvfile1)
                    fields1 = next(csvreader1)
                    for row in csvreader1:
                            rows1.append(row)

                    col1 = [d[0] for d in rows1]
                    question = question.upper()
                    if question[:2] in col1:
                        for d in range(0, len(rows1)):
                            if question[:2] == rows1[d][0]:
                                question = rows1[d][1]
            else:
                question = question.lower()
                question = question.capitalize()
            test3 = filenameRetrieve("2016prez.csv", 2, 5)
            html = urlopen('https://en.wikipedia.org/wiki/2016_United_States_presidential_election_in_' + question)
            bs = BeautifulSoup(html, 'html.parser')
            images = bs.find_all('img', {'src':re.compile('.svg')})
            embed = discord.Embed(title = "2016 Presidential Election",description="A description of this state in the 2016 election",colour=random.randint(0, 0xffffff))
            for image in images: 
                try :  
                    if (question == "New_Hampshire"):
                        result = image['src'].index("NewHamshirePresidentialElectionResults2016")
                        test = image['src']
                        embed.set_image(url="https:"+test)
                    else: 
                        result = image['src'].index(question + "_Presidential_Election_Results_2016")
                        test = image['src']
                        embed.set_image(url="https:"+test)
                except:
                    pass
            print(test)
            if float(test3[0].rstrip("%")) > float(test3[1].rstrip("%")):
                embed.add_field(name="**2016 Presidential Elections**", value= "**Hillary Clinton:** " + test3[0] + "\nDonald Trump: " + test3[1])
            else:
                embed.add_field(name="**2016 Presidential Elections**", value= "**Donald Trump:**" + test3[1] + "\nHillary Clinton: " + test3[0])
            
            test = filenameRetrieve("RCPLinks.csv", 2, 3)
            if  test[0] != "":
                questionRCP = question.lower()
                html = urlopen("https://www.realclearpolitics.com/epolls/2020/president/" + test[1] + "/" + questionRCP + "_trump_vs_biden-" + test[0] + ".html")
                bs = BeautifulSoup(html, 'html.parser')
                tbl = bs.findAll('tr',{'class':'rcpAvg'})

                data = []
                descriptor = []
                testing = 0
                str1 = ""
                for row in tbl:
                    cols = row.find_all('td')
                    cols = [ele.text.strip() for ele in cols]
                    data.append([ele for ele in cols if ele])
                    str1 = ' '.join(cols)
                    testing = testing + 1
                rcpThumbnail = [item for t in data for item in t] 
                
                embed.add_field(name="**2020 RCP Current Polling Average**", value= "Donald Trump: "  + rcpThumbnail[5] +  "%" + "\nJoe Biden: " + rcpThumbnail[4] + "%\n" + "**" + rcpThumbnail[6] + "**")

            
                # testing = 0
                # for row in rows:
                #     cols = row.find_all('th')
                #     cols = [ele.text.strip() for ele in cols]
                #     descriptor.append([ele for ele in cols if ele])
                #     str1 = ' '.join(cols)
                #     testing = testing + 1

            url="https://projects.fivethirtyeight.com/2020-general-data/presidential_state_toplines_2020.csv"
            s=requests.get(url).content
            c=pd.read_csv(io.StringIO(s.decode('utf-8')))
            c = c[:58]
            c.drop(c.columns[0], axis=1, inplace=True)
            c.drop(c.columns[1], axis=1, inplace=True)
            c.drop(c.columns[2], axis=1, inplace=True)
            question = question.replace("_"," ")
            indexofState = c.state[c.state == question].index.tolist()
            test = round(c.at[indexofState[0], "voteshare_inc"], 2)
            trumpExpectedShare = str(round(c.at[indexofState[0], "voteshare_inc"], 2))
            bidenExpectedShare = str(round(c.at[indexofState[0], "voteshare_chal"], 2))
            embed.add_field(name="**2020 538 Predicted Vote Share**", value= "Donald Trump: "  + trumpExpectedShare +  "%" + "\nJoe Biden: " + bidenExpectedShare + "%")



            trumpExpectedShare = str(round((c.at[indexofState[0], "winstate_inc"]*100), 2))
            bidenExpectedShare = str(round((c.at[indexofState[0], "winstate_chal"]*100), 2))
            embed.add_field(name="**2020 538 Probability of Win**", value= "Donald Trump: "  + trumpExpectedShare +  "%" + "\nJoe Biden: " + bidenExpectedShare + "%")


            await ctx.send(embed=embed)

        # if arg1 == "senate":
        #     html = urlopen('https://en.wikipedia.org/wiki/2016_United_States_Senate_election_in_' + question)
        #     bs = BeautifulSoup(html, 'html.parser')
        #     images = bs.find_all('img', {'src':re.compile('.svg')})
        #     embed = discord.Embed(title = "2016 Senate Election",description="A description of this state in its 2016 senate election",colour=random.randint(0, 0xffffff))
        #     for image in images: 
        #         try :  
        #             if (question == "California"):
        #                 result = image['src'].index("2016_CA_US_Senate")
        #             else:
        #                 result = image['src'].index("Election_Results_by_County")
        #             test = image['src']
        #             embed.set_image(url="https:"+test)
        #         except:
        #             pass

        #     await ctx.send(embed=embed)
        # if arg1 == "gov":
        #     html = urlopen('https://en.wikipedia.org/wiki/2016_' + question + '_gubernatorial_election')
        #     bs = BeautifulSoup(html, 'html.parser')
        #     images = bs.find_all('img', {'src':re.compile('.svg')})
        #     embed = discord.Embed(title = "2016 Gubernatorial Election",description="A description of this state in its 2016 gubernatorial election",colour=random.randint(0, 0xffffff))
        #     for image in images: 
        #         try :  
        #             result = image['src'].index("Election_Results_by_County")
        #             test = image['src']
        #             embed.set_image(url="https:"+test)
        #         except:
        #             pass
        #     await ctx.send(embed=embed)
# await ctx.send(f'Question : Election Result for:{[image[2]]}\nAnswer: ')
    


client.run('')

import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import copy
import math


# import numpy as np

# Please give us charts of the top 10 Startups or Startups sored 10 in each of these categories:
# User Stickiness
# Conversion %
# Profitability
# Scope of investment
# Relevance to customer
# Innovation
# Total score

def create_pie(data, column):
    data = data.groupby(column).size().sort_values(ascending=True)
    data = data.sort_index(ascending=False)
    print(data)
    plt.pie(data.values, labels=data.index, autopct='%.1f%%', explode=[0, 0, 0, 0, 0, 0, 0.2, 0.4, 0.7])
    plt.title('Distribution by User Stickness(%)')
    plt.legend(data.index, bbox_to_anchor=(1.2,0.8), loc="center right")
    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.75)
    plt.show()

def load_data(filepath):
    # read .csv
    reader = pd.read_csv(filepath)
    header_list = reader.columns.tolist()


    user_stickness = reader.sort_values(by=header_list[6], ascending=False)
    user_stickness = user_stickness.nlargest(10, header_list[6])
    user_stickness.plot.bar(x=header_list[0], y=header_list[6], title='Top 10 Startup by User Stickness')
    plt.bar(user_stickness.Name, user_stickness.User_Stickiness, label = '_nolegend_')
    plt.xticks(user_stickness.Name, rotation=90)
    plt.xlabel('Name')
    plt.ylabel('Score')
    plt.title('Top 10 Startups by User Stickness', fontsize=16)
    plt.tight_layout()
    plt.show()
 #   create_pie(reader, header_list[6])


    Innovation = reader.sort_values(by=header_list[1], ascending=False)
    Innovation = Innovation.loc[Innovation['Innovation'] == 10]
    plt.bar(Innovation.Name, Innovation.Innovation)
    #Innovation.plot.bar(x=header_list[0], y=header_list[1], title='Top 15 Startup by Innovation')
    plt.xticks(Innovation.Name, rotation=90)
    plt.xlabel('Name')
    plt.ylabel('Score')
    plt.title('Startups scored 10 by Innovation', fontsize=16)
    plt.tight_layout()
    plt.show()
#    create_pie(reader, header_list[1])

    Relevance = reader.sort_values(by=header_list[2], ascending=False)
    Relevance = Relevance.loc[Relevance['Relevance_to_Need_of_customer'] == 10]
    plt.bar(Relevance.Name, Relevance.Relevance_to_Need_of_customer)
    plt.xticks(Relevance.Name, rotation=90)
    plt.xlabel('Name')
    plt.ylabel('Score')
    plt.title('Startups scored 10 by Relevance to Need of customer', fontsize=16)
    plt.tight_layout()
    plt.show()
    Rel_data = reader.groupby(header_list[2]).size().sort_values(ascending=True)
    Rel_data = Rel_data.sort_index(ascending=False)
    plt.pie(Rel_data.values, labels=Rel_data.index, autopct='%.1f%%', explode=[0, 0, 0, 0, 0, 0, 0.2, 0.4, 0.7])
    plt.title('Distribution by Relevance to Need of customer(%)')
    plt.legend(Rel_data.index, bbox_to_anchor=(1.2, 0.8), loc="center right")
    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.75)
    plt.show()


    Scope = reader.sort_values(by=header_list[3], ascending=False)
    Scope = Scope.loc[Scope['Scope_of_Investment'] == 10]
    plt.bar(Scope.Name, Scope.Scope_of_Investment)
    plt.xticks(Scope.Name, rotation=90)
    plt.xlabel('Name')
    plt.ylabel('Score')
    plt.title('Startups scored 10 by Scope of Investment', fontsize=16)
    plt.tight_layout()
    plt.show()
    Scope_data = reader.groupby(header_list[3]).size().sort_values(ascending=True)
    Scope_data = Scope_data.sort_index(ascending=False)
    plt.pie(Scope_data.values, labels=Scope_data.index, autopct='%.1f%%', explode=[0, 0, 0, 0, 0, 0, 0.2, 0.4, 0.7])
    plt.title('Distribution by Scope of Investment(%)')
    plt.legend(Scope_data.index, bbox_to_anchor=(1.2, 0.8), loc="center right")
    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.75)
    plt.show()

    Profitability = reader.sort_values(by=header_list[4], ascending=False)
    Profitability = Profitability.loc[Profitability['Profitability'] == 10]
    plt.bar(Profitability.Name, Profitability.Profitability)
    plt.xticks(Profitability.Name, rotation=90)
    plt.xlabel('Name')
    plt.ylabel('Score')
    plt.title('Startups scored 10 by Profitability', fontsize=16)
    plt.tight_layout()
    plt.show()
    Pro_data = reader.groupby(header_list[4]).size().sort_values(ascending=True)
    Pro_data = Pro_data.sort_index(ascending=False)
    plt.pie(Pro_data.values, labels=Pro_data.index, autopct='%.1f%%', explode=[0, 0, 0, 0, 0, 0.2, 0.4, 0.7])
    plt.title('Distribution by Profitability(%)')
    plt.legend(Pro_data.index, bbox_to_anchor=(1.2, 0.8), loc="center right")
    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.75)
    plt.show()

    Convention = reader.sort_values(by=header_list[5], ascending=False)
    Convention = Convention.nlargest(10, header_list[5])
    Convention.plot.bar(x=header_list[0], y=header_list[5], title='Top 10 Startups by Conversion Possibility')
    plt.show()
    Con_data = reader.groupby(header_list[5]).size().sort_values(ascending=True)
    Con_data = Con_data.sort_index(ascending=False)
    plt.pie(Con_data.values, labels=Con_data.index, autopct='%.1f%%', explode=[0, 0, 0, 0, 0, 0.2, 0.4, 0.7])
    plt.title('Distribution by Conversion Possibility(%)')
    plt.legend(Con_data.index, bbox_to_anchor=(1.2, 0.8), loc="center right")
    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.75)
    plt.show()

if __name__ == "__main__":
    test_l = load_data('ROUND Z SCORECARD - Score Card.csv')

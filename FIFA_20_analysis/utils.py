
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random
from matplotlib.colors import ListedColormap

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from mlxtend.plotting import plot_confusion_matrix


def get_best_team(data, nationality, chosen_tactic):

    best_team = []

    print("\nBest Team using tactic {} of {}:\n{}".format(chosen_tactic['name'], nationality, '='*35))

    for i in chosen_tactic['positions']:
        potential_players = data[(data['nationality'] == nationality) 
                                    & (data['player_positions'].str.contains(i))
                                   ].sort_values(['overall'], ascending=False)

        ind = 0
        if len(potential_players) == 0:
            return []
        while potential_players.iloc[ind].short_name in best_team:
            ind +=1

        best_team.append(potential_players.iloc[ind].short_name)
        print(i + ':', potential_players.iloc[ind].short_name + ' (' + str(potential_players.iloc[ind].overall) + ')')

    return best_team


def get_best_talents(data, initial_overall=80):
    
    data['overall_diff'] = data.potential - data.overall
    
    data.sort_values(['overall_diff'], ascending = False, inplace = True)
    
    return data.loc[data.overall >= initial_overall, ['short_name', 'age', 'nationality', 'club', 'player_positions', 'overall', 'potential']].head(10)


def stats_players(data):
    
    pos_dict = {
        'GK': 'GK',
        'RW': 'ATA',
        'ST': 'ATA',
        'LW': 'ATA',
        'CAM': 'MED',
        'CB': 'DEF',
        'CM': 'MED',
        'CDM': 'MED',
        'CF': 'ATA',
        'LB': 'DEF',
        'RB': 'DEF',
        'RM': 'MED',
        'LM': 'MED',
        'LWB': 'DEF',
        'RWB': 'DEF'
    }
    
    data['general_position'] = data['main_position'].map(pos_dict)
    
    #use only the stats/attributes columns
    data = data.iloc[:, np.append([2, 14, -2, -1], np.arange(31, len(data.columns) - 28))]
    
    data.drop(['gk_diving', 'gk_handling', 'gk_kicking', 'gk_reflexes', 'gk_speed', 'gk_positioning', 'player_traits'], axis = 1, inplace = True)
    
    data.fillna(0, inplace = True)
    
    return data

def positions_distribution(data, target_positions):
    
    data = stats_players(data.copy())
    data = data.iloc[0:5000, :]
    
    data = data[data['general_position'].isin(target_positions)]
    
    
    pos_dict = {
        'GK': 0,
        'DEF': 1,
        'MED': 2,
        'ATA': 3
    }
    
    data = data.sample(frac=1)
    target = data['general_position'].map(pos_dict).values
    
    data_attributes = data.drop(['short_name', 'player_positions', 'main_position', 'general_position'], axis = 1)
    
    pca_model = PCA(n_components=2)
    reduced_data = pca_model.fit_transform(data_attributes)
    
    colors = ListedColormap(['grey', 'tab:red', 'tab:olive', 'tab:blue'])
    
    fig, ax = plt.subplots(figsize=(12, 10))
    #ax = fig.add_subplot(111, projection='3d')
    
    scatter = ax.scatter(reduced_data[:, 0], reduced_data[:, 1], c=target, cmap=colors)
    
    plt.legend(handles=scatter.legend_elements()[0], labels=target_positions)
    plt.xlabel('Component 1')
    plt.ylabel('Component 2')
    plt.title('Position Distribution: ' + ', '.join(target_positions))
    
    plt.savefig('static/positions_1.png')


def all_positions_distribution(data):
    
    data = stats_players(data.copy())
    data = data.iloc[0:5000, :]
    data = data[data['main_position'] != 'GK']
    
    pos_dict = {}
    
    l = ['CB', 'LB', 'RB', 'LWB', 'RWB', 'CMD', 'CM', 'CAM', 'RM', 'LM', 'RW', 'LW', 'CF', 'ST']

    for i, p in enumerate(l):
        pos_dict[p] = i
    
    data = data.sample(frac=1)
    target = data['main_position'].map(pos_dict).values
    
    data_attributes = data.drop(['short_name', 'player_positions', 'main_position', 'general_position'], axis = 1)
    
    pca_model = PCA(n_components=2)
    reduced_data = pca_model.fit_transform(data_attributes)
    
    colors = plt.get_cmap('viridis_r')
    
    fig = plt.figure(figsize=(18, 12))
    
    
    for i, p in enumerate(l):
        c = colors(i/len(l))
        inds = [j for j, x in enumerate(data['main_position']) if x == p]
        plt.scatter(reduced_data[inds, 0], reduced_data[inds, 1], label=p, color=c)
    
    
    plt.legend(loc='upper right')
    plt.xlabel('Component 1')
    plt.ylabel('Component 2')
    plt.title('Position Distribution: ' + ', '.join(l))
    
    plt.savefig('static/positions_2.png')


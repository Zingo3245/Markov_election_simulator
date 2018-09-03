#Import numpy for arrays and random to simulate probability. I later added matplotlib for plotting.
import numpy as np
import random
import matplotlib.pyplot as plt

print("Please enter how many election simulations you want to run:")
times = int(input())

def original_election():
    #We will start with the 2016 election. The primary will create a senario number.
    Current_President = 'Obama'
    canidate = []
    President_List = [Current_President]
    canidate_sen = {'Clinton': {'Trump': 1, 'Cruz': 2, 'Kasich': 3},
                   'Sanders': {'Trump': 4, 'Cruz': 5, 'Kasich': 6}}
    ClintonWins = 0
    TrumpWins = 0
    SandersWins = 0
    CruzWins = 0
    KasichWins = 0
    result = ['Clinton Wins', 'Sanders Wins']
    p = [.552, .448]
    dem_primary = np.random.choice(result, replace=True, p=p)
    if dem_primary == 'Clinton Wins':
        canidate.append('Clinton')
    else:
        canidate.append('Sanders')
    result = ['Trump Wins', 'Cruz Wins', 'Kasich Wins']
    p = [.611, .251, .138]
    rep_primary = np.random.choice(result, replace=True, p=p)
    if rep_primary == 'Trump Wins':
        canidate.append('Trump')
    elif rep_primary == 'Cruz Wins':
        canidate.append('Cruz')
    else:
        canidate.append('Kasich')
    scenario_num = canidate_sen[canidate[0]][canidate[1]]
    #Now for the controversial part. I created 6 different senarios which can be picked out based on who wins.
    #I'm trying to be as historically accurate as possible but there is some guess work.
    #The senario number will determine which lists are used.
    result = ([['Clinton Wins', 'Trump Wins'], ['Clinton Wins', 'Cruz Wins'], ['Clinton Wins', 'Kasich Wins'],
              ['Sanders Wins', 'Trump Wins'], ['Sanders Wins', 'Cruz Wins'], ['Sanders Wins', 'Kasich Wins']])
    p = [[.714, .286], [.857, .143], [.928, .072], [.55, .45], [.79, .21], [.895, .105]]
    election = np.random.choice(result[scenario_num - 1], replace=True, p=p[scenario_num - 1])
    if election == 'Clinton Wins':
        ClintonWins += 1
        Current_President = 'Clinton'
        President_List.append('Clinton')
    elif election == 'Trump Wins':
        TrumpWins += 1
        Current_President = 'Trump'
        President_List.append('Trump')
    elif election == 'Sanders Wins':
        SandersWins += 1
        Current_President = 'Sanders'
        President_List.append('Sanders')
    elif election == 'Cruz Wins':
        CruzWins += 1
        Current_President = 'Cruz'
        President_List.append('Cruz')
    else:
        KasichWins += 1
        Current_President = 'Kasich'
        President_List.append('Kasich')
    #Oh. It seems there are a lot of variables I want to pass on but I can only return so much.
    #I'll store all the values as a list which the next function will unpack
    compress = [Current_President, President_List, ClintonWins, TrumpWins, SandersWins, CruzWins, KasichWins]
    return compress

def simulated_elections(times):
    #First we run a recursive 2016 election and unpack the original values
    print("Who do you think will be the president at the final iteration?")
    print("Please enter: Clinton, Sanders, Trump, Cruz, or Kasich")
    Pick = str(input())
    twenty_sixteen = original_election()
    Current_President = twenty_sixteen[0]
    President_List = twenty_sixteen[1]
    ClintonWins = twenty_sixteen[2]
    TrumpWins = twenty_sixteen[3]
    SandersWins = twenty_sixteen[4]
    CruzWins = twenty_sixteen[5]
    KasichWins = twenty_sixteen[6]
    print("The winner of the 2016 election is", Current_President + ".")
    #I'll make a senario for each president that contains a primary and an election
    for x in range(times - 1):
        if Current_President == 'Clinton':
            canidate = []
            canidate_sen = {'Clinton': {'Trump': 1, 'Cruz': 2, 'Kasich': 3},
                           'Sanders': {'Trump': 4, 'Cruz': 5, 'Kasich': 6}}
            result = ['Clinton Wins', 'Sanders Wins']
            p = [.9, .1]
            dem_primary = np.random.choice(result, replace=True, p=p)
            if dem_primary == 'Clinton Wins':
                canidate.append('Clinton')
            else:
                canidate.append('Sanders')
            result = ['Trump Wins', 'Cruz Wins', 'Kasich Wins']
            p = [.611, .251, .138]
            rep_primary = np.random.choice(result, replace=True, p=p)
            if rep_primary == 'Trump Wins':
                canidate.append('Trump')
            elif rep_primary == 'Cruz Wins':
                canidate.append('Cruz')
            else:
                canidate.append('Kasich')
            scenario_num = canidate_sen[canidate[0]][canidate[1]]
            result = ([['Clinton Wins', 'Trump Wins'], ['Clinton Wins', 'Cruz Wins'], ['Clinton Wins', 'Kasich Wins'],
                      ['Sanders Wins', 'Trump Wins'], ['Sanders Wins', 'Cruz Wins'], ['Sanders Wins', 'Kasich Wins']])
            p = [[.46, .54], [.768, .232], [.839, .161], [.55, .45], [.79, .21], [.895, .105]]
            election = np.random.choice(result[scenario_num - 1], replace=True, p=p[scenario_num - 1])
            if election == 'Clinton Wins':
                ClintonWins += 1
                Current_President = 'Clinton'
                President_List.append('Clinton')
            elif election == 'Trump Wins':
                TrumpWins += 1
                Current_President = 'Trump'
                President_List.append('Trump')
            elif election == 'Cruz Wins':
                CruzWins += 1
                Current_President = 'Cruz'
                President_List.append('Cruz')
            elif election == 'Sanders Wins':
                SandersWins += 1
                Current_President = 'Sanders'
                President_List.append('Sanders')
            else:
                KasichWins += 1
                Current_President = 'Kasich'
                President_List.append('Kasich')
        elif Current_President == 'Trump':
            canidate = []
            canidate_sen = {'Trump': {'Sanders': 1, 'Clinton': 2},
                           'Cruz': {'Sanders': 3, 'Clinton': 4},
                           'Kasich': {'Sanders': 5, 'Clinton': 6}}
            result = ['Trump Wins', 'Cruz Wins', 'Kasich Wins']
            p = [.9, .05, .05]
            rep_primary = np.random.choice(result, replace=True)
            if rep_primary == 'Trump Wins':
                canidate.append('Trump')
            elif rep_primary == 'Cruz Wins':
                canidate.append('Cruz')
            else:
                canidate.append('Kasich')
            result = ['Clinton Wins', 'Sanders Wins']
            p = [.552, .448]
            dem_primary = np.random.choice(result, replace=True, p=p)
            if dem_primary == 'Clinton Wins':
                canidate.append('Clinton')
            else:
                canidate.append('Sanders')
            scenario_num = canidate_sen[canidate[0]][canidate[1]]
            result = ([['Trump Wins', 'Sanders Wins'], ['Trump Wins', 'Clinton Wins'], ['Cruz Wins', 'Sanders Wins'],
                      ['Cruz Wins', 'Clinton Wins'], ['Kasich Wins', 'Sanders Wins'], ['Kasich Wins', 'Clinton Wins']])
            p = [[.487, .513], [.54, .46], [.21, .79], [.143, .857], [.105, .895], [.072, .928]]
            election = np.random.choice(result[scenario_num - 1], replace=True, p=p[scenario_num - 1])
            if election == 'Trump Wins':
                TrumpWins += 1
                Current_President = 'Trump'
                President_List.append('Trump')
            elif election == 'Sanders Wins':
                SandersWins += 1
                Current_President = 'Sanders'
                President_List.append('Sanders')
            elif election == 'Cruz Wins':
                CruzWins += 1
                Current_President = 'Cruz'
                President_List.append('Cruz')
            elif election == 'Kasich Wins':
                KasichWins += 1
                Current_President = 'Kasich'
                President_List.append('Kasich')
            else:
                ClintonWins += 1
                Current_President = 'Clinton'
                President_List.append('Clinton')
        elif Current_President == 'Sanders':
            canidate = []
            canidate_sen = {'Sanders': {'Trump': 1, 'Cruz': 2, 'Kasich': 3},
                           'Clinton': {'Trump': 4, 'Cruz': 5, 'Kasich': 6}}
            result = ['Sanders Wins', 'Clinton Wins']
            p = [.9, .1]
            dem_primary = np.random.choice(result, replace=True, p=p)
            if dem_primary == 'Sanders Wins':
                canidate.append('Sanders')
            else:
                canidate.append('Clinton')
            result = ['Trump Wins', 'Cruz Wins', 'Kasich Wins']
            p = [.611, .251, .138]
            rep_primary = np.random.choice(result, replace=True, p=p)
            if rep_primary == 'Trump Wins':
                canidate.append('Trump')
            elif rep_primary == 'Cruz Wins':
                canidate.append('Cruz')
            else:
                canidate.append('Kasich')
            scenario_num = canidate_sen[canidate[0]][canidate[1]]
            result = ([['Sanders Wins', 'Trump Wins'], ['Sanders Wins', 'Cruz Wins'], ['Sanders Wins', 'Kasich Wins'],
                      ['Clinton Wins', 'Trump Wins'], ['Clinton Wins', 'Cruz Wins'], ['Clinton Wins', 'Kasich Wins']])
            p = [[.694, .306], [.646, .354], [.751, .249], [.714, .286], [.857, .143], [.928, .072]]
            election = np.random.choice(result[scenario_num - 1], replace=True, p=p[scenario_num - 1])
            if election == 'Trump Wins':
                TrumpWins += 1
                Current_President = 'Trump'
                President_List.append('Trump')
            elif election == 'Sanders Wins':
                SandersWins += 1
                Current_President = 'Sanders'
                President_List.append('Sanders')
            elif election == 'Cruz Wins':
                CruzWins += 1
                Current_President = 'Cruz'
                President_List.append('Cruz')
            elif election == 'Clinton Wins':
                ClintonWins += 1
                Current_President = 'Clinton'
                President_List.append('Clinton')
            else:
                KasichWins += 1
                Current_President = 'Kasich'
                President_List.append('Kasich')
        elif Current_President == 'Cruz':
            canidate = []
            canidate_sen = {'Cruz': {'Sanders': 1, 'Clinton': 2},
                           'Trump': {'Sanders': 3, 'Clinton': 4},
                           'Kasich': {'Sanders': 5, 'Clinton': 6}}
            result = ['Cruz Wins', 'Trump Wins', 'Kasich Wins']
            p = [.9, .05, .05]
            rep_primary = np.random.choice(result, replace=True, p=p)
            if rep_primary == 'Cruz Wins':
                canidate.append('Cruz')
            elif rep_primary == 'Trump Wins':
                canidate.append('Trump')
            else:
                canidate.append('Kasich')
            result = ['Clinton Wins', 'Sanders Wins']
            p = [.552, .448]
            dem_primary = np.random.choice(result, replace=True, p=p)
            if dem_primary == 'Clinton Wins':
                canidate.append('Clinton')
            else:
                canidate.append('Sanders')
            scenario_num = canidate_sen[canidate[0]][canidate[1]]
            result = ([['Cruz Wins', 'Sanders Wins'], ['Cruz Wins', 'Clinton Wins'], ['Trump Wins', 'Sanders Wins'],
                      ['Trump Wins', 'Clinton Wins'], ['Kasich Wins', 'Sanders Wins'], ['Kasich Wins', 'Clinton Wins']])
            p = [[.244, .756], [.177, .823], [.45, .55], [.714, .286], [.105, .895], [.072, .928]]
            election = np.random.choice(result[scenario_num - 1], replace=True, p=p[scenario_num - 1])
            if election == 'Cruz Wins':
                CruzWins += 1
                Current_President = 'Cruz'
                President_List.append('Cruz')
            elif election == 'Sanders Wins':
                SandersWins += 1
                Current_President = 'Sanders'
                President_List.append('Sanders')
            elif election == 'Trump Wins':
                TrumpWins += 1
                Current_President = 'Trump'
                President_List.append('Trump')
            elif election == 'Kasich Wins':
                KasichWins += 1
                Current_President = 'Kasich'
                President_List.append('Kasich')
            else:
                KasichWins += 1
                Current_President = 'Clinton'
                President_List.append('Clinton')
        else:
            canidate = []
            canidate_sen = {'Kasich': {'Sanders': 1, 'Clinton': 2},
                           'Trump': {'Sanders': 3, 'Clinton': 4},
                           'Cruz': {'Sanders': 5, 'Clinton': 6}}
            result = ['Kasich Wins', 'Trump Wins', 'Cruz Wins']
            p = [.9, .05, .05]
            rep_primary = np.random.choice(result, replace=True, p=p)
            if rep_primary == 'Kasich Wins':
                canidate.append('Kasich')
            elif rep_primary == 'Trump Wins':
                canidate.append('Trump')
            else:
                canidate.append('Cruz')
            result = ['Clinton Wins', 'Sanders Wins']
            p = [.552, .448]
            dem_primary = np.random.choice(result, replace=True, p=p)
            if dem_primary == 'Clinton Wins':
                canidate.append('Clinton')
            else:
                canidate.append('Sanders')
            scenario_num = canidate_sen[canidate[0]][canidate[1]]
            result = ([['Kasich Wins', 'Sanders Wins'], ['Kasich Wins', 'Clinton Wins'], ['Trump Wins', 'Sanders Wins'],
                      ['Trump Wins', 'Clinton Wins'], ['Cruz Wins', 'Sanders Wins'], ['Cruz Wins', 'Clinton Wins']])
            p = [[.107, .893], [.074, .926], [.45, .55], [.286, .714], [.21, .79], [.143, .857]]
            election = np.random.choice(result[scenario_num - 1], replace=True, p=p[scenario_num - 1])
            if election == 'Kasich Wins':
                KasichWins += 1
                Current_President = 'Kasich'
                President_List.append('Kasich')
            elif election == 'Sanders Wins':
                SandersWins += 1
                Current_President = 'Sanders'
                President_List.append('Sanders')
            elif election == 'Trump Wins':
                TrumpWins += 1
                Current_President = 'Trump'
                President_List.append('Trump')
            elif election == 'Cruz Wins':
                CruzWins += 1
                Current_President = 'Cruz'
                President_List.append('Cruz')
            else:
                ClintonWins += 1
                Current_President = 'Clinton'
                President_List.append('Clinton')
    print("In our simulation Clinton won", ClintonWins, "times.")
    print("In our simulation Trump won", TrumpWins, "times.")
    print("In our simulation Sanders won", SandersWins, "times.")
    print("In our simulation Cruz won", CruzWins, "times.")
    print("In our simulation Kasich won", KasichWins, "times.")
    if Pick == Current_President:
        print("Hey you got it right with", Pick + ".")
    else:
        print("Sorry.", Pick, "was not correct. It was", Current_President + ". Please try again.")
    ywins = [ClintonWins, TrumpWins, SandersWins, CruzWins, KasichWins]
    xwins = ['Clinton', 'Trump', 'Sanders', 'Cruz', 'Kasich']
    plt.figure(dpi=100)
    plt.bar(xwins, ywins, color='blue', edgecolor='black')
    plt.xlabel('Canidate name')
    plt.ylabel('Number of times canidate won')
    plt.title('Number of times each canidate won in the simulation')
    plt.show()
    plt.figure(dpi=100)
    plt.plot(President_List)
    plt.xlabel('Simulation Number')
    plt.ylabel('Current President')
    plt.title('Timeline of election winners')
    plt.show()

simulated_elections(times)

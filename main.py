import urllib.request
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

class Table_Data():
    def __init__(self):
        pass

    def get_table(self):
        ## Gets the 2017 QB statistics from Pro Football Reference using URLLIB
        self.getTableQB2017 = urllib.request.urlopen('https://www.pro-football-reference.com/years/2017/passing.htm').read()
        self.df_QB2017 = pd.read_html(self.getTableQB2017)
        self.df_QB2017 = self.df_QB2017[0].dropna(axis=0, thresh=4)

        ## Gets the 2018 QB statistics from Pro Football Reference using URLLIB
        self.getTableQB2018 = urllib.request.urlopen('https://www.pro-football-reference.com/years/2018/passing.htm').read()
        df_QB2018 = pd.read_html(self.getTableQB2018)
        self.df_QB2018 = df_QB2018[0].dropna(axis=0, thresh=4)

    def read_table(self):
        ## Cleaning up the 2017 table data to make it easier to read using PANDAS
        self.df_QB2017 = self.df_QB2017.rename(columns={'Yds.1': 'SkYd'})
        self.df_QB2017 = self.df_QB2017[0:60]
        self.df_QB2017 = self.df_QB2017.drop([29])
        self.df_QB2017[
            ['Age', 'G', 'GS', 'Cmp', 'Att', 'Cmp%', 'Yds', 'TD', 'TD%', 'Int', 'Int%', 'Lng', 'Y/A', 'AY/A', 'Y/C',
             'Y/G', 'Rate', 'QBR', 'SkYd', 'NY/A', 'ANY/A', 'Sk%', '4QC', 'GWD']] = self.df_QB2017[
            ['Age', 'G', 'GS', 'Cmp', 'Att', 'Cmp%', 'Yds', 'TD', 'TD%', 'Int', 'Int%', 'Lng', 'Y/A', 'AY/A', 'Y/C',
             'Y/G', 'Rate', 'QBR', 'SkYd', 'NY/A', 'ANY/A', 'Sk%', '4QC', 'GWD']].apply(pd.to_numeric)
        self.df_QB2017['Pos'] = 'QB'

        ## Cleaning up the 2018 table data to make it easier to read using PANDAS
        self.df_QB2018 = self.df_QB2018.rename(columns={'Yds.1': 'SkYd'})
        self.df_QB2018 = self.df_QB2018[0:41]
        self.df_QB2018 = self.df_QB2018.drop([29])
        self.df_QB2018[
            ['Age', 'G', 'GS', 'Cmp', 'Att', 'Cmp%', 'Yds', 'TD', 'TD%', 'Int', 'Int%', 'Lng', 'Y/A', 'AY/A', 'Y/C',
             'Y/G', 'Rate', 'QBR', 'SkYd', 'NY/A', 'ANY/A', 'Sk%', '4QC', 'GWD']] = self.df_QB2018[
            ['Age', 'G', 'GS', 'Cmp', 'Att', 'Cmp%', 'Yds', 'TD', 'TD%', 'Int', 'Int%', 'Lng', 'Y/A', 'AY/A', 'Y/C',
             'Y/G', 'Rate', 'QBR', 'SkYd', 'NY/A', 'ANY/A', 'Sk%', '4QC', 'GWD']].apply(pd.to_numeric)
        self.df_QB2018['Pos'] = 'QB'
        print(self.df_QB2018)

    def choose_option(self):
        ## Gets user input on which option they would like the program to run
        self.whatDo = str(input('\n' + 'What would you like to do with this table? (sort, graph, save)' + '\n').lower())
        newList = ['sort', 'graph', 'save']
        while self.whatDo not in newList:
            print('Please enter valid data')
            self.whatDo = str(
                input(
                    '\n' + 'What would you like to do with this table? (sort, graph, save)' + '\n'))
        if self.whatDo == 'save':
            self.df_QB2018.to_csv('QB_2018.csv')

    def sort_table(self):
        ## Sorts the 2018 table based on the statistic chosen by the user
        if self.whatDo == 'sort':
            statList = ['Age', 'G', 'GS', 'Cmp', 'Att', 'Cmp%', 'Yds', 'TD', 'TD%', 'Int', 'Int%', 'Lng', 'Y/A', 'AY/A', 'Y/C', 'Y/G', 'Rate', 'QBR', 'SkYd', 'NY/A', 'ANY/A', 'Sk%', '4QC', 'GWD']
            print('Age,', 'G,', 'GS,', 'Cmp,', 'Att,', 'Cmp%,', 'Yds,', 'TD,', 'TD%,', 'Int,', 'Int%,', 'Lng,', 'Y/A,',
                  'AY/A,', 'Y/C,',
                  'Y/G,', 'Rate,', 'QBR,', 'SkYd,', 'NY/A,', 'ANY/A,', 'Sk%,', '4QC,', 'GWD')
            self.sort_by = str(
                input(
                    '\n' + 'Which statistic would you like to sort this table by? (Choose from the options above)' + '\n'))
            while self.sort_by not in statList:
                print('Please enter valid data')
                self.sort_by = str(
                    input(
                        '\n' + 'Which statistic would you like to sort this table by? (Choose from the options above)' + '\n'))
            print(self.df_QB2018.sort_values(self.sort_by, ascending=False))


    def graph_table(self):
        ## Allow the user to graph their data using MATPLOTLIB
        if self.whatDo == 'graph':
            self.options = str(
                input('\n' + 'Do you want to graph a STATISTIC or COMPARE with 2017 (enter statistic or compare)?' + '\n').lower())
            if self.options == 'statistic':
                statList = ['Age', 'G', 'GS', 'Cmp', 'Att', 'Cmp%', 'Yds', 'TD', 'TD%', 'Int', 'Int%', 'Lng', 'Y/A', 'AY/A',
                        'Y/C', 'Y/G', 'Rate', 'QBR', 'SkYd', 'NY/A', 'ANY/A', 'Sk%', '4QC', 'GWD']
                ## Gets the top ten quarterbacks of the chosen statistic and graphs them on a bar graph using MATPLOTLIB
                print('Age,', 'G,', 'GS,', 'Cmp,', 'Att,', 'Cmp%,', 'Yds,', 'TD,', 'TD%,', 'Int,', 'Int%,', 'Lng,', 'Y/A,', 'AY/A,', 'Y/C,',
             'Y/G,', 'Rate,', 'QBR,', 'SkYd,', 'NY/A,', 'ANY/A,', 'Sk%,', '4QC,', 'GWD')
                self.whatStats = str(
                    input(
                        '\n' + 'Which statistic would you like to graph? (Choose from the options above)' + '\n'))
                while self.whatStats not in statList:
                    print('Please enter valid data')
                    self.whatStats = str(
                        input(
                            '\n' + 'Which statistic would you like to graph? (Choose from the options above)' + '\n'))
                self.df_QB2018 = self.df_QB2018.sort_values(by=[self.whatStats], ascending=False)
                self.df_QB2018 = self.df_QB2018[0:10]
                qb_player_list = list(self.df_QB2018.Player)
                self.df_QB_graph_by = self.df_QB2018[self.whatStats]
                plt.ylabel(self.whatStats)
                plt.title("2018 Quartback Statistics")
                plt.bar(qb_player_list, self.df_QB_graph_by)
                plt.xticks(qb_player_list, rotation='vertical')
                plt.tight_layout()
                plt.show()
            if self.options == 'compare':
                ## The user has chosen to compare either two different quarterbacks, two of the same quarterbacks and their production from each year,
                ## or the top ten quarterbacks of a chosen statistic for the 2017 and 2018 season
                newList = ['players', 'seasons']
                self.whatCompare = str(
                    input(
                        '\n' + 'What should we compare? Please choose from the following: Players, Seasons.' + '\n')).lower()
                while self.whatCompare not in newList:
                    print('Please enter valid data')
                    self.whatCompare = str(
                        input(
                            '\n' + 'What should we compare? Please choose from the following: Players, Seasons' + '\n')).lower()
                if self.whatCompare == 'players':
                    ## The user has chosen to compare two quarterbacks (uses a bar graph)
                    print('Please choose two players to compare')
                    self.qb_player1 = input("Player 1" + '\n')
                    self.df_players2018 = self.df_QB2018[['Player']]
                    self.qb_player1 = self.df_QB2018[self.df_QB2018['Player'].str.contains(self.qb_player1)]
                    print(self.qb_player1)
                    self.qb_player2 = input("Player 2:" + '\n')
                    self.qb_player2 = self.df_QB2018[self.df_QB2018['Player'].str.contains(self.qb_player2)]
                    self.qb_playerCompare = self.qb_player1.append(self.qb_player2)
                    print(self.qb_playerCompare)
                    print('Age,', 'G,', 'GS,', 'Cmp,', 'Att,', 'Cmp%,', 'Yds,', 'TD,', 'TD%,', 'Int,', 'Int%,', 'Lng,', 'Y/A,', 'AY/A,', 'Y/C,',
                    'Y/G,', 'Rate,', 'QBR,', 'SkYd,', 'NY/A,', 'ANY/A,', 'Sk%,', '4QC,', 'GWD')
                    statList = ['Age', 'G', 'GS', 'Cmp', 'Att', 'Cmp%', 'Yds', 'TD', 'TD%', 'Int', 'Int%', 'Lng', 'Y/A',
                                'AY/A', 'Y/C', 'Y/G', 'Rate', 'QBR', 'SkYd', 'NY/A', 'ANY/A', 'Sk%', '4QC', 'GWD']
                    self.compareStats = str(
                        input(
                            '\n' + 'What statistic should we compare? Please choose from the options above.' + '\n'))
                    while self.compareStats not in statList:
                        print('Please enter valid data')
                        self.compareStats = str(
                            input(
                                '\n' + 'Which statistic would you like to graph? (Choose from the options above)' + '\n'))
                    qb_player_list2018 = list(self.qb_playerCompare.Player)
                    self.df_QB_graph_by2018 = self.qb_playerCompare[self.compareStats]
                    print(self.compareStats, self.qb_playerCompare, self.df_QB_graph_by2018)
                    ax = self.df_QB_graph_by2018.plot(kind='bar')
                    ax.set_title('Quarterback Comparison: ' + self.compareStats)
                    ax.set_xlabel(self.whatCompare)
                    ax.set_ylabel(self.compareStats)
                    ax.set_xticklabels(qb_player_list2018, rotation='horizontal')
                    totals = []
                    # find the values and append to list
                    for i in ax.patches:
                        totals.append(i.get_height())
                    # set individual bar lables using above list
                    total = sum(totals)
                    # set individual bar lables using above list
                    for i in ax.patches:
                        # get_x pulls left or right; get_height pushes up or down
                        ax.text(i.get_x() + .20, i.get_height() - 5,
                                str(round((i.get_height()), 0)), fontsize=18,
                                color='white')
                    plt.tight_layout()
                    plt.show()
                if self.whatCompare == 'seasons':
                    ## Lets the program know the user has chosen to compare seasons
                    newList = ['top_ten', 'development']
                    self.compareSeasons = str(
                        input(
                            '\n' + 'Do you want to compare the top ten players in a certain statistic or a single players development? (choose TOP_TEN or DEVELOPMENT)' + '\n')).lower()
                    while self.compareSeasons not in newList:
                        print('Please enter valid data')
                        self.compareSeasons = str(
                            input(
                                '\n' + 'Which statistic would you like to graph? (Choose from the options above)' + '\n'))

                    if self.compareSeasons == 'top_ten':
                        ## Compares the top ten quarterbacks of the chosen statistic from each season using a box and whisker plot
                        statList = ['Age', 'G', 'GS', 'Cmp', 'Att', 'Cmp%', 'Yds', 'TD', 'TD%', 'Int', 'Int%', 'Lng',
                                    'Y/A', 'AY/A', 'Y/C', 'Y/G', 'Rate', 'QBR', 'SkYd', 'NY/A', 'ANY/A', 'Sk%', '4QC',
                                    'GWD']
                        print('Age,', 'G,', 'GS,', 'Cmp,', 'Att,', 'Cmp%,', 'Yds,', 'TD,', 'TD%,', 'Int,', 'Int%,', 'Lng,', 'Y/A,', 'AY/A,', 'Y/C,',
                        'Y/G,', 'Rate,', 'QBR,', 'SkYd,', 'NY/A,', 'ANY/A,', 'Sk%,', '4QC,', 'GWD')
                        self.compareTop = str(
                            input(
                                '\n' + 'What statistic shall we compare the top ten players from 2017 and 2018? (Please choose from the options above)' + '\n'))
                        while self.compareTop not in statList:
                            print('Please enter valid data')
                            self.compareTop = str(
                                input(
                                    '\n' + 'Which statistic would you like to graph? (Choose from the options above)' + '\n'))
                        self.df_QB2018 = self.df_QB2018.sort_values(self.compareTop, ascending=False)
                        self.df_QB2017 = self.df_QB2017.sort_values(self.compareTop, ascending=False)
                        self.df_QB2018 = self.df_QB2018[0:10]
                        self.df_QB2017 = self.df_QB2017[0:10]
                        self.df_QB2018_boxplot = self.df_QB2018[self.compareTop]
                        self.df_QB2017_boxplot = self.df_QB2017[self.compareTop]
                        self.df_QB2018 = self.df_QB2018[['Player', self.compareTop]]
                        self.df_QB2017 = self.df_QB2017[['Player', self.compareTop]]
                        self.df_QB2018 = self.df_QB2018.rename(columns={self.compareTop: '2018 ' + self.compareTop})
                        self.df_QB2017 = self.df_QB2017.rename(columns={self.compareTop: '2017 ' + self.compareTop})
                        print(self.df_QB2018)
                        print(self.df_QB2017)
                        data = [self.df_QB2017_boxplot, self.df_QB2018_boxplot]
                        fig7, ax7 = plt.subplots()
                        ax7.set_title('QB ' + self.compareTop + ' Comparison from the 2017-2018 seasons')
                        ax7.set_ylabel(self.compareTop)
                        ax7.set_xlabel('Season')
                        ax7.boxplot(data)
                        plt.xticks([1, 2], [2017, 2018])
                        for i in [1, 2]:
                            y = data[i - 1]
                            x = np.random.normal(i, 0.00, len(y))
                            plt.plot(x, y, 'r.', alpha=0.9, color= 'black')
                        plt.show()



                    if self.compareSeasons == 'development':
                        ## Compares the stats of quarterback(s) from the 2017 season and the 2018 season
                        self.compareSeasonsPlayer = str(
                            input(
                                '\n' + 'What player shall we compare seasons for?' + '\n'))
                        self.qb_player2018 = self.df_QB2018[self.df_QB2018['Player'].str.contains(self.compareSeasonsPlayer)]
                        self.qb_player2017 = self.df_QB2017[self.df_QB2017['Player'].str.contains(self.compareSeasonsPlayer)]
                        print(self.qb_player2018, self.qb_player2017)
                        statList = ['Age', 'G', 'GS', 'Cmp', 'Att', 'Cmp%', 'Yds', 'TD', 'TD%', 'Int', 'Int%', 'Lng',
                                    'Y/A', 'AY/A', 'Y/C', 'Y/G', 'Rate', 'QBR', 'SkYd', 'NY/A', 'ANY/A', 'Sk%', '4QC',
                                    'GWD']
                        print('Age,', 'G,', 'GS,', 'Cmp,', 'Att,', 'Cmp%,', 'Yds,', 'TD,', 'TD%,', 'Int,', 'Int%,', 'Lng,', 'Y/A,', 'AY/A,', 'Y/C,',
             'Y/G,', 'Rate,', 'QBR,', 'SkYd,', 'NY/A,', 'ANY/A,', 'Sk%,', '4QC,', 'GWD')
                        self.compareSeasonsStats = str(
                            input(
                                '\n' + 'What statistic should we compare? Please choose from the options above.' + '\n'))
                        while self.compareSeasonsStats not in statList:
                            print('Please enter valid data')
                            self.compareSeasonsStats = str(
                                input(
                                    '\n' + 'Which statistic would you like to graph? (Choose from the options above)' + '\n'))
                        self.qb_playerCompare = self.qb_player2017.append(self.qb_player2018)
                        qb_player_list2018 = list(self.qb_playerCompare.Player)
                        self.df_QB_graph_by2018 = self.qb_playerCompare[self.compareSeasonsStats]
                        print(self.compareSeasonsStats, self.qb_playerCompare, self.df_QB_graph_by2018)
                        ax = self.df_QB_graph_by2018.plot(kind='bar')
                        ax.set_title('Quarterback Comparison: ' + self.compareSeasonsStats)
                        ax.set_xlabel(self.whatCompare)
                        ax.set_ylabel(self.compareSeasonsStats)
                        ax.set_xticklabels(qb_player_list2018, rotation='horizontal')
                        totals = []
                        # find the values and append to list
                        for i in ax.patches:
                            totals.append(i.get_height())
                        # set individual bar lables using above list
                        total = sum(totals)
                        # set individual bar lables using above list
                        for i in ax.patches:
                            # get_x pulls left or right; get_height pushes up or down
                            ax.text(i.get_x() + .12, i.get_height() - 5,
                                    str(round((i.get_height()), 0)), fontsize=18,
                                    color='white')
                        plt.tight_layout()
                        plt.show()

Go = Table_Data()

Go.get_table()
Go.read_table()
Go.choose_option()
Go.sort_table()
Go.graph_table()

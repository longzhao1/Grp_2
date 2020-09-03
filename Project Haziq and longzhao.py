import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class cals:
    def visit(self):
        dict = {"country": ['Brunei', 'Indonesia', 'Malaysia', 'Philippines', 'Thailand', 'Vietnam', 'Myanmar', 'Japan',
                            'Hong Kong', 'China', 'Taiwan', " Korea, Republic Of ", 'India', 'Pakistan',
                            'Sri Lanka', 'Saudi Arabia', 'Kuwait', 'UAE'],
                "total": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]}
        # Import the IMVA.csv data: df
        df2 = pd.DataFrame(dict, columns=['country', 'total'])
        df = pd.read_csv('IMVA.csv')
        visitor = df['Periods'].str.split(' ', n = 2, expand = True)
        df = df.assign(year=visitor[1]) # assign new column called year
        #df = df.assign(month=visitor[2])
        df.index = df['year'] # set year as index
        del df['Periods'] # delete periods column
        del df['year']
        df.iloc[122:130] # select year 1978 to 1987
        df = df[df.columns[0:18]].head(120)
        df = df.replace(' na ',0)
        print(df)

        brunei = df[' Brunei Darussalam '].sum()
        indo = df[' Indonesia '].sum()
        my = df[' Malaysia '].sum()
        ph = df[' Philippines '].sum()
        th = df[' Thailand '].sum()
        vn = df[' Viet Nam '].sum()
        myanmar = df[' Myanmar '].sum()
        japan = df[' Japan '].sum()
        hk = df[' Hong Kong '].sum()
        china = df[' China '].sum()
        twn = df[' Taiwan '].sum()
        kr = df[" Korea, Republic Of "].sum()
        ind = df[" India "].sum()
        pakistan = df[" Pakistan "].sum()
        srilanka = df[" Sri Lanka "].sum()
        saudiarabia = df[" Saudi Arabia "].sum()
        kuwait = df[" Kuwait "].sum()
        uae = df[" UAE "].sum()

        df2['total'] = df2['total'].replace(1, brunei)
        df2['total'] = df2['total'].replace(2, indo)
        df2['total'] = df2['total'].replace(3, my)
        df2['total'] = df2['total'].replace(4, ph)
        df2['total'] = df2['total'].replace(5, th)
        df2['total'] = df2['total'].replace(6, vn)
        df2['total'] = df2['total'].replace(7, myanmar)
        df2['total'] = df2['total'].replace(8, japan)
        df2['total'] = df2['total'].replace(9, hk)
        df2['total'] = df2['total'].replace(10, china)
        df2['total'] = df2['total'].replace(11, twn)
        df2['total'] = df2['total'].replace(12, kr)
        df2['total'] = df2['total'].replace(13, ind)
        df2['total'] = df2['total'].replace(14, pakistan)
        df2['total'] = df2['total'].replace(15, srilanka)
        df2['total'] = df2['total'].replace(16, saudiarabia)
        df2['total'] = df2['total'].replace(17, kuwait)
        df2['total'] = df2['total'].replace(18, uae)

        df2.sort_values(by=['total'], inplace=True, ascending=False)
        df2.reset_index(drop=True, inplace=True)
        top3df = df2.nlargest(3,'total')

        print(df2)
        print(top3df)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Graphs~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # Top 3 bar chart
        ax = top3df.plot(kind='bar', x='country', y='total', title="Number of Visitors in Countries",
                        ylabel="Number of Tourists (in millions) ", rot=0, legend=False, figsize=(15, 15))
        for p in ax.patches:
            ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
        plt.savefig("scatterDiagram_Top3(haziq).png")
        # plt.show()

        # all countries bar chart
        ax = df2.plot(kind='bar', x='country', y='total', title="Number of Visitors in Countries",
                     ylabel="Number of Tourists (in millions) ", rot=45, legend=False, figsize=(25, 25))
        for p in ax.patches:
            ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
        plt.savefig("Country_comparison(haziq).png")
        # plt.show()

j = cals()
print(j.visit())
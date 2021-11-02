'''
This file is for logging the average accuracy of the model for a given dataset
'''
import pandas as pd

filepath = 'athlete_events.csv'
df = pd.read_csv(filepath)

# ! Mens atheletics after 1960
# length of df_1: 1395
# the average accuracy of the model over 50 iterations is:  56.32 %
# the lowest accuracy of the model over 50 iterations is 52.48 %
# the highest accuracy of the model over 50 iterations is 60.71 %
df = df[(df.Sex == 'M') & 
        (df.Height > 130) &
        (df.Age > 1) &
        (df.Weight > 1) & 
        (df.Year >= 1960) &
        (df.Sport == 'Athletics')
        ]

X_list = ['ID', 'Height', 'Weight', 'Age']
Y_list = ['ID', 'MedalValue']

# ! Mens atheletics after 1945
# length of df_1: 1641
# the average accuracy of the model over 50 iterations is:  55.72 %
# the lowest accuracy of the model over 50 iterations is 52.11 %
# the highest accuracy of the model over 50 iterations is 60.08 %
df = df[(df.Sex == 'M') & 
        (df.Height > 130) &
        (df.Age > 1) &
        (df.Weight > 1) & 
        (df.Year >= 1945) &
        (df.Sport == 'Athletics')
        ]

X_list = ['ID', 'Height', 'Weight', 'Age']
Y_list = ['ID', 'MedalValue']

# ! Mens atheletics
# length of df_1: 2409
# the average accuracy of the model over 50 iterations is:  54.49 %
# the lowest accuracy of the model over 50 iterations is 51.48 %
# the highest accuracy of the model over 50 iterations is 57.2 %
df = df[(df.Sex == 'M') & 
        (df.Height > 130) &
        (df.Age > 1) &
        (df.Weight > 1) & 
        (df.Sport == 'Athletics')
        ]

X_list = ['ID', 'Height', 'Weight', 'Age']
Y_list = ['ID', 'MedalValue']

# ! Mens Shot Put, Hammer Throw and Discus Throw
# length of df_1: 236
# the average accuracy of the model over 50 iterations is:  51.07 %
# the lowest accuracy of the model over 50 iterations is 43.55 %
# the highest accuracy of the model over 50 iterations is 62.5 %
df_a = df[(df.Sex == 'M') & 
        (df.Height > 130) &
        (df.Age > 1) &
        (df.Weight > 1) & 
        (df.Event == 'Athletics Men\'s Shot Put')]

df_b = df[(df.Sex == 'M') & 
        (df.Height > 130) &
        (df.Age > 1) &
        (df.Weight > 1) & 
        (df.Event == 'Athletics Men\'s Hammer Throw')]

df_c = df[(df.Sex == 'M') & 
        (df.Height > 130) &
        (df.Age > 1) &
        (df.Weight > 1) & 
        (df.Event == 'Athletics Men\'s Discus Throw')]

# Concatinate dataframes
dfss = [df_a, df_b, df_c]
df = pd.concat(dfss)

X_list = ['ID', 'Height', 'Weight', 'Age']
Y_list = ['ID', 'MedalValue']

# ! Mens Shot Put, Hammer Throw and Discus Throw
# length of df_1: 125
# the average accuracy of the model over 50 iterations is:  53.39 %
# the lowest accuracy of the model over 50 iterations is 37.84 %
# the highest accuracy of the model over 50 iterations is 63.83 %
df_a = df[(df.Sex == 'M') & 
        (df.Height > 130) &
        (df.Age > 1) &
        (df.Weight > 1) & 
        (df.Year > 1960) &
        (df.Event == 'Athletics Men\'s Shot Put')]

df_b = df[(df.Sex == 'M') & 
        (df.Height > 130) &
        (df.Age > 1) &
        (df.Weight > 1) & 
        (df.Year > 1960) &
        (df.Event == 'Athletics Men\'s Hammer Throw')]

df_c = df[(df.Sex == 'M') & 
        (df.Height > 130) &
        (df.Age > 1) &
        (df.Weight > 1) & 
        (df.Year > 1960) &
        (df.Event == 'Athletics Men\'s Discus Throw')]

# Concatinate dataframes
dfss = [df_a, df_b, df_c]
df = pd.concat(dfss)

X_list = ['ID', 'Height', 'Weight', 'Age']
Y_list = ['ID', 'MedalValue']
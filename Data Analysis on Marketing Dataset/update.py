import numpy as np
import pandas as pd

def update(df):

    np.random.seed(824)

    sample_index_age = np.random.choice(np.arange(df.shape[0]), size=500, replace=False)
    df.loc[sample_index_age,'age'] = np.nan
    df.age.astype('float64')

    sample_index_y = np.random.choice(np.arange(df.shape[0]), size=100, replace=False)
    df.loc[sample_index_y,'y'] = np.nan

    df.loc[df['education']=='unknown', 'education'] = np.nan

    for var in df.dtypes[df.dtypes=='object'].index[0:-1]:
        df.loc[df[var]=='unknown', var] = ''

    df = pd.concat([df,df.iloc[(df.shape[0]-1):df.shape[0]]])
    df.reset_index(drop=True, inplace=True)
    
    return df
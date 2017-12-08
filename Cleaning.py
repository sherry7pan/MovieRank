import pandas as pd


def data_cleaning():
    '''
    This data cleaning process is used to tranform corpus's converstional data into format that could be feed into the algorithms.
    It reads the original data set and returns a processed pandas dataframe.
    '''

    characters = pd.read_table('movie_characters_metadata.txt',header=None,sep='\+\+\+\$\+\+\+',engine='python')
    characters.columns = ['character_index','character_name','movie_index','movie_name','gender','position of credits']

    con = pd.read_table('movie_conversations.txt',header=None,sep='\+\+\+\$\+\+\+',engine='python')
    con.columns = ['character_p1','character_p2','movie_index','conversation_index']
    con_lst = list(con['conversation_index'])
    con_lst =[ele.replace('[','').replace(']','').replace('\'','').strip().split(',') for ele in con_lst]
    con['conversation_index']=pd.Series(con_lst)

    mlines = pd.read_table('movie_lines.txt',header=None,sep='\+\+\+\$\+\+\+',engine='python')
    mlines.columns = ['line_index','character_index','movie_index','character_name','line']
    mlines['line_index']=pd.Series([ele.strip() for ele in mlines['line_index']])
    mlines=mlines.set_index('line_index')

    con['conversation']=[[str(mlines['line'][idx.strip()]) for idx in ele] for ele in con['conversation_index'] ]
    con['doc']=pd.Series([''.join(ele) for ele in con['conversation']])
    con['word_list']= [[word.decode("utf8", errors='ignore') for word in ele.split()] for ele in con['doc']]
    con['doc']=[' '.join(ele) for ele in con['word_list']]

    con['corpus'] = pd.Series([''.join(char.lower() for char in ele if char not in '"#$%&()*+/:;<=>?@[\\]^_`{|}~') for ele in con['doc']])

    mv_names = characters['movie_name'].unique()
    movie_con = pd.DataFrame(mv_names)
    movie_con.columns = ['movie_name']
    movie_content = []
    mv_lst = con['movie_index'].unique()
    for movie in mv_lst:
        df=con[con['movie_index'] == movie]
        movie_content.append(" ".join( df['corpus']))
    movie_con['whole_con']=pd.Series(movie_content)
    return con['corpus'], movie_con

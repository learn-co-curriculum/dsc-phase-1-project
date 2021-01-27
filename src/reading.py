def load_into_df(filepath, dataframename, sep =',', encoding = 'utf-8-sig'):
    dataframename = pd.read_csv('filepath', sep, encoding)
    return f'{dataframename} successfully populated.' 


def load_multiple_dfs(dict_of_files):
    for filepath, dataframename in dict_of_files:
        if filepath.endswith('.tsv'):
            load_into_df(filepath, dataframename, sep ='\t', encoding = 'unicode_escape')
        else:
            load_into_df(filepath, dataframename)


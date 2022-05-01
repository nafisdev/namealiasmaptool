import pandas as pd


class DataPrep:

    def __init__(self):
        self.alias_dict =self.prepare_alias_dict()
        self.nickname_dict=self.prepare_nickname_dict()


    def prepare_alias_dict(self):
        """
        to prepare alias name dict
        :return:
        """
        alias_data = pd.read_csv('variant.txt', sep=" ", header=None)
        alias_dict={}
        for i in range(alias_data.size):
            set = alias_data.iloc[i][0].split('\t')
            for k in set:
                setcopy=set.copy()
                setcopy.remove(k)
                alias_dict[k.lower]=setcopy

        return alias_dict


    def prepare_nickname_dict(self):
        '''
        prepare nickname dict
        :return:
        '''
        nickname_data = pd.read_csv('nickname.txt', sep=" ", header=None)
        nickname_dict = {}
        for i in range(nickname_data.size):
            set = nickname_data.iloc[i][0].split('\t')
            for k in set:
                setcopy=set.copy()
                setcopy.remove(k)
                nickname_dict[k.lower()]=setcopy

        return nickname_dict






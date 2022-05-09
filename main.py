import pandas as pd


class DataPrep:

    def __init__(self):
        self.alias_dict = self.prepare_alias_dict()
        self.nickname_dict = self.prepare_nickname_dict()

    def prepare_alias_dict(self):
        """
        to prepare alias name dict
        :return:
        """

        alias_dict = {}

        alias_data = pd.read_csv('variant.txt', sep=" ", header=None)
        for i in range(alias_data.size):
            set = alias_data.iloc[i][0].lower().split('\t')
            for k in set:
                setcopy = set.copy()
                setcopy.remove(k)
                alias_dict[k] = setcopy
        # with open('variant_noformat.txt') as fin:
        #     for line in fin:
        #         set = line.lower().split()
        #         for k in set:
        #             setcopy=set.copy()
        #             setcopy.remove(k)
        #             alias_dict[k]=setcopy

        return alias_dict

    def prepare_nickname_dict(self):
        '''
        prepare nickname dict
        :return:
        '''
        nickname_dict = {}
        nickname_data = pd.read_csv('nickname.txt', sep=" ", header=None)
        for i in range(nickname_data.size):
            set = nickname_data.iloc[i][0].lower().split('\t')
            for k in set:
                setcopy=set.copy()
                if len(setcopy) == 1:
                    nickname_dict[setcopy[0]] = k
                setcopy.remove(k)
                nickname_dict[k]=setcopy
        # with open('nickname_noformat.txt') as fin:
        #     for line in fin:
        #         set = line.lower().split()
        #         for k in set:
        #             setcopy = set.copy()
        #             setcopy.remove(k)
        #             nickname_dict[k] = setcopy
        return nickname_dict

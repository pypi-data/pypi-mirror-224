import pandas as pd
from mineCube.core.helpers.colaborative_dependency_graph import collaborative_dependency_graph
from mineCube.core.helpers.algo.modified_HM import ModifiedHM
from mineCube.core.helpers.sum_nested_list import add_nested_lists
from mineCube.core.helpers.merge_lists import  merge_lists
class MixedCube:

    def __init__(self, offline_cube, online_cube, contribution_factor=0.5):
        self.offline_cube = offline_cube
        self.online_cube = online_cube
        self.contribution_factor = contribution_factor
        self.models = {}

    # if n_mc != n_pc and self.offline_cube.groups_activities[key] != self.online_cube.groups_activities[key]:
    #     if n_mc > n_pc:
    #         # if online have more values than the offline one  we will update the offline with zeros
    #         self.offline_cube.groups_activities[key] = self.online_cube.groups_activities[key]
    #         to_add = n_mc - n_pc
    #         arr = [[0 for i in range(n_mc)] for j in range(to_add)]
    #         for ele in self.offline_cube.csms[key]:
    #             ele.extend([0 for i in range(to_add)])
    #         for ele in self.offline_cube.cslms[key]:
    #             ele.extend([0 for i in range(to_add)])
    #         self.offline_cube.csms[key].extend(arr)
    #         self.offline_cube.cslms[key].extend(arr)
    #     else:
    #         self.online_cube.groups_activities[key] = self.offline_cube.groups_activities[key]
    #         # here we will do the inverse cause offline have more activities
    #         to_add = n_pc - n_mc
    #         arr = [[0 for i in range(n_pc)] for j in range(to_add)]
    #         for ele in self.online_cube.csms[key]:
    #             ele.extend([0 for i in range(to_add)])
    #         for ele in self.online_cube.cslms[key]:
    #             ele.extend([0 for i in range(to_add)])
    #         self.online_cube.csms[key].extend(arr)
    #         self.online_cube.cslms[key].extend(arr)
    # elif self.offline_cube.groups_activities[key] != self.online_cube.groups_activities[key]:

    def merge(self):
        if self.online_cube.dimensions == self.offline_cube.dimensions:
            for key, val in self.online_cube.csms.items():
                if key in self.offline_cube.csms.keys():
                    merged_list = merge_lists(self.offline_cube.groups_activities[key] , self.online_cube.groups_activities[key])
                    len_merged_list = len(merged_list)
                    csms_off = [[0 for _ in range(len_merged_list)] for _ in range(len_merged_list)]
                    cslms_off = [[0 for _ in range(len_merged_list)] for _ in range(len_merged_list)]
                    csms_onl = [[0 for _ in range(len_merged_list)] for _ in range(len_merged_list)]
                    cslms_onl = [[0 for _ in range(len_merged_list)] for _ in range(len_merged_list)]
                    for index1,_key1 in enumerate(merged_list):
                        if _key1 in self.offline_cube.groups_activities[key] and _key1 in self.online_cube.groups_activities[key]:
                            off_index1 = self.offline_cube.groups_activities[key].index(_key1)
                            onl_index1 = self.online_cube.groups_activities[key].index(_key1)
                        else:
                            off_index1 = None
                            onl_index1 = None
                        for index2,_key2 in enumerate(merged_list):
                            if _key2 in self.offline_cube.groups_activities[key] and _key2 in self.online_cube.groups_activities[key]:
                                off_index2 = self.offline_cube.groups_activities[key].index(_key2)
                                onl_index2 = self.online_cube.groups_activities[key].index(_key2)
                            else:
                                off_index2 = None
                                onl_index2 = None

                            if onl_index1!= None and off_index1!= None and onl_index2!= None and off_index2!= None:
                                csms_off[index1][index2] = self.offline_cube.csms[key][off_index1][off_index2]
                                cslms_off[index1][index2] = self.offline_cube.cslms[key][off_index1][off_index2]
                                csms_onl[index1][index2] = self.online_cube.csms[key][onl_index1][onl_index2]
                                cslms_onl[index1][index2] = self.online_cube.cslms[key][onl_index1][onl_index2]
                            else:
                                csms_off[index1][index2] = 0
                                cslms_off[index1][index2] = 0
                                csms_onl[index1][index2] = 0
                                cslms_onl[index1][index2] = 0
                    self.offline_cube.csms[key] = csms_off
                    self.offline_cube.cslms[key] = cslms_off
                    self.online_cube.csms[key] = csms_onl
                    self.online_cube.cslms[key] = cslms_onl
                    self.offline_cube.groups_activities[key] = merged_list
                    self.online_cube.groups_activities[key] = merged_list
        else:
            raise AttributeError('These two cubes cannot be merged because don\'t have same dimensions ! ')





    def mine(self, algo="HM", **kwargs):
        if algo == "HM":
            # use the heuristic miner algorithm
            for key, activities in self.online_cube.groups_activities.items():
                # print(activities)
                # csms = add_nested_lists(self.offline_cube.csms[key],self.online_cube.csms[key],self.contribution_factor)
                short_loops, dep_graph, and_xor_observations = collaborative_dependency_graph(activities,self.offline_cube.csms[key],self.online_cube.csms[key],self.offline_cube.cslms[key],self.online_cube.cslms[key],contribution_factor=self.contribution_factor)
                self.models[key] = ModifiedHM(activities, self.offline_cube.csms[key],self.online_cube.csms[key], short_loops, dep_graph, and_xor_observations,**kwargs)
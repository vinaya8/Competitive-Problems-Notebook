#Given an array of numbers where each number represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.
#Once you start picking you can't skip the fruits in between.

What is the total amount of fruit you can collect with this procedure?

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        hash_map={}
        max_fruit=0
        start=0
        for end in range(len(tree)):
            if tree[end] not in hash_map:
                hash_map[tree[end]]=0
            hash_map[tree[end]]+=1
            
            while len(hash_map) > 2:
                hash_map[tree[start]]-=1
                if hash_map[tree[start]] == 0:
                    del hash_map[tree[start]]
                start+=1

            max_fruit=max(max_fruit, end-start+1)
        
        return max_fruit
    
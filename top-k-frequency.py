class Solution:
  '''In the sorting version of this problem, I have used two lists instead of three
    Problem : Get the top k frequent elements in a list of numbers
    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency={}
        nums_needed = set()
        for num in nums:
            num_frequency = frequency.get(num,[0,num])
            frequency[num] = [num_frequency[0]+1,num_frequency[1]] 

        final_list=[num for count, num in sorted(list(frequency.values()))[-k:]]

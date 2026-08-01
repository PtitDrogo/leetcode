class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        db = {} #Value -> index
        for i, n in enumerate(nums):
            #check if the valid number is in my db
            filler = target - n
            #Check if n is in db
            print(f"trying to get {filler}")
            print(db.get(filler))
            if db.get(filler) is not None:
                return [db.get(filler), i]
            else:
                db[n] = i
            print(db)
        return [0, 0]
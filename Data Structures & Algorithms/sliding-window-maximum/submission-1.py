class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        l = r = 0
        #the idea is that the number on the left of our
        # dequeue will always be the biggest
        # When we add a number to the right, we only 
        # add it if its smaller than left
        # otherwise, we pop the left number until
        # the left number is bigger or equal than the number
        # we added.

        #NOTE : We use INDEXES, this allows us to easily
        #detect if our number are still in the window
        while r < len(nums):
            #This is essentially a stack and I always want 
            #the number that I add to be smaller 
            #Because My number is always the brand new
            #Shiny thing that I care about
            #if its bigger than all the other numbers, I
            # can safely get rid of all of them
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            #adding the index to the node
            q.append(r)
            
            if l > q[0]: #aka, is my biggest n index in the window
                q.popleft()

            #if our window is big enough, we add our biggest number
            if r + 1 >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
        return res
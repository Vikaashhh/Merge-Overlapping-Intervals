class Solution:
    def mergeOverlap(self, arr):
        # Step 1: Intervals ko unke start time ke hisaab se sort karo
        arr.sort(key=lambda x: x[0])
        
        # Step 2: Ek list banate hain jisme final answer store karenge
        merged = []
        
        # Step 3: Har interval ko check karte hain
        for interval in arr:
            # Agar merged list empty hai ya koi overlap nahi hai
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)  # directly add kar do
            else:
                # Agar overlap ho raha hai toh merge kar do
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged

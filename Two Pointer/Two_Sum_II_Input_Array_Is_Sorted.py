class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        p1 = 0 
        p2 = len(numbers)-1

        while(p1 < p2):
            sum1 = numbers[p1] + numbers[p2]
            if(sum1 == target):
                break
            elif(sum1 < target):
                p1+=1
            else:
                p2-=1
        
    
        return [p1+1, p2+1]

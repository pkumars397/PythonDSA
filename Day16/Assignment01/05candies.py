def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
        #time complexity -> O(n)  ,space complexity->O(1)
        maxCandyNum=max(candies) #Storing maximumCandies a kid has
        for i in range(len(candies)):
            totalCandy=candies[i]+extraCandies #finding total candy a kid can get
            if totalCandy>=maxCandyNum: #checking if total candy are greater than maxCandy
                candies[i]=True
            else:
                candies[i]=False
        return candies

candies = [2,3,5,1,3]
extraCandies = 3
print(kidsWithCandies(candies,extraCandies))
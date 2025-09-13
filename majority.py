def majority(arr):
    n=len(arr)
    freq={}
    for num in arr:
        freq[num]=freq.get(num,0)+1
    for num,count in freq.items():
        if count>n//2:
            return num
    return "no majority element"


nums=list(map(int,input("enter numbers  :  ").split()))
rst=majority(nums)
if rst:
    print("Majority element is  :",rst)
else:
    print("No majority elements")

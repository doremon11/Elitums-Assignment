def countLeapYears(d):
    #d1=d.date
    d1=d.split("/")
    years,month,day=int(d1[2]),int(d1[1]),int(d1[0])
    
    if month>2:
        pass
    else:
    	 years -= 1
    ans = int(years / 4)
    ans -= int(years / 100)
    ans += int(years / 400)
    return ans

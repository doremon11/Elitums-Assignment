import leapcheck

def datediff(start_date,end_date):
    monthDays = [31, 28, 31, 30, 31, 30,
			31, 31, 30, 31, 30, 31]
    d1=start_date.date
    d2=end_date.date
    start=d1.split("/")
    years1,month1,day1=int(start[2]),int(start[1]),int(start[0])
    end=d2.split("/")
    years2,month2,day2=int(end[2]),int(end[1]),int(end[0])
    n1 = years1 * 365 + day1
    for i in range(0, month1 - 1):
    	n1 += monthDays[i]
    n1 += leapcheck.countLeapYears(d1)
    n2 = years2 * 365 + day2
    for i in range(0, month2 - 1):
    	n2 += monthDays[i]
    n2 += leapcheck.countLeapYears(d2)
    return abs(n2 - n1)

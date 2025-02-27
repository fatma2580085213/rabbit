print("welcom to place the rabbit")
filed =[ ["1","2","3"], ["4","5","6"], ["7","8","9"]] 
print (f"{filed[0]} \n {filed[1]} \n {filed[2]}")
position = input ("enter the row and the column")
row = int (position[0])
column = int (position[1])
filed [row-1][column-1] = "rabbit"
print (f"{filed[0]} \n {filed[1]} \n {filed[2]}")

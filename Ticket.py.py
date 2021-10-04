import json
def write_json(users,filename = "assets/user_accounts.json"):
	with open(filename,"w") as f:
		json.dump(users,f, indent=4)

def write_jsonticket(userticket,filename = "assets/tickets.json"):
	with open(filename,"w") as f:
		json.dump(userticket,f, indent=4)

def Ticket(r,c,price =10):
	row = r
	col = c
	price = price
	u_name = input("Enter name of customer\n")
	gender = input("Enter your Gender\n")
	age = int(input("Enter youe Age\n"))
	phno = int(input("Enter your Mobile no\n"))

	with open("assets/user_accounts.json") as json_file:
		users = json.load(json_file)
		temp = users["User_accounts"]
		y =  {"Row":row,"Col":col,"Username":u_name,"Age":age,"Gender":gender,"Mobile_no":phno,"Price":price}
		temp.append(y)

		write_json(users)

	with open("assets/tickets.json") as tjson_file:
		ticks = json.load(tjson_file)
		t = ticks["Tickets"]
		z = {"Username":u_name,"T_row":row,"T_col":col,"T_Price":price}
		t.append(z)

		write_jsonticket(ticks)

def Statistics(row,col):
  	total_income = 0
  	with open("assets/tickets.json", 'r') as file:
  		content = file.read()
  		data = json.loads(content)
  		#print(data)
  		ticket_data = data['Tickets']
  		tcounter = 0
  		current_income=0
  		for i in ticket_data:
  			tcounter +=1
  			price = i["T_Price"]
  			current_income = current_income+price

  		print("Number of Tickets: ",tcounter)
  		per = (tcounter/(row*col))*100
  		real_per = "{:.2f}".format(per)
  		print("Percentage: "+str(real_per)+"%")
  		print("Current income: $"+str(current_income))

  		if row*col <=60:
  			total_income = row*col*10
  		else:
  			r = row//2
  			total_income =	r* col* 10
  			total_income+=(row-r)*col *8
  		print("Total income: $"+str(total_income))




def showUserInfo():
	r = int(input("Enter Row number for the you wish to check info:"))
	c = int(input("Enter column number for the you wish to check info:"))
	with open("assets/user_accounts.json", 'r') as file:
		data = json.loads(file.read())
		count = 1	
		for i in data['User_accounts']:
			if i["Row"]==r and i["Col"]==c:
				print(count,")")
				print("Name: " +i["Username"])
				print("Age: "+str(i["Age"]))
				print("Gender: "+i["Gender"])
				print("Mobile: "+str(i["Mobile_no"]))
				print("price:"+str(i["Price"]))
				count +=1
		else:
			 print("Enter a valid seat ")
	file.close()

 #def End():


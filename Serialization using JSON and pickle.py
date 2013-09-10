import json

#Exercise fix this function, so it adds the given name and salary pair to the json it returns
def add_employee(jsonSalaries, name, salary): 
    # Add your code here
	obj = json.loads(jsonSalaries)
	obj[name] = salary
	jsonSalaries = json.dumps(obj)
	return jsonSalaries 

#Test code - shouldn't need to be modified
originalJsonSalaries = '{"Alfred" : 300, "Jane" : 301 }'
newJsonSalaries = add_employee(originalJsonSalaries, "Me", 800)
print(newJsonSalaries)
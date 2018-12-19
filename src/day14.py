import pdb
import collections

def rot_right(to, recipes):
	return to%len(recipes)

def tick(recipes, elves):
	new_recipe = 0
	for e in elves:
		new_recipe += recipes[e]
	str_recipe = str(new_recipe)
	for c in str_recipe:
		recipes.append(int(c))

	for i, e in enumerate(elves):
		to = e + recipes[e] + 1
		elves[i] = rot_right(to, recipes)


def solve(goal, num_elves): 
	elves = [n for n in range(num_elves)]
	recipes = [3, 7]

	while(len(recipes)<goal+10):
		tick(recipes, elves)

	return recipes


def solvepart1():
	goal = 890691
	recipes = solve(goal, 2)
	ans = "".join(map(str, recipes[goal:goal+10]))
	return ans

def solvepart2():
	goal = "890691"
	goal_len = len(goal)
	elves = [n for n in range(2)]
	recipes = [3, 7]
	checked = 0
	while True:
		tick(recipes, elves)
		while(len(recipes)>goal_len+checked):
			if ''.join(map(str, recipes[checked:checked+goal_len]))==goal:
				return checked	
			checked += 1

	
if __name__=='__main__':
	print solvepart1()
	print solvepart2()

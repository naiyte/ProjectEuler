squareofsum = 0
sumofsquare = 0
for x in range(1,101):
	sumofsquare = sumofsquare + x**2
	squareofsum = squareofsum + x

print (squareofsum**2-sumofsquare)
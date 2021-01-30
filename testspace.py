#this is a better way of opening a file. It closes without having to add a "close" line. 
with open("list_of_countries_and_recipes.csv", 'r') as recipe_file:
    line = recipe_file.readline()
    print(line)
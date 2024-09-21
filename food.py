#Importing the necessary libraries
import pandas as pd


#Obtain the list of available recipes and their ingredients along with their priority
dishes_df = pd.read_csv(filepath_or_buffer = '/Food.csv') #Enter the pathname to your food CSV file
#Columns - "Recipe", "Ingredient", "Priority"

#Asking for user to input a list of ingredients they possess
from pick import pick
title = 'Please choose the ingredients you possess (press SPACE to mark, ENTER to continue): '
options = dishes_df['Ingredient'].unique()
selected = pick(options, title, multiselect=True, min_selection_count=1)
input_ingredients = []
for i in range(len(selected)):
    input_ingredients.append(selected[i][0])


#Add a column to the original list, labelling an ingredient as present or not
present = []
for i in dishes_df['Ingredient']:
    present.append(i in input_ingredients)
dishes_df['Present'] = present


#For each recipe, get a count of the unique ingredients that are required
#and a count of the ingredients that are present
dishes_count_df = dishes_df[['Recipe', 'Ingredient', 'Priority']].groupby(by = ['Recipe', 'Priority'])['Ingredient'].nunique().to_frame('Ingredient').reset_index()
dishes_count_df = dishes_count_df[dishes_count_df['Priority'] == 'Y']
possible_dishes_count_df = dishes_df.groupby(by = ['Recipe', 'Priority', 'Present'])['Ingredient'].nunique().to_frame('Ingredient').reset_index()
possible_dishes_count_df = possible_dishes_count_df[(possible_dishes_count_df['Priority'] == 'Y') & (possible_dishes_count_df['Present'] == True)]


#Obtain the final list of recipes that the user can cook.
#This list will also have the count of ingredients, which is an un-avoidable byproduct
final_count_df = pd.merge(left = dishes_count_df[['Recipe', 'Ingredient']],
right = possible_dishes_count_df[['Recipe', 'Ingredient']],
on = ['Recipe', 'Ingredient'])


#Stop the program if the user doesn't have enough ingredients
if(len(final_count_df) == 0):
    print("Unfortunately, you cannot cook anything")
    import sys
    sys.exit()


#Obtain a sub-set of the original list, but only containing the recipes that the
#user can cook while also including the non-priority and absent ingredients as well
final_recipe_df = final_count_df['Recipe'].to_frame(name = 'Recipe')
final_dishes_df = pd.merge(left = final_recipe_df, right = dishes_df,
how = 'left', on = ['Recipe'])


#Print the final list of possible recipes along with their ingredients list
print("Here is the list of recipes you can cook\n")
for i in final_recipe_df['Recipe']:
    print(i)
print("\nHere is their ingredient requirement\n")
print(final_dishes_df)
print("\n")

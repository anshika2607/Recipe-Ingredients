RecipeIngredients
This is a part-time project I undertook thanks to quarantine.

Problem statement - Given a list of ingredients the user possesses, query a database(imported as a DataFrame in this code) to identify the recipes they can cook.

Caveats/Call-outs - The quantity of the ingredients isn't considered here. We assume they'll have enough quantity of each ingredient to cook each recipe.

The database was also created by me, with a small sample of Recipes(from South India). The ingredients are written using their English names.

The database identifies a many-to-many mapping between Recipes and Ingredients. A mapping will exist between a Recipe and an Ingredient, if the Ingredient is used in that Recipe. However, this mapping can be of two levels -> Priority and Non-Priority. Priority mappings are these where that Recipe cannot be cooked without that Ingredient. In other words, that Ingredient is compulsory/priority for that Recipe. A Non-Priority mapping indicates that it is possible ot cook that Recipe without the Ingredient. In other words, while we can use the Ingredient to enhance the flavour of the Recipe, it is not compulsory and can be skipped.

Workflow - 1). The database is first loaded as a Dataframe. It has three columns - Recipe, Ingredient and Priority.

2). We then use the "pick" library(define here: https://github.com/wong2/pick.git) to print the list of Ingredients and ask the user to select the ones they possess. The user has to choose a minimum of one Ingredient.

3). We then add a fourth column to the Dataframe called "Present" which flags True if the user possesses the Ingredient mentioned in it's corresponding Row, and a False if not.

4). For each Recipe in the Dataframe, we identify the unique count of "priority" ingredients needed. This tells us the number of ingredients needed to cook the dishes. Not that this step is independant of the user's input ingredient list. As a result, this step can be performed even before step (3).

5). We then do something similar to step (4), but this time considering the user's input. For each Recipe in the Dataframe, we calculate the unique count of ingredients that are both a "priority" and "present". This tells us the number of priority ingredients that the user possesses for each recipe.

6). From steps (4) and (5), we have obtained two separate lists of recipes with a count of priority ingredients and (priority x present) ingredients.

7). Now, we just compare these two lists to obtain a list of Recipes where the priority count and (priority x present) counts are the same. This indicates that the user possesses all the priority ingredients for that particular recipe.

8). Once we have done the filtering in step (7), we have the final list of recipes the user can cook, we display this list.

9). Then, we print the original DataFrame, but filtered to the rows that contain the recipe the user can cook. This will also show the Non-Priority ingredients for each recipe which, the user can use to decide to use it or not if they have it.

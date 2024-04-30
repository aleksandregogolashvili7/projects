fruits= {"apple":130,"avocado":50,"banana":110,"cantaloupe":50,"grapefruit":60,"grape":90,"honeydew melon":50,
     "kiwifruit":90,"pear":100,"peach":60,"orange":80,"strawberries":50,"plums":70,"pineaple":50,
     "sweet cherries":100,"tangerine":50,"watermelon":80}
fruit=input("Item: ").lower().strip()
if fruit not in fruits:
    None
else:

     print("Calories:",fruits[fruit])


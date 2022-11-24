from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def index(request, recipe):
    servings = int(request.GET.get("servings", 1))
    recipe_obj = DATA.get(recipe)
    keys = DATA.get(recipe).keys()
    values = DATA.get(recipe).values()
    recipe = dict(zip(keys, values))

    if servings:
        values = []

        for k, v in recipe_obj.items():
            values.append(v * servings)
            recipe = dict(zip(keys, values))
            print(recipe)

    context = {
        'recipe': recipe,
        'servings': servings,
    }

    return render(request, 'calculator/index.html', context)
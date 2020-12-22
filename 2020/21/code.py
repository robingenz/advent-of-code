def get_input() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt") as f:
        return [l.strip() for l in f.readlines()]


def parse_input(lines: list) -> list:
    foods = list()
    for line in lines:
        split = line.replace(", ", " ").replace(")", "").split(" (contains ")
        foods.append({
            "ingredients": split[0].split(" "),
            "allergens": split[1].split(" ")
        })
    return foods


def get_allergens(foods: list) -> set:
    return set([y for x in foods for y in x["allergens"]])


def get_ingredients(foods: list) -> set:
    return set([y for x in foods for y in x["ingredients"]])


def get_allergen_candidates(foods: list, allergens: set) -> dict:
    allergen_candidates = dict()
    for allergen in allergens:
        ingredients = [set(x["ingredients"])
                       for x in foods if allergen in x["allergens"]]
        allergen_candidates[allergen] = list(set.intersection(*ingredients))
    return allergen_candidates


def map_allergen_to_ingredient(allergens: set, allergen_candidates: dict) -> dict:
    allergen_to_ingredient = dict()
    while len(allergen_to_ingredient) < len(allergens):
        for allergen, candidates in allergen_candidates.items():
            if len(candidates) == 1:
                ingredient = candidates[0]
                allergen_to_ingredient[allergen] = ingredient
                for allergen, candidates in allergen_candidates.items():
                    if ingredient in candidates:
                        candidates.remove(ingredient)
    return allergen_to_ingredient


def get_allergenic_ingredients(allergens: set, allergen_candidates: dict) -> set:
    allergen_to_ingredient = map_allergen_to_ingredient(
        allergens, allergen_candidates)
    return set(allergen_to_ingredient.values())


def part1(foods: list) -> int:
    allergens = get_allergens(foods)
    allergen_candidates = get_allergen_candidates(foods, allergens)
    allergenic_ingredients = get_allergenic_ingredients(
        allergens, allergen_candidates)
    ingredients = get_ingredients(foods)
    non_allergenic_ingredients = ingredients - allergenic_ingredients
    return len([y for x in foods for y in x["ingredients"] if y in non_allergenic_ingredients])


def part2(foods: list) -> int:
    return 0


def main():
    file_input = parse_input(get_input())
    print(f"Part 1: {part1(file_input)}")
    print(f"Part 2: {part2(file_input)}")


if __name__ == "__main__":
    main()

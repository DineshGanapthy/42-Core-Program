from .dark_spellbook import dark_spell_allowed_ingredients

def validate_ingredients(ingredients: str) -> str:

    allowed = dark_spell_allowed_ingredients()
    normalized = ingredients.lower()

    if any(item in normalized for item in allowed):
        return "VALID"
    return "INVAILD"
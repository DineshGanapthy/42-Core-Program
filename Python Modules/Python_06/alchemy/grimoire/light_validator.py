from .light_spellbook import light_spell_allowed_ingredients

def validate_ingredients(ingredients: str) -> str:

    allowed = light_spell_allowed_ingredients()
    normalized = ingredients.lower()

    if any(item in normalized for item in allowed):
        return "VALID"
    return "INVAILD"
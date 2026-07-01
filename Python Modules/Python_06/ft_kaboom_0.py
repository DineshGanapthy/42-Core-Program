import alchemy.grimoire as grimoire

def ft_kaboom_0() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly\n")
    output = grimoire.light_spell_record("Fantasy", "Earth, wind and Fire")
    print(f"Testing record light spell: {output}")


if  __name__=="__main__":
    ft_kaboom_0()
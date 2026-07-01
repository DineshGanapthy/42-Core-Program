from alchemy.potions import strength_potion, healing_potion

def ft_distillation_0() -> None:
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    print(f"Testing strength_potion: {strength_potion()}")
    print(f"Testing healing_potion: {healing_potion()}")

if  __name__=="__main__":
    ft_distillation_0()
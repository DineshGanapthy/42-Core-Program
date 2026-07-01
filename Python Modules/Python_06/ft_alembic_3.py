from alchemy.elements import create_air

def ft_alembic_3() -> None:
    print("=== Alembic 3 ===")
    print("Accessing alchemy/elements.py using 'import ...' structure")
    print(f"Tesing create_air: {create_air()}")

if  __name__=="__main__":
    ft_alembic_3()
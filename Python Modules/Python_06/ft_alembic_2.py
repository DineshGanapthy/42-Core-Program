import alchemy.elements

def ft_alembic_2() -> None:
    print("=== Alembic 2 ===")
    print("Accessing alchemy/elements.py using 'import ...' structure")
    print(f"Tesing create_earth: {alchemy.elements.create_earth()}")

if  __name__=="__main__":
    ft_alembic_2()
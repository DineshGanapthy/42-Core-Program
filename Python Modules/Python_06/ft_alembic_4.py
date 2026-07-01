import alchemy 

def ft_alembic_4() -> None:
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy")
    print(f"Tesing create_air: {alchemy.create_air()}")
    print("Now show that not all functions can be reached")
    print(f"Testing the hidden create_earth: {alchemy.create_earth()}")

if  __name__=="__main__":
    ft_alembic_4()

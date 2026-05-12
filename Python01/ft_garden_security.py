class SecurePlant:
    def __init__(self, name: str) -> None:
        """Initialize a Plant instance."""
        self.name = name
        self.__height = 15
        self.__age = 10
    
    def get_height(self) -> int:
        """Return Plant Height"""
        return self.__height

    def get_age(self) -> int:
        """Reutrn Plant Age"""
        return self.__age

    def set_height(self, height: int) -> None:
        """Set Plant Height"""
        if height < 0:
            print(f"{self.name}: Error height can't be negative")
            print("Height update rejected")
        else:
            self.__height = height
            print(f"Height updated: {height}cm")
        
    def set_age(self, age: int) -> None:
        """Set Plant Age"""
        if age < 0:
            print(f"{self.name}: Error age can't be negative")
            print("Age update rejected")
        else:
            self.__age = age
            print(f"Age updated: {age} days")

    def get_info_first(self) -> None:
        """Print/Show Created plant information"""
        print(f"Plant created: {self.name}: {self.__height:.1f}cm, {self.__age} days old")
        print()

    def get_info(self) -> None:
        """Print/Show Current State plant information"""
        print()
        print(f"Current state: {self.name}: {self.__height:.1f}cm, {self.__age} days old")


def ft_garden_security() -> None:
    """Main Function"""
	
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose")
    plant.get_info_first()
    plant.set_height(25)
    plant.set_age(30)
    print()
    plant.set_height(-5)
    plant.set_age(-35)
    plant.get_info()
	

if __name__ == "__main__":
    ft_garden_security()
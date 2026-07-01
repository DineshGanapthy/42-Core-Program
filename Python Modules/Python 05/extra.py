from typing import Any
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    """ I need this constructer here to help me store data """
    def __init__(self) -> None:
        self._storage: List[]

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """ Validate input before processing """
        pass
    
    @abstractmethod
    def ingest(self, data: Any) -> None:
        """ Ingests the Validated data """
        pass

    def output(self) -> tuple[int, str]:
        """ Outputs the ingested data """
        return (result)

class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        self.result = ''

    def validate(self, data: Any) -> bool:
        try:
            if isinstance(data, (int, float)):
                self.result += (str(data))
                return True
            elif isinstance(data, (list)):
                for i in data:
                    if not isinstance(i, (int, float)):
                        self.result += str(i)
                        return False
                return True
            else:
                return False
        except ValueError:
            return False


    def ingest(self, data: Any) -> None:
        try:
            if not self.validate(data):
                raise ValueError
            return (f"Processing data: {data}\n"
                    f"Extracting 3 values...\n"
                    f"Numeric value 0: {data[0]}\n"
                    f"Numeric value 1: {data[1]}\n"
                    f"Numeric value 2: {data[2]}\n")
        except (TypeError, ValueError) as e:
            return "Got Exception : Improper numeric data"

    def output(self) -> tuple[int, str]:
        print('HHHH' + self.result)
        return super().output(self.result)


# class TextProcessor(DataProccessor):
#     # def __init__(self) -> None:
#     #     super().__init__()

#     def validate(self, data: Any) -> bool:
#         try:
#             if isinstance(data, (str)):
#                 return True
#             elif isinstance(data, (list)):
#                 for i in data:
#                     self._data.append(str(i))
#                     if not isinstance(i, (str)):
#                         return False
#                 return True
#             else:
#                 return False
#         except ValueError:
#             return False


#     def ingest(self, data: Any) -> str:
#         try:
#             if not self.validate(data):
#                 return "Got Exception : Improper numeric data"
#             return (f"Processing data: {data}\n"
#                     f"Extracting 3 values...\n"
#                     f"Numeric value 0: {data[0]}\n"
#                     f"Numeric value 1: {data[1]}\n"
#                     f"Numeric value 2: {data[2]}\n")
#         except (TypeError, ValueError) as e:
#             return f"Error: {data} Improper numeric data"


#     def output(self, result: str) -> str:
#         return super().output(result)




def ft_data_processor() -> None:
    print("=== Code Nexus - Data Processor ===\n")
    
    """ Testing Numeric Processor """
    print("Testing Numeric Processor...")
    num = NumericProcessor()
    print(f"Trying to validate input '42' : {num.validate(42)}")
    print(f"Trying to validate input 'Hello' : {num.validate("Hello")}")

    print(f"Test invalid ingestion of string 'Foo' without prior validation:")
    print(f"{num.ingest("Foo")}")

    processors = [(NumericProcessor(), [1,2,3,4,5])]
    for proc, data in processors:
        print(f"{proc.ingest(data)}")

    num.output()

""" Testing Text Processor """

if __name__ == "__main__":
    ft_data_processor()



# def ft_data_processor() -> None:
#     print("=== Code Nexus - Data Processor ===\n")
    
#     num = NumericProcessor

#     # processors = [(NumericProcessor(), [42])]
#     # for proc, data in processors:
#     #     print(f"{num.validate(data)}")

#     processors = [(NumericProcessor(), ["hello"])]
#     for proc, data in processors:
#         print(f"Trying to validate input '{data}' :{proc.validate(data)}")

#     processors = [(NumericProcessor(), [1,2,3,4,5])]
#     for proc, data in processors:
#         print(f"{proc.ingest(data)}")

# if __name__ == "__main__":
#     ft_data_processor()


    num_list = [1 ,2 ,3 ,4, 5]
    print(f"Processing data : {num_list}")
    num.ingest(num_list)

    print("Extracting 3 values...")
    for idx in range(3):
        rank, val = .output() #rank returns the row's position relative to others (e.g., 1st, 2nd, 3rd)
        print(f"Numeric value {idx}: {val}\n")

    num_list = [1,2,3,4,5]
    print(f"Processing data : {num_list}")
    num.ingest(num_list)

    print("Extracting 3 values...")
    for numbers in range(3):
        rank, val = num.output() #rank returns the row's position relative to others (e.g., 1st, 2nd, 3rd)
        print(f"Numeric Value {numbers}: {val}")

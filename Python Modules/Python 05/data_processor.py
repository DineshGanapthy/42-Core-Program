from typing import Any
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    """ I need this constructer here to help me store data """
    def __init__(self) -> None:
        self._storage: List[tuple[int, str]] = []
        self._current_rank: int = 1 # Got help from AI in these two lines

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
        if not self._storage:
            raise IndexError("No data available to output.")
        return self._storage.pop(0)

class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)) and not isinstance(data, bool): # Need to include this extra 
            return True                           #because Bool is considered an ingeter so it will pass true even thought its not an integer. 
        elif isinstance(data, (list)):
            for i in data:
                if not isinstance(i, (int, float)):
                    return False
            return True
        else:
            return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        
        if isinstance(data, list):
            for item in data:
                self._storage.append((self._current_rank, str(item)))
                self._current_rank += 1
        else:
            self._storage.append((self._current_rank, str(data)))
            self._current_rank += 1

class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            for i in data:
                if not isinstance(i, str):
                    return False
            return True
        else:
            return False
            
    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        elif isinstance(data, list):
            for item in data:
                self._storage.append((self._current_rank, item)) # No need to type cast here as 
                self._current_rank += 1                         # the data is aleady a string
        else:
            self._storage.append((self._current_rank, data))
            self._current_rank += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        #Checking data type is a dictionary and if all key values and it paires are strings
        if isinstance(data, dict):
            for key, val in data.items():
                if not isinstance(key, str) or not isinstance(val, str):
                    return False
            return True
        elif isinstance(data, list):
            for item in data:
                if not isinstance(item, dict):
                    return False
                for key, val in item.items():
                    if not isinstance(key, str) or not isinstance(val, str):
                        return False
            return True
        else:
            return False
            
    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        if isinstance(data, list):
            for log_dict in data:
                log_level = log_dict.get('log_level', '')
                log_message = log_dict.get('log_message', '')
                log_str = f"{log_level}: {log_message}"
                self._storage.append((self._current_rank, log_str)) 
                self._current_rank += 1              
        else:
            log_str = f"{log_dict.get('log_level','')}: {log_dict.get('log_message','')}" #way directly putting it in
            self._storage.append((self._current_rank, log_str))
            self._current_rank += 1


def ft_data_processor() -> None:
    print("=== Code Nexus - Data Processor ===\n")
    
    """ Testing Numeric Processor """
    print("Testing Numeric Processor...")
    num = NumericProcessor()
    print(f"Trying to validate input '42' : {num.validate(42)}")
    print(f"Trying to validate input 'Hello' : {num.validate("Hello")}")

    print(f"Test invalid ingestion of string 'Foo' without prior validation:")
    try:
        print(f"{num.ingest("Foo")}")
    except ValueError as e:
        print(f"Got Exception : {e}")

    try:
        num_list = [1,2,3,4,5]
        print(f"Processing data : {num_list}")
        num.ingest(num_list)

        print("Extracting 3 values...")
        for index in range(3):
            rank, val = num.output() #rank returns the row's position relative to others (e.g., 1st, 2nd, 3rd)
            print(f"Numeric Value {index}: {val}")
    except ValueError as e:            # Just etsting around with extra errors. Error checking
        print(f"Got Exception : {e}")
    except NameError as e:
        print(f"Got Exception : {e}")
    print()

    """ Testing Text Processor """
    print("Testing Text Processor...")
    text = TextProcessor()
    print(f"Trying to validate input '42' : {text.validate(42)}")
    
    text_list = ['Hello', 'Nexus', 'World']
    print(f"Processing data : {text_list}")
    text.ingest(text_list)

    print("Extracting 1 value...")
    for index in range(1):
        rank, val_1 = text.output() #rank returns the row's position relative to others (e.g., 1st, 2nd, 3rd)
        print(f"Text Value {index}: {val_1}")
    print()

    """ Testing log Processor """
    print("Testing Log Processor...")
    log = LogProcessor()
    print(f"Trying to validate input 'hello' : {log.validate("Hello")}")
    
    my_dict = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'}, 
        {'log_level': 'ERROR ', 'log_message': 'Unauthorized access!!'}
        ]
    print(f"Processing data : {my_dict}")
    log.ingest(my_dict)

    print("Extracting 2 value...")
    for index in range(2):
        rank, val_2 = log.output()
        print(f"Log entry {index}: {val_2}")
    print()


if __name__ == "__main__":
    ft_data_processor()

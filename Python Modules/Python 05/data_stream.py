from typing import Any
from abc import ABC, abstractmethod

class DataStream:
    def __init__(self) -> None:
        self.processors: List[DataProcessor] = []
        self.processed_counters: Dict[str, int] = {}

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)
        name = proc.__class__.__name__
        if name not in self.processed_counters:
            self.processed_counters[name] = 0

    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:
            handled = False
            for proc in self.processors:
                if proc.validate(element):
                    proc.ingest(element)

                    increment = len(element) if isinstance(element, list) else 1
                    name = proc.__class__.__name__
                    self.processed_counters[name] += increment 

                    handled = True
                    break

            if not handled:
                print(f"DataStream error - Can't process element in stream: {element}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No Processor found, no data")
            return
        
        for proc in self.processors:
            name = proc.__class__.__name__
            total = self.processed_counters.get(name, 0)
            remaining = len(proc._storage)

            display_name = name.replace("Processor", " Processor")
            print(f"{display_name}: total {total} item processed, remaining {remaining} on processor")


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


def ft_data_stream() -> None:
    print("=== Code Nexus - Data Stream ===\n")

    print("Initialize Data Stream...")
    stream_engine = DataStream()
    stream_engine.print_processors_stats()
    print()

    print("Resgistering Numeric Processor")
    num = NumericProcessor()
    stream_engine.register_processor(num)
    print()
    
    #Data Batches 
    batch = ['Hello World', [3.14, -1, 2.71], 
        [
            {'log_level': 'WARNING', 'log_message': "Telent acess! Use ssh instead"},
            {'log_level': 'INFO' , 'log_message': 'User wil is connected'}
        ],
        42,
        ['Hi' , 'Five']
    ]   

    print(f"Send first batch of data on stream: {batch}")
    print()
    stream_engine.process_stream(batch)
    print()

    stream_engine.print_processors_stats()
    print()

    print("Registering other data processors")
    text = TextProcessor()
    log = LogProcessor()
    stream_engine.register_processor(text)
    stream_engine.register_processor(log)
    print()

    print("Send the same batch again")
    stream_engine.process_stream(batch)
    stream_engine.print_processors_stats()
    print()

    print ("Consume some elements from the data processors: Numeric 3, Text 2, Log 1")
    for _ in range(3): num.output()
    for _ in range(2): text.output()
    for _ in range(1): log.output()

    stream_engine.print_processors_stats()



if __name__ == "__main__":
    ft_data_stream()

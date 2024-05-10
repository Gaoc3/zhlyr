import json
from json import JSONDecodeError
from dataclasses import dataclass
from typing import Union, List, Dict, Any

@dataclass
class Serializer:
    '''
    A dataclass that can be serialized to JSON and deserialized from JSON.
    '''
    __data: Union[str, List, Dict[str, Any]]  # Making the field private

    def __post_init__(self):
        # Convert JSON string to dictionary if data is a string
        if isinstance(self.__data, str):
            self.__data = json.loads(self.__data)

    def __serializer(self, data):
        if isinstance(data, bool):
            return data
        elif isinstance(data, int):
            return data
        elif isinstance(data, float):
            return data
        elif isinstance(data, str):
            try:
                return json.loads(data)
            except JSONDecodeError:
                return data
        elif isinstance(data, list):
            return [self.__serializer(element) for element in data]
        elif isinstance(data, dict):
            return Serializer(data) 
        else:
            return data  # Return data unchanged for other types
    
    def __getattr__(self, item):
        # Allow direct access to JSON keys using dot notation
        if item in self.__data:
            return self.__serializer(self.__data[item])
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{item}'")

    def __repr__(self):
        json_str = ", ".join([f"{key}={self.__format_data(data)}" for key, data in self.__data.items()])
        return f"{self.__class__.__name__}(data=({json_str}))"

    def __format_data(self, data):
        if isinstance(data, list):
            return list(self.__format_data(element) for element in data)
        elif isinstance(data, dict):
            return Serializer(data)  # Use Serializer to create objects
        return data


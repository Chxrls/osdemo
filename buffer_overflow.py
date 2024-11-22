# Example of a potential vulnerability
import os

def vulnerable_func(data):
    buffer = data[:50] # truncate data for input safety
    
    if len(buffer) < 50:
        print(f"Buffer: {buffer}")
        print(f"Input length: {len(data)}")

    else:
        print("Error: Buffer Overflow")
        print(f"Input length: {len(data)}")

data = input("Enter input: ")
vulnerable_func(data)

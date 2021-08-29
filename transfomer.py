import sys
import json

# Initialize
BINARY_TO_BASE64 = json.loads(open("table.json", "r").read())
BASE64_TO_BINARY = {v: k for k, v in BINARY_TO_BASE64.items()}


# Define function
def str2bin(input_data: str):
    """
    Args:
        input_data (str)
    Return:
        binary_data (binary)
    """
    binary_data = ""
    for s in input_data:
        binary_data += format(ord(s), "08b")
    return binary_data


def split(input_data: str, split_number: int, replace="0"):
    """
    Args:
        input_data:
        split_number:
        replace:
    Returns:
        split_list (list):
    """
    split_list = []
    split_list = [input_data[i:i + split_number] for i in range(0, len(input_data), split_number)]
    mergine = (len(input_data) % split_number)
    if mergine:
        split_list[-1] = split_list[-1] + (replace * (split_number - mergine))
    return split_list


# Process
argvs = sys.argv
input_data = argvs[1]
print(f"{input_data=}\n")
# Encode
print("=========Encoding===========")
# Step 1 string to binary
b = f"{str2bin(input_data=input_data)}"
print(f"binary= {b}")
# Step 2 split binary and fill 0
splited = split(input_data=b, split_number=6, replace="0")
print(f"filled={splited}")

# Step 3 convert binary to Base64 format
converted = ""
for string in splited:
    converted += BINARY_TO_BASE64[string]
print(f"{converted=}")
# Step 4 fill blank to `=`
encoded = ""
for s in split(input_data=converted, split_number=4, replace="="):
    encoded += s

# Step 5 plint result
print(f"{encoded=}\n")

# Decode
print("=========Decoding======")
print(f"{encoded=}\n")
d = ""
for s in [i for i in encoded if i != "="]:
    d += BASE64_TO_BINARY[s]
decode = split(input_data=d, split_number=8, replace="")
print(f"filled= {decode}")
result = ""
for i, d in enumerate(decode):
    if len(d) != 8:
        del decode[i]
    result += chr(int(d, 2))
print(f"decoded= {result}")

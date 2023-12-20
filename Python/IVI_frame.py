def hex_to_bin(hex_string):
    # Making the input without any spaces
    hexString = hex_string.replace(" ", "")

    # Going from string to decimal number
    decimalNumber = int(hexString, 16)

    # Going from the decimal number to binary mode (excluding 0b)
    binNumber = bin(decimalNumber)[2:]

    # Checking for length to be multiple of 8 if not ADD 0s
    if len(binNumber) % 8 != 0:
        # This works because the binary data is represented as a 'str' class
        binNumber = '0' * (8 - len(binNumber) % 8) + binNumber

    return binNumber


def signal_to_value(signal_info4, binary_string):
    # Ensure the binary string is indeed a multiple of 8S
    if len(binary_string) % 8 != 0 or not all(c in '01' for c in binary_string):
        raise ValueError("The binary string is not a valid multiple of 8 bits.")

    if signal_info4[3] < 1 or signal_info4[3] > 8:
        raise ValueError("The size is outside of range!")
    elif signal_info4[2] < 0 or signal_info4[2] > 7:
        raise ValueError("Starting position of the bit is outside of range")

    # Split the binary string into groups of 8 bits
    groups = [binary_string[i:i + 8] for i in range(0, len(binary_string), 8)]

    # Extract the signal information
    signal_name, group_number, reverse_start_position, size = signal_info4

    # Adjust the start position as per the reversed indexing within the group
    start_position = 7 - reverse_start_position

    # Select the appropriate group
    group = groups[group_number]
    # Extract the signal value from the group
    if size == 1:
        signal_value_bin = group[start_position]
    else:
        signal_value_bin = group[start_position: start_position + size]

    # Convert binary signal value to decimal
    signal_value_decimal = int(signal_value_bin, 2)
    print(signal_name, "->", signal_value_decimal)

    # return signal_value_decimal


def show_values(inputs, sig_il):
    binary_frame = hex_to_bin(inputs)

    # Extract and print the values for each signal
    for signal_info in sig_il:
        signal_to_value(signal_info, binary_frame)


hex_input = "60 20 45 6C FE 3D 4B AA"
hex_input2 = "40 12 6C AF 05 78 4A 04"

# Define the signal information based on the provided input
signal_info_list = [
    ["PassengerSeatMemoRequest", 0, 7, 3],  # PassengerSeatMemoRequest
    ["TimeFormatDisplay", 5, 3, 1],  # TimeFormatDisplay
    ["ClimFPrightBlowingRequest", 5, 7, 4]  # ClimFPrightBlowingRequest
]

print("First values:")
show_values(hex_input, signal_info_list)
print("\nSecond values:")
show_values(hex_input2, signal_info_list)

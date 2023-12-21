# Original string provided by the user
hex_string = ("00 06 02 08 40 00 00 10 00 00 00 00 00 05 D0 08 21 20 00 00 02 00 00 00 00 06 01 08 80 00 00 00 00 00 "
              "00 00 00 00 00 11 29 FB 84 33 1D E5 5E 9D")

# 00 06 02 08 80 00 00 00 00 00 00 00 00 05 D0 08 FF 60 00 00 02 00 00 00 00 06 01 08 80 00 00 00 00 00 00 00 00 00
# 10 C7 77 8A 70 AB AF 88 2A 8C

# 00 06 02 08 40 00 00 10 00 00 00 00 00 05 D0 08 21 20 00 00 02 00 00 00 00 06 01 08 80 00 00 00 00 00 00 00 00 00
# 00 11 29 FB 84 33 1D E5 5E 9D

signals = ["LDW_AlertStatus", "DW_FollowUpTimeDisplay", "LCA_OverrideDisplay"]
index_signals = [x for x in range(len(signals))]
signal_values = [2, 45, 1]
byte_positions = [2, 4, 5]
bit_positions = [5, 7, 2]
sizes = [2, 6, 1]
interest = {}

for i in range(len(signals)):
    interest[index_signals[i]] = [signals[i], signal_values[i], byte_positions[i], bit_positions[i], sizes[i]]


def decimal_to_binary(decimal_value):
    # Convert the decimal value to binary
    binary_value = bin(decimal_value)

    # Remove the '0b' prefix which indicates a binary number
    return binary_value[2:]


# Capturing the binary values of the signals
for i in range(len(interest)):
    interest[index_signals[i]] = [signals[i], signal_values[i], byte_positions[i], bit_positions[i], sizes[i],
                                  decimal_to_binary(signal_values[i])]
    if len(decimal_to_binary(signal_values[i])) != interest[index_signals[i]][4]:
        raise ValueError("Something went wrong: check the data input")

def manipulationString(hex_raw):
    # Step 1: Remove all spaces
    hex_raw_no_spaces = hex_raw.replace(" ", "")

    # Step 2 and 3: Separate the strings into groups of 2 and create an array
    array_of_pairs = [hex_raw_no_spaces[i:i + 2] for i in range(0, len(hex_raw_no_spaces), 2)]

    # Step 4: Create an array that focuses on the first 36 elements
    interestString = array_of_pairs[:36]

    # Step 5: Split interestString into subgroups
    first_PDU = interestString[4:12]
    second_PDU = interestString[16:24]
    third_PDU = interestString[28:36]

    # Step 6: Create a new array with the elements grouped as 8 elements
    PDU_array = [first_PDU, second_PDU, third_PDU]
    return PDU_array

listPDU = manipulationString(hex_string)

extract_byte0 = listPDU[0][interest[index_signals[0]][2]]
extract_byte1 = listPDU[1][interest[index_signals[1]][2]]
extract_byte2 = listPDU[2][interest[index_signals[2]][2]]


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


bin_byte0 = hex_to_bin(extract_byte0)
bin_byte1 = hex_to_bin(extract_byte1)
bin_byte2 = hex_to_bin(extract_byte2)
# print()


def replace_bits(original_string, value_to_insert, reverse_position):
    # Calculate the start position
    start_position = 7 - reverse_position

    # Length of the value to be inserted
    length_of_value = len(value_to_insert)

    # Replace the bits in the original string
    new_string = original_string[:start_position] + value_to_insert + original_string[start_position + length_of_value:]

    return new_string


new_String0 = replace_bits(bin_byte0, interest[index_signals[0]][5], interest[index_signals[0]][3])
new_String1 = replace_bits(bin_byte1, interest[index_signals[1]][5], interest[index_signals[1]][3])
new_String2 = replace_bits(bin_byte2, interest[index_signals[2]][5], interest[index_signals[2]][3])


def binary_to_hex(binary_string):
    # Convert the binary string to an integer
    integer_value = int(binary_string, 2)

    # Determine the number of hex digits needed
    hex_digits = len(binary_string) // 4

    # Convert the integer to a hexadecimal string with padding for leading zeros
    hex_string = format(integer_value, '0' + str(hex_digits) + 'X')

    return hex_string


new_HexCodes0 = binary_to_hex(new_String0)
new_HexCodes1 = binary_to_hex(new_String1)
new_HexCodes2 = binary_to_hex(new_String2)

print(new_HexCodes0, new_HexCodes1, new_HexCodes2)

# Replace the bytes in listPDU with new hex values
listPDU[0][interest[index_signals[0]][2]] = new_HexCodes0
listPDU[1][interest[index_signals[1]][2]] = new_HexCodes1
listPDU[2][interest[index_signals[2]][2]] = new_HexCodes2

combined_string0 = ''.join(listPDU[0])
combined_string1 = ''.join(listPDU[1])
combined_string2 = ''.join(listPDU[2])


def reassembleString(hex_code, pdu1, pdu2, pdu3):
    # Step 1: Remove all spaces
    hex_raw_no_spaces = hex_code.replace(" ", "")

    updated_string = (hex_raw_no_spaces[:8] + pdu1 + hex_raw_no_spaces[24:32] + pdu2 + hex_raw_no_spaces[48:56] + pdu3
                      + hex_raw_no_spaces[72:])

    spaced_hex_string = ' '.join(updated_string[i:i + 2] for i in range(0, len(updated_string), 2))

    print("Modified frame: ", spaced_hex_string)


print("Your input:     ", hex_string)
reassembleString(hex_string, combined_string0, combined_string1, combined_string2)

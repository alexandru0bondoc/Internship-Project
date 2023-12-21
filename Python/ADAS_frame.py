def convert_decimal_to_binary(decimal_value):
    """
    Converts a decimal value to binary string, omitting the '0b' prefix
    Input:
        - decimal_value: The decimal value to convert
    Output:
        - A binary string of the decimal value
    """
    return bin(decimal_value)[2:]


def extract_interesting_parts_of_hex_string(hex_value):
    """
    Extracts segments (PDUs) of a hex string that are of interest for further processing
    Input:
        - hex_value: A string containing hex values (the original hex_string)
    Output:
        - A list of lists, where each sublist contains pairs of hex values from the
          segments of interest (PDU)
    """
    # Remove spaces to sanitize input
    hex_value = hex_value.replace(" ", "")

    # Slicing the hex string into pairs to work with standard byte lengths
    # Easier to track :)
    pairs = [hex_value[i:i + 2] for i in range(0, len(hex_value), 2)]

    # Extracts only the relevant pairs for the PDU
    return [pairs[4:12], pairs[16:24], pairs[28:36]]


def convert_hex_to_binary(value_of_hex):
    """
    Converts a hexadecimal string to a padded binary string ensuring byte alignment
    Input:
        - value_of_hex: The hexadecimal string to convert
    Output:
        - A binary string of the hexadecimal value, padded to maintain byte alignment
    """
    # The original format is a string to say so
    # From the string we go base 16 = hex (yet still the 'str' class)
    # The [2: is for omitting the '0b' prefix
    binary_string = bin(int(value_of_hex, 16))[2:]

    # Zfill adds leading zeros to the binary string to complete the last byte
    return binary_string.zfill((len(binary_string) + 7) // 8 * 8)


def insert_value_at_position(original_string, value, position):
    """
    Inserts a binary value into a specific bit position within a binary string
    Input:
        - original_string: The original binary string
        - value: The binary value to insert
        - position: The REVERSE bit position where the value should be inserted
    Output:
        - The modified binary string with the value inserted at the specified position
    """
    start = 7 - position  # Calculate the start index based on the bit position

    end = start + len(value)  # The end index is offset by the length of the value

    # Replace the bits at the specified position with the new value
    return original_string[:start] + value + original_string[end:]


def convert_binary_to_hex(binary_string):
    """
    Converts a binary string to a hexadecimal string, padding based on the binary string's length
    Input:
        - binary_string: The binary string to convert
    Output:
        - A hexadecimal string of the binary value, formatted with leading zeros
    """
    # Calculate the necessary length of the hex string
    hex_length = len(binary_string) // 4

    # Format the integer representation of the binary string into hexadecimal, padded with zeros
    return format(int(binary_string, 2), f'0{hex_length}X')


def reassemble_hex_string(original_hex, pdu1, pdu2, pdu3):
    """
    Reassembles a hex string with updated PDUs (Protocol Data Units)
    Input:
        - original_hex: The original hex string before updating
        - pdu1, pdu2, pdu3: The updated PDU strings to be inserted
    Output:
        - The fully reassembled hex string with updated PDUs
    """
    # Sanitize the input by removing spaces
    hex_no_spaces = original_hex.replace(" ", "")
    # Construct the updated hex string by inserting the PDUs at the correct intervals
    updated_string = (hex_no_spaces[:8] + pdu1 + hex_no_spaces[24:32] + pdu2 + hex_no_spaces[48:56] + pdu3
                      + hex_no_spaces[72:])
    # The output needs to be in a nice format :)
    return ' '.join(updated_string[i:i + 2] for i in range(0, len(updated_string), 2))


def process_hex_string(value_hex, interest_dict):
    """
    The logistics how this can work instead of doing the main I did a function :)
    Input:
        - value_hex: The hex string to be processed
        - interest_dict: A dictionary defining the parts of the hex string to be updated and how
    Output:
        - The processed and updated hex string
    """
    # Extract the PDUs that will be updated
    pdus = extract_interesting_parts_of_hex_string(value_hex)
    # Convert the hex PDUs to binary
    binary_values = [convert_hex_to_binary(''.join(pdus[i][interest_dict[index][2]]))
                     for i, index in enumerate(interest_dict)]
    # Insert new values at specified positions within the binary PDUs
    new_binary_strings = [insert_value_at_position(binary_values[i], interest_dict[index][5], interest_dict[index][3])
                          for i, index in enumerate(interest_dict)]
    # Convert the updated binary PDUs back to hex
    new_hex_codes = [convert_binary_to_hex(new_binary_strings[i]) for i in range(len(interest_dict))]

    # Update the original PDUs with the new hex values
    for i, index in enumerate(interest_dict):
        pdus[i][interest_dict[index][2]] = new_hex_codes[i]

    # Reassemble the complete hex string with the updated PDUs
    combined_strings = [''.join(pdu) for pdu in pdus]
    return reassemble_hex_string(value_hex, *combined_strings[:3])


def show_output(hex_fin, dict_interest):
    """
    Prints the original and modified hex string
    Input:
        - hex_fin: The original hex string to display
        - dict_interest: The dictionary of interests used for processing
    """
    print("Your input:     ", hex_fin)
    modified_frame = process_hex_string(hex_fin, dict_interest)
    print("Modified frame: ", modified_frame)


# Input is provided and the functions above are called to perform the processing
# Improvements (optimization and error handling can be implemented)

# Input the hex string of interest in a format like this
hex_string = ("00 06 02 08 40 00 00 10 00 00 00 00 00 05 D0 08 21 20 00 00 02 00 00 00 00 06 01 08 80 00 00 00 00 00 "
              "00 00 00 00 00 11 29 FB 84 33 1D E5 5E 9D")
hex_string2 = ("00 06 02 08 80 00 00 00 00 00 00 00 00 05 D0 08 FF 60 00 00 02 00 00 00 00 06 01 08 80 00 00 00 00 00 "
               "00 00 00 00 10 C7 77 8A 70 AB AF 88 2A 8C")

# This can be done in a list format, but I went with a dictionary approach
# For a better manipulation of the metadata
# It's easier to input one modified small data or to bring a new key:value pair in a dictionary then manipulating a list
# Input the values for the signals
signals = ["LDW_AlertStatus", "DW_FollowUpTimeDisplay", "LCA_OverrideDisplay"]
signal_values = [2, 45, 1]
byte_positions = [2, 4, 5]
bit_positions = [5, 7, 2]
sizes = [2, 6, 1]

# Build structure for the dictionary with a list comprehension method
interest = {index: [signals[index], signal_values[index], byte_positions[index], bit_positions[index], sizes[index]] for
            index in range(len(signals))}

# Converting the signal_value to a binary value and add it to the dictionary
# Easier to track things with it
for index in interest:
    binary_value = convert_decimal_to_binary(signal_values[index])
    if len(binary_value) != sizes[index]:
        raise ValueError("Something went wrong: check the data input")
    interest[index].append(binary_value)

# How it was
show_output(hex_string, interest)
print('\n')

# How it became 
show_output(hex_string2, interest)


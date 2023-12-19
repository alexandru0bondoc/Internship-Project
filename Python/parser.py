def timestamp_to_milliseconds(timestamp):
    try:
        hours, minutes, seconds = map(float, timestamp.split(':'))
        return int(hours * 3600000 + minutes * 60000 + seconds * 1000)
    except ValueError:
        return None  # Return None for invalid timestamps

def word_parser(filename, start_timestamp, end_timestamp):
    last_words = []
    start_ms = timestamp_to_milliseconds(start_timestamp)
    end_ms = timestamp_to_milliseconds(end_timestamp)

    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    timestamp = line[6:18]  # Extract timestamp from a specific position in the line
                    current_ms = timestamp_to_milliseconds(timestamp)

                    if current_ms is not None and start_ms <= current_ms <= end_ms:
                        words = line.split()  # Split the line into words

                        if words:
                            last_word = words[-1]  # Take the last word from the list
                            last_words.append(last_word.strip())  # Append it, removing any leading/trailing whitespace
                except ValueError:
                    continue  # Skip lines with invalid timestamp format

        return last_words

    except FileNotFoundError:
        print(f"Couldn't find this file: {filename}")

log = 'logcat_applications.txt'
start_timestamp = '17:56:07.996'
end_timestamp = '17:56:08.357'

# Extract and print the last words
result = word_parser(log, start_timestamp, end_timestamp)
print(result)

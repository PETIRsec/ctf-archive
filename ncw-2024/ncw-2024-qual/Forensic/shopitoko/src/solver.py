import re

status_codes = {}
    
def count_status_codes(log_file):
    pattern = r'\s(\d{3})\s'

    with open(log_file, 'r') as file:
        for line in file:
            match = re.search(pattern, line)
            if match:
                status_code = match.group(1)
                status_codes[status_code] = status_codes.get(status_code, 0) + 1

    return status_codes

# Assuming the log file is named 'server.log'
log_file = 'server.log'
status_code_counts = count_status_codes(log_file)

print("Different HTTP status codes found:")
for code, count in status_codes.items():
    print(f"Status code {code}: {count} occurrences")

print(f"\nTotal number of different status codes: {len(status_codes)}")
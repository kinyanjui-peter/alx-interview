#!/usr/bin/python3
"""
"""
import sys
import datetime
import re


def checkFormat(userInput):
    """aA fuction that check validity of userInput data"""
    pattern1 = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - '
    pattern2 = r'\[\d{2}/(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)/\d{4}\] '
    pattern3 = r'"GET /projects/260 HTTP/1.1" \d{3} \d*$'
    pattern = pattern1 + pattern2 + pattern3
    if userInput == "":
        return ("Please input your Data")
    if not re.match(pattern, userInput):
        return("wrong format")
    return "congratulations!!! Correct format"
    # read through stdin in the format:-


def print_statistics(total_file_size, status_counts):
    """Print statistics based on the computed metrics."""
    print(f"Total file size: {total_file_size}")
    for status_code, count in sorted(status_counts.items()):
        print(f"Status {status_code}: {count}")

def main():
    total_file_size = 0
    status_counts = {}
    print("Enter your data strictly following the format")
    print("<IP Address> - [<date>] 'GET /projects/260 HTTP/1.1'")
    print("status code> <file size>")

    try:
            for line in sys.stdin:
                line = line.strip()
                if checkFormat(line) == "Congratulations!!! Correct format":
                    parts = line.split()
                    file_size = int(parts[-1])
                    total_file_size += file_size
                    status_code = parts[-2]
                    status_counts[status_code] = status_counts.get(status_code, 0) + 1

                if len(status_counts) >= 8:  # All possible status codes collected
                    break

        except KeyboardInterrupt:
            pass

        print_statistics(total_file_size, status_counts)

    if __name__ == "__main__":
        main()

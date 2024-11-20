import sys

# Conversion factors with a diction
metric_prefixes = {
    'b': 1,        # bits
    'B': 8,        # bytes (1 byte = 8 bits)
    'Kb': 1000,     # kilobits
    'KB': 8 * 1000,     # kilobytes (1 KB = 8 * 1000 bits)
    'Kib': 1024,   # kibibits (2^10 bits)
    'KiB': 8 * 1024,  # kibibytes (2^10 * 8 bits)
    'Mb': 1e6,     # megabits
    'MB': 8e6,     # megabytes (1 MB = 8 * 10^6 bits)
    'Mib': 1024 ** 2, # mebibits (2^20 bits)
    'MiB': 8 * 1024 ** 2, # mebibytes (2^20 * 8 bits)
    'Gb': 1 * 10**9,     # gigabits
    'GB': 8 * 10**9,     # gigabytes (1 GB = 8 * 10^9 bits)
    'Gib': 1024 ** 3, # gibibits (2^30 bits)
    'GiB': 8 * 1024 ** 3 # gibibytes (2^30 * 8 bits)
}

def convert(value, input_unit, output_unit):
    # I REALLY DONT KNOW HOW TO TAKE CARE OF PREFIX CASE
    # caseInsens_input = ""
    # inpList = input_unit.strip.split("")
    # caseInsens_input += inpList[0].upper() + inpList[1]
    if input_unit not in metric_prefixes or output_unit not in metric_prefixes:
        print(f"Error: Unsupported unit {input_unit} or {output_unit}")
        return 
    
    # Convert the input value to bits
    value_in_bits = float(value) * metric_prefixes[input_unit]
    
    # Convert from bits to the output unit
    output_value = value_in_bits / metric_prefixes[output_unit]
    
    return output_value

def main():
    # ref (CHAtGPT): this part catches an out-of-range error and return null/nothing
    if len(sys.argv) != 4:
        print("Error: Please provide exactly three arguments.")
        print("Usage: byte-converter.py <value> <input unit> <output unit>")
        return

    # three input arguments from the terminal
    value = sys.argv[1]
    input_unit = sys.argv[2] 
    output_unit = sys.argv[3]

    # Perform conversion
    result = convert(value, input_unit, output_unit)
    if result is not None:
        print(result)

if __name__ == "__main__":
    main()
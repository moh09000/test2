import base64

# Base64 URL decode function (padding may be required)
def base64_url_decode(encoded_str):
    # Replace URL-safe characters with standard Base64 characters
    base64_str = encoded_str.replace('-', '+').replace('_', '/')
    # Add necessary padding if missing
    padding = len(base64_str) % 4
    if padding != 0:
        base64_str += '=' * (4 - padding)
    # Decode the Base64 string
    return base64.b64decode(base64_str).decode('utf-8', errors='ignore')

# Function to process a file of tokens
def process_token_file(file_path):
    # Open the file and read tokens line by line
    with open(file_path, 'r') as file:
        tokens = file.readlines()

    # Process each token
    for token_num, encoded_str in enumerate(tokens, 1):
        encoded_str = encoded_str.strip()  # Remove any surrounding whitespace
        if encoded_str:
            # Splitting the input string by "."
            parts = encoded_str.split(".")
            decoded_parts = [base64_url_decode(part) for part in parts]

            # Output the decoded parts
            print(f"Token {token_num}:")
            for i, part in enumerate(decoded_parts, 1):
                print(f"  Decoded part {i}: {part}")
            print()

# Example usage
file_path = 'tokens.txt'  # Update this to the path of your file containing tokens
process_token_file(file_path)

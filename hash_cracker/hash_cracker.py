import hashlib

def crack_hash(hash_to_crack, hash_type, wordlist_path):
    # Check if the wordlist file can be opened
    try:
        with open(wordlist_path, 'r') as file:
            print("Wordlist file opened successfully.")
    except FileNotFoundError:
        print(f"File not found: {wordlist_path}")
        return

    # Start cracking the hash
    with open(wordlist_path, 'r') as file:
        for word in file:
            word = word.strip()
            if hash_type == 'md5':
                hashed = hashlib.md5(word.encode()).hexdigest()
            elif hash_type == 'sha1':
                hashed = hashlib.sha1(word.encode()).hexdigest()
            elif hash_type == 'sha256':
                hashed = hashlib.sha256(word.encode()).hexdigest()
            else:
                print("Unsupported hash type.")
                return

            if hashed == hash_to_crack:
                print(f"[+] Password found: {word}")
                return
    print("[-] Password not found in wordlist.")

# Example usage:
# Set the hash type and hash to crack. 
# You can change the hash_type and hash_to_crack to any of the supported types.
hash_type = 'md5'  # You can change this to 'md5', 'sha1', or 'sha256'
hash_to_crack = 'ec0e2603172c73a8b644bb9456c1ff6e'  # Example md5 hash of "batman"
wordlist_path = r"C:\Users\glitc\OneDrive\Desktop\Coding_Projects\hash_cracker\wordlist.txt"  # Path to your wordlist file

crack_hash(hash_to_crack, hash_type, wordlist_path)
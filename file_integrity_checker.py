import hashlib
import os

def compute_file_hash(file_path, hash_algorithm='sha256'):
    hash_obj = hashlib.new(hash_algorithm)
    with open(file_path, 'rb') as file:
        chunk_size = 4096
        while chunk := file.read(chunk_size):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

def verify_file_integrity(file_path, expected_hash, hash_algorithm='sha256'):
    computed_hash = compute_file_hash(file_path, hash_algorithm)
    if computed_hash == expected_hash:
        print("File integrity verified. Hashes match.")
    else:
        print("File integrity verification failed. Hashes do not match.")
        print(f"Computed hash: {computed_hash}")
        print(f"Expected hash: {expected_hash}")

def main():
    file_path = input("Enter the path to the file: ")
    if not os.path.isfile(file_path):
        print("File not found.")
        return
    expected_hash = input("Enter the expected hash value: ")
    hash_algorithm = input("Enter the hash algorithm (default is sha256): ").lower() or 'sha256'
    verify_file_integrity(file_path, expected_hash, hash_algorithm)

if __name__ == "__main__":
    main()

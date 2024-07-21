# FileIntegrityChecker

A Python script to verify file integrity using hash algorithms.

## Description

FileIntegrityChecker is a simple Python script that allows users to verify the integrity of files by computing their hash values and comparing them to expected hash values. It supports multiple hash algorithms such as SHA-256, SHA-1, and MD5.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/FileIntegrityChecker.git
    cd FileIntegrityChecker
    ```

2. Ensure you have Python installed. This script requires Python 3.6 or higher.

## Usage

1. Run the script:
    ```bash
    python file_integrity_checker.py
    ```

2. Follow the on-screen prompts to:
    - Enter the path to the file you want to check.
    - Enter the expected hash value.
    - Enter the hash algorithm (default is sha256).

## Example

```text
Enter the path to the file: /path/to/your/file.txt
Enter the expected hash value: d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2
Enter the hash algorithm (default is sha256): sha256
File integrity verified. Hashes match.

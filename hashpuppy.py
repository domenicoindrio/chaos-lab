import argparse, sys
# HashPuppy, a simple python script for guessing a probable hash type based solely on length

# Algorithm mapping
algo = {
    "md5": 32,
    "sha1": 40,
    "sha256": 64,
    "sha512": 128
}

def guess_algorithm_by_hash_length(hash_string):
    hash_string = hash_string.strip()
    length = len(hash_string)
    for name, expected_lenght in algo.items():
        if length == expected_lenght:
            return name
    return None


def main():
    parser = argparse.ArgumentParser(description="HashPuppy, a simple python script for guessing a probable hash type based solely on length")
    parser.add_argument("-hs", required=True, type=str, help="Hashstring to identify")
    
    args = parser.parse_args()
    

    try:
        algorithm = guess_algorithm_by_hash_length(args.hs)
        if algorithm:
            print(f"[+] Based solely on lenght, the hash algorithm for the provided hashstring could be: {algorithm.upper()}")
            sys.exit(0)
        else:
            print("[-] Unknown hash length, unable to determine algorithm")
            sys.exit(1)
    except Exception as e:
        print(f"[-] Error: {e}")
        sys.exit(1)



if __name__ == "__main__":
    main()
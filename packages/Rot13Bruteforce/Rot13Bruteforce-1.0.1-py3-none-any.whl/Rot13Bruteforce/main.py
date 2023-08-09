def rot13_bruteforce(string):
    results = {}
    
    for i in range(26):
        result = ''.join(chr(((ord(char) - ord('A' if char.isupper() else 'a') + i) % 26) + ord('A' if char.isupper() else 'a')) if char.isalpha() else char for char in string)
        results[i] = result
        
    return results

def print_rot13_results(results):
    for index, result in results.items():
        print(f"{index}: {result}")
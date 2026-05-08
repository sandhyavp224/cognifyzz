def reverse_string(s):
    return s[::-1]
if __name__ == "__main__":
    s = input("Enter a string to reverse: ")
    reversed_s = reverse_string(s)
    print(f"Reversed string: {reversed_s}")
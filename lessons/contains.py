"""An example of a list utility algorithm"""

# Name: contains
# Function with 2 parameters:
#   needle - what we are searching for
#   haystack - what were searching through
# Return type: bool
def contains(needle: str, haystack: list[str]) -> bool:
    # Start from first index
    i: int = 0
    # Loop through each index of list
    while i < len(haystack):
        #   Test if equal to needle
        if haystack[i] == needle:
            #     # Yes! Return true
            return True
        i += 1
    # Return false
    return False
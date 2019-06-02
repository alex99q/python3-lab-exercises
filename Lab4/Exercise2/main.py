from list_utilities import ListUtilities

input_list = ListUtilities(input("Type your words separated by space: ").split())

n = int(input("Longer than what number should the words be?: "))

print(*input_list.sift(n), sep=", ")
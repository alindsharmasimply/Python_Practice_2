def mutate_string(string, position, character):
    l = string[:position] + character + string[position + 1:]
    return l


print mutate_string(raw_input(), input(), raw_input())

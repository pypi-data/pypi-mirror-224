def pascal_to_kebab(pascal: str) -> str:
    kebab = [pascal[0].lower()]
    for char in pascal[1:]:
        if char.isupper():
            kebab.append("-")
        kebab.append(char.lower())

    return "".join(kebab)


def pascal_to_name(pascal: str) -> str:
    name = [pascal[0]]
    for char in pascal[1:]:
        if char.isupper():
            name.append(" ")
        name.append(char)
    return "".join(name)

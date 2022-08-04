def guesser(name, domain):
    name_parts = name.lower().split(' ')
    # print(name_parts)
    first_name = name_parts[0].strip()
    initial = first_name[0]
    last_name = name_parts[-1].strip()
    last_initial = last_name[0]

    emails = [(f"{first_name}.{last_name}@{domain}"), (f"{first_name}{last_name}@{domain}"),
              (f"{last_name}@{domain}"), (f"{first_name}@{domain}"),
              (f"{last_name}.{first_name}@{domain}"), (f"{last_name}{first_name}@{domain}")]

    if len(first_name) > 1:
        extension = ((f"{initial}.{last_name}@{domain}"), (f"{initial}{last_name}@{domain}"),
                     (f"{initial}{last_initial}@{domain}"), (f"{initial}.{last_initial}@{domain}"))
        emails.extend(extension)

    if len(name_parts) > 2:
        middle_name = name_parts[1].replace(".", "").strip()
        extension = ((f"{first_name}.{middle_name}.{last_name}@{domain}"),
                     (f"{first_name}{middle_name}{last_name}@{domain}"),
                     (f"{first_name}.{middle_name}@{domain}"),
                     (f"{first_name}{middle_name}@{domain}"),
                     (f"{initial}.{middle_name}.{last_name}@{domain}"),
                     (f"{initial}{middle_name}{last_name}@{domain}"),
                     (f"{middle_name}.{last_name}@{domain}"),
                     (f"{middle_name}{last_name}@{domain}"),
                     (f"{middle_name}.{first_name}@{domain}"),
                     (f"{middle_name}{first_name}@{domain}"))
        emails.extend(extension)
        if len(middle_name) > 1:
            middle_initial = middle_name[0]
            extension = ((f"{first_name}.{middle_initial}.{last_name}@{domain}"),
                         (f"{first_name}{middle_initial}{last_name}@{domain}"),
                         (f"{initial}.{middle_initial}.{last_name}@{domain}"),
                         (f"{initial}{middle_initial}{last_name}@{domain}"),
                         (f"{initial}{middle_initial}{last_initial}@{domain}"),
                         (f"{initial}.{middle_initial}.{last_initial}@{domain}"))
            emails.extend(extension)

    elif len(name_parts) > 3:
        middle_name = name_parts[1].replace(".", "").strip()
        middle_name_2 = name_parts[2].replace(".", "").strip()
        extension = ((f"{first_name}.{middle_name}.{middle_name_2}.{last_name}@{domain}"),
                     (f"{first_name}{middle_name}{middle_name_2}{last_name}@{domain}"),
                     (f"{first_name}.{middle_name_2}.{last_name}@{domain}"),
                     (f"{first_name}{middle_name_2}{last_name}@{domain}"),
                     (f"{first_name}.{middle_name}.{middle_name_2}@{domain}"),
                     (f"{first_name}{middle_name}{middle_name_2}@{domain}"),
                     (f"{initial}.{middle_name}.{middle_name_2}.{last_name}@{domain}"),
                     (f"{initial}{middle_name}{middle_name_2}{last_name}@{domain}"),
                     (f"{initial}.{middle_name}.{middle_name_2}@{domain}"),
                     (f"{initial}{middle_name}{middle_name_2}@{domain}"))

        emails.extend(extension)
        if len(middle_name) > 1 and len(middle_name_2) > 1:
            middle_initial = middle_name[0]
            middle_initial_2 = middle_name_2[0]
            extension = ((f"{first_name}.{middle_initial}.{middle_initial_2}.{last_name}@{domain}"),
                         (f"{first_name}{middle_initial}{middle_initial_2}{last_name}@{domain}"),
                         (f"{first_name}.{middle_initial_2}.{last_name}@{domain}"),
                         (f"{first_name}{middle_initial_2}{last_name}@{domain}"),
                         (f"{initial}.{middle_initial}.{middle_initial_2}.{last_name}@{domain}"),
                         (f"{initial}{middle_initial}{middle_initial_2}{last_name}@{domain}"),
                         (f"{initial}.{middle_initial_2}.{last_name}@{domain}"),
                         (f"{initial}{middle_initial_2}{last_name}@{domain}"),
                         (f"{initial}{middle_initial}{middle_initial_2}{last_initial}@{domain}"))
            emails.extend(extension)

    return emails
def get_formatted_name(first_name, last_name, middle_name = ''):
    """Returning formatted names."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"

    else:
        full_name = f"{first_name} {last_name}"
    
    return full_name

entreprenuer = get_formatted_name('naval', 'ravikant')
print(entreprenuer.title())

villian = get_formatted_name('sagar','jacky','alias')
print(villian.title())
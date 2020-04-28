# 11.1 & 11.2 - City, Countrys & Populations
def get_formatted_string(city_name, country_name, population=None):
    """Generate a neatly single string'City, Country' format"""
    if population:
        string = f"{city_name.title()}, {country_name.title()} - population {population}"
    else:
        string = f"{city_name.title()}, {country_name.title()}"
    return string
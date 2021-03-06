def transform(legacy_data):
    new_data = {}
    for key, value in legacy_data.items():
        for item in value:
            new_data[item.lower()] = key
    return new_data

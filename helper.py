# Define the region mapping
region_mapping = {
    'North': ['AC', 'AM', 'AP', 'RR', 'PA', 'RO', 'TO'],
    'Northeast': ['MA', 'PI', 'CE', 'RN', 'PB', 'SE', 'BA', 'PE', 'AL'],
    'Southeast': ['SP', 'RJ', 'MG', 'ES'],
    'South': ['PR', 'SC', 'RS'],
    'Midwest': ['MS', 'MT', 'GO', 'DF']
}

# Function to map states to regions


def map_region(state):
    for region, states in region_mapping.items():
        if state in states:
            return region
    return 'Unknown'  # In case the state is not found

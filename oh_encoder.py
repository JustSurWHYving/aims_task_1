def one_hot_encoder(data):
    
    unique_values = list(set(data))
    encoding = []

    for value in data:
        one_hot_encoded = [1 if value == category else 0 for category in unique_values]
        encoding.append(one_hot_encoded)

    return encoding

# Example usage:
# Assuming you have a list of categorical values
categories = ['A', 'B', 'A', 'C']

one_hot_encoded_data = one_hot_encoder(categories)
print(one_hot_encoded_data)
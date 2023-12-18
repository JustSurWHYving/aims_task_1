# code taken & understood from GPT 3.5

class OrdinalEncoder:
    def __init__(self, categories):
        """
        Initializes the ordinal encoder with the specified categories.

        Parameters:
        - categories: list of unique categorical labels in the desired order
        """
        self.categories = categories
        self.encoding_dict = {category: index for index, category in enumerate(categories)}

    def encode(self, data):
        """
        Encodes a list of categorical labels into ordered numerical values.

        Parameters:
        - data: list of categorical labels

        Returns:
        - list of encoded numerical values
        """
        return [self.encoding_dict[category] for category in data]

# Example usage:
# Assuming you have a list of categorical values and their ordinal order
categories = ['Low', 'Medium', 'High']

ordinal_encoder = OrdinalEncoder(categories)

# Encode the categorical values
categorical_values = ['Low', 'Medium', 'High', 'Low', 'High']
encoded_values = ordinal_encoder.encode(categorical_values)

print(encoded_values)

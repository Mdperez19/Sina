class DamerauLevenshteinDistance:
    def __init__(self, min_distance=0.5):
        self.min_distance = min_distance

    def calculate_normalized_levenshtein_distance(self, string_1: str, string_2: str) -> float:
        distance = self.calculate_distance_between_words(string_1, string_2)

        max_string_length = max(len(string_1), len(string_2))

        normalized_distance = float(max_string_length - distance) / float(max_string_length)

        if normalized_distance < self.min_distance:
            return -1

        return normalized_distance

    @staticmethod
    def calculate_distance_between_words(string_1: str, string_2: str) -> int:
        # Create an array of size (N+1) x (M+1), where N and M are the lengths of the strings
        matrix = {}
        n = len(string_1)
        m = len(string_2)

        # Initialize the first row and the first column with the values 0 to N and 0 to M
        for i in range(-1, n + 1):
            matrix[(i, -1)] = i + 1
        for j in range(-1, m + 1):
            matrix[(-1, j)] = j + 1

        # Fill the rest with the following formula
        for i in range(n):
            for j in range(m):
                # If the characters in positions i and j are the same, the cost is 0, otherwise it is 1
                if string_1[i] == string_2[j]:
                    cost = 0
                else:
                    cost = 1

                # Calculate the minimum of insertion, deletion, substitution and transposition operations
                matrix[(i, j)] = min(
                    matrix[(i - 1, j)] + 1,
                    matrix[(i, j - 1)] + 1,
                    matrix[(i - 1, j - 1)] + cost,
                )

                # Check transposition
                if i > 0 and j > 0 and string_1[i] == string_2[j - 1] and string_1[i - 1] == string_2[j]:
                    matrix[(i, j)] = min(
                        matrix[(i, j)],
                        matrix[(i - 2, j - 2)] + cost,
                    )

        distance = matrix[(n - 1, m - 1)]

        # Return the value of the bottom right cell, which is the edit distance
        return distance

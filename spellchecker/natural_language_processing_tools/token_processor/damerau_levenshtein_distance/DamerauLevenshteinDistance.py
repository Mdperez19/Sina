class DamerauLevenshteinDistance:
    def __init__(self, max_distance=4):
        self.max_distance = max_distance

    def calculate_distance_between_words(self, string_1: str, string_2: str) -> int:
        matrix = {}
        n = len(string_1)
        m = len(string_2)

        for i in range(-1, n + 1):
            matrix[(i, -1)] = i + 1
        for j in range(-1, m + 1):
            matrix[(-1, j)] = j + 1

        for i in range(n):
            for j in range(m):
                if string_1[i] == string_2[j]:
                    cost = 0
                else:
                    cost = 1

                matrix[(i, j)] = min(
                    matrix[(i - 1, j)] + 1,
                    matrix[(i, j - 1)] + 1,
                    matrix[(i - 1, j - 1)] + cost,
                )

                if i > 0 and j > 0 and string_1[i] == string_2[j - 1] and string_1[i - 1] == string_2[j]:
                    matrix[(i, j)] = min(
                        matrix[(i, j)],
                        matrix[(i - 2, j - 2)] + cost,
                    )

        distance = matrix[(n - 1, m - 1)]

        return distance if distance < self.max_distance else -1

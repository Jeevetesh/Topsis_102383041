# import pandas as pd
# import numpy as np
# import sys
# import os

# class DecisionAnalyzer:
#     def __init__(self, file_path):
#         """Load the input file and initialize the decision matrix."""
#         if not os.path.isfile(file_path):
#             print("Error: File not found.")
#             sys.exit(1)

#         if file_path.endswith('.csv'):
#             self.data = pd.read_csv(file_path)
#         elif file_path.endswith('.xlsx'):
#             self.data = pd.read_excel(file_path)
#         else:
#             print("Error: Unsupported file format. Please use CSV or XLSX.")
#             sys.exit(1)

#         # Validate data structure
#         if self.data.shape[1] < 3:
#             print("Error: Input file must have at least three columns.")
#             sys.exit(1)

#         self.decision_matrix = self.data.iloc[:, 1:].to_numpy()
#         self.num_criteria = self.decision_matrix.shape[1]
#         self.num_alternatives = self.decision_matrix.shape[0]

#     def calculate_scores(self, criteria_weights, criteria_impacts):
#         """Compute TOPSIS scores and ranks."""
#         if len(criteria_weights) != self.num_criteria or len(criteria_impacts) != self.num_criteria:
#             print("Error: Number of weights and impacts must match the number of criteria.")
#             sys.exit(1)

#         # Normalize decision matrix
#         normalized_matrix = self.decision_matrix / np.sqrt(np.sum(self.decision_matrix**2, axis=0))

#         # Apply weights
#         weighted_matrix = normalized_matrix * criteria_weights

#         # Determine ideal best and worst
#         ideal_best = [np.max(weighted_matrix[:, i]) if criteria_impacts[i] == '+' else np.min(weighted_matrix[:, i]) for i in range(self.num_criteria)]
#         ideal_worst = [np.min(weighted_matrix[:, i]) if criteria_impacts[i] == '+' else np.max(weighted_matrix[:, i]) for i in range(self.num_criteria)]

#         # Compute distances to ideal best and worst
#         distance_to_best = np.sqrt(np.sum((weighted_matrix - ideal_best)**2, axis=1))
#         distance_to_worst = np.sqrt(np.sum((weighted_matrix - ideal_worst)**2, axis=1))

#         # Calculate scores
#         scores = distance_to_worst / (distance_to_best + distance_to_worst)

#         # Append scores and ranks to data
#         self.data['Topsis Score'] = scores
#         self.data['Rank'] = scores.argsort()[::-1] + 1

#         return self.data


# def main():
#     if len(sys.argv) != 5:
#         print("Usage: python <script_name.py> <input_file> <weights> <impacts> <output_file>")
#         sys.exit(1)

#     input_file = sys.argv[1]
#     weights = list(map(float, sys.argv[2].split(',')))
#     impacts = sys.argv[3].split(',')
#     output_file = sys.argv[4]

#     if len(weights) != len(impacts):
#         print("Error: Weights and impacts must have the same number of elements.")
#         sys.exit(1)

#     analyzer = DecisionAnalyzer(input_file)
#     result = analyzer.calculate_scores(weights, impacts)

#     if output_file.endswith('.csv'):
#         result.to_csv(output_file, index=False)
#     elif output_file.endswith('.xlsx'):
#         result.to_excel(output_file, index=False)
#     else:
#         print("Error: Unsupported output file format. Use CSV or XLSX.")
#         sys.exit(1)

#     print(f"Results successfully saved to {output_file}")


# if __name__ == "__main__":
#     main()

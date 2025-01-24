# Topsis_102383041
# TOPSIS Assignment

This repository contains the implementation of the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** method for multi-criteria decision making (MCDM). The project uses a dataset to rank alternatives based on multiple criteria.

## Files

1. **102383041-data.xlsx**: The dataset used for the TOPSIS analysis.
2. **102383041.py**: The Python script that implements the TOPSIS method and ranks the alternatives.
3. **102383041-result.csv**: The output file containing the rankings and performance scores for each alternative.
4. **README.md**: This file.
5. **setup.py**: Contains the setup script for packaging and distributing the project.

## Steps to Execute

1. **Install Required Libraries**:
   Ensure you have the necessary libraries installed:
   ```bash
   pip install pandas numpy openpyxl
   ```

2. **Run the Script**:
   Execute the script `102383041.py` to perform the following tasks:
   - Load the dataset from the `102383041-data.xlsx` file.
   - Apply the TOPSIS method.
   - Generate rankings based on the calculated scores.
   - Save the results to `102383041-result.csv`.

   ```bash
   python 102383041.py <input_file> <weights> <impacts>
   ```

   Example:
   ```bash
   python 102383041.py 102383041-data.xlsx "1,2,3,4" "+,+,-,+"
   ```
   - `<input_file>`: The Excel file containing the dataset.
   - `<weights>`: Comma-separated weights for the criteria.
   - `<impacts>`: Comma-separated impacts for the criteria (`+` for beneficial, `-` for non-beneficial).

3. **Analyze the Results**:
   - View `102383041-result.csv` for the rankings and performance scores.
   - Check which alternative ranks highest and why.

## Results Summary

- The TOPSIS method calculates scores for each alternative and ranks them based on their closeness to the ideal solution.
- The generated `102383041-result.csv` contains the rankings and provides insights into the best alternative based on given criteria, weights, and impacts.

## Key Functions and Libraries Used

- **pandas**: For data manipulation and analysis.
- **numpy**: For mathematical operations and normalization.
- **openpyxl**: For reading Excel files.

## Notes

- Ensure the dataset file (`102383041-data.xlsx`) is properly formatted with numeric values for all criteria.
- Verify the weights and impacts provided as inputs match the number of criteria in the dataset.
- Modify the paths in the script if necessary to match your file structure.

## Contact

If you have any questions or need further assistance, feel free to reach out.

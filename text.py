# import pandas as pd
# import numpy as np

# # Load Excel file and parse relevant sheets
# file_path = 'CORO 29-07-25.xlsx'  # Update path if needed
# xls = pd.ExcelFile(file_path)

# # Read PAYMENT and Purchase sheets, skipping header metadata rows
# payment_df = xls.parse('PAYMENT', skiprows=3)
# purchase_df = xls.parse('Purchase', skiprows=3)

# # Rename columns for easier handling
# payment_df.columns = ['Date', 'Vch_Type', 'Vch_No', 'Debit']
# purchase_df.columns = ['Date', 'Vch_Type', 'Vch_No', 'Credit']

# # Drop rows with missing Debit or Credit values
# payment_df = payment_df.dropna(subset=['Debit']).reset_index(drop=True)
# purchase_df = purchase_df.dropna(subset=['Credit']).reset_index(drop=True)

# # Initialize index pointers and result list
# payment_index = 0
# purchase_index = 0
# output_rows = []

# # Iterate through the debit and credit entries
# while payment_index < len(payment_df) and purchase_index < len(purchase_df):
#     debit_row = payment_df.loc[payment_index]
#     credit_row = purchase_df.loc[purchase_index]

#     debit_amt = debit_row['Debit']
#     credit_amt = credit_row['Credit']

#     if np.isclose(debit_amt, credit_amt):  # Equal
#         output_rows.append({
#             'Payment_Vch_No': debit_row['Vch_No'],
#             'Purchase_Vch_No': credit_row['Vch_No'],
#             'Matched_Amount': debit_amt
#         })
#         payment_index += 1
#         purchase_index += 1

#     elif debit_amt > credit_amt:  # type: ignore # Debit is larger
#         output_rows.append({
#             'Payment_Vch_No': debit_row['Vch_No'],
#             'Purchase_Vch_No': credit_row['Vch_No'],
#             'Matched_Amount': credit_amt
#         })
#         # Reduce debit for next iteration
#         payment_df.at[payment_index, 'Debit'] -= credit_amt
#         purchase_index += 1

#     else:  # Credit is larger
#         output_rows.append({
#             'Payment_Vch_No': debit_row['Vch_No'],
#             'Purchase_Vch_No': credit_row['Vch_No'],
#             'Matched_Amount': debit_amt
#         })
#         # Reduce credit for next iteration
#         purchase_df.at[purchase_index, 'Credit'] -= debit_amt
#         payment_index += 1

# # Convert result to DataFrame
# output_df = pd.DataFrame(output_rows)

# # Save to Excel
# output_df.to_excel('matched_output.xlsx', index=False)
# print("Comparison complete. Output saved to 'matched_output.xlsx'")





import pandas as pd
import numpy as np

# Load Excel file and parse relevant sheets
file_path = 'CORO 29-07-25.xlsx'  # Adjust if needed
xls = pd.ExcelFile(file_path)

# Read and clean the PAYMENT and Purchase sheets
payment_df = xls.parse('PAYMENT', skiprows=3)
purchase_df = xls.parse('Purchase', skiprows=3)

# Rename columns
payment_df.columns = ['Payment_Date', 'Vch_Type', 'Payment_Vch_No', 'Debit']
purchase_df.columns = ['Purchase_Date', 'Vch_Type', 'Purchase_Vch_No', 'Credit']

# Drop rows with missing values
payment_df = payment_df.dropna(subset=['Debit']).reset_index(drop=True)
purchase_df = purchase_df.dropna(subset=['Credit']).reset_index(drop=True)

# Initialize tracking variables
payment_index = 0
purchase_index = 0
output_rows = []

# Match debit and credit amounts
while payment_index < len(payment_df) and purchase_index < len(purchase_df):
    debit_row = payment_df.loc[payment_index]
    credit_row = purchase_df.loc[purchase_index]

    debit_amt = debit_row['Debit']
    credit_amt = credit_row['Credit']

    if np.isclose(debit_amt, credit_amt):  # Equal amounts
        output_rows.append({
            'Payment_Date': debit_row['Payment_Date'],
            'Purchase_Date': credit_row['Purchase_Date'],
            'Payment_Vch_No': debit_row['Payment_Vch_No'],
            'Purchase_Vch_No': credit_row['Purchase_Vch_No'],
            'Matched_Amount': debit_amt,
            'Remaining_Amount': 0
        })
        payment_index += 1
        purchase_index += 1

    elif debit_amt > credit_amt:  # Debit is larger
        output_rows.append({
            'Payment_Date': debit_row['Payment_Date'],
            'Purchase_Date': credit_row['Purchase_Date'],
            'Payment_Vch_No': debit_row['Payment_Vch_No'],
            'Purchase_Vch_No': credit_row['Purchase_Vch_No'],
            'Matched_Amount': credit_amt,
            'Remaining_Amount': debit_amt - credit_amt
        })
        payment_df.at[payment_index, 'Debit'] -= credit_amt
        purchase_index += 1

    else:  # Credit is larger
        output_rows.append({
            'Payment_Date': debit_row['Payment_Date'],
            'Purchase_Date': credit_row['Purchase_Date'],
            'Payment_Vch_No': debit_row['Payment_Vch_No'],
            'Purchase_Vch_No': credit_row['Purchase_Vch_No'],
            'Matched_Amount': debit_amt,
            'Remaining_Amount': credit_amt - debit_amt
        })
        purchase_df.at[purchase_index, 'Credit'] -= debit_amt
        payment_index += 1

# Final output
output_df = pd.DataFrame(output_rows)

# Save to Excel
output_df.to_excel('matched_output_with_dates.xlsx', index=False)
print("Comparison complete. Output saved to 'matched_output_with_dates.xlsx'")



# import pandas as pd
# import numpy as np

# # Load Excel file and parse relevant sheets
# file_path = 'CORO 29-07-25.xlsx'  # file name should be here 
# xls = pd.ExcelFile(file_path)

# # Read and clean the PAYMENT and Purchase sheets
# payment_df = xls.parse('PAYMENT', skiprows=3)
# purchase_df = xls.parse('Purchase', skiprows=3)

# # Rename columns clearly
# payment_df.columns = ['Payment_Date', 'Payment_Vch_Type', 'Payment_Vch_No', 'Debit']
# purchase_df.columns = ['Purchase_Date', 'Purchase_Vch_Type', 'Purchase_Vch_No', 'Credit']

# # Drop rows with missing values
# payment_df = payment_df.dropna(subset=['Debit']).reset_index(drop=True)
# purchase_df = purchase_df.dropna(subset=['Credit']).reset_index(drop=True)

# # Initialize tracking variables
# payment_index = 0
# purchase_index = 0
# output_rows = []

# # Iterate through payment and purchase
# while payment_index < len(payment_df) and purchase_index < len(purchase_df):
#     debit_row = payment_df.loc[payment_index]
#     credit_row = purchase_df.loc[purchase_index]

#     debit_amt = debit_row['Debit']
#     credit_amt = credit_row['Credit']

#     if np.isclose(debit_amt, credit_amt):  # Equal
#         matched_amt = debit_amt
#         remaining_amt = 0
#         payment_index += 1
#         purchase_index += 1

#     elif debit_amt > credit_amt:  # Debit larger
#         matched_amt = credit_amt
#         remaining_amt = debit_amt - credit_amt
#         payment_df.at[payment_index, 'Debit'] -= credit_amt
#         purchase_index += 1

#     else:  # Credit larger
#         matched_amt = debit_amt
#         remaining_amt = credit_amt - debit_amt
#         purchase_df.at[purchase_index, 'Credit'] -= debit_amt
#         payment_index += 1

#     # Combine full rows with required structure
#     output_rows.append({
#         # Purchase details
#         'Purchase_Date': credit_row['Purchase_Date'],
#         'Purchase_Vch_Type': credit_row['Purchase_Vch_Type'],
#         'Purchase_Vch_No': credit_row['Purchase_Vch_No'],
#         'Credit': credit_amt,
#         # Payment details
#         'Payment_Date': debit_row['Payment_Date'],
#         'Payment_Vch_Type': debit_row['Payment_Vch_Type'],
#         'Payment_Vch_No': debit_row['Payment_Vch_No'],
#         'Debit': debit_amt,
#         # Match details
#         'Matched_Amount': matched_amt,
#         'Remaining_Amount': remaining_amt
#     })

# # Convert to DataFrame
# output_df = pd.DataFrame(output_rows)

# # Save to Excel
# output_df.to_excel('final_matched_output.xlsx', index=False)
# print("Done: Output saved as 'final_matched_output.xlsx'")

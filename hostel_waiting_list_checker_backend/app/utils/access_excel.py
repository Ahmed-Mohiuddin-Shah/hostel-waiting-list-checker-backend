from fastapi import HTTPException
import numpy as np
import pandas as pd

def get_excel_data(excel_file_path: str):
    try:
        # Read the Excel file in real-time
        sheets = pd.read_excel(excel_file_path, sheet_name=None)
        combined_sheets_df = pd.concat(sheets.values(), ignore_index=True)
        combined_sheets_df = combined_sheets_df.where(pd.notnull(combined_sheets_df), None)
        combined_sheets_df.replace([np.inf, -np.inf], None, inplace=True)

        # Convert the DataFrame to a dictionary format to return as JSON
        data = combined_sheets_df.to_dict(orient="records")
        return data

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading Excel file: {e}")

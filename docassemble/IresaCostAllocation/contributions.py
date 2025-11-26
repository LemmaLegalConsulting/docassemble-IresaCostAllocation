import pandas as pd
import re

def calculate_cost(costs_file, income, order):
    df = pd.read_csv(costs_file, dtype=str)
    order = str(order)

    income_index = -1
    for idx, row in df.iterrows():
        range_str = row['income']
        
        numbers = [float(n) for n in re.findall(r'(\d+\.?\d*)', range_str)]
        
        if len(numbers) == 2:
            if numbers[0] <= income <= numbers[1]:
                income_index = idx
                break
        elif len(numbers) == 1: 
            if income >= numbers[0]:
                income_index = idx
    
    if income_index == -1 and not df.empty:
        last_row_idx = len(df) - 1
        last_row = df.iloc[last_row_idx]
        
        range_str = last_row['income']
        numbers = [float(n) for n in re.findall(r'(\d+\.?\d*)', str(range_str))] 
        if len(numbers) == 2 and income > numbers[1]:
            income_index = last_row_idx
        elif len(numbers) == 1 and income >= numbers[0]: 
            income_index = last_row_idx


    if income_index == -1:
        return {}

    if order not in df.columns:
        return {}

    results = {}
    for i in range(3):
        lookup_idx = income_index - i
        if lookup_idx >= 0:
            row_data = df.iloc[lookup_idx]
            results[f'level_{i}'] = float(row_data[order])
        else:
            results[f'level_{i}'] = 0.0
            
    return results
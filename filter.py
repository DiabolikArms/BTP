import pandas as pd
import json

# Function to load data from CSV file
def load_csv(file_path):
    df = pd.read_csv(file_path)
    return df

# Function to load data from Excel (.xls) file
def load_xls(file_path):
    df = pd.read_excel(file_path, engine='xlrd')
    return df

# Function to load data from JSON file
def load_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data 

# Function to save data to JSON file
def save_to_json(data, output_file):
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)

# Function to save data to CSV file
def save_to_csv(df, output_file):
    df.to_csv(output_file, index=False)

# Function to save data to Excel (.xls or .xlsx) file
def save_to_excel(df, output_file):
    df.to_excel(output_file, index=False, engine='openpyxl')


# # Function to filter the JSON data based on a specific column value
# def filter_json_data(data, column_name, value):
#     filtered_data = []

#     for comment in data:
#         if str(comment.get(column_name, '')).lower() == str(value).lower():
#             filtered_data.append(comment)
    
#     return filtered_data

def filter_json_data(data, column_name, value):
    filtered_data = []

    # Helper function to search within replies
    def search_in_replies(replies, column_name, value):
        for reply in replies:
            if column_name in reply and str(reply.get(column_name, '')).lower() == str(value).lower():
                return True
        return False

    # Helper function to search within comments
    def search_in_comments(comments, column_name, value):
        for comment in comments:
            # Check if column exists and matches the value
            if column_name in comment and str(comment.get(column_name, '')).lower() == str(value).lower():
                return True
            # Check within replies
            if 'replies' in comment and search_in_replies(comment['replies'], column_name, value):
                return True
        return False

    # Main loop to search within articles
    for article in data:
        # Check at the article level
        if column_name in article and str(article.get(column_name, '')).lower() == str(value).lower():
            filtered_data.append(article)
        # Check within comments
        elif 'comments' in article and search_in_comments(article['comments'], column_name, value):
            filtered_data.append(article)

    return filtered_data


# Function to filter DataFrame based on a specific column value
def filter_by_column_value(df, column_name, value):
    return df[df[column_name] == value]

if __name__ == "__main__":
    # Load data
    file_type = 'json'  # Either 'csv', 'excel', or 'json'
    file_path = 'Result_4/times_of_india_comments.json' 

    # Load the file 
    if file_type == 'csv':
        df = load_csv(file_path)
    elif file_type == 'excel':
        df = load_xls(file_path)
    elif file_type == 'json':
        data = load_json(file_path)
    else:
        raise ValueError("Unsupported file type")

    # Prompt user input for filtering
    column_name = input("Enter the column name you want to filter by: ")
    value = input(f"Enter the value for {column_name} to filter: ")

    # Apply the filter
    if file_type == 'json':
        filtered_data = filter_json_data(data, column_name, value)
    else:
        filtered_df = filter_by_column_value(df, column_name, value)
        filtered_data = filtered_df.to_dict(orient='records')  # Convert DataFrame back to list of dictionaries

    
    if file_type == 'json':
        print(filtered_data[:5])
    else:
        print(filtered_df.head())

    output_type = 'json'
    base_output_file = 'filtered_output'

    if output_type == 'json':
        output_file = f"{base_output_file}.json"
        save_to_json(filtered_data, output_file)
    elif output_type == 'csv':
        output_file = f"{base_output_file}.csv"
        save_to_csv(filtered_df, output_file)
    elif output_type == 'xls' or output_type == 'xlsx':
        output_file = f"{base_output_file}.xlsx" 
        save_to_excel(filtered_df, output_file)
    else:
        raise ValueError("Unsupported output type")

    print(f"Filtered data saved to {output_file}")

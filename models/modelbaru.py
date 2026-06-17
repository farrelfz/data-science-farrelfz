import pandas as pd
import os
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def get_data_with_membership():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, '../data/Ecommerce_Customers.csv')
    df = pd.read_csv(csv_path)

    # Menambahkan kolom Membership_Group menggunakan qcut
    df['Membership_Group'], bins = pd.qcut(
        df['Length of Membership'],
        q=4,
        labels=['New', 'Developing', 'Loyal', 'VIP'],
        retbins=True
    )
    return df, bins

def get_membership_ranges(bins):
    range_df = pd.DataFrame({
        'Group': ['New', 'Developing', 'Loyal', 'VIP'],
        'Min Membership (Years)': bins[:-1],
        'Max Membership (Years)': bins[1:]
    })
    return range_df

def train_prediction_model():
    df, _ = get_data_with_membership()
    
    # Fitur yang digunakan
    X = df[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']]
    y = df['Yearly Amount Spent']
    
    # Inisialisasi model
    model = LinearRegression()
    model.fit(X, y)
    
    return model

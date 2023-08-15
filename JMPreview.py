import streamlit as st
import pandas as pd

excel_file = 'Database.xlsx'
df = pd.read_excel(excel_file)

# Filter data based on selected category
def filter_by_category(category):
    if category == "All":
        return df
    return df[df['Category'] == category]

def main():
    st.title("JM Merch Display Tool")

    # Dropdown for selecting category
    categories = ["All"] + df['Category'].unique().tolist()
    selected_category = st.selectbox("Select Category", categories)

    filtered_df = filter_by_category(selected_category)

    for index, row in filtered_df.iterrows():
        st.write(f"#### {row['Prod_Name']}")
        st.image(row['Prod_Image'], use_column_width=200)
        st.write(f"##### Price: Rs.{row['Prod_Price']}")
        st.write(f"Price: <span style='text-decoration: line-through;'>Rs.{row['MRP']}</span>", unsafe_allow_html=True)


if __name__ == '__main__':
    main()

import numpy as np
def print_dataframe(processed_df):

    print(processed_df.values)
    non_numeric_cols = processed_df.select_dtypes(include=['object']).columns
    print(non_numeric_cols)
    for col in non_numeric_cols:
        print(f"Unique values in {col}:", processed_df[col].unique())
    print("DF Types")
    print(processed_df.dtypes)
    print("DF Info")
    print(processed_df.info())
    print("DF Summary")
    print(processed_df.describe(include='all'))
    print("DF Is Null")
    print(processed_df.isnull().sum())
    print("Check for INF")
    print(processed_df.isin([np.inf, -np.inf]).sum())
    print("check for mixted type_cols")
    #pd.set_option('display.max_columns', None)  # None means unlimited
    mixed_type_cols = processed_df.applymap(type).nunique() > 1
    print(mixed_type_cols)
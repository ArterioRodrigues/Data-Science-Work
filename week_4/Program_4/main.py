import pandas as pd


license_df = pd.read_csv("../data/license.csv")
zipcode_df = pd.read_csv("../data/zipcode.csv")




license_df["AnimalName"] = license_df["AnimalName"].apply(lambda name: str(name).capitalize())
license_df = license_df.drop(['LicenseExpiredDate', 'Extract Year'], axis = 1)

zipcode_df = zipcode_df.rename(columns = {"zip": "ZipCode"})


new_df = pd.merge(license_df, zipcode_df, how='left', on='ZipCode')

print(license_df.head())
print(new_df.head())
#
#
#new_df = new_df.dropna()
#
#print(new_df)

##################################

#bite_df = pd.read_csv("../data/dog_bite.csv")
#print(bite_df.head())
#bite_df = bite_df.drop(['Species'], axis = 1)
#
#print(bite_df.head())


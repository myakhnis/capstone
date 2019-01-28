import pandas as pd
import os
import sqlalchemy as sqa


def main(sourcefile): 
    
    # extract data from source
    data = extract(sourcefile)

    # apply any needed transformations
    data = transform(data)

    # load into MySQL
    db = load(data)

def extract(sourcefile):
    # split filepath into root and name
    root, name = os.path.split(sourcefile)

    # split name into base and extension
    base, ext = os.path.splitext(name)

    print(ext)

    if ext == ".csv":
        data = pd.read_csv(sourcefile)
    
    print(data.head())
    
    return data

def transform(data):
    return data

def load(data):
    # connect to the database
    engine = sqa.create_engine('mysql://scott:tiger@localhost/foo', echo=True)

    return engine

if __name__ == "__main__":
    main("nvda.csv")




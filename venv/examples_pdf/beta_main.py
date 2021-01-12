import os 
from PyPDF2 import PdfFileReader as pdf_reader
import pandas as pd

mList = os.listdir()
#print(mList)

df = pd.DataFrame(mList, columns=["books"])

#print(df)
#print(df["books"][2])

#df["pages"] = []

df["pages"] = df["books"].apply(lambda x: pdf_reader(x).getNumpages())


import tabula
import camelot
from pdfrw import PdfReader
import pandas as pd
import xlsxwriter
import re

## Importing PDF
file = "Data\DBS_P3Q42020.pdf"

## Get number of pages
num_pages = len(PdfReader(file).pages)

## Function to clean camelot table_c
def split_newline(df_c):
    for k in range(len(df_c)):
        if "\n" in df_c[0].iloc[k]:
            text = df_c[0].iloc[k].split("\n")
            for z in range(len(text)):
                df_c.at[k,z] =  text[z]
    return df_c

def remove_spaces(df_c):
    for i in range(len(df_c)):
        for col in df_c.columns[2:]:
            text = df_c[col].iloc[i]

            if text.count(' ')>1:
                text = ''.join(e for e in text if e.isalnum())
                df_c.at[i,col] = text
    return df_c


with pd.ExcelWriter('test_dbs.xlsx', engine='xlsxwriter') as writer:
    for i in range(1,num_pages+1):
        try:
            table_t = tabula.read_pdf(file,pages=i,multiple_tables=True,stream=True)
            table_c = camelot.read_pdf(file, pages=str(i))

            if len(table_c) > 0:

                df = pd.DataFrame()
                for j in range(len(table_c)):
                    df_c = table_c[j].df

                    ## Run through the first column to assess if there is '\n'
                    df = df.append(remove_spaces(split_newline(df_c)))
                    print("Page "+ str(i) + " using Camelot")
                    df.to_excel(writer,sheet_name = "Page "+str(i), index=False, header=False)

            elif len(table_t) > 0:
                df = table_t[0]
                print("Page "+ str(i) + " using Tabula")
                df.to_excel(writer,sheet_name = "Page "+str(i), index=False, header=False)

        except AttributeError:
            pass


# table_c = camelot.read_pdf(file, pages="76")
# df = table_c[0].df
# df_c = split_newline(df)
#
# for i in range(len(df_c)):
#     for col in df_c.columns[2:]:
#         text = df_c[col].iloc[i]
#
#         if text.count(' ')>1:
#             text = ''.join(e for e in text if e.isalnum())
#             df_c.at[i,col] = text
#
# print(df_c)

#
#
# for i in range(len(df)):
#     for col in df.columns:
#         text = df[col].iloc[i]
#
#         if "\n" in text:
#             text = df[col].iloc[i].split("\n")
#             for j in range(len(text)):
#                 df.at[i,j] =  text[j]
#         elif text.count(' ')>1:
#             text = ''.join(e for e in text if e.isalnum())
#             df.at[i,col] = text


#
# table_t = tabula.read_pdf(file,pages=35,multiple_tables=True,stream=True, guess=True)
# print(len(table_t))
# print(table_t[0])
# print(type(table_t[0]))
#df.to_csv('foo.csv', index=False, header=False)

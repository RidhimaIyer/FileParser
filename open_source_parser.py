import pandas as pd 
from datetime import date, datetime
import logging 
import os 

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)
basedir = os.path.abspath(os.path.dirname(__name__))

def update_lc_amt(elem):
    '''updates lc_amount to remove "," in data and adjust integer sign'''
    try:
        elem = elem.replace(",", "")
        if "-" in elem: 
            val = "-" + elem[:-1]
            return val 
        else:
            return elem
    except Exception as e:
        logging.info("Error updating LC amount during file parsing")

def parse_file(input_file, output_file):
    ''' parses input_file and writes clean data to output_file. Uses pandas to do the parsing'''
    try:
        print("here")
        logging.info(f"Starting file parsing. InputFile Provided: {input_file}")
        df = pd.read_csv(input_file, delimiter="~", names=["temp"])
        header = df[df["temp"].str.contains("Stat") == True].head(1)
        df = df[df["temp"].str.contains("\|") & ~df["temp"].str.contains("\|-") & ~df["temp"].str.contains("Stat")]
        df = pd.concat([header, df])
        df_parsed = df["temp"].str.split("|", expand=True).apply(lambda x: [element.strip() for element in x])
        df_parsed = pd.DataFrame(df_parsed.values[1:], columns=df_parsed.iloc[0])
        df_parsed.drop([""],axis=1, inplace=True)
        df_parsed["LC amnt"] = df_parsed["LC amnt"].apply(update_lc_amt)
        df_parsed.to_csv(output_file, index=False, sep=";")
        logging.info(f"Outfile generated with cleaned data. Outfile: {output_file}")
    except Exception as e:
        logging.info("Error parsing file")
   

if __name__ == "__main__":
    try:
        input_file = str(basedir) + "/forParsing_task.xls"
        output_file = str(basedir) + "/cleanedOutput.csv"
        start_time = datetime.now()
        parse_file(input_file, output_file)
        print(f"Took time: {datetime.now() - start_time}")
    except Exception as e:
        logging.info("Error parsing file")
    

# Took time: 0:00:00.117820


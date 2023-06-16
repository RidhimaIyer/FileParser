
import pandas as pd 
import re
from datetime import datetime
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

def get_col_val(line, index, delimiter="|"):
    '''Takes file line as input and returns column value based on index and delimiter'''
    try:
        start = get_col_index(line,delimiter,  index)
        end = get_col_index(line,delimiter, index+1)
        return line[start+1:end], start+1, end+1
    except Exception as e:
        logging.info("Error getting col val from file line")

def get_col_index(line, delimiter, occurance):
    ''' Takes file line as input and returns delimiter index based on number of occurance(i.e col index)'''
    try:
        if (occurance == 1):
            return line.find(delimiter)
        else:
            return line.find(delimiter, get_col_index(line, delimiter, occurance - 1) + 1)
    except Exception as e:
        logging.info("Error getting delimiter index based on occurance")
    

def parse_line(line, input_delimiter="|", output_delimiter=";"):
    '''Parses each line to remove spaces before and after delimiter and replace pipe(|) delimeter to semicolor(;) as required'''
    try:
        parsedline = re.sub(r'(?:(?<=\|)\s*|\s*(?=\|))','', line)
        parsedline = parsedline[1:-1]
        parsedline = parsedline.replace(input_delimiter, output_delimiter)
        parsedline += "\n"
        return parsedline
    except Exception as e:
        logging.info("Error parsing line")

def parse_file(header_list, input_file, output_file):
    '''Parses input file and writes clean data in outfile. For each file line parses the format, adjusts lc_amt and writes to outfile'''
    try:
        logging.info(f"Starting file parsing. InputFile Provided: {input_file}")
        with open(input_file, "r") as file:
            lines = file.readlines()
            header = None 
            lc_amt_index = None
            with open(output_file, "w") as outfile:
                for line in lines:
                    if line.find(header_list[0]) != -1 and header==None:
                        header = parse_line(line, "|", ";")
                        outfile.write(header)
                        header = header.split(";")
                        lc_amt_index = header.index("LC amnt") 
                    if line.find(header_list[0]) == -1 and line.find("|-") and line.find("|") != -1:
                        line = parse_line(line, "|", ";")
                        lc_amt, start_idx, end_idx=get_col_val(line, lc_amt_index, delimiter=";" )
                        lc_amt = update_lc_amt(lc_amt)
                        line = line[:start_idx] + lc_amt + line[end_idx-1:]
                        outfile.write(line)
            logging.info(f"Outfile generated with cleaned data. Outfile: {output_file}")
    except Exception as e:
        logging.info("Error parsing file")


if __name__ == "__main__":
    try:
        start_time = datetime.now()
        input_file=str(basedir) + "/forParsing_task.xls"
        output_file=str(basedir) + "/cleanedVanillaOutput.csv"
        header = ["Stat",]
        parse_file(header, input_file, output_file)
        logging.info(f"Took time: {datetime.now() - start_time}")
    except Exception as e:
        logging.info("Error parsing file")
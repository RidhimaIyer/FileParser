# File Parser

## Open Source Parser

**Script Detail: This Script uses pandas library to parse input file provided and generate a cleaned outfile with structured data in a delimited format. Here delimiter used for outfile is ";".**

## Package Requirements:
    
    pipenv 
    pandas

## Usage
    1. Setup Virtual environment. This will create a new virtual environment and download all required packages 

        pipenv install 

    2. start the application 

        pipenv run python open_source_parser.py

    3. Input/Output file:

        Input Filename: forParsing_task.xls
        Filename: cleanedOutput.csv


# Vanilla Parser

**Script Details: This script uses vanilla in built python libraries to parse input file provided and generate a cleaned outfile with structured data in a delimited format. Here delimiter used for outfile is ";".**

## Package Requirements:
    
    pipenv 

## Usage
    1. Setup Virtual environment. 

        pipenv install 

    2. start the application 

        pipenv run python vanilla_parser.py 

        Note: Since it doesnt require any exteral package , we can also start it by using below statement 
        
        python vanilla_parser.py

    3. Input/Output file:

        Input Filename: forParsing_task.xls
        Filename: cleanedVanillaOutput.csv


## RunTime Comparison

Both scripts were run multiple times and it was observed vanilla script was always faster than the opensource script by few ms and thus goes to assume would perform better with larger files. 
For 1 such sample local run below timings were observed for opensource and vanilla scripts:

    OpenSource script timing: 0:00:00.018939
    Vanilla script timing: 0:00:00.011409

Note: Time can be observed as the logger output in each script run. 
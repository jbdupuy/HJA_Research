Hello! Welcome to the repo for the original data and python scripting related to research done in the HJA Andrews Experimental Forest associated with the paper: 
Lookingbill, T.R.; DuPuy, J.; Jacobs, E.; Gonzalez, M.; Kostadinov, T.S. A 20-Year Ecotone Study of Pacific Northwest Mountain Forest Vulnerability to Changing Snow Conditions. 
Land 2024, 13(4), 424. https://doi.org/10.3390/land13040424


Important things to keep in mind:
1) For any data-related questions, please feel free to reach out to Jack DuPuy (jack.dupuy@richmond.edu) or Todd Lookingbill (tlooking@richmond.edu).
2) The "HJA Hobo Mastersheet" contains information about each HOBO including coordinates, seedling type, and whether it was used for camera validation. 
3) A masterscript has been developed to reproduce our data for any HOBO csv file for any year. It can also be used to replicate our data analysis methods on external  HOBO data.
4) The script is called Snow_Statistics.py, and it can be found in the "Masterscript and Example Usage" folder. Sample data from 2022 has been provided along with the expected output if you run the script in that folder on your machine. Another output file demonstrates what it will do if ran inside the 2013 folder. 
5) To use the script yourself: place it inside the folder with the csvs that you want to analyze, navigate to that folder using your terminal, then type "python Snow_Statistics.py" and it should run. Thanks for visiting, feel free to reach out with questions!

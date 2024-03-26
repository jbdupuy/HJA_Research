Hello! Welcome to the repo for the HOBO data and python scripting related to research done in the HJA Andrews Experimental Forest by Todd R. Lookingbill, Jack DuPuy, Ellery Jacobs, Matteo Gonzalez, and Tihomir S. Kostadinov completed in 2022.

Important things to keep in mind:
1) As of now (2/22/2024), this repo represents a somewhat disorganized, raw version of scripts/data. This includes test print lines (commented out), a complicated hierarchical structure, and both .HOBO and .csv files for every data logger for every year.
2) The plan is to clean up the existing scripts/hierarchy and create a streamlined version of the scripts that can read any HOBO data and reproduce our metrics over the course of 2024. A new Readme will reflect these changes and how to use the new scripts when they are complete.
3) Beginning in 2020, some data loggers got off-track timewise: they still recorded every 6 hours but not directly at 3:00, 9:00, 15:00, and 21:00. This makes scripts/hierarchy from 2020-2022 especially cluttered/more challenging to interpret. A main goal of creating streamlined/standardized scripts is to eliminate some of these challenges for future use.
4) For now, I've included an example folder where you can see results for all 2022 HOBOs with a 00:36 start time, examine the scripts that created those results, and run the scripts yourself on 3 example HOBO csv files.
5) All scripts for different start times/years have the same format. Keep in mind that scripts present inside folders will only work on csv files inside those same folders.

If you have any questions, feel free to reach out to Jack DuPuy at jack.dupuy@richmond.edu. Thank you!

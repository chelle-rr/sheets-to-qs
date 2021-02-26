Use this script to turn spreadsheet data in this format to QuickStatements.
Currently, only for use with the following data types (no times or quantities, sorry!):
 * Strings (monolingual text, URLs, external identifiers)
 * Items

To use:
1.  Download the script and place the folder in a location convenient for you
2.  Prepare your spreadsheet (here's a sample)
    1. The first row (column headers) should contain properties
    2. The columns should match the order you'd like the statements to appear (with the exception of label, aliases, and description)
2. Export the sheet to .tsv and place in the same folder as the script
3. Open Terminal and change the directory to **folder** (type in *cd* then drag and drop the folder on the Terminal window)
4. Run the script (*python3 transform_create.py*)
5. Enter the name of your input file and desired output file name when prompted
6. Open your new output .tsv and check it out before use!
  

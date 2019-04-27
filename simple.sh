#!/bin/bash

# select filename using dialog
# store it to $FILE
FILE=$(dialog --title "Delete a file" --stdout --title "Please choose a file to delete" --fselect /tmp/ 14 48)

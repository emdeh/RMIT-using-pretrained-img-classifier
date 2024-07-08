#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: /emdeh
# DATE CREATED: 08/07/2024 (DD/MM/YYYY)                             
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Create empty dictionary for the results
    results_dic = dict()
    
    # Creates list of files in directory
    in_files = listdir(image_dir)

    # Iterate through each file in the directory
    for idx in range(0, len(in_files), 1):
      # Skip file if it starts with a dot
      if in_files[idx][0] != ".":
        # Split the file by underscore to get the pet label
        pet_label = in_files[idx].split("_")

        # Create an empty list to store valid words
        words_in_label = []

        # Iterate through each word in the pet label
        for word in pet_label:
          # Check if the word contains only alphabetic characters
          if word.isalpha():
            # Append the word to the list of valid words
            words_in_label.append(word)

        # Convert the list of valid words to lowercase and join them with a space
        pet_label = " ".join(words_in_label).lower().strip()

        # Add the pet label to the dictionary
        results_dic[in_files[idx]] = [pet_label]

    return results_dic

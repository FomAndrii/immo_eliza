## Immo_Eliza
**Repository:** challenge-collecting-data  
**Type of Challenge:** Consolidation  
**Duration:** 4 days  
**Deadline:** 15/11/2024 16:30  
**Team challenge:** Group  

## Table of Contents
1. [Project Description](#project-description)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Deliverables](#deliverables)
5. [Team](#team)

## Project Description
The real estate company "ImmoEliza" wants to create a Machine Learning model to make price predictions on real estate sales in Belgium.
In this project we need to build a dataset gathering information about at least 10.000 properties all over Belgium.
The structure (`scv` file) of dataset is:
- Locality
- Type of property (House/apartment)
- Subtype of property (Bungalow, Chalet, Mansion, ...)
- Price
- Type of sale (Exclusion of life sales)
- Number of rooms
- Living Area
- Fully equipped kitchen (Yes/No)
- Furnished (Yes/No)
- Open fire (Yes/No)
- Terrace (Yes/No)
  - If yes: Area
- Garden (Yes/No)
  - If yes: Area
- Surface of the land
- Surface area of the plot of land
- Number of facades
- Swimming pool (Yes/No)
- State of the building (New, to be renovated, ...)

### Must-have features
- Data all over Belgium.
- Minimum 10 000 inputs without duplicates
- No empty row. If you are missing information, set the value to `None`.
- The dataset must be clean. Try as much as possible to record only numerical values.
  **Example**: Instead of defining whether the kitchen is equipped using `"Yes"`, use binary values.

## Installation
### Project Directory Structure

```plaintext
immo-eliza/
├──  1.immo_eliza_scraping.md       # the main task  from BeCode
├── README.md                       # Project overview and instructions
├── ImmoLinks.txt                   # Sctript to scrape links of properties by excluding few types
├── PropertyData.csv                # Script to scrape property information from a test set of 100 links
├── PropertyDataScraper.py          # Script to scrape property information from a test set of 100 links
├── get_property_data.py            # Script to scrape property information from a test set of 100 links
├── get_property_links.py           # Script to scrape links of properties by excluding few types
├── subset_100properties.txt        # Script to scrape property information from a test set of 100 links

└── u.ipynb_checkpoints
    ├── fImmo-checkpoint.ipynb      # checkpoints file 
└── __pycache__
    ├── collecting_data_from_url_properties.cpython-312.pyc
└── new_env                         # folders and files for new env
└── web_drivers
    ├── chromedriver.exe            # driver file for chrome
```

# Installation
## Clone the repository (bash):

git clone https://github.com/FomAndrii/immo_eliza

## Usage

To start the program, run:
1) get_property_links.py - for scraping links of properties by excluding few types in ImmoLinks.txt
2) get_property_data_py - for accumulate dataset in PropertyData.csv

python main.py

Output: The seating arrangement will display in the console, indicating which colleagues have been assigned to each table and any remaining unoccupied seats.

## Deliverables
**Source Code**: Complete, functional Python code, organized according to the project structure.
**README**: A detailed README.md with installation and usage instructions, clear objectives, and a project summary.
**Branching Strategy**: The main branch contains only essential features. Additional features or updates are on separate branches and merged via pull requests.

## Contributors
List of team members:
SUNIL Dhanya (https://www.linkedin.com/in/dhanyasunil/)  
FOMICHOV Anfrii(https://www.linkedin.com/in/andrii-fomichov-73928642/)

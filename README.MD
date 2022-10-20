# LaTeX-Linter

![falken](https://github.com/FalkenDev/LaTeX-Linter/blob/main/linter.png?raw=true)

The linter ensures common stylistic and configurable rules for TeX files and, therefore, eases the discussion on, merging, and exchange of TeX content. The software is going to written in Python and used in terminal to terminate the tasks.

## Content
- [Download](#download)
- [Usage](#usage)
- [Platform](#platform)
- [Version](#version)
- [Contact](#contact)
- [License](#license)
## Download
### Docker
>
> Command line for run the program in terminal:
>
> docker run -it -v $(pwd)/***Your_input_map_here***:/latex-linter/input -v $(pwd)/***Your_output_map_here***:/latex-linter/output falkendev/latex-linter:1.0
>
> #### Info
> $(pwd) = returns the path to the map you are in
>
> * The first volume you put in the map with your TeX files you want to lint ( Change ***Your_input_map_here*** to your map ).
>
> * The second volume you put the map you whant to get your Linted TeX files in ( Change ***Your_output_map_here*** to your map ).


## Usage
> python3 main.py


***Python3 Version: Python 3.8.10***
### File
#### Press 1 in main menu in terminal


> 1 | Specific File - Enter which file u want to use from input folder. All the files that are displaying in terminal can be used.


> q | Go Back - Return to main menu.
### Settings
#### Press 2 in main menu in terminal


> 1 | Edit Customized settings - Choose which setting rule you want to change value of for customized settings.


> 2 | Change to Customized settings - Use Customized settings for the Linter.


> 2 | Change to Standard settings - Use Standard settings for the Linter.


> q | Go Back - Return to main menu.
### Linter
#### Press 3 in main menu in terminal


> Start linting the file with the specific settings


***!OPS! Needs atleast to choose which file to use in terminal for the linter to run !OPS!***
## Platform
## Version

- V1.0.0 - Sprint 1 - Added Menu, Settings and File class ( Unit tested )
- V2.0.0 - Sprint 2 - All the Linter Rules
- V3.0.0 - Sprint 3 - Everything is Unit tested, code improvments, and software can be used in Docker and downloadable at docker.hub

## Contact
Have any questions?


Reach me at:


<falkendev@gmail.com>


<https://www.twitch.tv/falkendev>
## License And Tools
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)

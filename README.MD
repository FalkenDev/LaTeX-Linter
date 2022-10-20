# LaTeX-Linter

![falken](https://github.com/FalkenDev/LaTeX-Linter/blob/main/linter.png?raw=true)

The linter ensures common stylistic and configurable rules for TeX files and, therefore, eases the discussion on, merging, and exchange of TeX content. The software is written in Python and used in terminal to terminate the tasks.

## Content
- [About](#about)
- [Download](#download)
- [Usage](#usage)
- [Version](#version)
- [Contact](#contact)
- [License](#license)
## About
A terminal based program that ensures common stylistic and configurable rules for TeX files.

Rules that check and fix TeX files:
* Intention (tabs or spaces) for environment blocks (e.g., \begin{itemize} … \end{itemize}; **( Can be configurable which environments blocks should be excluded )**
* Newline after a sentence for better git support **( Can be set to True or False )**
* Format comments (space after %) **( The space value is adjustable )**
* Blank lines before section, chapter, etc. **( The Blank lines value is adjustable )**


***Every rule can be customized in either settings.json or in terminal***
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

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)] https://www.python.org/)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)] https://www.docker.com/)
![Alpine Linux](https://img.shields.io/badge/Alpine_Linux-%230D597F.svg?style=for-the-badge&logo=alpine-linux&logoColor=white)] https://www.alpinelinux.org/)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)] https://git-scm.com/)
![LaTeX](https://img.shields.io/badge/latex-%23008080.svg?style=for-the-badge&logo=latex&logoColor=white)] https://www.latex-project.org/)

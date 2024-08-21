# IRD Bulk Searching Program

This is a python program made for the sole purpose of searching numerous pan numebers in the IRD database.


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With


* [![Python][Python-logo]][Python-url]

This program is entirely built out of python.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

These are the instructions on how you can get started on using the program.



## Setup

Install all the requirements of the program from file 'req.txt'. Also better to create a virtual environment.
```bash
python -m venv venv

.\venv\Scripts\activate
```
For installing requirements:
```py
pip install -r req.txt
```
   

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Usage
There are two parts to the program.
```
1. searching for details in IRD site 
2. performing a similarity test for all of the records.

first is done by a code ".\code_final.py"
second is performed by code ".\final list\matcher.py"
```
1. create a .csv file in excel (coma delimited)
 Where 1st column contains names and 2nd columns contains PAN numbers.
2. From VS code, copy the contents of that csv file to a file named ".\source.txt" and save it.
3. run the code ".\code_final.py" from venv. Perform instruction on the screen. 
5. When program finishes the loop, open the new file named "PAN_DETAILS_SEARCHED.csv" using excel and copy only the 2nd column and 4th column into a different csv file, ".\final list\compare_list.csv" comma delimited.
6. again from VS code, open that csv file and copy its contents into the similar file named "compare_list.txt"
7. run the code ".\final list\matcher.py" and obtain it's result in ".\final result\match_result.csv"

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch
3. Commit your Changes
4. Push to the Branch
5. Open a Pull Request


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[product-screenshot]: images/screenshot.png
[Python-logo]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
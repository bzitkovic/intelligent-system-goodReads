# Intelligent system for recommending books

## About The Project
The project is a system that recommends books for users based on their preferences entered into the system. Data is based on GoodReads data source. Also, it is necessary to meet some rules when recommending the book:
* The book must not be from a genre in which the user has no preferences
* The system must be able to offer an answer as to why it chose that particular book or books
* The system must be able to recommend more than one book to the user, if possible
* The book must be described in detail when offered to the user

The system also uses decision tree as a method for chosing the best books for the user.

### Built With
* [Python](https://www.python.org/)
* [Pandas](https://pandas.pydata.org/)
* [Sckit-Learn](https://scikit-learn.org/)

### Prerequisites

You will need pandas and sckit-learn libraries to run the program.
  ```sh
  pip install scikit-learn
  pip install pandas
  ```
  
### Installation

The following are the installation steps:

Clone the repo
   ```sh
   git clone https://github.com/bzitkovic/intelligent-system-goodReads.git
   ```
## Usage
You can run the program as:

First:
   ```sh
   python3 good_reads.py
   ```
   Or
   ```sh
   python good_reads.py
   ```
   
## License

Distributed under the GPL-3.0 License. See `LICENSE.txt` for more information.

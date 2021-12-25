# Sequence Searcher
Sequence searcher is a project that aims to empower search abilities and enable performing advanced and complex search queries on
    [The Online Encyclopedia of Integer Sequences (OEIS)](https://oeis.org/) database.
The OEIS database is searchable by keyword and by subsequence and this project provides more advanced options to search
    in the database (Not to be confused with the official [OEIS](https://oeis.org/) search engine).



# Search Queries
The search features are divided into the following sections:

### 1. Search without Order
It gives you the capability to search about a set of numbers in the sequence.
Also, you can specify a number of terms to dropped if they are not found in the sequence.  
* `1, 2, 3, 4`: Any sequence contains these four terms without considering order will match (E.g., A185577, 1, 5, 2, 1, 2, 7, 5, 1, 3, 8, 6, 4) 

### 2. Search with Keys 
###### Normal Search Considering Terms Order
* `1, 2, 3, 4`: Sequence contains these four terms in the same order anywhere in the sequence.
###### Question Mark
* `1, 5, ?1, 13, 20`: The third term could be any number (The question mark indicates any possible number).
* `1, 5, ?2, 13, 20`: The third term and the fourth one could be any number (2 means two terms).
* `1, 5, ?*, 13, 20`: Any possible set of numbers between the two sequences [1, 5] and [13, 20].
* `1, 5, ?*, 13, 20, ?3, 60, 70`: Any possible set of numbers between the two sequences [1, 5] and [13, 20], and three numbers between [13, 20] and [60, 70].
###### Range 
* `1, 5, ?1, 13, 20:23`: The third term could be any number, the fifth is between 20 and 23.
* `1:4, 5, ?1, 13, 20:30`: The first term could be 1, 2, 3 or 4. Also, The third term could be any number, the fifth is between 20 and 23.
Note: The search process will show results anywhere in the sequence, i.e. it is not limited to the beginning of the sequence. 


### 3. Fuzzy Matching 
This algorithm allows terms in the sequence to be off by one or two, and it would still match.
Also, the results will be ranked according to the number of the dropped terms. There are three types of fuzzy matching: 

#### Fuzzy Matching I 
In this type, one term can be dropped at a time from either the OEIS sequence or/and the input sequence. 
You can specify the number of terms that can be dropped. 

Example:
```
OEIS Sequence A40: 2, 3,    5, 7, 11,     13, 17, 19,     23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103
Input Sequence   : 2, 3, 4, 5, 7, 11, 11, 13, 17, 19, 21, 23, 29, 31,     41, 43, 47,     59, 61, 67, 71, 73, 79, 83, 89
Number of Terms Allowed For Drop: 7
Both Sequences will match. 
Rank = Number of Terms Allowed For Drop - The Number of Terms that had Been Dropped = 7 - 5 = 2.
```

#### Fuzzy Matching II
In this algorithm, more than one term can be dropped at a time from either the OEIS sequence or/and the input sequence. 
You can specify the number of terms that can be dropped and the maximum gap size that is allowed to be skipped while comparing the sequences.  

Note: If there is a terms skip in BOTH sequences, the smallest number of terms will be considered to be subtracted from the terms that are allowed to be dropped. For example:
```
Seq1: 1, 2, 3, 4, 5, 100, 101, 102, 6, 7, 8, 9, 10
Seq2: 1, 2, 3, 4, 5, 100, 101, 102, 103, 104, 6, 7, 8, 9, 10
Number of Terms Allowed For Drop: 6
Maximum Gap Size: 6
The number of terms that will be subtracted from the terms allowed to be dropped is 3 and not 5.
Rank = Number of Terms Allowed For Drop - The Number of Terms that had Been Dropped = 6 - 3 = 3.
```

#### Fuzzy Matching III 
In this method, any number of terms is allowed for dropping from the OEIS sequence, 
but a specific number of terms from the input sequence. 

In other words, this type can be used to check the existence of the input sequence terms in the same order in other 
sequences while allowing some terms to be off.

For example, it could be useful when the sequence is the terms of another sequence according to 
specific indexing rule (like, k^2 + k + 1) 
``` 
Input Sequence: 5, 41, 269, 1093, 3299, 7867, 16319
Number of terms allowed to be dropped: 0

The output will be A054553 and A122566 (Until Dec 25)
The input sequence is actually A122566(k^2 + k + 1)
```


### 4. Searching using Terms Lookup Formula
This method allows you to match sequences in the database to formula or terms with a variable
* `n / 10, n, n * 5, n ^ 2, 3*n+2`: These terms can match the following sequence `1, 10, 50, 100, 32`

The supported operations are:
1. Multiplication (*), Division (/), Addition (+), Subtraction (-) and Power (^).
2. Sin, Cos, Tan and Exp (e^number).
3. Round, fix or trunc, abs, floor and ceil.
4. Constants: PI and E.


### 5. Advanced Search Queries
1. Shift The Sequence with Constant and Search
2. Scale The Sequence with Constant and Search
3. Shift The Sequence with (N, N+1, N+2 ...) and Search
4. Scale The Sequence with (N, N+1, N+2 ...) and Search
5. Scale and Shift The Sequence with Constant and Search
6. Scale and Shift The Sequence with (N, N+1, N+2 ...) and Search
7. Search About Differences of Adjacent Terms 
8. Search About Summation of Adjacent Terms 
9. Search About Product of Adjacent Terms 
10. Shift with Primes and Search
11. Scale with Primes and Search
12. Search About Similar Sequence
13. Check if the Sequence is The Summation of Two Sequences (Too Much Time - Need Enhancement)
14. Check if The Sequence is The Product of Two Sequences (Too Much Time - Need Enhancement)
15. Search About Cumulative Sums
16. Search About Cumulative Products 
17. Check if The Input is a Difference of a Sequence in The Database
18. Check if The Input is a Sum of Adjacent Terms of a Sequence in The Database
19. Check if The Input is a Product of Adjacent Terms of a Sequence in The Database
20. Check if The Input is a Cumulative Sum of a Sequence in The Database
21. Check if The Input is a Cumulative Product of a Sequence in The Database
22. Design your own operation ... (To be added)



# OEIS Database and Instructions
The database that is used in this project is part of the intellectual property of 
[The Online Encyclopedia of Integer Sequences (OEIS)](https://oeis.org/),
which is the official search engine for the database.
However, the database is made available under the
[Creative Commons Attribution Non-Commercial 3.0 license](https://creativecommons.org/licenses/by-nc/3.0/)
and you have to download it from the official website before using this project: 
1. Clone this repository or download it as a zip archive from GitHub.
2. Download two compressed files given [here](https://oeis.org/wiki/Welcome#Compressed_Versions) from OEIS.
3. Decompress the files, which should have default filenames of `names` and `stripped` (without .txt).
4. Move these two files to the `data` directory.
5. Install the requirements `pip3 install -r requirements.txt`. 
   * [More details](https://pip.pypa.io/en/stable/user_guide/#requirements-files).
6. Run `main.py` and enjoy!
7. Note: The script was only tested on Linux using Python 3.8.10

# Notes
Disclaimer: This project is under developing and testing, 
and it may contain bugs which could affect the validity of the results! 

### Special Thanks 
* Dr. Neil J. Sloane for his suggestions of Fuzzy Matching and Searching by Terms Lookup Formula. 

### For Suggestions 
mm && almazari && 16 [.::at::.] cit [.::dot::.] just [.::dot::.] edu [.::dot::.] jo

### TODO 
- [ ] Speed Enhancement for Summation/Multiplication of Two Sequences
- [X] Fuzzy Matching II - Implement GAP size control.
- [X] Fuzzy Matching III.
- [ ] Terms Lookup Formula - Dropping Terms.
- [ ] Operation Design
- [X] Fuzzy Matching
- [X] Search by Terms with a Variable 
- [X] Terms Lookup Formula Speed Enhancement
- [ ] Add More Options in Simple Search Queries (Prime, Odd, Even, Mod, ORing, ANDing)
- [ ] Support Parenthesis
- [ ] Intelligent Search Operation
- [X] Add Testing Unit
- [ ] Change The Functions Structure - Refactoring
  - [ ] Terms Selection
  - [ ] Coloring
  - [ ] Input Validation in Functions and Try-Exception 
  - [ ] Software Engineering and Packaging
- [X] Input Validation 
- [X] Sequence Input Enhancement 
- [X] Le Rabot - with extended version - Won't be done (Can be accomplished via Operation Design)
- [ ] Test on Windows
- [X] View Sequence
- [ ] Enhance Fuzzy Matching - Values Shifting 
- [X] Searching without Order - Dropping Terms.
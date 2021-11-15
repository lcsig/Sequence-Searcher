# OEIS Search Engine
OEIS Search Engine is a program to perform search queries on the OEIS Database (The script is still under development and testing)



# Search Queries
### Simple Search Queries
###### Order
* `1, 2, 3, 4`: Sequence contains these four terms without considering order. 
* `1, 2, 3, 4`: Sequence contains these four terms in the same order anywhere in the sequence.
###### Question Mark
* `1, 5, ?1, 13, 20`: The third term could be any number (The question mark indicates any possible number).
* `1, 5, ?2, 13, 20`: The third term and the fourth one could be any number (2 means two terms).
* `1, 5, ?*, 13, 20`: Any possible set of numbers between the two sequences [1, 5] and [13, 20].
* `1, 5, ?*, 13, 20, ?3, 60, 70`: Any possible set of numbers between the two sequences [1, 5] and [13, 20], and three numbers between [13, 20] and [60, 70].
###### Range 
* `1, 5, ?1, 13, 20--23`: The third term could be any number, the fifth is between 20 and 23.
* `1--4, 5, ?1, 13, 20--30`: The first term could be 1, 2, 3 or 4. Also, The third term could be any number, the fifth is between 20 and 23.
###### The script will search anywhere in the sequence and not from the beginning. Other techniques could be added upon request.
### Advanced Search Queries
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



# Notes
## Database Update
To update the database:
1. Download two compressed files given [here](https://oeis.org/wiki/Welcome#Compressed_Versions) from OEIS.
2. Decompress the files, which should have default filenames of `names` and `stripped` (without .txt).
3. Move these two files to the `data` directory.
4. Run `oeis.py` script and enjoy!
## TODO 
- [ ] Add More Options in Simple Search Queries (Prime, Odd, Even, Mod, ORing, ANDing)
- [ ] Support Parenthesis
- [ ] Intelligent Search Operation
- [ ] Operation Design 
- [ ] Speed Enhancement
- [ ] Change The Functions Structure and Add Testing Unit
- [ ] Input Validation 
- [ ] Sequence Input Enhancement 

For Suggestions ... ("mm && almazari && 16 [.::at::.] cit [.::dot::.] just [.::dot::.] edu [.::dot::.] jo")
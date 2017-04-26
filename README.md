# Project - Swiss Tournament


## SCOPE

The purpose of the project is to write and test code that will process different
aspects of a Swiss System Tournament, in which players in a tournament are not
eliminated when they lose a match, instead they are paired in each round with
opponents having the same win/loss record or as close as possible.  This style
will result in a single winner but all players will play the same number of
rounds and have the same number of matches.

This Readme file contains instructions on using the files for a swissPairings
tournament.


## Download Files From GitHUb

Download and install these four files from GitHUb to a PC that has Python
and PSQL installed to the same directory.

These four files are:

    1) tournament.sql
    2) tournament.py
    3) tournament_test.py
    4) README.MD


## SQL DATABASE SETUP (tournament.sql)

Initially a PSQL DATABASE called 'tournament' will need to be created. The file
tournament.sql contains the sql executable instructions to create that database.

This can be accomplished by the following:

1.  At the vagrant prompt type in 'psql' to open the SQL server.

2.  To load the contents of the file named 'tournament.sql'.
    At the vagrant prompt type the following:
    vagrant=>\i tournament.sql
    This will execute the commands from the tournament.sql file.
    The 'tournament.sql' file will create a Database named 'tournament' that
    will contain two tables named 'players' and 'matches'.  The 'players'
    table will contain the players ID and the players fullname.  The 'matches'
    table will contain the match id along with the match that was played where
    the winner column will contain the id of the winning player and the loser
    column will contain the id of the losing player.

    If the Database already exists then the Database will be deleted and
    recreated again.


## Python Tournament Code (tournament.py)

The file 'tournament.py' contains the functions that manipulate the data in the
tournament Database and keeps up with the players and their standings in the
SwissPairings tournament.


## Python Test Code (tournament_test.py)

The file 'tournament_test.py' contains the functions that are used to test
the functions contained in the 'tournament.py' file.  If successfully ran
you will see 10 numbered items that reflect if that particular test passed.

Finally, upon successfull completion, the last statement output will read
"Success!  All test pass!".


## License

The content of this repository is licensed under MIT License.

Copyright (c) 2017 Mitchell Smith

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

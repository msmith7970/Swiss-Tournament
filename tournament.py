#!/usr/bin/env python2.7
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
from contextlib import contextmanager


@contextmanager
def connect(commit_flag):
    """Connect to the PostgreSQL database.  Returns a database connection.
    using context manager.  This is a helper function that conects to the
    psql database as DB, returns the cursor as c to the funciton that
    called it, utilizing a commit_flag variable that when set to 'yes'
    will perform a commit to the database and then finally close out the
    cursor and the connection to the  database."""

#   Define the database name as database_name
    database_name = 'tournament'

    try:
        DB = psycopg2.connect("dbname={}".format(database_name))
        c = DB.cursor()
        yield c
    except:
        raise
    else:
        if commit_flag == 'yes':
            DB.commit()
    finally:
        c.close()
        DB.close()


def deleteMatches():
    """Remove all the match records from the database.  Leave the values for
    players."""

#   SQL is a variable containing the SQL command used with the Database to
#     protect against SQL injection.

    commit_flag = 'yes'
#   use TRUNCATE for speed and to immediately free up space in memory.
    with connect(commit_flag) as c:
        SQL = "TRUNCATE matches;"
        c.execute(SQL)


def deletePlayers():
    """Remove all the player records from the database.  This will delete
    the contents from the table players and all tables (ie - matches table)
    having a foreign key reference leaving the structue of the tables intact
    such as the column names."""

#   SQL is a variable containing the SQL command used with the Database to
#     protect against SQL injection.

    commit_flag = 'yes'
    with connect(commit_flag) as c:
        SQL = "TRUNCATE players CASCADE"
        c.execute(SQL)


def countPlayers():
    """Returns the number of players currently registered.

    num contains an interger value of the number of players that are
    registered to paly in the tournament."""

#   SQL is a variable containing the SQL command used with the Database to
#     protect against SQL injection.

    commit_flag = 'yes'
    with connect(commit_flag) as c:
        SQL = "SELECT COUNT(*) from players;"
        c.execute(SQL)
        result = c.fetchone()
        num = result[0]
        return num


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name:     the player's full name (need not be unique).
      wins:     When a new palyer is registered their inital value of wins is
                set to 0 (zero).
      matches:  When a new palyer is registered their inital value of matches
                is set to 0 (zero).
    """

#   SQL is a variable containing the SQL command used with the Database to
#     protect against SQL injection.
#   Data is a variable for the values used in the SQL statement sent to the
#     Database in a tuple format to project against SQL injection.

    commit_flag = 'yes'
    with connect(commit_flag) as c:
        SQL = "INSERT INTO players (fullname) VALUES (%s);"
        Data = (name,)
        c.execute(SQL, Data)


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins
    form the psql table called 'matches'.

    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, called standings, where each of the tuples contains
        (id, name, wins, matches):

        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played

    Variables:
        standings = is the name of the new list containing a list of tuples
            where each tuple was fromed using data from players
            and matches tables.
        newTuple = used to hold the newly formed record and applend it to
            the new list called standings as you loop thru the SQL query.
        results = a temporary variable used to hold the contents from the
            table called standings.
    """

    standings = []
    commit_flag = 'no'
    with connect(commit_flag) as c:
        SQL = "SELECT                                       \
                 players.id,                                \
                 players.fullname,                          \
                (                                           \
                SELECT COUNT(matches.winner) FROM matches   \
                  WHERE                                     \
                    matches.winner = players.id) AS wins,   \
                (                                           \
                SELECT COUNT(matches.winner) FROM matches   \
                  WHERE                                     \
                    matches.loser = players.id              \
                  OR                                        \
                    matches.winner = players.id) AS matches \
                FROM                                        \
                  players                                   \
                LEFT JOIN                                   \
                  matches USING (id)                        \
                ORDER BY wins DESC;"
        c.execute(SQL)

#       Loop thru the SQL Query and put the data from each row of the Query
#         into the results variable.
        results = ((row[0], str(row[1]), row[2], row[3])
                   for row in c.fetchall())


#       Append each record to the new list called standings.
        for result in results:
            newTuple = (result[0], result[1], result[2], result[3])
            standings.append(newTuple)
        return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      ID:   the id corresponds to the match played
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """

#   SQL is a variable containing the SQL command used with the Database to
#     protect against SQL injection.
#   Data is a variable for the values used in the SQL statement sent to the
#     Database in a tuple format to project against SQL injection.

    commit_flag = 'yes'
    with connect(commit_flag) as c:
        SQL = "INSERT INTO matches (winner, loser) VALUES (%s, %s);"
        Data = (winner, loser)
        c.execute(SQL, Data)


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name

    Variables:
        nextRound:  is the name of a list used to contain a list of the
                    players id and the players fullname from the standings
                    tablecreated in the playerStandings function, sorted
                    on thenumber of wins from high to low.
        playersinfo:    holds a record from the standings table to retreive
                        the palyers id and fullname.
        pair:       This is the list of pairs of players for the next round
                    of a match.

    """
    nextRound = []
    playersinfo = playerStandings()

#   Loop thru the results contained in the varaible playersinfo, which
#   contains the players id, players name, the players number of wins and
#   the players number of matches and reduce it to a new list called
#   nextRound containing a list of tuples where each tuple is the playeers
#   ID and the players fullname.
    for playerinfo in playersinfo:
        new_tuple = playerinfo[0], playerinfo[1]
        nextRound.append(new_tuple)

#   Initilize the variable pair to create a new list, which will contain
#   a list of tuples containing the players id and and players fullname.  The
#   tuples will be paired together for the next match.  This pairing will be
#   based on the number of wins from high to low.
#   i is the index used to loop thru the list nextRound.
#   The while loop will loop thru the nextRound list and combine the first
#   two tuples then increment the counter by 2 and combine the next two
#   tuples in the list and so on.

    i = 0
    pair = []
    while i < len(playersinfo):
        temp_pair = nextRound[i] + nextRound[i+1]
        pair.append(temp_pair)
        i += 2
    return pair

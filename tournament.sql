-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Bfore running the code in tournament.py or tournament_test.py, a databse
-- named "tournament" must be created.
-- This SQL file will perfrom that task for you.

-- 1) On your virtual machine, navigate to the folder that contains the
-- tournamnt files and type in "psql" and hit the enter key.
-- 2) At the vagrant prompt type in vagrant=>"\i tournament.sql" and hit
-- the enter key.  You should see lines printed out that look similar to the
-- following:
-- DROP DATABASE
-- CREATE DATABASE
-- You are now connected to database "tournament" as user "vagrant"
-- CREATE TABLE
-- CREATE TABLE

-- CREATE THE DATATBASE:
-- Create a new database called tournament.  First check to see if it already
-- exists and if so drop it and rebuilt it.  After successfully building it,
-- then connect to it with the \c command.
DROP DATABASE IF EXiSTS tournament;
CREATE DATABASE tournament;
\c tournament

-- CREATE THE TABLES:
-- Build two tables:
--   First table is called players.
--   Second table is called matches.

-- players Table:
-- The players table has a column for:
--   ID, which is the PRIMARY Key
--   fullname, which holds the fullname of a player
CREATE TABLE players (id SERIAL PRIMARY KEY,
                              fullname TEXT
                      );

-- matches Table:
-- The matches table is a record of who played who in a match.
-- The matches table has a column for:
--   ID, which is the PRIMARY Key that corrresponds to a match
--   winner, which holds the ID of the winner from the players table for a match
--   loser, which holds the ID of the loser from the players table for a match
CREATE TABLE matches (id SERIAL PRIMARY KEy,
                      winner INTEGER REFERENCES players(id),
                      loser INTEGER REFERENCES players(id)
                      );

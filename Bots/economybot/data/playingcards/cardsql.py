import sqlite3


db = "data/playingcards/cards.db"

class CardSQL():
    def __init__(self):
        pass
    
    def dropAll(self):


DROP TABLE IF EXISTS Card;
DROP TABLE IF EXISTS Suits;
DROP TABLE IF EXISTS Values;
DROP TABLE IF EXISTS Images;


CREATE TABLE Card (
suit INTEGER(1) NOT NULL,
value INTEGER(5) NOT NULL,
image VARCHAR NOT NULL,
FOREIGN KEY(suit) REFERENCES Suits(suit),
FOREIGN KEY(value) REFERENCES Values(value),
FOREIGN KEY(image) REFERENCES Images(link));

CREATE TABLE Suits (
suit INTEGER PRIMARY KEY NOT NULL,
name VARCHAR NOT NULL);

CREATE TABLE Values (
value INTEGER PRIMARY KEY NOT NULL,
name VARCHAR NOT NULL);

CREATE TABLE Images (
link VARCHAR PRIMARY KEY NOT NULL);


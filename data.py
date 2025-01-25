import mysql.connector
import random

"""
cursor.execute("CREATE TABLE IF NOT EXISTS tools ()")
cursor.execute("CREATE TABLE IF NOT EXISTS resources ()")
cursor.execute("CREATE TABLE IF NOT EXISTS items ()")
"""

def getDB():
    # Gets our database
    db = mysql.connector.connect(host="localhost",user="root",passwd="passpass",database="data")
    return db

def createTables():
    db = getDB()
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT, userDiscordID BIGINT UNSIGNED NOT NULL, userDiscordName VARCHAR(32) NOT NULL, coins INT UNSIGNED NOT NULL, coordinatesX INT NOT NULL, coordinatesY INT NOT NULL, UNIQUE(userDiscordID))")
    cursor.execute("CREATE TABLE IF NOT EXISTS tools (userDiscordID BIGINT UNSIGNED NOT NULL PRIMARY KEY, pickaxe INT UNSIGNED NOT NULL, axe INT UNSIGNED NOT NULL, sword INT UNSIGNED NOT NULL, FOREIGN KEY(userDiscordID) REFERENCES users(userDiscordID))")
    cursor.execute("CREATE TABLE IF NOT EXISTS resources (userDiscordID BIGINT UNSIGNED NOT NULL PRIMARY KEY, stone INT UNSIGNED NOT NULL, wood INT UNSIGNED NOT NULL, string INT UNSIGNED NOT NULL, FOREIGN KEY(userDiscordID) REFERENCES users(userDiscordID))")

def createUser(userDiscordID, userDiscordName):
    db = getDB()
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (userDiscordID,userDiscordName,coins,coordinatesX,coordinatesY) VALUES (%s,%s,%s,%s,%s)", (userDiscordID, userDiscordName, 0, random.randint(-100,100), random.randint(-100,100)))
    cursor.execute("INSERT INTO tools (userDiscordID,pickaxe,axe,sword) VALUES (%s,%s,%s,%s)", (userDiscordID,0,0,0))
    cursor.execute("INSERT INTO resources (userDiscordID,stone,wood,string) VALUES (%s,%s,%s,%s)", (userDiscordID,0,0,0))
    db.commit()

def getUser(userDiscordID):
    db = getDB()
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM users WHERE userDiscordID = {userDiscordID}")

    user = None
    for user in cursor: pass
    return user

###createTables()

def getUserTools(userDiscordID):
    db = getDB()
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM tools WHERE userDiscordID = {userDiscordID}")

    user = None
    for user in cursor: pass
    return user

def updateUserResources(userDiscordID, resource, amt):
    # Updates a user's resources
    db = getDB()
    db.cursor().execute(f"UPDATE resources SET {resource} = {resource} + {amt} WHERE userDiscordID = {userDiscordID}")
    db.commit()
    




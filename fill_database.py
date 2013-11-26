import sys
import MySQLdb as mdb
from time import gmtime, strftime
import random
import datetime
from random_words import *
from random import randrange
import string


def time_gen():
    return datetime.datetime(random.randint(1900, 2012),
                             random.randint(1, 12),
                             random.randint(1, 28),
                             random.randint(0, 23),
                             random.randint(0, 59),
                             random.randint(0, 59),
                             random.randint(0, 1000))


def string_gen(size, chars):
    return ''.join(random.choice(chars) for x in range(size))

def is_used(dictionary, key, value):
    for dct in dictionary:
        if key in dct and dct[key] == value:
            return True
    return False

def insert_user(cursor, id):
    password = string_gen(8, string.printable)
    last_login = time_gen()
    is_superuser = random.randint(0, 1)
    username = RandomNicknames().random_nick(None, 'u') + str(random.randint(1, 100000))
    first_name = RandomNicknames().random_nick(None, 'u')
    last_name = RandomNicknames().random_nick(None, 'u')
    email = RandomEmails().randomMail()
    is_staff = random.randint(0, 1)
    is_active = random.randint(0, 1)
    date_joined = time_gen()
    cursor.execute('INSERT INTO auth_user VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                   (id, password, last_login, is_superuser, username, first_name, last_name, email,
                    is_staff, is_active, date_joined))

#def insert_tag(cursor):
#    tags = []
#    while len(tags) < 100:
#        tag_name = {
#            "tag_name": None
#        }
#
#        temp_tag = RandomWords().random_word()
#        while is_used(tags, "tag_name", temp_tag):
#            temp_tag = RandomWords().random_word()
#        tag_name["tag_name"] = temp_tag
#
#        tags.append(tag_name)
#        cursor.execute('INSERT INTO ask_tag (tag_name) VALUES (%s);',
#                      (tag_name["tag_name"]))


def insert_question(cursor, id):

    lorem_text = LoremIpsum()
    lorem_text.MAX_WORDS = 15

    header = lorem_text.get_sentence()
    contents = lorem_text.get_sentences(random.randint(1, 10))
    author = randrange(1, 10010)
    creation_date = datetime.datetime.now()
    rating = random.randint(-500, 500)

    cursor.execute("INSERT INTO ask_question VALUES (%s, %s, %s, %s, %s, %s)",
                   (id, header, contents, author, creation_date, rating))

def insert_answer(cursor, id):

    lorem_text = LoremIpsum()
    lorem_text.MAX_WORDS = 25

    contents = lorem_text.get_sentences(random.randint(2, 10))
    question = randrange(1, 100010)
    author = randrange(1, 10010)
    date = datetime.datetime.now()
    correct = random.randint(0, 1)
    rating = random.randint(-500, 500)
    cursor.execute("INSERT INTO ask_answer VALUES (%s, %s, %s, %s, %s, %s, %s)",
                   (id, contents, question, author, date, correct, rating))


def insert_comment(cursor, id):

    lorem_text = LoremIpsum()
    lorem_text.MAX_WORDS = 10
    contents = lorem_text.get_sentences(random.randint(1, 3))
    date = datetime.datetime.now()
    author = randrange(1, 10016)

    answer = randrange(1, 1000024)
    cursor.execute("INSERT INTO ask_commentanswer VALUES (%s, %s, %s, %s, %s)",
                        (id, contents, date, author, answer))

    #answer = randrange(1, 1000024)
    #cursor.execute("INSERT INTO ask_commentquestion VALUES (%s, %s, %s, %s, %s)",
                        #(id, contents, date, author, answer))



con = mdb.connect('localhost', 'ask_user', '', 'ask_db')

with con:
    cur = con.cursor()
#    for x in xrange(1, 10010):
#        insert_user(cur, x)
#    for x in xrange(1, 100010):
#        insert_question(cur, x)
#    for x in xrange(1, 1000010):
#        insert_answer(cur, x)
    for x in xrange(400100, 600100):
        insert_comment(cur, x)

# create database ask_db character set utf-8
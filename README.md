# cmdnote
# Welcome to cmdnote Project!

This is a simple script which allows you to write note via your terminal while you are coding/working.


# Getting Started

These instructions will help you cmdNote and get you running in no time!
## Setting the database

You need to have a database file in the directory where you want to take notes. You can create different databases in different directories.

    python cmdnote.py new

This will create database file in the current location

## Adding new note

For adding the new note run the below command.

    python cmdnote.py add Your Note Here
You can add your note after the 'add' keyword.

## Viewing the notes

    python cmdnote.py view

## Deleting a note

    python cmdnote.py rm NoteNumber

You can see the note number from view note command.

# Making commands fast!
You can also add the path to 'cmdnote.py' to your .bashrc file in order to avoid typing the whole command every time.
Below is a sample .bashrc entry

    NOTE='C:/Users/pranavj/Desktop/cmdnote/cmdnote.py'
    alias note='python $NOTE'

You can now directly type 'note' followed by commands

    note new
    note add Hello Application!
    note view
    note rm 2



#!/usr/bin/python3

""" Functions to parse the text for future database insertion """

# TODO Add error handling

class FileReader:
    """ Wrapper to the generator function to keep the context """

    def __init__(self, filename) :

        self.filename = filename
        self.inputfile = open(filename)

    def nextLine(self) :
        """
        Generator function that returns the next token
        to insert into the database
        """

        for line in self.inputfile :
            # TODO implement logic for token fragmentation

            yield token


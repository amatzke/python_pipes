import logging
import datetime

""" Add the current date in this step"""
class Step(object):

    def run(self, input):
        logging.info('Adding the Date')       
        now = datetime.datetime.now() 
        input['DATE'] = str(now)

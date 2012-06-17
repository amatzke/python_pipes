import logging

""" Double all inputs in this step"""
class Step(object):

    def run(self, input):
        logging.info('Doubling the input message')        
        input['DOUBLE'] = input['original'] + input['original']

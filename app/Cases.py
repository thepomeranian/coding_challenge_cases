from flask import Flask, request, jsonify
from flask_restful import Resource
from datetime import datetime
from dateutil import parser


class Cases(Resource):

    def get(self):
        """Returns all cases with number of hours"""
        return {'case': 'test'}

    def post(self):
        """Takes in JSON and outputs all cases with number of hours"""
        json_data = request.get_json(force=True)
        # time_tracker = []
        case = {}
        hours = 0
        for item in json_data:
            if not case.get(item['case_id']):
                case[item['case_id']] = {}
                case[item['case_id']]['time_tracker'] = []
            if 'state' in item:
                if item['state']['to'] == 'open':
                    case[item['case_id']]['state'] = 'open'
                if item['state']['from'] == 'open' or item['state']['to'] == 'open':
                    if 'team' in case[item['case_id']]:
                        if case[item['case_id']]['team'] == 'Runtime':
                            case[item['case_id']]['time_tracker'].append(
                                parser.parse(item['timestamp']))
                            # if item['state']['to'] == 'closed' and len(case[item['case_id']]['time_tracker']) is 1:
                            #   hours = hours + case[item['case_id']]['time_tracker'][0].hour
                            print case[item['case_id']]['time_tracker']
            if 'assignee' in item:
                if item['team'] == 'Runtime' and case[item['case_id']]['state'] == 'open':
                    case[item['case_id']]['team'] = 'Runtime'
                    case[item['case_id']]['time_tracker'].append(
                        parser.parse(item['timestamp']))
                    # print "goes here"
                    print case[item['case_id']]['time_tracker']
            if len(case[item['case_id']]['time_tracker']) is 2:
                hours = hours + \
                    self.calculate(
                        case[item['case_id']]['time_tracker'][0], case[item['case_id']]['time_tracker'][1])
                case[item['case_id']]['time_tracker'].pop(0)
                case[item['case_id']]['time_tracker'].pop(0)
                case[item['case_id']]['hours'] = hours
            # print case

        return case

    def calculate(self, start, end):
        """Calculates the time in hours between start and end time"""
        hours = end - start
        hours = abs(hours.days) * 24 + abs(hours.seconds) // 3600
        return hours

    """
    Notes:
    * figure out how to best store start and stop times of each case 
      * this will need some more thought -- there has to be a way to check all of the conditions: state is open, assigned to runtime in a cleaner way -- another method? is_open() is_runtime()?
    * write calculate method to check time between start and finish 
      * this should be easier to do since i can take it as an individual function
    * testing
      * check if post body is valid json
      * assert calculate method works properly
      * if i end up writing methods for checking state and assignee i can test those as well
      * i could try my hand at flask testing and test the get and post endpoints
    * write a banging readme
    """

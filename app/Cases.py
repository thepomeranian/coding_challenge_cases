from flask import Flask, request, jsonify
from flask_restful import Resource
from datetime import datetime
from dateutil import parser
import json


class Cases(Resource):

    def __init__(self):
        self.case = {}
        self.hours = 0

    def get(self):
        pass

    def post(self):
        """Takes in JSON and outputs all cases with number of hours"""
        json_data = request.get_json(force=True)

        for item in json_data:
            self.get_or_create(item['case_id'])

            if 'state' in item:
                if item['state']['to'] == 'open':
                    self.set_state(item['case_id'])
                    self.check_team(item['case_id'])
                    if 'team' in self.case[item['case_id']]:
                        if self.case[item['case_id']]['team'] == 'Runtime':
                            self.case[item['case_id']]['time_tracker'].append(
                                parser.parse(item['timestamp']))
                            # print self.case[item['case_id']]['time_tracker']

                if item['state']['from'] == 'open':
                    if 'team' in self.case[item['case_id']]:
                        if self.case[item['case_id']]['team'] == 'Runtime':
                            self.case[item['case_id']]['time_tracker'].append(
                                parser.parse(item['timestamp']))
                        if item['state']['to'] == 'closed':
                            self.case[item['case_id']]['time_tracker'].append(
                                parser.parse(item['timestamp']))
                            # print self.case[item['case_id']]['time_tracker']
                            # print case[item['case_id']]['time_tracker']
                        # print case[item['case_id']]['team']
            if 'assignee' in item:
                if item['team'] == 'Runtime' and self.case[item['case_id']]['state'] == 'open':
                    self.case[item['case_id']]['team'] = 'Runtime'
                    self.case[item['case_id']]['time_tracker'].append(
                        parser.parse(item['timestamp']))
                    # print self.case[item['case_id']]['time_tracker']

            if len(self.case[item['case_id']]['time_tracker']) == 2:

                self.hours = self.hours + \
                    self.calculate(
                        self.case[item['case_id']]['time_tracker'][0], self.case[item['case_id']]['time_tracker'][1])
                self.case[item['case_id']]['time_tracker'].pop(0)
                self.case[item['case_id']]['time_tracker'].pop(0)
                self.case[item['case_id']]['hours'] = self.hours
            # print case

        return json.dumps(self.case)

    def calculate(self, start, end):
        """Calculates the time in hours between start and end time"""
        hours = end - start
        hours = abs(hours.days) * 24 + abs(hours.seconds) // 3600
        return hours

    def get_or_create(self, case_id):
        if not self.case.get(case_id):
            self.case[case_id] = {}
            self.case[case_id]['time_tracker'] = []
        else:
            print "already created"

    def set_state(self, case_id):
        self.case[case_id]['state'] = 'open'

    def check_team(self, case_id):
        pass

    def check_state(self, case_id):
        pass

    def set_team(self, case_id):
        pass

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
    * rewrite handling case states, check for runtime, and appending to timetracker. the issues seem to stem from there. hour calculation is currently off as well
    * might want to think about breaking this down into methods once the math checks out
    """

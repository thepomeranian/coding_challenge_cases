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
        return json.dumps(self.case)

    def post(self):
        """Takes in JSON and outputs all cases with number of hours"""
        json_data = request.get_json(force=True)

        for item in json_data:
            self.get_or_create(item['case_id'])

            if 'state' in item:
                if item['state']['to'] == 'pending':
                    self.set_state(item['case_id'], 'pending')
                elif item['state']['to'] == 'closed':
                    self.set_state(item['case_id'], 'closed')
                elif item['state']['to'] == 'open':
                    self.set_state(item['case_id'], 'open')
                    if self.is_Runtime(item['case_id']):
                        self.add_timestamp(item['case_id'], item['timestamp'])
                if item['state']['from'] == 'open':
                    if self.is_Runtime(item['case_id']):
                        self.add_timestamp(item['case_id'], item['timestamp'])

            if 'team' in item:
                self.set_team(item['case_id'], item['team'])
                if self.is_open(item['case_id']):
                    if self.previous(item['case_id']):
                        print 'previous team works'
                        self.add_timestamp(item['case_id'], item['timestamp'])
                        print self.case[item['case_id']]['time_tracker']
                    if self.is_Runtime(item['case_id']):
                        self.add_timestamp(item['case_id'], item['timestamp'])

        return [{"case_id": case, "hours": self.case[case]['hours']} for case in self.case]

    def add_timestamp(self, case_id, timestamp):
        if self.is_Runtime(case_id) or self.previous(case_id):
            print 'adding ' + timestamp
            self.case[case_id]['time_tracker'].append(
                parser.parse(timestamp))
            self.check_time_tracker(case_id)

    def check_time_tracker(self, case_id):
        print self.case[case_id]['time_tracker']
        if len(self.case[case_id]['time_tracker']) == 2:
            self.case[case_id]['hours'] = self.case[case_id]['hours'] + \
                self.calculate(self.case[case_id]['time_tracker'][
                               0], self.case[case_id]['time_tracker'][1])
            self.case[case_id]['time_tracker'].pop(0)
            self.case[case_id]['time_tracker'].pop(0)
            print 'time_tracker is now ' + str(len(self.case[case_id]['time_tracker']))
            print 'hours is now ' + str(self.case[case_id]['hours']) + ' ' + str(case_id)
            self.case[case_id]['hours'] = self.case[case_id]['hours']

    def calculate(self, start, end):
        """Calculates the time in hours between start and end time"""
        hours = end - start
        hours = abs(hours.days) * 24 + abs(hours.seconds) // 3600
        return hours

    def get_or_create(self, case_id):
        if not self.case.get(case_id):
            self.case[case_id] = {}
            self.case[case_id]['time_tracker'] = []
            self.case[case_id]['hours'] = 0

    def set_state(self, case_id, state='open'):
        self.case[case_id]['state'] = state
        print 'state set to ' + self.case[case_id]['state']

    def is_open(self, case_id):
      # check if state is open
        if self.case[case_id]['state'] == 'open':
            return True

    def set_team(self, case_id, team=None):
        if 'team' in self.case[case_id]:
            self.case[case_id]['previous_team'] = self.case[case_id]['team']
        self.case[case_id]['team'] = team
        print 'team set to ' + self.case[case_id]['team']

    def is_Runtime(self, case_id):
        if 'team' in self.case[case_id]:
            if self.case[case_id]['team'] == 'Runtime':
                return True
        else:
            return False

    def previous(self, case_id):
        if 'previous_team' in self.case[case_id]:
            if self.case[case_id]['previous_team'] == 'Runtime':
                return True
        return False

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

from flask import Flask, request, jsonify
from flask_restful import Resource



class Cases(Resource):

    def get(self):
      """Returns all cases with number of hours"""
      return {'case': 'test'}

    def post(self):
      """Takes in JSON and outputs all cases with number of hours"""
      json_data = request.get_json(force=True)
      time_tracker = []
      case = {}

      for item in json_data:
        if not case.get(item['case_id']):
          case[item['case_id']] = {}
        if 'state' in item:
          if item['state']['to'] == 'open':
            case[item['case_id']] = {'state': 'open'}
        if 'assignee' in item:
          if item['team'] == 'Runtime' and case[item['case_id']]['state'] == 'open':
            case[item['case_id']]['team'] = 'Runtime'
            time_tracker.append(item['timestamp'])
        print time_tracker
        print case
        # if 
      # for item in json_data:
      #   if item['case_id'] not in tracker:
      #     case['case_id'] = item['case_id']
      #   if tracker[ caitem['case_id']]:
      #     if item['team'] == 'Runtime':
      #       print "ok"

      # tracker.append(case)
      return case


    def calculate(start, end):
      """Calculates the time in hours between start and end time"""
      pass

    def get_or_create(case_id):
      """Finds the case_id, if it doesn't exist, create it"""
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
    """
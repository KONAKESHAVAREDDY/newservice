from st2common.runners.base_action import Action
import requests
import json
class CreateIncidentAction(Action):

    def run(stackstorm_event):
    # ServiceNow API endpoint
        url = 'https://your-instance.service-now.com/api/now/table/incident'

    # ServiceNow API credentials
        username = 'admin'
        password = 'grBDH*m7bH0@'


    # JSON payload for creating an incident
        payload = {
            'short_description': 'new ticket',
            'description': 'Creating new tcket on servicenow'
        }

    # Set the headers for the request
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

    # Make the API call to create an incident
        try:
            response = requests.post(url, auth=(username, password), headers=headers, data=json.dumps(payload))
            response.raise_for_status()
            incident_data = response.json()
            sys_id = incident_data.get('result', {}).get('sys_id')
            return {'sys_id': sys_id}
        except requests.exceptions.RequestException as e:
            return str(e)

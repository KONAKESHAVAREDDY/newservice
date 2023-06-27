from st2common.runners.base_action import Action
import requests


class CreateIncidentAction(Action):
    def run(self, instance_name):
        url = "https://" + instance_name + ".servicenow.com/api/now/table/incident"
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": "Bearer your-servicenow-api-token",
        }
        payload = {
            "short_description": "New incident created by StackStorm",
            "description": "This incident was created by StackStorm integration",
            "category": "Hardware",
            "priority": "3",
        }

        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()

        return response.json()["result"]["number"]

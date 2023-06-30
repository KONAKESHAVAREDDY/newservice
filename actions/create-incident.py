from lib.actions import BaseAction


class CreateIncidentAction(BaseAction):
    def run(self, payload):
        s = self.client

        path = '/table/incident'
        response = s.resource(api_path=path).create(payload=payload)
        sys_id= response.get('sys_id')
        return sys_id

import slack_sdk

class SlackClient():
    def __init__(self, token, users=None):
        self._sc = slack_sdk.WebClient(token=token)
        self._users = users or {}
        self._user_lookup = {u['profile']['display_name']: u['id'] for u in self._users.values() if 'profile' in u and 'display_name' in u['profile']}

    @staticmethod
    def process_response(resp):
        assert resp['ok']
        return resp

    def get_users(self, force_reload=False):
        if not self._users or force_reload:
            resp = self.process_response(self._sc.users_list())
            self._users = {r['id']: r for r in resp['members']}
            self._user_lookup = {u['profile']['display_name']: u['id'] for u in self._users.values() if 'profile' in u and 'display_name' in u['profile']}
        return self._users

    def resolve_channel(self, user_or_channel):
        self.get_users()
        target = self._user_lookup.get(user_or_channel, user_or_channel)
        if target[0] == 'U':
            resp = self._sc.conversations_open(users=target, as_user=True)
            return resp['channel']['id']
        return target

    def chat(self, recipient, *args, **kwargs):
        return self.process_response(self._sc.chat_postMessage(channel=self.resolve_channel(recipient), *args, **kwargs))

    def upload(self, recipient, *args, **kwargs):
        return self.process_response(self._sc.files_upload_v2(channel=self.resolve_channel(recipient), *args, **kwargs))

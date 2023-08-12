import os


def get_client(token=None, **kwargs):
    if token is None and 'SLACK_API_TOKEN' not in os.environ:
        raise ValueError('A valid token must be provided or put in SLACK_API_TOKEN.')
    from . import client
    return client.SlackClient(token or os.environ['SLACK_API_TOKEN'], **kwargs)

def make_blocks(*args):
    for a in args:
        if isinstance(a, dict):
            yield {"type": "section", "fields": [
                   {
                       "type": "mrkdwn",
                       "text": f"*{field_name}*: {field_value}"
                   } for field_name, field_value in a.items()
                   ]}
        else:
            yield {"type": "section", "text":
                      {
                          "type": "mrkdwn",
                          "text": a
                      }
                   }

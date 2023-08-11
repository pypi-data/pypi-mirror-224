import json
from dataclasses import asdict

from client import LlamaClient
from schema.completion import ChatCompletion
from schema.request import Message, Request


def main():
    client = LlamaClient('tcp://localhost:5555')

    messages = [
        Message(role='system', content='You are a helpful assistant.'),
        Message(role='user', content='What is the capital of france?###Assistant:'),
        Message(role='Assistant', content='The capital of France is Paris###Human:'),
        Message(role='user', content='What did I ask you?###Assistant:')
    ]
    STOP = ["### Assistant:", "### Human:, ###system:, ###"]
    request = Request(
        model='gpt-3.5-turbo',
        messages=messages,
        temperature=0.8,
        n=256,
        stop=STOP)

    json_str = json.dumps(asdict(request), indent=4)
    print(json_str)

    response: ChatCompletion = client.send_request(request)

    json_str = json.dumps(asdict(response), indent=4)
    print(json_str)


if __name__ == "__main__":
    main()

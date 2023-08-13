import argparse
import sys

from xethhung12_tg_msg import send

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='Tg send message',
        description='The command line tool sending message to telegram through Telegram Bot',
    )
    parser.add_argument('--receiver-id', help='the id of telegram receiver')
    parser.add_argument('--bot-token', help='the token of the tg bot')
    parser.add_argument('--from-stdin', help='the message from stdin', dest='from_source', action='store_const',
                        const='stdin')
    parser.add_argument('--msg', help='the message from program argument')
    args = parser.parse_args()

    receiver = args.receiver_id
    token = args.bot_token

    msg = None
    if args.from_source == "stdin":
        msg = sys.stdin.read()
    if msg is None:
        msg = args.msg

    if msg is None:
        raise Exception("message is empty")

    send(token, receiver, msg)

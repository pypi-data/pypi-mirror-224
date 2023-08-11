""" File responsible for execute visual tests with percy """
from .json_treatment import JsonTreatment
import argparse


def _get_args():
    """ Parameters to use in script execution"""
    parser = argparse.ArgumentParser(
        description=('A script that collects results of JSON and sends a report of the status of the test to'
                     'the confluence page')
    )
    parser.add_argument(
        '--zephyr-token', help='The zephyr token credential',
    )
    parser.add_argument(
        '--jira_token', help='The jira token credential',
    )
    parser.add_argument(
        '--confluence-user', help='The confluence user credential',
    )
    parser.add_argument(
        '--confluence-password', help='The confluence password credential',
    )
    parser.add_argument(
        '--json-file', help='The json file absolute path',
    )

    return parser.parse_args()


def main():
    """ Function to execute the script """
    args = _get_args()
    zephyr = JsonTreatment(args.zephyr_token, args.jira_token, args.confluence_user, args.confluence_password)
    zephyr.load_json_file(args.json_file)


if __name__ == '__main__':
    main()

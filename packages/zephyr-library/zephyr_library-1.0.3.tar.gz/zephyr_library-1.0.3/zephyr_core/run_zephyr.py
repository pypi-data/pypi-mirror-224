""" File responsible for execute visual tests with percy """
from .json_treatment import JsonTreatment
from .create_test_cycles import CreateTestCycle
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
        '--jira-version', help='The app version that will be sent to Jira',
    )
    parser.add_argument(
        '--test-suite-type', help='The test suite type',
    )
    parser.add_argument(
        '--json-file', help='The json file absolute path',
    )
    parser.add_argument(
        '--create-cycle-per-component', help='The json file absolute path',
    )

    return parser.parse_args()


def main():
    """ Function to execute the script """
    args = _get_args()
    zephyr = JsonTreatment(args.zephyr_token, args.jira_token, args.confluence_user, args.confluence_password)
    zephyr.load_json_file(args.json_file)

    cycle = CreateTestCycle(args.zephyr_token, args.jira_token, args.confluence_user, args.confluence_password,
                            args.jira_version, args.create_zephyr_cycle_per_component, args.test_suite_type)
    cycle.create_test_cycle(args.json_file)


if __name__ == '__main__':
    main()

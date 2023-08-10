""" File responsible for execute the update test case """
import argparse
import json
from .core_logger import logger
from .update_test_case import update_test_case_zone


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
        '--update-test-case', help="""Test cases that will be update with the specified zones.'
                                                  'Ex: '{"zephyrids":["BEESQM-T39646"], "zone": "BE"}'""",
    )

    return parser.parse_args()


def main():
    """ Function to execute the script """
    args = _get_args()

    try:
        if not args.update_test_case:
            logger.error('Invalid argument! Please, provide a valid json string or file!')
            exit()
        if args.update_test_case.startswith('{'):
            json_test_case_ids_and_zone = json.loads(args.update_test_case)
            logger.info('Valid json string! Running the test...')
        else:
            with open(args.update_test_case, "r") as file:
                json_test_case_ids_and_zone = json.load(file)
                logger.info('Valid file! Running the test...')
        if json_test_case_ids_and_zone:
            update_test_case_zone(json_test_case_ids_and_zone, args.zephyr_token)
        else:
            logger.error('Invalid argument! Please provide a valid json string or file!')
    except Exception as e:
        logger.error('Invalid argument! Please, provide a valid json string or file!')
        logger.debug(e)


if __name__ == '__main__':
    main()

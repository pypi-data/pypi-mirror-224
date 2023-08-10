import logging
from os import environ

from rich.logging import RichHandler

from trongrid_extractoor.api import Api
from trongrid_extractoor.helpers.argument_parser import parse_args
from trongrid_extractoor.helpers.string_constants import PACKAGE_NAME
from trongrid_extractoor.helpers.time_helpers import MAX_TIME, TRON_LAUNCH_TIME, str_to_timestamp


def extract_tron_events():
    """When called by the installed script use the Rich logger."""
    args = parse_args()

    Api().events_for_token(
        args.token,
        since=args.since,
        until=args.until or MAX_TIME,
        resume_csv=args.resume_csv,
        output_dir=args.output_dir,
        event_name=args.event_name
    )

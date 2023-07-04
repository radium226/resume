from pendulum import parse, Date


DAY_DATE_PARSE_FORMAT = "YYYY[-]MM[-]DD"


def parse_day(text: str) -> Date:
    if isinstance(result := parse(text, format=DAY_DATE_PARSE_FORMAT), Date):
        return result
    else:
        raise Exception("We should not be here! ")
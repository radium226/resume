from pendulum import parse, Period, Date, today


MONTH_PARSE_FORMAT = "YYYY[-]MM"

def parse_month(text: str) -> Date:
    if isinstance(result := parse(text, format=MONTH_PARSE_FORMAT), Date):
        return result
    else:
        raise Exception("We should not be here! ")

def current_month() -> Date:
    return today().at(0).set(day=1)


def parse_period(period_obj: dict) -> Period:
    return (parse(to_obj, format=MONTH_PARSE_FORMAT) if (to_obj := period_obj.get("to", None)) else current_month()) - parse_month(period_obj["from"])
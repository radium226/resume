from pendulum import parse, Period


MONTH_PARSE_FORMAT = "YYYY[-]MM"


def parse_period(period_obj) -> Period:
    from_ = parse(period_obj["from"], format=MONTH_PARSE_FORMAT).at(0).set(day=1)
    to = (parse(to_obj, format=MONTH_PARSE_FORMAT) if (to_obj := period_obj.get("to", None)) else today()).at(0).set(day=1)
    return to - from_
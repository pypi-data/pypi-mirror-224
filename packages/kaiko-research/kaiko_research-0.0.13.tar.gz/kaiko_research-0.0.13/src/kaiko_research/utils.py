import re
from datetime import datetime


def convert_to_date_string(date_obj):
    return str(date_obj) + 'T00:00:00.000Z'


def compare_dates(d1, d2):
    given_date_first = datetime.strptime(d1, '%Y-%m-%d').date()
    given_date_second = datetime.strptime(d2, '%Y-%m-%d').date()
    if (given_date_first > given_date_second):
        print("The start date must be before the end date, please check your inputs")
        return False
    return True


def check_dates(date_str):
    if not (is_valid_date_format(date_str)):
        print(
            'The date that you entered does not have appropriate format. Please check that the format corresponds to "YYYY-MM-DD"')
        return False
    elif (not is_date_not_in_future(date_str)):
        print(
            'The date you entered is in the future, please enter the date in the past')
        return False
    return True


def is_valid_date_format(s):
    try:
        datetime.strptime(s, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def is_date_not_in_future(date_str):
    try:
        given_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        today = datetime.today().date()  # Get today's date

        if given_date <= today:
            return True
        else:
            return False
    except ValueError:
        return False


def validate_time(time_field, time_value, error):
    ISO8601_REGEX = re.compile(
        "^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})\.(\d{3})Z$"
    )
    if not bool(ISO8601_REGEX.match(time_value)):
        error(
            time_field,
            f"The {time_field} is not in ISO 8601 format, please refer to an example: 2023-01-01T00:00:00.000Z",
        )


def validate_bases(bases_field, bases_value, error):
    count = (
        len(bases_value)
        if isinstance(bases_value, list)
        else len(bases_value.split(","))
    )
    if count > 5:
        error(
            bases_field,
            f"The {bases_field} contains more than five exchanges, please check your query",
        )


def validate_bases_weights(weights_field, weights_value, error):
    weights = [float(_) for _ in weights_value.split(",")]
    if (sum(weights)) != 1:
        error(
            weights_field,
            f"The {weights_field} does not sum up to 1, please check the weights allocation",
        )


def validate_risk_level(risk_field, risk_value, error):
    risk = float(risk_value)
    if risk >= 1 or risk < 0.9:
        error(risk_field, f"The {risk_field} is outside of [0.9, 1) interval")


def check_nest(obj, nest=[]):
    for k in obj.keys():
        if type(obj[k]) == dict:
            nest = check_nest(obj[k], nest)
        else:
            nest += [obj[k]]
    return nest


def flatten_dataframe(df):
    row = df.loc[0, :].to_dict()
    print(check_nest(row))
    return df

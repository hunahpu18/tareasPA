"""
@author: Jesus Rivera
CDMX
"""

import re
import numpy as np
"""

Ejercicio 1
---------------------------

"""


def get_filename(path: str) -> str:
    return re.search(r"\w+\.+\w+$", path).group(0)


"""

Ejercicio 2
---------------------------

"""


def translate_date(month) -> str:
    month = month.group(0).lower()
    months = {'jan': 'ene', 'feb': 'feb', 'mar': 'mar',
              'apr': 'abr', 'may': 'may', 'jun': 'jun',
              'jul': 'jul', 'aug': 'ago', 'sep': 'sep',
              'oct': 'oct', 'nov': 'nov', 'dic': 'dic'}
    return months[month]


def date_in_spanish(date: str) -> str:
    """
       Translates a string date to spanish. That is, all references to months
       abbreviations like 'Jan', 'Feb', 'Mar' and so on are changed to 'Ene',
       'Feb', 'Mar', respectively.

       Parameters
       ----------
       date : str
           Date to be translated.

       Returns
       ------
           str
           The translated base_date.

       Examples
       --------
       >>> date_in_spanish("23-Apr-2021")
       23-Abr-2021
       >>> date_in_spanish("Dec-24-2020")
       Dic-24-2020
       """
    return re.sub(r"\w{3}", translate_date, date, count=1)


"""

Ejercicio 3
---------------------------

"""


def from_standard_equity_option_convention(code: str) -> dict:
    """
    Transform a standard equity option convention code to record representation.

    Parameters
    ----------
    code : str
        Standard equity option convention code (see
        https://en.wikipedia.org/wiki/Option_naming_convention).

    Returns
    -------
        dict
        A dictionary containing:
        'symbol': Symbol name
        'expire': Option expiration base_date
        'right': Put (P) or Call (C).
        'strike': Option strike

    Examples:
    >>> from_standard_equity_option_convention('YHOO150416C00030000')
    {'symbol': 'YHOO', 'expire': '20150416', 'right': 'C', 'strike': 30.0}
    """
    aux = re.search(r"([A-Za-z]{1,6})(\d{6})([CP])(\d{8})", code)
    print(aux)
    res = {'symbol': aux.group(1), 'expire': '20'+aux.group(2),
           'right': aux.group(3), 'strike': float(aux.group(4)[:5] + '.' + aux.group(4)[5:])}
    return res


"""

Ejercicio 4
---------------------------

"""


def exercise_4(symbols: str):
    """
      Changes every apostrophe ' for two apostrophes
    """
    symbols_str = re.sub(r"'", "''", str(symbols))
    return symbols_str


"""

Ejercicio 5
---------------------------

"""


def validate_account(account: str):
    """
    Validates if an account starts with DU and it's followed by seven digits from 0 to 9

    Parameters
    ----------
    account : str
        Account name or id to be validated

    Returns
    -------
    prints the account if valid account
    """
    if re.match(r'DU[0-9]{7}', account):
        print("Account: ", account)


"""

Ejercicio 6
---------------------------

"""


def exercise_6(text: str):
    """
       rewrites regex to match '^([0-9][0-9][0-9][0-9][0-9][0-9])$'

       Parameters
       ----------
       text : str
           Account name or id to be validated

       Returns
       -------
       prints the account if valid account
       """
    if re.match(r'^(\d{6})$', text):
        print("Correct OTP format: %s.", text)


"""

Ejercicio 7
---------------------------

"""


def exercise_7(text: str):
    if re.match(r"^\d(,\d)*$", text) is None:
        error_message = \
            "Try again, your answer does not correspond to a comma " + \
            "separated integers list. Type something like '1, 2, 3' " + \
            "without the apostrophes."
        return error_message


"""

Ejercicio 8
---------------------------

"""


def collect_commission_adjustment(data) -> dict:
    """
    Retrieve a commision adjustment record from the section "Commission
    Adjustments" in one Interactive Brokers activity report.

    PARAMETERS
    ----------
    data : list[]
        Line from the activity report in the "Commission Adjustment" section
        in list format. That is, each element in the list is a comma
        separated item from the line.

    RETURNS
    -------
        dict
        Containing the open position information in dictionary format.

    Examples
    --------
    >>> collect_commission_adjustment(['Commission Adjustments', 'Data', 'USD',
    ... '2021-04-23',
    ... 'Commission Computed After Trade Reported (C     210430C00069000)',
    ... '-1.0906123', '\\n'])
    {'end_date': '20210423', 'symbol': 'C', 'expire': '20210430', \
'right': 'C', 'strike': 69.0, 'sectype': 'OPT', 'amount': -1.0906123}
    >>> collect_commission_adjustment(
    ... ['Commission Adjustments', 'Data', 'USD', '2021-02-19',
    ... 'Commission Computed After Trade Reported (ALB)', '-0.4097', '\\n'])
    {'end_date': '20210219', 'symbol': 'ALB', 'sectype': 'STK', \
'amount': -0.4097}
    >>> collect_commission_adjustment(
    ... ['Commission Adjustments', 'Data', 'USD', '2021-02-19',
    ... 'Commission Computed After Trade Reported (ALB)', '-0.4097', '\\n'])
    {'end_date': '20210219', 'symbol': 'ALB', 'sectype': 'STK', \
'amount': -0.4097}
    """
    pass


"""

Ejercicio 9
---------------------------

"""


def banxico_value(tag, data):
    """
    Get data values from Banxico portals.

Parameters
    ----------
    tag : str
        Internal tag name of the variable to retrieve.
    data : str
        Html page to locate the tag value.

    Returns
    --------
        float
        The associated tag value.


    Examples
    --------
    >>> banxico_value('YHOO','YHOO-12.32USD')
    -12.32
    >>> banxico_value('YHOO','YHOO-12x32USD')
    -12.32
    """

    float_nt = "[^0-9-]*([-]*[0-9]+.[0-9]+)[^0-9]"
    try:
        res = float(re.search(tag + float_nt, data).group(1))
    except AttributeError:
        res = np.nan
    return res


"""

Ejercicio 10
---------------------------

"""


def exercise_10(dat_df):
    """
    returns columns in data_df that begin with imf followed by at least one digit, regardless of upper or lower case
    :param dat_df:
    :return:
    """
    # se puede omitir el 'else None' pues en caso de no encontrar el patron de busqueda re.match devuelve None
    col_sel = list(
            map(
                lambda s: s if re.match("[Ii][Mm][Ff][0-9]+", s) else None,
                dat_df.columns,
            ))
    # se puede omitir el ' is not None' puesto que cualquier objeto en python distinto de None es evaluado como True
    # o usar list(filter(None,col_sel))
    col_sel = [c for c in col_sel if c is not None]

    return col_sel


if __name__ == '__main__':
    print(f'{get_filename("$HOME/proyecto1/modulo5/programa3.py") = }')
    print(f'{date_in_spanish("23-Apr-2021") = }')
    print(f'{from_standard_equity_option_convention("YHOO150416C00030000") = }')
    print(f'Validate Account')
    validate_account("DU3141592")
    print(f'{banxico_value("YHOO","YHOO-12.32USD") = }')
    print(f'{banxico_value("YHOO","YHOO12x32USD") = }')

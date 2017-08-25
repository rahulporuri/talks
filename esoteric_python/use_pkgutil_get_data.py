from pkgutil import get_data
import pandas


if __name__ == "__main__":
    banklist_data_file = get_data('pandas', 'io/tests/data/banklist.html')
    print pandas.read_html(banklist_data_file)

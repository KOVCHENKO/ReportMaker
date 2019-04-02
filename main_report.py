import sys

from git_report.git_report import git_report
from user_report.user_report import user_report

report_types = {
    'users': user_report,
    'git': git_report,
}


def make_report(report_type):
    try:
        report_types[report_type]()
    except KeyError as e:
        # можно также присвоить значение по умолчанию вместо бросания исключения
        raise ValueError('Undefined unit: {}'.format(e.args[0]))


if __name__ == '__main__':
    report_type = str(sys.argv[1])
    make_report(report_type)

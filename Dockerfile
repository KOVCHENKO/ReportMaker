FROM python:3.7
ADD ./ /
RUN pip install openpyxl
RUN pip install pymysql
RUN pip install gitpython
RUN ls -al
CMD python main_report.py users

FROM python:3.4
ADD ./user_report.py /
RUN pip install openpyxl
RUN pip install pymysql
RUN ls -al
CMD python report.py

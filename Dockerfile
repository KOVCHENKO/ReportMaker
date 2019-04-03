FROM python:3.4
ADD ./main_report.py /
RUN pip install openpyxl
RUN pip install pymysql
RUN ls -al
CMD python main_report.py users
CMD python main_report.py git

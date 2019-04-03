#### How to send user payments and other DB reports
docker build --tag=reports .

docker run -it --rm reports

#### How to run with cron
0 8 * * * docker run --rm foo


#### How to run git reports
python main_report.py git
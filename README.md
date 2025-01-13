# WebHealthCheck
Sandbox to start with Simple tests to be applied to a tpical web site, e.g. finding broken links, etc.

## Usage:
1. Edit env.py to have the URL and environment name
2. Run:
```
pytest test_samples.py
```

## Useful pytest options
To generate htm report, run failed tests (those previously failed) first
```commandline
pytest --ff .\test_sample.py  --html=your_report_filename.htm
```

to explicitly cleanup previous run results
```commandline
pytest --lf .\test_sample.py --cache-clear  --html=your_report_file_lf.htm
```

to only rerun failed tests (those failed in previous run)
```commandline
pytest --lf .\test_sample.py  --html=your_report_file_lf_rerun.htm
```

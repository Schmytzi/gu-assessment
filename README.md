# Technical Assessment GU
## Task 1: Check QC results
Solution is in file: main.py

This script takes a QC file from an unnamed virology pipeline and does two things:

1. Output how man samples fail QC (percentage of covered reference bases < 95 or qc_fail flag set) by origin
2. Notify someone if more than 10% of samples from one origin fail QC

### Usage
```
Usage: main.py [OPTIONS] INPUT

  This script checks a QC file (specified by INPUT) for high failure rates
  from single origins

Options:
  -e, --email TEXT  E-mail address to send notification. If not specified, no e-mail will be sent
  --smtp TEXT       SMTP server to use for e-mail delivery. Please host your
                    own because I don't support authentication, yet  [default:
                    localhost]
  --help            Show this message and exit.
```

### Installation
Create a python venv and install all packages in `requirements.txt`.
Then just run it from the current directory or copy it wherever you want.

## Task 2: Written assignment
The answers are in `answers_task2.md`.
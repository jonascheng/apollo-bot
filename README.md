# For Linux users

1. build docker

replace `your-employee-no` and `your-secret` accordingly.

```console
docker build --build-arg EMPLOYEE_NO=your-employee-no --build-arg PSWD='your-secret' -t app .
```

2. run docker

```console
docker run --rm --name=app --privileged -d -v /tmp/apollo:/screenshots app
```

# For Windows users (beta)

1. install Chrome browser
2. install python for windows

Search and install Python 3.10 from Microsoft Store

3. install selenium

```
pip install selenium
```

4. download webdriver for Chrome

Please download from
[ChromeDrive - WebDrive for Chrome](https://sites.google.com/chromium.org/driver/getting-started)

the version should match to your Chrome browser one.

5. extract the downloaded file and place at the same level of python script `selenium-with-headless-chrome.py`

6. copy `clock-in-out.b__` to `clock-in-out.bat`

7. modify employee id and password in the batch script `clock-in-out.bat`

8. run `clock-in-out.bat` daily when you clock-in and clock-out, or create a task scheduler.
   [How to add a cron job on Windows](https://active-directory-wp.com/docs/Usage/How_to_add_a_cron_job_on_Windows/index.html)

Please ignore any javascript exception while running the `clock-in-out.bat`, you can check the result in `c:\windows\temp\hh-mm-ss-Result.png`

1. build docker

replace `your-employee-no` and `your-secret` accordingly.

```console
docker build --build-arg EMPLOYEE_NO=your-employee-no --build-arg PSWD='your-secret' -t app .
```

2. run docker

```console
docker run --rm --name=app --privileged -d -v /tmp/apollo:/screenshots app
```
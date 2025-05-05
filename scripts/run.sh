docker build --platform linux/arm64 -t crash_log .
docker run --rm -p 5000:5000 --env-file .env crash_log

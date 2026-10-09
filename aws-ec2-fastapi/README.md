# AWS EC2 with FastAPI

[← AI Engineer](../README.md)

**Level:** 🟢 Beginner · **Type:** `Tutorial` · Commands run from the repo root.

A simple FastAPI app that pretends to be a bookstore (`main.py`, `books.json`), and how to deploy it to AWS EC2 behind NGINX, or to AWS Lambda. More commands are in [`aws-ec2-fastapi/Run_Commands.md`](./Run_Commands.md).

## Deploy to AWS EC2

1. Create an EC2 instance (`t2.micro`) with the latest stable Ubuntu AMI.
2. [SSH into the instance](https://aws.amazon.com/blogs/compute/new-using-amazon-ec2-instance-connect-for-ssh-access-to-your-ec2-instances/) and install the dependencies:

   ```bash
   sudo apt-get update
   sudo apt install -y python3-pip nginx
   ```

3. Copy the app to the instance (`main.py`, `books.json`, `requirements.txt`) and install its requirements.
4. Add an NGINX site config. Replace the IP with your instance's public IP:

   ```bash
   sudo vim /etc/nginx/sites-enabled/fastapi_nginx
   ```

   ```
   server {
       listen 80;
       server_name <YOUR_EC2_IP>;
       location / {
           proxy_pass http://127.0.0.1:8000;
       }
   }
   ```

5. Restart NGINX and start FastAPI:

   ```bash
   sudo service nginx restart
   python3 -m uvicorn main:app
   ```

6. Allow HTTP traffic on port 80 in the instance's security group. Visit the public IP to reach the API.

## Deploy to AWS Lambda

Add a Lambda handler with Mangum:

```python
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)
```

Install the dependencies into a local folder, zip them, then add the app files:

```bash
pip install -t lib -r requirements.txt
(cd lib; zip ../lambda_function.zip -r .)
zip lambda_function.zip -u main.py
zip lambda_function.zip -u books.json
```

## Depends on

- An AWS account. Never commit your `.pem` key file.

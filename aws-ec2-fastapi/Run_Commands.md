# ## After connecting to the EC2 Instance

1. sudo apt-get update
2. sudo apt install -y python3-pip nginx
3. sudo vim /etc/nginx/sites-enabled/fastapi_nginx

   > server {
   > listen 80;
   > server_name 34.221.18.206;
   >
   > location / {
   > proxy_pass http://127.0.0.1:8000;
   > proxy_set_header Host $host;
   > proxy_set_header X-Real-IP $remote_addr;
   > proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
   > proxy_set_header X-Forwarded-Proto $scheme;
   > }
   > }
   >
4. sudo service nginx restart
5. git clone `<repo>`
6. curl http://127.0.0.1:8000

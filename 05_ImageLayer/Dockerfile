# 베이스 이미지
FROM ubuntu:latest

# nginx 설치
RUN apt-get update && \
apt-get install -y -q nginx

# 파일 복사
COPY index.html /usr/share/nginx/html

# nginx 시작
CMD ["nginx", "-g", "daemon off;"]


# 베이스 이미지
FROM ubuntu:22.04

# nginx 설치
RUN apt -y update && apt -y upgrade
RUN apt -y install nginx

# 포트 지정
EXPOSE 80

# 서버 실행(foreground 실행)
CMD ["nginx", "-g", "daemon off;"]
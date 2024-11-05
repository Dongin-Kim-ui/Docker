FROM golang:alpine AS builder

WORKDIR /go/src/app
COPY main.go .

RUN go mod init
RUN go build -o webserver .

FROM scratch
WORKDIR /app
COPY --from=builder /go/src/app/ /app/


CMD ["./webserver"]


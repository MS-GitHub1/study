import redis

def main():
    # 连接redis
    cli = redis.Redis(host="47.105.48.249",port=6379)
    cli.set("xiao","达到")
    print(cli.get("xiao").decode())

if __name__ == '__main__':
    main()
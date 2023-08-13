def requestArgs(url,headers,params,proxies):
    args = {'url':url}
    if(bool(headers)):
        args.update({'headers' : headers})
    if(bool(params)):
        args.update({'params' : params})
    if(bool(proxies)):
        print("hi")
        args.update({'proxies' : proxies})
    return args
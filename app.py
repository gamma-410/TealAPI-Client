import requests as req
from sys import argv
from fabric.colors import green, yellow, red

url = "https://teal-api.glitch.me"

email = ""
password = ""
user_id = ""


if argv[1] == "get":
    if argv[2] == "all":
        res = req.get(url + "/view").json()
        for i in res:
            print("\n")
            print(green("id: " + i["userid"]) +
                  " -- " + green(str(i["id"])) + "\n")
            if i["to"]:
                print(">>> " + str(i["to"]) + " へ送信\n")
            print("「" + i["tweet"] + "」")
            print("\n" + yellow(i["date"]) + " -- " +
                  red("❤️ " + str(i["like"])))
        print("\n")
    elif argv[2] == "tweets":
        res = req.get(url + "/view/" + argv[3]).json()
        for i in res:
            print("\n")
            print(green("id: " + i["userid"]) +
                  " -- " + green(str(i["id"])) + "\n")
            print("「" + i["tweet"] + "」")
            print("\n" + yellow(i["date"]) + " -- " +
                  red("❤️ " + str(i["like"])))
        print("\n")
    elif argv[2] == "tweet":
        res = req.get(url + "/view/" + argv[3] + "/" + argv[4]).json()
        for i in res:
            print("\n")
            print(green("id: " + i["userid"]) +
                  " -- " + green(str(i["id"])) + "\n")
            print("「" + i["tweet"] + "」")
            print("\n" + yellow(i["date"]) + " -- " +
                  red("❤️ " + str(i["like"])))
        print("\n")
    elif argv[2] == "users":
        res = req.get(url + "/users").json()
        for i in res:
            print("\n")
            print(green("id: " + i["userid"]) +
                    " -- " + green(str(i["id"])) + "\n")
            print("「" + i["detail"] + "」")
        print("\n")
    elif argv[2] == "user":
        res = req.get(url + "/user/" + argv[3]).json()
        print("\n")
        print(green("id: " + res["userid"]) +
                  " -- " + green(str(res["id"])) + "\n")
        print("「" + res["detail"] + "」")
        print("\n")



elif argv[1] == "post":
    if argv[2] == "change":
        params = {'email': email, 'password': password, 'detail': argv[3]}
        req.post(url + "/user/" + user_id, params=params)
    elif argv[2] == "signup":
        params = {'email': email, 'password': password, 'userid': user_id}
        req.post(url + "/signup", params=params)
    elif argv[2] == "new":
        params = {'email': email, 'password': password, 'text': argv[3]}
        req.post(url + "/new", params=params)
    elif argv[2] == "reply":
        params = {'email': email, 'password': password, 'reply': argv[3]}
        req.post(url + "/reply/" + argv[4], params=params)
    elif argv[2] == "like":
        req.post(url + "/like/" + argv[3])
    elif argv[2] == "delete":
        if argv[3] == "tweet":
            params = {'email': email, 'password': password}
            req.post(url + "/delete/tweet/" + user_id + "/" + argv[4], params=params)
        elif argv[3] == "user":
            params = {'email': email, 'password': password}
            req.post(url + "/delete/user/" + argv[4], params=params)

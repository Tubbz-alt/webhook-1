from requests import *; from time import sleep; from os import system


def main():
    limit = 0
    sent  = 0
    fail  = 0


    system(f'cls && title sent[{sent}] : rl\'d[{limit}] : failed[{fail}]')
    webhook = input('webhook: '); system('cls')


    if get(webhook).status_code == 200: pass 
    else: print('invalid webhook'); input('[enter] to return'); main()


    message = input('message: '); system('cls')


    _delete = input('delete: '); system('cls')


    try:
        while fail < 5:
            r = post(webhook, {"content": message})
            try:
                if r.json()["retry_after"]:
                    x = r.json()["retry_after"]

                    limit += 1
                    system(f'title sent[{sent}] : rl\'d[{limit}] : failed[{fail}]')

                    print(f'rl\'ed : time[{x / 1000}]s'); sleep(x / 1000)
            except:
                if r.status_code == 204:
                    sent += 1
                    system(f'title sent[{sent}] : rl\'d[{limit}] : failed[{fail}]')

                    print(f'sent : total[{sent}]')
                else:
                    fail += 1
                    system(f'title sent[{sent}] : rl\'d[{limit}] : failed[{fail}]')

                    print(f'failed : total[{fail}]')
    except KeyboardInterrupt:
        fail += 5


    if _delete == 'y': delete(webhook) 
    print('-' * 17, f'\ncompleted : sent[{sent}] : rl\'d[{limit}] : failed[{fail}]')
    input('[enter] to exit'); exit()


main()

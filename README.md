<br/>
<p align="center">
  <a>
    <img src="https://i.gyazo.com/1d637b0914c54b08ec8f04a83efabfa1.gif" width="582"/></a>
  </a>
  <h3 align="center">webhook-spam</h3>
  <p align="center">
    discord webhook-spam, extremely clean & easy-to-read code w/ a sigint handler & interactive title
  </p>
<p align="center">
  extremely simple concept, took no less than five minutes.
  </p>
</p>

#
#### sigint handler, usage:
since the webhook-spam is wrapped in a while loop, 

i've included a sigint handler to end the loop should the user press `CTRL+C` on their keyboard.
```
sent[1]
*CTRL+C*
-----------------
completed : sent[1] : rl'd[0] : failed[0]
```
#
comes with an interactive title,

rather than using `ctypes`, i've used the command-line method using `system` from the `os` lib in python.

every **request made** will be **logged**, including the **following**:
```
- HTTP / 204 : (sent)
- HTTP / 429 : (ratelimit)
- HTTP / NA  : (failure)
```
#
### requirements:
- prior knowledge using python3
- discord webhook, see [#resources]
### optional:
- vpn/proxy, see:
```
https://discord.com/developers/docs/topics/rate-limits
```
#
### setup:
- python3
- `requests`, `os`, `time`, install via pip:
```
ex:
pip install requests
```
- complete, launch the program via python3
#
### resources:
Python:
```
https://python.org/
```
Discord Webhook Documentation:
```
https://discord.com/developers/docs/resources/webhook
```

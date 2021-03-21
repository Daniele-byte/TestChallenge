import requests

PASTEBIN_API_KEY='flag{0h_n0_my_4p1_k3y}'

def capitalize(string: str):
    return input_string.upper()

def post_on_pastebin(string: str):
    data = {
        'api_option': 'paste',
        'api_dev_key': PASTEBIN_API_KEY,
        'api_paste_code': string,
    }
    r = requests.post('https://pastebin.com/api/api_post.php', data=data)
    return r.text

if __name__ == "__main__":
    print("Please give me a string!!!!")
    input_string = input()
    capitalized_string = capitalize(input_string)
    print("Here is your CAPITALIZED string!!! Enjoy ur day!! :D")
    print(capitalized_string)
    print("I also posted it on pastebin :o")
    t = post_on_pastebin(capitalized_string)
    print(t)


import requests, time, random, string; from pywebio.output import put_html; from pywebio.input import input, TEXT; from pywebio.platform.flask import start_server

c = 0
f = 0

def MyApp():
    global f
    global c
    user = input("Enter Instagram UserName:", type=TEXT)
    link = input("Enter Post Link:", type=TEXT)
    while True:
        email = f"{''.join(random.choices(string.ascii_lowercase, k=8))}{''.join(random.choices(string.ascii_lowercase + string.digits, k=10))}@{random.choice(['gmail.com'])}"
        req = requests.post("https://api.likesjet.com/freeboost/7", json={"link": link,"instagram_username": user,"email": email}).text
        if 'Success!' in req:
            c += 1
            put_html(f'<h3>✅ I Can Send Some Likes.</h3><i> BY: Team Whitehat</i>')
            time.sleep(0.1)
        elif 'once' in req:
         put_html(f'<h3>❌ You Can Send Likes Already.</h3><i> BY: Team whitehat</i>')
        else:
            f += 1
            put_html(f'<h3>❌ Error While Sending Likes.</h3><i> BY: Team whitehat</i>')
            time.sleep(0.1)

if __name__ == '__main__':
    start_server(MyApp, port=8086, debug=True)

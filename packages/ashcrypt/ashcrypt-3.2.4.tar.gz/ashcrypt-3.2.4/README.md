## Introducing Ashcrypt: Your Guardian of Secrets 🔒
Tired of wrestling with passwords and entrusting your private files to sketchy apps? Meet Ashcrypt – your ultimate solution to cloak your content from prying eyes. Imagine a world where your data is as secure as Fort Knox, yet easily accessible only by you. That's the power Ashcrypt brings to the table.

**Say goodbye to complexity:** Ashcrypt simplifies the intricate world of cryptography, making it incredibly straightforward to use. No more battling with cryptic code – just effective protection for your data. Experience the elegance of simplicity with Ashcrypt.

## 🛡️ Why Ashcrypt? Because Privacy Matters!
In a realm where digital security is everything, Ashcrypt stands tall as your reliable ally. Imagine being in charge, with no more concerns about leaky apps or exposed files.

Why did I create Ashcrypt? Simply put, I was fed up with the endless password shuffle and the constant unease about entrusting my private files to unverified apps. I wanted a solution that could shield my content effortlessly. And that's why Ashcrypt was born – a seamless way to safeguard your data from prying eyes. If you've ever felt the same, Ashcrypt is here for you.
## 📦 What's Under the Hood?
**Library:** Your path to seamless security. It's your companion for performing encryption and decryption on your data using the robust AES-256 (CBC) encryption algorithm. Designed with developers in mind, it makes data protection a breeze.

**App:** Where magic happens. A sleek, unified software solution merging the library's might into a user-friendly application. Whether you're a seasoned developer or just starting, this app is your ultimate ally.
## 🔑  Effortlessly Secure Encryption!
Worried about complex encryption steps? Don't worry! With Ashcrypt, encrypting a file is as simple as can be. Check this out:
```python
from ashcrypt import CryptFile

key = CryptFile.genkey()
CryptFile('passwords.csv', key).encrypt()
# Voila! Your file is now called ==> passwords.csv.crypt
```
## 💾 Secure Database Integration
Got valuable data you want to stash? Ashcrypt has your back:
```python
from ashcrypt import Crypt, CryptFile, Database

binary_data = CryptFile.get_binary('image.png')
key = Crypt.genkey()  # Get a key

encrypted_binary_data = Crypt(binary_data, key).encrypt(get_bytes=True)
conn = Database('data-holder.db')
conn.insert(name='image.png', content=encrypted_binary_data)
```
## 🚀 Or, Simplify with the App

![alt text](docs/assets/GUI.png)


## 🧙‍♂️ Installation Made Easy
Starting is a breeze. If you want to use Ashcrypt as a library, just use pip:
```python
pip install ashcrypt
```
Want the entire repository? Run this command for a simple setup:
```shell
curl -sSfL https://raw.githubusercontent.com/AshGw/ashcrypt/main/important/setup.sh | bash
```
## 📚 Dive into the Docs
I designed this documentation with simplicity in mind. Check out the Docs to unleash Ashcrypt's full potential.
## 🔐 License to Thrill
Ashcrypt is open-source and licensed under the MIT License.
## 🙌 Shout-Outs
Ashcrypt draws its strength from the robust cryptographic practices and the inspiration gleaned from a myriad of open-source implementations. Yet, it stands tall on the shoulders of one true heavyweight – the renowned 'cryptography' library. With 'cryptography' as its bedrock, Ashcrypt ensures your data's safety isn't a matter of chance but a guarantee.

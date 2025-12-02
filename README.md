# CyberWebTool
A cybersecurity tool to exploit vulnerabilites found in the OWASP Juice Shop website (v19.1.0).<br>

## Use Cases (and associated OWASP JS Achievements):
1. Injection - Login Admin
2. XSS - DOM XSS
3. Broken Access Control - View Basket
4. Improper Input Validation - Zero Stars
5. Broken Authentication - Password Strength

## Developed with JuiceShop
This application was developed with the OWASP Juice Shop website in order to test capabilities. I recommend using the docker image for further development / testing.<br>
[Download/Setup JuiceShop](https://github.com/juice-shop/juice-shop?tab=readme-ov-file#from-sources)<br>
[Download Docker](https://www.docker.com/)<br>

## Juice Shop Docker Setup
Run the following after installing docker to download Juice Shop: `docker pull bkimminich/juice-shop`<br>
Run the following to run the Juice Shop: `docker run --rm -p 127.0.0.1:3000:3000 bkimminich/juice-shop`<br>
Navigate to [http://localhost:3000](http://localhost:3000) to access Juice Shop.<br>

## Use:
1. Open the Juice Shop in your chosen way (Docker is the recommened way) and leave the default port.<br>
2. Ensure Firefox is downloaded<br>
3. Install the required packages:<br>
`pip install -r requirements.txt`<br>
4. Run the exploits:<br>
`python3 .\CyberWebTool.py` (Windows)<br>
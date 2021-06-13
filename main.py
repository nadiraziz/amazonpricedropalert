from bs4 import BeautifulSoup
import requests
import smtplib
URL = "https://www.amazon.in/gp/product/B086984LJ3/ref=s9_acss_bw_cg_top_2a1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-4&pf_rd_r=KHA3SE5G3PM8PJ2K5AQ8&pf_rd_t=101&pf_rd_p=59313b9b-3f6b-46ea-9915-9c9d0a78c00b&pf_rd_i=26313569031"


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Accept-Language": "en-US,en;q=0.5",
}

response = requests.get(URL, headers=header)
price_webpage = response.text

soup = BeautifulSoup(price_webpage, "html.parser")

price = soup.find(id="priceblock_ourprice").get_text()
price = price.replace('₹\xa0', '')
price = price.replace('.00', '')
price = price.replace(',', '')
price_as_float = float(price)
print(float(price))

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 11000

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login("nadirazizyah@gmail.com", "Azeez@7505")
        connection.sendmail(
            from_addr="nadiraziziyah@gmail.com",
            to_addrs="nadiraziz930@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}"
        )
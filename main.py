# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Selenium WebDriver Chrome options configuration for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode (without opening a window)
chrome_options.add_argument("--window-size=1920x1080")  # Set the window size

# Initialize the WebDriver with the specified options
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the URL of the dollar exchange rate page
driver.get('https://economia.uol.com.br/cotacoes/cambio/')

# Fetch the dollar quote element and format the text
dollar_quote_element = driver.find_element(By.CSS_SELECTOR, 'body > div.exchange-page > article > div:nth-child(2) > div > div.col-sm-24.col-md-16.col-lg-17.content-article > div > div > div.image-content-pad > div.slot-c > div > div > div > div.chart-header > div.chart-info.row.ng-scope > div.chart-info-buy.col-sm-5.col-xs-2.no-gutter-xs > div > span.chart-info-val.ng-binding').text
dollar_quote = dollar_quote_element.replace(",", ".")  # Replace comma with dot for float conversion
dollar_quote = "{:.2f}".format(float(dollar_quote))  # Format to two decimal places

# Fetch the dollar variation
dollar_variation = driver.find_element(By.CSS_SELECTOR, 'body > div.header-slot > div > div > section.currencies > div:nth-child(1) > a > div > span.data.pos').text

# Print fetched data
print(dollar_quote)
print(dollar_variation)

# Fetch Bovespa index points and variation
bovespa_points = driver.find_element(By.CSS_SELECTOR, 'body > div.header-slot > div > div > section.stock > div > a > div > span.value.pts').text
bovespa_variation = driver.find_element(By.CSS_SELECTOR, 'body > div.header-slot > div > div > section.stock > div > a > div > span.data.neg').text

# Print fetched data
print(bovespa_points)
print(bovespa_variation)

# Fetch the last update time and modify its text
last_update_element = driver.find_element(By.CSS_SELECTOR, 'body > div.exchange-page > article > div:nth-child(2) > div > div.col-sm-24.col-md-16.col-lg-17.content-article > div > div > div.image-content-pad > div.slot-c > div > div > div > div.chart-header > div.chart-upd.row > span').text
last_update = last_update_element.replace("Última atualização", "Last Update")

# Print the last update
print(last_update)

# Close the browser
driver.quit()

# Function to apply color based on the variation value
def apply_color(variation):
    if '-' in variation:
        return f'<span style="color: red;">{variation}%</span>'  # Negative variation in red
    else:
        return f'<span style="color: green;">{variation}%</span>'  # Positive variation in green

# Apply the color function to dollar and Bovespa variations
dollar_variation_colored = apply_color(dollar_variation)
bovespa_variation_colored = apply_color(bovespa_variation)

# Construct the email body with HTML content
email_body = f"""
<html>
<body>
    <div class="container" style="font-family: Arial, sans-serif; margin: 0 auto; padding: 20px; max-width: 600px; border: 1px solid #ccc; border-radius: 10px;">
        <h2>Daily Financial Update</h2>
        <div class="info">
            <p>Dollar exchange rate: <span style="font-weight: bold;">${dollar_quote}</span></p>
            <p>Dollar Variation: {dollar_variation_colored}</p>
        </div>
        <div class="info">
            <p>Bovespa score: <span style="font-weight: bold;">{bovespa_points}</span></p>
            <p>Bovespa Variation: {bovespa_variation_colored}</p>
        </div>
        <p>{last_update}</p>
    </div>
</body>
</html>
"""

# Setup the MIME multipart message and set the email details
msg = MIMEMultipart()
msg['Subject'] = "Daily Financial Update :-)"
msg['From'] = "teste.miguelmarsico.com@gmail.com"
msg['To'] = "teste.miguelmarsico.com@gmail.com"
password = 'alarakcwyycuwucm'  # It's recommended to use environment variables or secure methods to store passwords
msg.attach(MIMEText(email_body, 'html'))  # Attach the HTML content

# Login and send the email
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()  # Start TLS encryption
s.login(msg['From'], password)
s.sendmail(msg['From'], [msg['To']], msg.as_string())
print('Email sent')

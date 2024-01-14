import pyshorteners

def shorten_url(url):
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(url)
    return shortened_url

# Example
original_url = "https://www.amazon.in/Lava-Blaze-5G-Blue-Expandable/dp/B0CBRN65NP?ref_=Oct_DLandingS_D_7c3acb5c_0"
short_url = shorten_url(original_url)
print(f"Original URL: {original_url}")
print(f"Shortened URL: {short_url}")
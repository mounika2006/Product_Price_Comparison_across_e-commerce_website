# # # # import requests
# # # # from typing import Dict, List, Optional
# # # # import re



# # # # class FlipkartPriceFetcher:
# # # #     def __init__(self, serpapi_key: str):
# # # #         self.api_key = serpapi_key
# # # #         self.base_url = "https://serpapi.com/search.json"
   
# # # #     def fetch_prices(self, query: str, max_results: int = 5) -> List[Dict]:
# # # #         params = {
# # # #             "engine": "google_shopping",
# # # #             "q": f"{query} flipkart",
# # # #             "gl": "in",
# # # #             "google_domain": "google.co.in",
# # # #             "api_key": self.api_key,
# # # #             "num": max_results,
# # # #             "tbs": "ecom:1"
# # # #         }
       
# # # #         try:
# # # #             response = requests.get(self.base_url, params=params)
# # # #             data = response.json()
           
# # # #             products = []
# # # #             for product in data.get('shopping_results', []):
# # # #                 price_data = product.get('price_data', {})
# # # #                 price_str = product.get('price', '')
               
# # # #                 price = 0
# # # #                 if price_data.get('value'):
# # # #                     price = float(price_data['value'])
# # # #                 elif price_str:
# # # #                     price_match = re.search(r'₹?([\d,]+)', price_str)
# # # #                     if price_match:
# # # #                         price = float(price_match.group(1).replace(',', ''))
               
# # # #                 if price > 0:
# # # #                     products.append({
# # # #                         'price': price,
# # # #                         'link': product.get('link', ''),
# # # #                         'name': product.get('title', '')[:80]
# # # #                     })
# # # #             return products
# # # #         except Exception as e:
# # # #             print(f"Error: {e}")
# # # #             return []
   
# # # #     def get_lowest_price(self, query: str, max_results: int = 5) -> Optional[Dict]:
# # # #         """Returns only the product with the lowest price."""
# # # #         products = self.fetch_prices(query, max_results)
# # # #         if not products:
# # # #             print("No products found.")
# # # #             return None
       
# # # #         # Find the product with minimum price
# # # #         lowest = min(products, key=lambda x: x['price'])
# # # #         return lowest
   
# # # #     def print_lowest_price(self, query: str, max_results: int = 5):
# # # #         """Clean output: Only the lowest price + link."""
# # # #         lowest = self.get_lowest_price(query, max_results)
# # # #         if not lowest:
# # # #             return
       
# # # #         print(f"\n🏆 Lowest Flipkart Price: ₹{lowest['price']:,.0f}")
# # # #         print(f"   📱 {lowest['link']}")
# # # #         print(f"   ({lowest['name']})\n")



# # # # # SIMPLE USAGE - Just product name input
# # # # if __name__ == "__main__":
# # # #     API_KEY = "913baa38df89f798c36d1060941926131a709a8bfa44a2247f47d6dd21e1de17"  # Your existing key
   
# # # #     fetcher = FlipkartPriceFetcher(API_KEY)
   
# # # #     # User input or test
# # # #     product_name = input("Enter product name (or 'refrigerator' for test): ").strip()
# # # #     if not product_name:
# # # #         product_name = "refrigerator under 10000"  # Default test
   
# # # #     print(f"🔍 Searching Flipkart: {product_name}")
   
# # # #     # Use the new lowest price method
# # # #     fetcher.print_lowest_price(product_name)









# # ........................................................................................................

# import requests
# from typing import Dict, List, Optional
# import re

# class FlipkartPriceFetcher:
#     def __init__(self, serpapi_key: str):
#         self.api_key = serpapi_key
#         self.base_url = "https://serpapi.com/search.json"
   
#     def fetch_prices(self, query: str, max_results: int = 10) -> List[Dict]:
#         params = {
#             "engine": "google_shopping",
#             "q": f"{query} flipkart",
#             "gl": "in",
#             "google_domain": "google.co.in",
#             "api_key": self.api_key,
#             "num": max_results,
#             "tbs": "ecom:1"
#         }
      
#         try:
#             response = requests.get(self.base_url, params=params)
#             data = response.json()
          
#             products = []
#             for product in data.get('shopping_results', []):
#                 price_data = product.get('price_data', {})
#                 price_str = product.get('price', '')
              
#                 price = 0
#                 if price_data.get('value'):
#                     price = float(price_data['value'])
#                 elif price_str:
#                     price_match = re.search(r'₹?([\d,]+\.?\d*)', price_str)
#                     if price_match:
#                         price = float(price_match.group(1).replace(',', ''))
                
#                 # Extract rating (handles different formats)
#                 rating = product.get('rating', 0.0)
#                 if isinstance(rating, str):
#                     rating_match = re.search(r'(\d+\.?\d*)', rating)
#                     rating = float(rating_match.group(1)) if rating_match else 0.0
                
#                 # Extract shipping info
#                 shipping = "Free Shipping" if product.get('shipping') else "Check Shipping"
#                 delivery = product.get('delivery', shipping)
                
#                 if price > 0:
#                     products.append({
#                         'price': price,
#                         'link': product.get('link', ''),
#                         'name': product.get('title', '')[:80],
#                         'rating': rating,
#                         'shipping': delivery or shipping,
#                         'reviews': product.get('reviews_count', 0)
#                     })
            
#             # Sort by price (lowest first)
#             products.sort(key=lambda x: x['price'])
#             return products
#         except Exception as e:
#             print(f"Error: {e}")
#             return []
   
#     def get_lowest_price(self, query: str, max_results: int = 10) -> Optional[Dict]:
#         products = self.fetch_prices(query, max_results)
#         return products[0] if products else None
   
#     def print_lowest_price(self, query: str, max_results: int = 10):
#         lowest = self.get_lowest_price(query, max_results)
#         if not lowest:
#             print("❌ No Flipkart products found.")
#             return
        
#         print(f"\n🏆 LOWEST FLIPKART DEAL FOUND!")
#         print(f"   💰 Price: ₹{lowest['price']:,.0f}")
#         print(f"   ⭐ Rating: 4.2/5 (53 reviews)")
#         print(f"   🚚 Shipping: {lowest['shipping']}")
#         print(f"   📱 Buy Now: https://www.flipkart.com/{lowest['name']}")
#         print(f"   📦 Product: {lowest['name']}")
#         print("\n" + "="*60)

# # USAGE - Same as before
# if __name__ == "__main__":
#     API_KEY = "0c64bffa3140c19ac328ccb2f02f10c6b7ec8fbfa9e6bd58fd6899a0a6279a2e"
   
#     fetcher = FlipkartPriceFetcher(API_KEY)
   
#     product_name = input("Enter product name (or 'refrigerator' for test): ").strip()
#     if not product_name:
#         product_name = "refrigerator under 10000"
   
#     print(f"🔍 Searching Flipkart: {product_name}")
#     fetcher.print_lowest_price(product_name)
# # ...................................................................................................


# # from selenium import webdriver
# # from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.chrome.options import Options
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # from webdriver_manager.chrome import ChromeDriverManager
# # import time
# # import re

# # def extract_price(text):
# #     if not text:
# #         return None
# #     # Matches "₹12,999", "₹ 500", "Rs. 1200"
# #     m = re.search(r'(₹|Rs\.?)\s?([\d,]+)', text)
# #     if not m:
# #         return None
# #     return float(m.group(2).replace(',', ''))

# # def get_flipkart_lowest_price(product_name):
# #     options = Options()
# #     # ❌ DISABLE HEADLESS for debugging (so you can see if a CAPTCHA appears)
# #     # options.add_argument("--headless=new") 
# #     options.add_argument("--window-size=1920,1080")
    
# #     # 🔥 STRONG ANTI-DETECTION
# #     options.add_argument("--disable-blink-features=AutomationControlled")
# #     options.add_experimental_option("excludeSwitches", ["enable-automation"])
# #     options.add_experimental_option('useAutomationExtension', False)
# #     options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

# #     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
# #     # Overwrite the navigator.webdriver property to hide Selenium
# #     driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

# #     url = f"https://www.flipkart.com/search?q={product_name}&sort=price_asc"
# #     print(f"Searching: {url}")
# #     driver.get(url)

# #     products = []

# #     try:
# #         wait = WebDriverWait(driver, 15)
        
# #         # 1. Attempt to Close Login Popup (Generic approach)
# #         try:
# #             # Wait a moment for popup
# #             time.sleep(2) 
# #             # Click the 'X' button if it exists (usually has text '✕' or specific class)
# #             close_btn = driver.find_element(By.XPATH, "//button[contains(text(), '✕')]")
# #             close_btn.click()
# #             print("Login popup closed.")
# #         except:
# #             pass # No popup

# #         # 2. Universal Selector Strategy: Look for `data-id`
# #         # Flipkart puts a 'data-id' attribute on EVERY product card, regardless of layout.
# #         wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-id]")))
        
# #         # Scroll to trigger lazy loading
# #         driver.execute_script("window.scrollTo(0, 500);")
# #         time.sleep(1)

# #         # Get all containers with a data-id
# #         cards = driver.find_elements(By.XPATH, "//div[@data-id]")
# #         print(f"Found {len(cards)} potential product cards.")

# #         for card in cards:
# #             try:
# #                 # Get the whole text of the card to quickly check if it has a price
# #                 card_text = card.text
# #                 if "₹" not in card_text:
# #                     continue

# #                 # --- Extract Link ---
# #                 # Find the first <a> tag inside this card
# #                 link_el = card.find_element(By.TAG_NAME, "a")
# #                 link = link_el.get_attribute("href")
                
# #                 # --- Extract Title ---
# #                 # Usually the link has an 'aria-label' or 'title', or we grab the text of a div inside
# #                 title = ""
# #                 try:
# #                     # Try finding the main title class (often has generic class names, so we try multiple)
# #                     # Strategy: Find the image, its alt text is often the title
# #                     img = card.find_element(By.TAG_NAME, "img")
# #                     title = img.get_attribute("alt")
# #                 except:
# #                     # Fallback: use link text
# #                     title = link_el.text

# #                 # --- Extract Price ---
# #                 # Look for the specific price symbol inside this card
# #                 price = extract_price(card_text)

# #                 if price and title and link:
# #                      # Filter out accessories (often irrelevant cheap items appear in search)
# #                     if price < 50: 
# #                         continue

# #                     products.append({
# #                         "title": title,
# #                         "price": price,
# #                         "link": link
# #                     })

# #             except Exception:
# #                 continue

# #     except Exception as e:
# #         print(f"Scraping failed (Check browser for CAPTCHA): {e}")
# #         # Optional: input("Press Enter to close browser...") # Uncomment to keep browser open on error
# #     finally:
# #         driver.quit()

# #     if not products:
# #         return None

# #     # Sort and return lowest
# #     products.sort(key=lambda x: x["price"])
# #     return products[0]

# # # --- WRAPPER FUNCTION ---
# # def get_flipkart_price(product_name):
# #     result = get_flipkart_lowest_price(product_name)

# #     if not result:
# #         return {
# #             "success": False,
# #             "price": "No products found",
# #             "link": f"https://www.flipkart.com/search?q={product_name}"
# #         }

# #     return {
# #         "success": True,
# #         "price": f"₹{int(result['price'])}",
# #         "price_value": result["price"],
# #         "title": result["title"],
# #         "link": result["link"]
# #     }

# # if __name__ == "__main__":
# #     item = "mouse"
# #     print(get_flipkart_price(item))




# # import undetected_chromedriver as uc
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # import time
# # import re

# # def extract_price(text):
# #     if not text:
# #         return None
# #     m = re.search(r'(₹|Rs\.?)\s?([\d,]+)', text)
# #     if not m:
# #         return None
# #     return float(m.group(2).replace(',', ''))

# # def get_flipkart_lowest_price(product_name):
# #     # Setup Options
# #     options = uc.ChromeOptions()
# #     options.add_argument("--disable-gpu")
# #     options.add_argument("--window-size=1920,1080")
# #     options.add_argument("--no-sandbox")
    
# #     # 🔥 HEADLESS MODE (Runs hidden)
# #     # We use '--headless=new' which is less detectable than the old method
# #     options.add_argument("--headless=new")

# #     print(f"Initializing hidden browser for '{product_name}'...")
    
# #     # Initialize Undetected Chrome
# #     # headless=True is required here for the patcher to work correctly in background
# #     driver = uc.Chrome(options=options, headless=True, use_subprocess=False)

# #     url = f"https://www.flipkart.com/search?q={product_name}&sort=price_asc"
# #     products = []

# #     try:
# #         driver.get(url)
# #         wait = WebDriverWait(driver, 20)
        
# #         # 1. Check if blocked
# #         try:
# #             wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-id]")))
# #         except:
# #             print("⚠️ Flipkart blocked the headless request or page failed to load.")
# #             driver.quit()
# #             return None

# #         # 2. Scroll silently
# #         driver.execute_script("window.scrollBy(0, 800);")
# #         time.sleep(2)

# #         # 3. Scrape
# #         cards = driver.find_elements(By.XPATH, "//div[@data-id]")
        
# #         for card in cards:
# #             try:
# #                 text_content = card.text
# #                 price = extract_price(text_content)
                
# #                 if not price or price < 50:
# #                     continue

# #                 # Link
# #                 link_el = card.find_element(By.TAG_NAME, "a")
# #                 link = link_el.get_attribute("href")

# #                 # Title
# #                 try:
# #                     img = card.find_element(By.TAG_NAME, "img")
# #                     title = img.get_attribute("alt")
# #                 except:
# #                     title = link_el.text.split('\n')[0]

# #                 # Rating
# #                 rating = "N/A"
# #                 if "★" in text_content:
# #                     rm = re.search(r'(\d\.\d)\s?★', text_content)
# #                     if rm:
# #                         rating = rm.group(1)

# #                 products.append({
# #                     "title": title,
# #                     "price": price,
# #                     "rating": rating,
# #                     "link": link
# #                 })
# #             except:
# #                 continue

# #     except Exception as e:
# #         print(f"Error: {e}")
# #     finally:
# #         driver.quit()

# #     if not products:
# #         return None

# #     products.sort(key=lambda x: x["price"])
# #     return products[0]

# # def get_flipkart_price(product_name):
# #     try:
# #         result = get_flipkart_lowest_price(product_name)
        
# #         if not result:
# #             return {
# #                 "success": False,
# #                 "price": "No products found",
# #                 "link": f"https://www.flipkart.com/search?q={product_name}"
# #             }

# #         return {
# #             "success": True,
# #             "price": f"₹{int(result['price'])}",
# #             "price_value": result["price"],
# #             "title": result["title"],
# #             "rating": result["rating"],
# #             "link": result["link"]
# #         }
# #     except Exception as e:
# #         return {"success": False, "price": "Error", "link": ""}

# # # --- TEST BLOCK ---
# # if __name__ == "__main__":
# #     item = "refrigerator"
# #     print("Running in background (this may take 10-15 seconds)...")
# #     data = get_flipkart_price(item)
    
# #     if data["success"]:
# #         print(f"✅ Found Cheapest '{item}':")
# #         print(f"Title:  {data['title']}")
# #         print(f"Price:  {data['price']}")
# #         print(f"Link:   {data['link']}")
# #     else:
# #         print("❌ Product not found.")







# # import undetected_chromedriver as uc
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # import time
# # import re
# # import sys
# # import os

# # # Try importing BeautifulSoup for better parsing
# # try:
# #     from bs4 import BeautifulSoup
# #     HAS_BS4 = True
# # except ImportError:
# #     HAS_BS4 = False
# #     print("⚠️ Recommendation: Run 'pip install beautifulsoup4' for better accuracy.")

# # # ==========================================
# # # 🔧 PATCH: Silence 'WinError 6'
# # # ==========================================
# # def safe_del(self):
# #     try:
# #         self.quit()
# #     except:
# #         pass
# # uc.Chrome.__del__ = safe_del
# # # ==========================================

# # def extract_price(text):
# #     if not text: return None
# #     m = re.search(r'(₹|Rs\.?)\s?([\d,]+)', text)
# #     if not m: return None
# #     return float(m.group(2).replace(',', ''))

# # def get_flipkart_lowest_price(product_name):
# #     options = uc.ChromeOptions()
# #     options.add_argument("--disable-gpu")
# #     options.add_argument("--no-sandbox")
# #     options.add_argument("--headless=new") 
# #     options.add_argument("--blink-settings=imagesEnabled=false") 

# #     print(f"Initializing hidden browser for '{product_name}'...")
    
# #     driver = None
# #     try:
# #         driver = uc.Chrome(options=options, headless=True, use_subprocess=False)
        
# #         url = f"https://www.flipkart.com/search?q={product_name}&sort=price_asc"
# #         driver.get(url)
        
# #         wait = WebDriverWait(driver, 10)
# #         try:
# #             wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-id]")))
# #         except:
# #             print("⚠️ Flipkart blocked the request or page failed to load.")
# #             return None

# #         # Scroll to ensure text loads
# #         driver.execute_script("window.scrollBy(0, 500);")
# #         time.sleep(2)

# #         # Get the PAGE SOURCE and parse with BeautifulSoup (More reliable than Selenium text)
# #         if HAS_BS4:
# #             soup = BeautifulSoup(driver.page_source, 'html.parser')
# #             # Find all product cards (attributes with data-id)
# #             cards = soup.find_all('div', attrs={'data-id': True})
# #         else:
# #             # Fallback to Selenium elements if BS4 is missing
# #             cards = driver.find_elements(By.XPATH, "//div[@data-id]")

# #         products = []

# #         for card in cards:
# #             try:
# #                 # --- TEXT EXTRACTION ---
# #                 if HAS_BS4:
# #                     full_text = card.get_text(" ", strip=True) # Join with space
# #                     html_content = str(card)
# #                 else:
# #                     full_text = card.text.replace("\n", " ")
# #                     html_content = full_text

# #                 price = extract_price(full_text)
                
# #                 if not price or price < 50:
# #                     continue

# #                 # 1. LINK & TITLE
# #                 if HAS_BS4:
# #                     link_tag = card.find('a')
# #                     link = "https://www.flipkart.com" + link_tag['href'] if link_tag else ""
                    
# #                     img_tag = card.find('img')
# #                     title = img_tag['alt'] if img_tag and 'alt' in img_tag.attrs else full_text[:50]
# #                 else:
# #                     link_el = card.find_element(By.TAG_NAME, "a")
# #                     link = link_el.get_attribute("href")
# #                     title = full_text.split('\n')[0]

# #                 # 2. REVIEWS (We use this to find the Rating!)
# #                 # Matches: (2,962)
# #                 reviews = "0"
# #                 reviews_match = re.search(r'\(([\d,]+)\)', full_text)
                
# #                 # 3. RATING (Relative Logic)
# #                 rating = "N/A"
                
# #                 # Logic: If we found reviews "(2962)", the rating number is usually 
# #                 # strictly numbers like "3.9" or "4.2" just BEFORE it.
# #                 if reviews_match:
# #                     reviews = reviews_match.group(1)
                    
# #                     # Look for a number between 1.0 and 5.0 appearing BEFORE the reviews count
# #                     # Regex: Find "d.d" followed optionally by a Star, then space, then the bracket
# #                     # Example text: "4.2 ★ (2,962)" or "4.2 (2,962)"
# #                     rating_search = re.search(r'([1-5]\.\d)\s*★?\s*\(', full_text)
# #                     if rating_search:
# #                         rating = rating_search.group(1)
                
# #                 # Fallback: Just look for any "d.d" floating text if 'N/A'
# #                 if rating == "N/A":
# #                      # Look for the green badge specifically (Class often XQDdHH)
# #                      if HAS_BS4:
# #                          badge = card.find(class_=re.compile(r'(XQDdHH|_3LWZlK)'))
# #                          if badge:
# #                              rating = badge.get_text(strip=True)

# #                 # 4. DELIVERY
# #                 delivery = "Check details"
                
# #                 # Search specific phrases in the full text string
# #                 if "Free delivery" in full_text:
# #                     delivery = "Free delivery"
# #                 elif "Delivery by" in full_text:
# #                     # Try to capture "Delivery by 19 Dec"
# #                     match = re.search(r'(Delivery by.*?\d{1,2}\s[A-Za-z]{3})', full_text)
# #                     if match:
# #                         delivery = match.group(1)
# #                     else:
# #                         delivery = "Delivery info available"
                
# #                 # If guest mode hides the date, try to find "Today" or "Tomorrow"
# #                 if delivery == "Check details":
# #                     if "Tomorrow" in full_text:
# #                         delivery = "Delivery Tomorrow"
# #                     elif "Today" in full_text:
# #                         delivery = "Delivery Today"

# #                 products.append({
# #                     "title": title,
# #                     "price": price,
# #                     "rating": rating,
# #                     "reviews": reviews,
# #                     "delivery": delivery,
# #                     "link": link
# #                 })

# #             except Exception:
# #                 continue

# #         if not products:
# #             return None

# #         products.sort(key=lambda x: x["price"])
# #         return products[0]

# #     except Exception as e:
# #         print(f"Error: {e}")
# #         return None
# #     finally:
# #         if driver:
# #             try:
# #                 driver.quit()
# #             except:
# #                 pass

# # def get_flipkart_price(product_name):
# #     result = get_flipkart_lowest_price(product_name)
    
# #     if not result:
# #         return {
# #             "success": False,
# #             "price": "No products found",
# #             "link": f"https://www.flipkart.com/search?q={product_name}",
# #             "title": product_name,
# #             "rating": "N/A",
# #             "reviews": "0",
# #             "delivery": "N/A"
# #         }

# #     return {
# #         "success": True,
# #         "price": f"₹{int(result['price'])}",
# #         "price_value": result["price"],
# #         "title": result["title"],
# #         "rating": result["rating"], 
# #         "reviews": result["reviews"], 
# #         "delivery": result["delivery"],
# #         "link": result["link"]
# #     }

# # if __name__ == "__main__":
# #     item = "mouse"
# #     print(f"Searching for '{item}'...")
# #     data = get_flipkart_price(item)
    
# #     if data["success"]:
# #         print(f"\n✅ SUCCESS:")
# #         print(f"Title:    {data['title']}")
# #         print(f"Price:    {data['price']}")
# #         print(f"Rating:   {data['rating']}")
# #         print(f"Reviews:  {data['reviews']}")
# #         print(f"Delivery: {data['delivery']}")
# #         print(f"Link:     {data['link']}")
# #     else:
# #         print("❌ Not found")










# # from playwright.sync_api import sync_playwright
# # import time
# # import re

# # def scrape_flipkart_single_product(product_name):
# #     url = f"https://www.flipkart.com/search?q={product_name}"

# #     print(f"Flipkart: Searching for {product_name}")
# #     print(f"Flipkart: URL = {url}")

# #     with sync_playwright() as p:
# #         browser = p.chromium.launch(headless=True)
# #         context = browser.new_context(
# #             viewport={"width": 1366, "height": 768},
# #             user_agent=(
# #                 "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
# #                 "AppleWebKit/537.36 (KHTML, like Gecko) "
# #                 "Chrome/120.0.0.0 Safari/537.36"
# #             )
# #         )
# #         page = context.new_page()
# #         page.goto(url, timeout=60000)

# #         # Close login popup
# #         try:
# #             page.click("button._2KpZ6l._2doB4z", timeout=5000)
# #         except:
# #             pass

# #         # Wait for products to render
# #         page.wait_for_selector("div[data-id]", timeout=20000)

# #         cards = page.locator("div[data-id]")
# #         count = cards.count()
# #         print(f"Flipkart: Found {count} products")

# #         results = []

# #         for i in range(min(count, 10)):
# #             card = cards.nth(i)

# #             try:
# #                 title = card.locator("a, div").first.inner_text(timeout=2000)

# #                 price_text = card.locator("text=/₹/").first.inner_text(timeout=2000)
# #                 price_value = int(re.sub(r"[^\d]", "", price_text))

# #                 link = card.locator("a").first.get_attribute("href")
# #                 product_url = "https://www.flipkart.com" + link if link else url

# #                 results.append({
# #                     "price": f"₹{price_value}",
# #                     "price_value": price_value,
# #                     "product_name": title.strip(),
# #                     "buy_url": product_url
# #                 })

# #                 print(f"Flipkart: ✅ ₹{price_value} - {title[:40]}")

# #             except:
# #                 continue

# #         browser.close()

# #     if not results:
# #         return {
# #             "platform": "Flipkart",
# #             "product_name": product_name,
# #             "available": False
# #         }

# #     results.sort(key=lambda x: x["price_value"])
# #     cheapest = results[0]

# #     return {
# #         "platform": "Flipkart",
# #         "product_name": cheapest["product_name"],
# #         "price": cheapest["price"],
# #         "product_url": cheapest["buy_url"],
# #         "available": True
# #     }


# # # ---------------- TEST ----------------
# # if __name__ == "__main__":
# #     result = scrape_flipkart_single_product("mouse")

# #     print("\n" + "=" * 80)
# #     print(f"Platform : {result['platform']}")
# #     print(f"Product  : {result.get('product_name')}")
# #     print(f"Price    : {result.get('price')}")
# #     print(f"Link     : {result.get('product_url')}")
# #     print(f"Available: {result['available']}")







import requests
from typing import Dict, List, Optional
import re
from urllib.parse import urlparse, parse_qs, unquote


class FlipkartPriceFetcher:
    def __init__(self, serpapi_key: str):
        self.api_key = serpapi_key
        self.base_url = "https://serpapi.com/search.json"
   
    def extract_flipkart_product_id(self, link: str) -> str:
        """Extract Flipkart product ID from Google Shopping link - Enhanced"""
        try:
            # Direct Flipkart links first
            flipkart_pid_match = re.search(r'pid=([a-zA-Z0-9]{14,})', link)
            if flipkart_pid_match:
                return flipkart_pid_match.group(1)
            
            # Direct path product ID
            path_pid = re.search(r'/([a-zA-Z0-9]{14,})/?', link)
            if path_pid:
                return path_pid.group(1)
            
            # Google Shopping udata params (enhanced patterns)
            parsed = urlparse(link)
            query_params = parse_qs(parsed.query)
            
            if 'udata' in query_params:
                udata = unquote(query_params['udata'][0])
                # Multiple enhanced patterns for Flipkart PID in udata
                pid_patterns = [
                    r'pid=([a-zA-Z0-9]{14,})',
                    r'\/([a-zA-Z0-9]{14,})\?',
                    r'([a-zA-Z0-9]{14,})(?=&|\s|"|\')',
                    r'id=([a-zA-Z0-9]{14,})',
                    r'([a-zA-Z0-9]{14,})(?=\?|\/|&)'
                ]
                for pattern in pid_patterns:
                    match = re.search(pattern, udata, re.IGNORECASE)
                    if match:
                        return match.group(1)
            
            # Check source HTML or other params
            source_match = re.search(r'source=flipkart.*?([a-zA-Z0-9]{14,})', link, re.IGNORECASE)
            if source_match:
                return source_match.group(1)
                
            return ""
        except:
            return ""
    
    def get_flipkart_product_url(self, product_id: str, product_name: str) -> str:
        """Generate direct Flipkart product URL from product ID"""
        if not product_id or len(product_id) < 14:
            # Enhanced search link with exact product name
            safe_query = re.sub(r'[^\w\s]', ' ', product_name).strip()
            encoded_query = '+'.join(safe_query.split())
            return f"https://www.flipkart.com/search?q={encoded_query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
        return f"https://www.flipkart.com/{product_id}?pid={product_id}"
    
    def fetch_prices(self, query: str, max_results: int = 10) -> List[Dict]:
        params = {
            "engine": "google_shopping",
            "q": f"{query} flipkart",
            "gl": "in",
            "google_domain": "google.co.in",
            "api_key": self.api_key,
            "num": max_results,
            "tbs": "ecom:1"
        }
     
        try:
            response = requests.get(self.base_url, params=params)
            data = response.json()
         
            products = []
            for product in data.get('shopping_results', []):
                price_data = product.get('price_data', {})
                price_str = product.get('price', '')
             
                price = 0
                if price_data.get('value'):
                    price = float(price_data['value'])
                elif price_str:
                    price_match = re.search(r'₹?([\d,]+\.?\d*)', price_str)
                    if price_match:
                        price = float(price_match.group(1).replace(',', ''))
                
                # CORRECTED RATING EXTRACTION - No hardcoded values
                rating = 0.0
                reviews_count = 0
                
                # Method 1: Direct rating field
                rating_raw = product.get('rating')
                if rating_raw is not None:
                    if isinstance(rating_raw, (int, float)):
                        rating = float(rating_raw)
                    elif isinstance(rating_raw, str) and rating_raw.strip():
                        rating_match = re.search(r'(\d+\.?\d*)', rating_raw)
                        if rating_match:
                            rating = float(rating_match.group(1))
                
                # Method 2: reviews field
                reviews_raw = product.get('reviews')
                if reviews_raw and rating == 0.0:
                    if isinstance(reviews_raw, str):
                        # "4.6 (123 ratings)" format
                        combined_match = re.search(r'(\d+\.?\d*)\s*\(?\s*(\d+)', reviews_raw)
                        if combined_match:
                            rating = float(combined_match.group(1))
                            reviews_count = int(combined_match.group(2))
                
                # Method 3: reviews_count field
                reviews_count_raw = product.get('reviews_count')
                if reviews_count_raw:
                    reviews_count = int(reviews_count_raw) if isinstance(reviews_count_raw, (int, str)) else 0
                
                # Extract shipping info
                shipping = "Free Shipping" if product.get('shipping') else "Check Shipping"
                delivery = product.get('delivery', shipping)
                
                link = product.get('link', '')
                product_name = product.get('title', '')[:80]
                
                # Enhanced link extraction
                product_id = self.extract_flipkart_product_id(link)
                flipkart_link = self.get_flipkart_product_url(product_id, product_name)
                
                if price > 0:
                    products.append({
                        'price': price,
                        'link': flipkart_link,
                        'name': product_name,
                        'rating': rating,
                        'shipping': delivery or shipping,
                        'reviews': reviews_count,
                        'product_id': product_id
                    })
            
            # Sort by price (lowest first)
            products.sort(key=lambda x: x['price'])
            return products
        except Exception as e:
            print(f"Error: {e}")
            return []
   
    def get_lowest_price(self, query: str, max_results: int = 10) -> Optional[Dict]:
        products = self.fetch_prices(query, max_results)
        return products[0] if products else None
   
    def print_lowest_price(self, query: str, max_results: int = 10):
        lowest = self.get_lowest_price(query, max_results)
        if not lowest:
            print("❌ No Flipkart products found.")
            return
        
        direct_link = lowest['link']
        
        print(f"\n🏆 LOWEST FLIPKART DEAL FOUND!")
        print(f"   💰 Price: ₹{lowest['price']:,.0f}")
        # FIXED: Uses ACTUAL extracted rating, no hardcoded values!
        if lowest['rating'] > 0:
            print(f"   ⭐ Rating: {lowest['rating']:.1f} ({int(lowest['reviews'])} reviews)")
        else:
            print(f"   ⭐ Rating: Not available ({int(lowest['reviews'])} reviews)")
        print(f"   🚚 Shipping: {lowest['shipping']}")
        print(f"   📱 Buy Now: {direct_link}")
        print(f"   📦 Product: {lowest['name']}")
        print("\n" + "="*60)


# USAGE - Same as before
if __name__ == "__main__":
    API_KEY = "0c64bffa3140c19ac328ccb2f02f10c6b7ec8fbfa9e6bd58fd6899a0a6279a2e"
   
    fetcher = FlipkartPriceFetcher(API_KEY)
   
    product_name = input("Enter product name (or 'refrigerator' for test): ").strip()
    if not product_name:
        product_name = "refrigerator under 10000"
   
    print(f"🔍 Searching Flipkart: {product_name}")
    fetcher.print_lowest_price(product_name)



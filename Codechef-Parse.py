from selenium import webdriver
from selenium.webdriver.chrome.options import Options  
import os, sys

url = ' '.join(sys.argv[1:])
code = url.split('/')[-1]
if os.path.exists('data/CodeChef/'+code+'.py'):
    print('Problem Already Solved')
    sys.exit()

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)
mathjax = driver.find_element_by_class_name('mathjax-support')
with open('tmp/CodechefProblem.txt', 'w', encoding='utf-8') as f:
    f.write(mathjax.text)
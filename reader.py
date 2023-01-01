# Importing required modules
import PyPDF2


from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

Options = webdriver.ChromeOptions()
Options.add_experimental_option("detach", True)
my_path = r"C:\Users\ksjun\OneDrive\Desktop\random\chromedriver.exe"
driver = webdriver.Chrome(options=Options,executable_path= my_path)


# Creating a pdf file object
pdfFileObj = open("C:\\Users\\ksjun\\OneDrive\\Desktop\\random\\lb450.pdf",'rb')

# Creating a pdf reader object
pdfReader = PyPDF2.PdfReader(pdfFileObj)

# Getting number of pages in pdf file
pages = len(pdfReader.pages)
op=''

link_list=[]
# Loop for reading all the Pages
for i in range(pages):

        # Creating a page object
        pageObj = pdfReader.pages[i]

        # Printing Page Number
        #print("Page No: ",i)

        # Extracting text from page
        # And splitting it into chunks of lines
        text = pageObj.extract_text().replace("\n","")

        link=''
        flag=True
        for iter in range(len(text)-1):
            if text[iter]=='(':
                link=''
                flag=True
                continue

            if flag:
                link+=text[iter]
            if text[iter]==')':
                flag=False
                link.replace('\n',"")
                link=link[:-1]
                if 'https' in link:
                    link_list.append(link)
                link=''
pdfFileObj.close()

my_file = []
newfile = open('output.txt','a')

for num in range(len(link_list)):

    driver.get(link_list[num])

    if 'practice' in link_list[num]:
        try:
            title = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'g-m-0')))

            desc = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'problems_problem_content__Xm_eO')))

            my_file.append(str(num+1))
            my_file.append('')
            my_file.append(title.text)
            my_file.append(desc.text)
        finally:
            my_file.append('')
            my_file.append('')
        

    elif 'leetcode' in link_list[num]:
        try:
            title = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'mr-2 text-lg font-medium text-label-1 dark:text-dark-label-1')))

            desc = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, '_1l1MA')))


            my_file.append(str(num+1))
            my_file.append('')
            my_file.append(title.text)
            my_file.append(desc.text)
        finally:
            my_file.append('')
            my_file.append('')

    elif link_list[num][8:17] =='www.geeks':
        try:
            title = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'article-title')))

            desc = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'p')))


            my_file.append(str(num+1))
            my_file.append('')
            my_file.append(title.text)
            my_file.append(desc.text)

            example = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'pre')))
            my_file.append(example.text)

        finally:
            my_file.append('')
            my_file.append('')

    newfile.writelines(my_file)
    my_file=[]

newfile.close()
        
        

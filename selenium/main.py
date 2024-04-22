from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/Lenovo-IdeaPad-Student-Processor-Bluetooth/dp/B0CQB84CTP/ref=sxin_15_pa_sp_search_thematic_sspa?_encoding=UTF8&content-id=amzn1.sym.554a8ca1-8404-495b-9d4a-d917c67c9b4f%3Aamzn1.sym.554a8ca1-8404-495b-9d4a-d917c67c9b4f&cv_ct_cx=laptops%2Band%2Baccessories&dib=eyJ2IjoiMSJ9.-QI-ORzXdqqqc6FM_XdMhSePhpZPPrt32E7OJb8Y43QBzPhMUUnlUYa84MUeNPch.tDOI3EgRNya57jBeF4kG03MoXZrFTC5G7TzULf04N9g&dib_tag=se&keywords=laptops%2Band%2Baccessories&pd_rd_i=B0CQB84CTP&pd_rd_r=5196c1f8-f54d-4c56-9f89-ac56e9468933&pd_rd_w=kZ4EE&pd_rd_wg=rHhDv&pf_rd_p=554a8ca1-8404-495b-9d4a-d917c67c9b4f&pf_rd_r=0X7SSZG3RYVGSXW9Y48X&qid=1713270543&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sr=1-3-2c727eeb-987f-452f-86bd-c2978cc9d8b9-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9zZWFyY2hfdGhlbWF0aWM&th=1")

# driver.close()
# driver.quit()
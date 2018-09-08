def b():
    # return "商城"
    return 'new UiSelector().text("我的")'


def a():
    c = 'new UiSelector().text(' + '\"' + b() + '\"' + ')'
    print(c)
    # driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()

print(b())
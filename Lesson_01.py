from selene import browser, be, have


# browser.open('https://demoqa.com/text-box')
# browser.element('[id="userName"]').type('Bugaev Dmitry') #.should(be.blank) .press_enter()
# browser.element('[id="userEmail"]').type('bugaev1404g@mail.ru')
# browser.element('[id="submit"]').press_enter()
# browser.element('[id="name"]').should(have.text('Name:Bugaev Dmitry'))
# browser.element('[id="email"]').should(have.text('Email:bugaev1404g@mail.ru'))

# browser.open('https://ya.ru')
# browser.element('[id="text"]').type('Прогноз погоды Санкт-Петербург').press_enter()
# browser.element('html').should(have.text('Погода в Санкт-Петербурге'))

from selene import browser, have

# def test_success_login():
#     browser.open('https://niffler.qa.guru')
#     browser.element('[id="username"]').type('stas')
#     browser.element('[id="password"]').type('12345')
#     browser.element('[id="login-button"]').click()
#
#     browser.element('[id="spendings"]').should(have.text('History of Spendings'))
#     browser.quit()
#
# def test_success_login_with_press_enter():
#     browser.open('https://niffler.qa.guru')
#     browser.element('[id="username"]').type('stas')
#     browser.element('[id="password"]').type('12345').press_enter()
#
#     browser.element('[id="spendings"]').should(have.text('History of Spendings'))
#     browser.quit()
#
# def test_wrong_credentials():
#     browser.open('https://niffler.qa.guru')
#     browser.element('[id="username"]').type('stas')
#     browser.element('[id="password"]').type('12345sgsrgwr').press_enter()
#
#     browser.element('[class="form__error"]').should(have.text('Bad credentials'))
#     browser.quit()
#
# test_success_login()


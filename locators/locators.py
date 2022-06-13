from selenium.webdriver.common.by import By


class LogInLocators:
    login_link = (By.LINK_TEXT, "Log in")
    user_input = (By.XPATH, "//input[@id='username']")
    password_input = (By.XPATH, "//input[@id='password']")
    login_button = (By.TAG_NAME, "button")


class CreateSurveyLocators:
    create_survey_link = (By.XPATH, '//a[text()="Create Survey"]')
    scratch_text = (By.XPATH, '//button[text()="Start from scratch"]')
    survey_name = (By.ID, "surveyTitle")
    create_button_id = (By.ID, "newSurvey")
    assert_survey_title = (By.CSS_SELECTOR, 'h2[class^="global-navigation-header-title"]')


 
class AddQuestionLocators:
    question = (By.CSS_SELECTOR, "#editTitle")
    question_type = (By.ID, "changeQType")
    mcq = (By.LINK_TEXT, "Multiple Choice")
    dropdown = (By.LINK_TEXT, "Dropdown")
    checkbox = (By.LINK_TEXT, "Checkboxes")
    next = (By.XPATH, "//a[text()='NEXT QUESTION']")
    answer_choice_option = (By.XPATH,
                            "//div[@data-id='editQuestionContent']//tbody[@data-field-type='answer']//tr[contains(concat(' ', normalize-space(@class), ' '), ' choice ') and not(contains(@class,'hide'))][%VAR%]//div[starts-with(@id,'newChoice')]")

    done_button = (By.XPATH, '//button[contains(text(),"Done")]')
    assert_count_Question = (By.XPATH, '//form[@name="surveyForm"]/div[1]/div[1]/div')


class AttemptQuestionsLocators:
    preview_score_click = (By.LINK_TEXT, "PREVIEW & SCORE")
    answer_q1_click = (By.XPATH, '//span[contains(text(), "1")]')
    # answer_q1_click = (By.XPATH, '(//input[@type="radio"])[1]')
    # answer_q2_click = (By.XPATH, '//option[contains(text(), "2")]')
    # answer_q2_click = (By.XPATH, '(//input[@type="dropdown"])[1]')
    answer_q2_click = (By.XPATH, "//select[@class='select no-touch']")
    frame_id = (By.ID, "surveyPreview")
    # answer_q3_click = (By.XPATH, '(//div[@class="question-body clearfix notranslate "]//span[@class="checkbox-button-display "])[%VAR%]')
    answer_q3b_click = (By.XPATH, '(//span[contains(text(), "2")])[3]')
    answer_q3c_click = (By.XPATH, '(//span[contains(text(), "3")])[3]')
    done_button = (By.XPATH, '//button[contains(text(),"Done")]')
    assert_message = (By.XPATH, "//div[@id='previewEnd']/div[@class='message']")

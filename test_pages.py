from herokuapp import MainPage, FramesPage, NestedFramesPage, DynamicPage, ChallengingPage, Const
from time import sleep


# Write a selenium webdriver script to perform the following:
#     • Using Chrome navigate directly to http://the-internet.herokuapp.com
#     • Follow the link titled "frames"
#     • Follow the link to "nested frames"
#     • print the text in each frame in the following order:
#         ◦ middle
#         ◦ bottom
#         ◦ left
#         ◦ right
def test_nested_frames(browser):
    main_page = MainPage(browser, Const.HEROKUAPP_URL)
    main_page.open()
    main_page.should_be_main_url()
    main_page.go_to_frames_page()

    frames_page = FramesPage(browser, browser.current_url)
    frames_page.should_be_frames_url()
    frames_page.go_to_nested_frames_page()

    nested_frames_page = NestedFramesPage(browser, browser.current_url)
    nested_frames_page.should_be_nested_frames_url()
    nested_frames_page.change_middle_text()
    nested_frames_page.should_be_middle_text()
    sleep(Const.DELAY)
    nested_frames_page.change_bottom_text()
    nested_frames_page.should_be_bottom_text()
    sleep(Const.DELAY)
    nested_frames_page.change_left_text()
    nested_frames_page.should_be_left_text()
    sleep(Const.DELAY)
    nested_frames_page.change_right_text()
    nested_frames_page.should_be_right_text()
    sleep(Const.DELAY)


# Write a selenium webdriver script to perform the following:
#     • Using Chrome navigate directly to http://the-internet.herokuapp.com/dynamic_loading/1
#     • Click "Start"
#     • When the loading has finished, read, and print the text that is displayed
def test_dynamic_page(browser):
    page = DynamicPage(browser, f'{Const.HEROKUAPP_URL}{Const.DYNAMIC}')
    page.open()
    page.should_be_dynamic_url()
    sleep(Const.DELAY)
    page.click_start_btn()
    page.should_present_finish_text()
    page.print_finish_text()


# Write a selenium webdriver script to perform the following in sequence:
#     • Using chrome navigate directly to http://the-internet.herokuapp.com/challenging_dom
#     • Highlight the text in the third row of the Diceret column for two seconds.
#     • Highlight the delete link in the row containing “Apeirian7” for two seconds
#     • Highlight the edit link for the row containing “Apeirian2” for two seconds.
#     • Highlight “Definiebas7” for two seconds, then highlight “Iuvaret7” for two seconds.
#     • Click the Green button.
def test_challenging_page(browser):
    page = ChallengingPage(browser, f'{Const.HEROKUAPP_URL}{Const.CHALLENGING}')
    page.open()
    page.should_be_challenging_url()
    page.highlight_third_row()
    page.highlight_delete_link()
    page.highlight_edit_link()
    page.highlight_definiebas()
    page.highlight_iuvaret()
    page.click_green_btn()
    sleep(Const.DELAY)

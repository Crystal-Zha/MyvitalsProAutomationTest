# -*- coding: UTF-8 -*-

"""
这个page是编写account界面所有的元素以及常用的操作
"""
import random
import time

from selenium.webdriver.common.by import By

from appium_function.element_function import BaseFun


class SettingPage(BaseFun):
    # 主页设置按钮
    setting_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/iv_settings')

    # 主页设备按钮
    device_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/iv_devices')

    # 主页趋势图
    summary_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/iv_trends')

    '''========账户信息界面======='''
    # 账号头像
    account_photo_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/setting_iv_head')
    # 用户名
    user_name_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/settings_user_name')

    # 进入用户信息界面按钮
    enter_to_user_info_button_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/iv_user_info_right')
    # name
    name_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/ed_user_name')
    # account
    account_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/tv_account')
    # 身高
    height_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/ed_user_height')
    # 体重
    weight_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/ed_user_weight')
    # birthday
    birthday_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/ed_user_birthdate')
    # gender
    gender_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/ed_user_gender')
    # done
    done_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/tv_done')
    # next
    next_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/tv_next')

    goals_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/ll_goals')

    '''=========目标体重详情页============='''
    target_weight_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/ed_goals_weight')
    save_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/goals_done')

    units_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/tv_units')

    '''======单位详情页======'''
    # 血压单位
    blood_pressure_units_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/setting_unit_bp_tv')
    mmHg_loc = (By.NAME, 'mmHg')
    kPa_loc = (By.NAME, 'kPa')

    # 体重单位
    weight_units_loc = (By.NAME, 'Weight Units:')
    kg_loc = (By.NAME, 'kg')
    lbs_loc = (By.NAME, 'lbs')

    # 距离单位
    distance_units_loc = (By.NAME, 'Distance Units:')
    km_loc = (By.NAME, 'km')
    miles_loc = (By.NAME, 'miles')

    # 身高单位
    height_units_loc = (By.NAME, 'Height Units:')
    cm_loc = (By.NAME, 'cm')
    feet_loc = (By.NAME, 'feet')

    # 温度单位
    temperature_units_loc = (By.NAME, 'Temperature Units:')
    celsius_loc = (By.NAME, '℃')
    fahrenheit_loc = (By.NAME, '℉')

    # 血糖单位
    glucose_units_loc = (By.NAME, 'Glucose units')
    mgdL_loc = (By.NAME, 'mg/dL')
    mmolL_loc = (By.NAME, 'mmol/L')

    save_units_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/unit_save')

    glucose_range_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/tv_glucose_range')

    '''血糖范围详情页'''
    before_meals_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/tv_before_meals_bedtime')
    before_meals_low_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/ed_before_low')
    before_meals_high_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/ed_before_high')

    after_meals_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/tv_after_meals')
    after_meals_low_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/ed_after_low')
    after_meals_high_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/ed_after_high')

    warning_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/tv_warning')
    warning_content_loc = (By.NAME, 'Please consult your doctor to find out the target range that fits you.'
                                    ' The default values are recommended by the American Diabetes Association (ADA) '
                                    'but can varies due to age, type of diabetes, and treatment plans.')
    save_target_glucose_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/btn_target_glucose_save')

    '''=======吃饭事件详情======'''
    meal_time_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/tv_meal_time')
    wake_up_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/ly_wakeup')
    breakfast_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/ly_breakfast')
    lunch_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/ly_lunch')
    dinner_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/ly_dinner')
    bedtime_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/ly_bedtime')
    save_meal_time_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/btn_meal_time_save')

    '''=========about详情============'''
    about_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/tv_about')
    copyright_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/ll_copyright')
    regulatory_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/tv_regulatory')
    personal_health_data_guide_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/tv_personal')
    app_version_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/ll_app_version')

    '''=========contract us============'''
    contact_us_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/tv_contact_us')
    back_to_previous_page = (By.XPATH, '//android.widget.ImageButton[@content-desc="转到上一层级"]')
    input_message_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/message_composer_input_text')
    attachment_button_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/attachments_indicator_icon')
    send_button_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/message_composer_send_btn')

    # 切换账户
    switch_account_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/switch_account')

    '''=========登出=========='''
    # 登出
    logout_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/log_out')

    # 确认框文本
    message_loc = (By.NAME, 'Are you sure you want to log out？')

    # 确认框ok按钮
    dialog_ok_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/tv_right')

    # cancel
    dialog_cancel_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/tv_left')

    def click_setting(self):
        self.click(self.setting_loc)

    def click_logout(self):
        self.click(self.logout_loc)

    def click_ok(self):
        self.click(self.dialog_ok_loc)

    def click_cancel(self):
        self.click(self.dialog_cancel_loc)

    def click_gender(self):
        self.click(self.gender_loc)

    def click_height(self):
        self.click(self.height_loc)

    def click_weight(self):
        self.click(self.weight_loc)

    def click_birthday(self):
        self.click(self.birthday_loc)

    def click_goals(self):
        self.click(self.goals_loc)

    def click_units(self):
        self.click(self.units_loc)

    def click_glucose_range(self):
        self.click(self.glucose_range_loc)

    def click_meal_time(self):
        self.click(self.meal_time_loc)

    def click_about(self):
        self.click(self.about_loc)

    def click_contact_us(self):
        self.click(self.contact_us_loc)

    def click_switch_account(self):
        self.click(self.switch_account_loc)

    def click_account_photo(self):
        self.click(self.account_photo_loc)

    def enter_to_user_info_button(self):
        self.click(self.enter_to_user_info_button_loc)

    def click_user_name(self):
        self.click(self.user_name_loc)

    def click_done(self):
        self.click(self.done_loc)

    def select_gluocose_unit_to_mmdlL(self):
        self.click(self.mgdL_loc)

    def select_glucose_unit_to_mmolL(self):
        self.driver.find_element_by_name('mmol/L').click()

    def click_save_glucose_range(self):
        self.click(self.save_target_glucose_loc)

    def çlick_save_units(self):
        self.click(self.save_units_loc)

    # 登出
    def logout(self):
        self.click_setting()
        self.click_logout()
        self.click_ok()

    def change_user_name(self, user_name):
        self.click(self.name_loc)
        time.sleep(2)
        self.driver.find_element_by_id('com.ihealthlabs.MyVitalsPro:id/ed_user_name').clear()
        self.send_keys(self.name_loc, user_name)

    def input_target_weight(self):
        self.click(self.target_weight_loc)
        target_weight = random.randint(1, 100)
        self.send_keys(self.target_weight_loc, target_weight)
        self.click(self.save_loc)
        time.sleep(2)

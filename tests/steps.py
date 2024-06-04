import allure
from coms.qa.fixtures.application import Application
from coms.qa.frontend.helpers.attach_helper import screenshot_attach
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.case_ap_page import CaseApPage
from dit.qa.pages.checklist_page import CheckListPage
from dit.qa.pages.document_ec_page import DocumentEcpPage
from dit.qa.pages.main_page import MainPage
from dit.qa.pages.object_building_page import ObjectBuildingPage
from dit.qa.pages.orders_page import OrdersPage
from dit.qa.pages.register_events_page import RegisterEventsPage
from dit.qa.pages.start_page import StartPage
from dit.qa.pages.summer_cafe_page import SummerCafePage
from dit.qa.pages.task_page import TaskPage

__all__ = [
    'open_start_page',
    'sign_in',
    'open_main_page',
    'open_task_page',
    'open_task_card',
    'open_checklist_page',
    'open_checklist_card',
    'open_object_building_page',
    'open_object_building_card',
    'open_summer_cafe_page',
    'open_summer_cafe_card',
    'open_orders_page',
    'open_orders_card',
    'open_case_ap_page',
    'open_case_ap_card',
    'open_document_ecp_page',
    'open_register_functional_events_page',
    'open_register_functional_events_card',
]


def open_start_page(app: Application) -> None:
    with allure.step('Opening Start page'):
        try:
            page = StartPage(app)
            page.open()

            page.wait_for_loading()

            screenshot_attach(app, 'start_page')
        except Exception as e:
            screenshot_attach(app, 'start_page_error')

            raise TimeoutError('Start page was not loaded') from e


def sign_in(app: Application, login: str, password: str) -> None:
    with allure.step(f'{login} signing in'):
        try:
            auth_form = StartPage(app)
            auth_form.submit_login.click()

            auth_form.login.send_keys(login)
            auth_form.password.send_keys(password)

            screenshot_attach(app, 'auth_data')
        except Exception as e:
            screenshot_attach(app, 'auth_data_error')

            raise NoSuchElementException('Entering data exception') from e

        auth_form.submit.click()


def open_main_page(app: Application) -> None:
    with allure.step('Opening Main page'):
        try:
            page = MainPage(app)
            page.wait_for_loading()
            page.wait_for_loading_frame()

            screenshot_attach(app, 'main_page')
        except Exception as e:
            screenshot_attach(app, 'main_page_error')

            raise TimeoutError('Main page was not loaded') from e


def open_task_page(app: Application) -> None:
    with allure.step('Opening Task page'):
        try:
            page = TaskPage(app)
            page.base_url = 'https://aisgin.mos.ru/InspectionTask'
            page.open()

            page.wait_for_loading()

            screenshot_attach(app, 'task_page')
        except Exception as e:
            screenshot_attach(app, 'task_page_error')

            raise TimeoutError('Task page was not loaded') from e


def open_task_card(app: Application) -> None:
    with allure.step('Opening Task card'):
        try:
            page = TaskPage(app)
            page.task_btn[0].webelement.click()

            page.wait_task_card()

            screenshot_attach(app, 'task_card_card')
        except Exception as e:
            screenshot_attach(app, 'task_card_card_error')

            raise TimeoutError('Task card was not loaded') from e


def open_checklist_page(app: Application) -> None:
    with allure.step('Opening Сhecklist page'):
        try:
            page = CheckListPage(app)
            page.base_url = 'https://aisgin.mos.ru/Controls'
            page.open()

            page.wait_for_loading()

            screenshot_attach(app, 'checklist_page')
        except Exception as e:
            screenshot_attach(app, 'checklist_page_error')

            raise TimeoutError('Сhecklist page was not loaded') from e


def open_checklist_card(app: Application) -> None:
    with allure.step('Opening Сhecklist card'):
        try:
            page = CheckListPage(app)
            page.check_btn[0].click()

            page.wait_checklist_card()

            screenshot_attach(app, 'checklist_card_page')
        except Exception as e:
            screenshot_attach(app, 'checklist_card_page_error')

            raise TimeoutError('Сhecklist card was not loaded') from e


def open_object_building_page(app: Application) -> None:
    with allure.step('Opening Object building page'):
        try:
            page = ObjectBuildingPage(app)
            page.base_url = 'https://aisgin.mos.ru/UnauthorizedBuilding'
            page.open()

            page.wait_for_loading()

            screenshot_attach(app, 'object_building_page')
        except Exception as e:
            screenshot_attach(app, 'object_building_page_error')

            raise TimeoutError('Object building page was not loaded') from e


def open_object_building_card(app: Application) -> None:
    with allure.step('Opening Object building card'):
        try:
            page = ObjectBuildingPage(app)
            page.check_btn[0].click()

            page.wait_object_building_card()

            screenshot_attach(app, 'object_building_card')
        except Exception as e:
            screenshot_attach(app, 'object_building_card_error')

            raise TimeoutError('Object building card was not loaded') from e


def open_summer_cafe_page(app: Application) -> None:
    with allure.step('Opening Summer cafe page'):
        try:
            page = SummerCafePage(app)
            page.base_url = 'https://aisgin.mos.ru/SummerCafe/Find?NtoPurpose=SummerCafe'
            page.open()

            page.wait_for_loading()

            screenshot_attach(app, 'summer_cafe_page')
        except Exception as e:
            screenshot_attach(app, 'summer_cafe_page_error')

            raise TimeoutError('Summer cafe page was not loaded') from e


def open_summer_cafe_card(app: Application) -> None:
    with allure.step('Opening Summer cafe card'):
        try:
            page = SummerCafePage(app)
            page.check_btn[0].click()

            page.wait_summer_cafe_card()

            screenshot_attach(app, 'summer_cafe_card')
        except Exception as e:
            screenshot_attach(app, 'summer_cafe_card_error')

            raise TimeoutError('Summer cafe card was not loaded') from e


def open_orders_page(app: Application) -> None:
    with allure.step('Opening Orders page'):
        try:
            page = OrdersPage(app)
            page.base_url = 'https://aisgin.mos.ru/Disposals'
            page.open()

            page.wait_for_loading()

            screenshot_attach(app, 'orders_page')
        except Exception as e:
            screenshot_attach(app, 'orders_page_error')

            raise TimeoutError('Orders page was not loaded') from e


def open_orders_card(app: Application) -> None:
    with allure.step('Opening Orders card'):
        try:
            page = OrdersPage(app)
            page.check_btn[0].click()

            page.wait_orders_card()

            screenshot_attach(app, 'orders_card')
        except Exception as e:
            screenshot_attach(app, 'orders_card_error')

            raise TimeoutError('Orders card was not loaded') from e


def open_case_ap_page(app: Application) -> None:
    with allure.step('Opening Case Ap page'):
        try:
            page = CaseApPage(app)
            page.base_url = 'https://aisgin.mos.ru/ApDelo'
            page.open()

            page.wait_for_loading()

            screenshot_attach(app, 'case_ap_page')
        except Exception as e:
            screenshot_attach(app, 'case_ap_page_error')

            raise TimeoutError('Case ap page was not loaded') from e


def open_case_ap_card(app: Application) -> None:
    with allure.step('Opening Case Ap card'):
        try:
            page = CaseApPage(app)
            page.check_btn[0].click()

            page.wait_case_card()

            screenshot_attach(app, 'case_ap_card')
        except Exception as e:
            screenshot_attach(app, 'case_ap_card_error')

            raise TimeoutError('Case ap card was not loaded') from e


def open_document_ecp_page(app: Application) -> None:
    with allure.step('Opening Documents Ec page'):
        try:
            page = DocumentEcpPage(app)
            page.base_url = 'https://aisgin.mos.ru/DocumentSigning'
            page.open()

            page.wait_for_loading()

            screenshot_attach(app, 'documents_page')
        except Exception as e:
            screenshot_attach(app, 'documents_page_error')

            raise TimeoutError('Documents Ec page was not loaded') from e


def open_register_functional_events_page(app: Application) -> None:
    with allure.step('Opening Register functional events page'):
        try:
            page = RegisterEventsPage(app)
            page.base_url = 'https://aisgin.mos.ru/ui/planning/tasks/funcevent'
            page.open()

            page.wait_for_loading()

            screenshot_attach(app, 'register_functional_events_page')
        except Exception as e:
            screenshot_attach(app, 'register_functional_events_page_error')

            raise TimeoutError('Register functional events page was not loaded') from e


def open_register_functional_events_card(app: Application) -> None:
    with allure.step('Opening Register functional events card'):
        try:
            page = RegisterEventsPage(app)
            page.tasks[0].click()

            page.wait_register_events_card()

            screenshot_attach(app, 'register_functional_events_card')
        except Exception as e:
            screenshot_attach(app, 'register_functional_events_card_error')

            raise TimeoutError('Register functional events card was not loaded') from e

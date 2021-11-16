import io
import json
import os
import shutil
import sqlite3
import sys
import csv

import folium
from folium.plugins import Draw
from PyQt5 import QtWidgets, QtWebEngineWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QDialog
from PyQt5.QtWebEngineWidgets import QWebEngineView

from edit_message import EditMessageUi
from helping_message import HelpingMessageUi
from main_menu import MainMenuWindowUi
from message import MessageWindowUi
from register import RegisterWindowUi
from status import StatusWindowUi
from wrong import WrongDialog
from edit import Editing
from send import SendUi
from admin import Admin_Ui
from login import LoginWindowUi
from admin_password import PASSWORD, LOGIN


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class WebEnginePage(QtWebEngineWidgets.QWebEnginePage):
    def javaScriptAlert(self, securityOrigin: QtCore.QUrl, msg: str):
        coords_dict = json.loads(msg)
        self.coords = coords_dict['geometry']['coordinates']

    def get_coords(self):
        return self.coords


class LoginWindow(QMainWindow, LoginWindowUi):  # окно входа
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet("#MainWindow{border-image:url(Background/Background_login.png)}")
        self.sign_up.clicked.connect(self.open_register_window)
        self.sign_in.clicked.connect(self.open_menu_window)

    def open_register_window(self):  # кнопка зарегестрироваться
        self.register_w = RegisterWindow()
        self.register_w.showMaximized()
        self.close()

    def open_menu_window(self):  # кнопка войти
        login = self.Login_le.text()
        password = self.Password_le.text()
        if login == LOGIN and password == PASSWORD:
            self.admin_w = AdminWindow()
            self.admin_w.showMaximized()
            self.close()
        else:
            connect = sqlite3.connect('database.db')
            cursor = connect.cursor()
            login_password_1 = cursor.execute("""SELECT login, password FROM users 
                    WHERE login = ? AND password = ?""", (login, password)).fetchall()
            login_password_2 = cursor.execute("""SELECT login, password FROM users 
                    WHERE login = ?""", (login,)).fetchall()
            if login.isalnum() and password.isalnum():  # проверка на не пустую строку
                if login_password_1:  # проверка на наличие аккаунта
                    self.menu_w = MenuWindow(login)
                    self.menu_w.showMaximized()
                    self.close()
                elif login_password_2:
                    self.Message.setText('Неверный пароль')
                else:
                    self.Message.setText('Вы не зарегестрированы')
            else:
                self.Message.setText('Введите логин и пароль корректно')
            connect.close()


class RegisterWindow(QMainWindow, RegisterWindowUi):  # окно регистрации
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet("#MainWindow{border-image:url(Background/Background_register.png)}")
        self.sign_up.clicked.connect(self.open_menu_window)
        self.back.clicked.connect(self.to_back)

    def check_password(self, password):  # проверка пароля на условия
        n = 'qwertyuiop/asdfghjkl/zxcvbnm/йцукенгшщзхъ/фывапролджэё/ячсмитьбю/1234567890'
        if password == '':
            return 'Введите пароль'
        if len(password) <= 8:
            return 'Длина пароля меньше 9 символов'
        if (''.join([i for i in password if not (i.isdigit())]).isupper()) or (
                ''.join([i for i in password if not (i.isdigit())]).islower()) \
                or len([i for i in password if i.isalpha()]) == 0:
            return 'В пароле все символы \nодного регистра'
        if len([i for i in password if i.isdigit()]) == 0:
            return 'В пароле нет ни одной цифры'
        if len([i for i in range(1, len(password) - 1) if
                not ((password[i - 1] + password[i] + password[i + 1]).lower() in n)]) != \
                len(password) - 2:
            return 'В пароле используется \nподряд идущие три символа'
        return 'ok'

    def open_menu_window(self):  # кнопка зерегестрироваться
        login = self.Login_le.text()
        password = self.Password_le.text()
        connect = sqlite3.connect('database.db')
        cursor = connect.cursor()
        login_password = cursor.execute("""SELECT login, password FROM users 
                WHERE login = ? AND password = ?""", (login, password)).fetchall()
        if login != '':
            result = self.check_password(password)  # проверка пароля на соответсвие правил
            if result == 'ok':
                if not login_password:  # проверка на отсутствие аккаунта
                    if len(login) >= 3:
                        cursor.execute("""INSERT INTO users(login, password) 
                                VALUES(?, ?)""", (login, password))
                        connect.commit()
                        self.menu_w = MenuWindow(login)
                        self.menu_w.showMaximized()
                        self.close()
                    else:
                        self.Message.setText('Логин должен быть не менее 3 символов')
                else:
                    self.Message.setText('Пользователь с таким именем уже зарегестрирован')
            else:
                self.Message.setText(result)
        else:
            self.Message.setText('Введите логин')
        connect.close()

    def to_back(self):  # кнопка назад
        self.login_w = LoginWindow()
        self.login_w.showMaximized()
        self.close()


class MenuWindow(QMainWindow, MainMenuWindowUi):  # главное меню
    def __init__(self, login):
        super().__init__()
        self.setupUi(self)
        self.login = login
        self.setStyleSheet("#MainWindow{border-image:url(Background/Background_menu.png)}")
        self.message.clicked.connect(self.open_message_window)
        self.edit_message.clicked.connect(self.open_edit_message_window)
        self.status_message.clicked.connect(self.open_status_window)

    def open_edit_message_window(self):  # окно выбора редактирования сообщений
        self.message_w = EditMessageWindow(self.login)
        self.message_w.showMaximized()

    def open_message_window(self):  # открытие окно с отправкой сообщения
        self.message_w = MessageWindow(self.login)
        self.message_w.showMaximized()

    def open_status_window(self):  # открытие окно со статусом сообщений
        self.status_w = StatusMessageWindow(self.login)
        self.status_w.showMaximized()


class MessageWindow(QMainWindow, MessageWindowUi):  # отправить сообщение о проблеме
    def __init__(self, login):
        super().__init__()
        self.setupUi(self)
        self.login = login
        self.coord = ''
        self.setStyleSheet("#MainWindow{border-image:url(Background/Background_message.png)}")
        map = folium.Map(location=[55.753215, 37.622504], zoom_start=4)
        draw = Draw(
            draw_options={
                'polyline': False,
                'rectangle': False,
                'polygon': False,
                'circle': False,
                'marker': True,
                'circlemarker': False},
            edit_options={'edit': False})
        map.add_child(draw)
        data = io.BytesIO()
        map.save(data, close_file=False)
        self.page = WebEnginePage(self.map)
        self.map.setPage(self.page)
        self.map.setHtml(data.getvalue().decode())
        self.send.clicked.connect(self.sending)
        self.photo.clicked.connect(self.get_photo)
        self.help.clicked.connect(self.help_window)
        self.apply_address.clicked.connect(self.address)

    def address(self):
        self.coord = ' '.join([str(i) for i in self.page.get_coords()][::-1])

    def help_window(self):  # открыть окно помощи
        self.help_w = HelpingWindow()
        self.help_w.showMaximized()

    def get_photo(self):  # получить url фотографии
        self.url_photo = QFileDialog.getOpenFileName(self, 'Прикрепить фото', '',
                                                     'Фото (*.jpg);;Фото (*.jpeg);;Фото '
                                                     '(*.png);;Фото (*.bmp)')[0]
        try:
            self.name_photo = self.url_photo.split('/')[-1]
        except Exception:
            self.wrong_wn = WrongWindow()
            self.wrong_wn.show()

    def sending(self):
        try:
            # копирование фото в папку с приложением
            if self.url_photo != '' and self.coord != '':
                shutil.copy(self.url_photo, f'{os.getcwd()}/Image')
                connect = sqlite3.connect('database.db')
                cursor = connect.cursor()
                cursor.execute("""INSERT INTO message(login, category, details, coordinates, photo)
                    VALUES(?, ?, ?, ?, ?)""",
                               (self.login, self.category.text(), self.message.toPlainText(),
                                self.coord, self.name_photo))
                connect.commit()
                connect.close()
                self.send_w = SendWindow()
                self.send_w.show()
                self.close()
            else:
                self.wrong_wn = WrongWindow()
                self.wrong_wn.show()
        except Exception:
            self.wrong_wn = WrongWindow()
            self.wrong_wn.show()


class SendWindow(QDialog, SendUi):  # окно уведомления отправленного сообщения
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ok.clicked.connect(self.closing)

    def closing(self):
        self.close()


class WrongWindow(QDialog, WrongDialog):  # окно ошибки при не заполненных данных
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ok.clicked.connect(self.closing)

    def closing(self):
        self.close()


class HelpingWindow(QMainWindow, HelpingMessageUi):  # окно помощь
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet("#MainWindow{border-image:url(Background/Background_help1.png)}")
        self.agree.clicked.connect(self.closing)

    def closing(self):
        self.close()


class EditMessageWindow(QMainWindow, EditMessageUi):  # окно для выбора редактирования сообщений
    def __init__(self, login):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet("#MainWindow{border-image:url(Background/Background_egit_message.png)}")
        self.login = login
        self.database.setColumnCount(3)
        self.database.setHorizontalHeaderLabels(['id', 'Название', 'Описание'])
        self.database.resizeColumnsToContents()
        self.updating()
        self.database.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)  # запрет редактирования
        self.edit.clicked.connect(self.open_edit_window)
        self.delete.clicked.connect(self.delete_message)

    def updating(self):  # обновление таблицы
        connect = sqlite3.connect('database.db')
        cursor = connect.cursor()
        self.result_2 = cursor.execute('''SELECT id, category, details FROM message 
                    WHERE login = ?''', (self.login,)).fetchall()
        connect.commit()
        connect.close()
        self.database.setRowCount(len(self.result_2))
        for i in range(len(self.result_2)):  # заполнение таблицы данными из бд
            self.database.setItem(i, 0, QTableWidgetItem(str(self.result_2[i][0])))
            self.database.setItem(i, 1, QTableWidgetItem(self.result_2[i][1]))
            self.database.setItem(i, 2, QTableWidgetItem(self.result_2[i][2]))
        self.id.clear()
        for i in self.result_2:
            self.id.addItem(str(i[0]))

    def delete_message(self):  # удаление сообщения
        connect = sqlite3.connect('database.db')
        cursor = connect.cursor()
        photo = cursor.execute('''SELECT photo FROM message 
                    WHERE id = ?''', (self.id.currentText(),)).fetchall()
        self.result_1 = cursor.execute('''DELETE FROM message 
                    WHERE id = ?''', (self.id.currentText(),)).fetchall()
        self.result_2 = cursor.execute('''SELECT photo FROM message 
                    WHERE id = ?''', (self.id.currentText(),)).fetchall()
        connect.commit()
        connect.close()
        os.remove(f'Image/{photo[0][0]}')
        self.updating()

    def open_edit_window(self):  # открытие окна редактирования
        self.editing_wn = EditingWindow(self.id.currentText())
        self.editing_wn.showMaximized()
        self.updating()


class EditingWindow(QMainWindow, Editing):  # окно для редактирования сообщения
    def __init__(self, id_m):
        super().__init__()
        self.setupUi(self)
        self.id_m = id_m
        self.setStyleSheet("#MainWindow{border-image:url(Background/Background_message.png)}")
        connect = sqlite3.connect('database.db')
        cursor = connect.cursor()
        coords = cursor.execute('''SELECT coordinates FROM message 
                            WHERE id = ?''', (self.id_m,)).fetchone()
        result = cursor.execute('''SELECT login, category, details, coordinates, photo FROM message 
                    WHERE id = ?''', (id_m,)).fetchall()
        map = folium.Map(location=[55.753215, 37.622504], zoom_start=4)
        folium.Marker(location=[float(i) for i in coords[0].split(' ')],
                      popup=result[0][1]).add_to(map)
        draw = Draw(
            draw_options={
                'polyline': False,
                'rectangle': False,
                'polygon': False,
                'circle': False,
                'marker': True,
                'circlemarker': False},
            edit_options={'edit': False})
        map.add_child(draw)
        data = io.BytesIO()
        map.save(data, close_file=False)
        self.page = WebEnginePage(self.map)
        self.map.setPage(self.page)
        self.map.setHtml(data.getvalue().decode())
        self.category.setText(result[0][1])
        self.message.setText(result[0][2])
        self.coord = result[0][3]
        self.photos = result[0][4]
        self.login = result[0][0]
        self.photo.clicked.connect(self.get_photo)
        self.send.clicked.connect(self.sending)
        self.apply_address.clicked.connect(self.address)

    def address(self):  # получение координат
        self.coord = ' '.join([str(i) for i in self.page.get_coords()][::-1])

    def get_photo(self):  # получить url фотографии
        self.url_photo = QFileDialog.getOpenFileName(self, 'Прикрепить фото', '',
                                                     'Фото (*.jpg);;Фото (*.jpeg);;Фото '
                                                     '(*.png);;Фото (*.bmp)')[0]
        os.remove(self.photos)
        self.photos = self.url_photo

    def sending(self):
        # копирование фото в папку с приложением
        shutil.copy(self.photos, f'{os.getcwd()}/Image')
        connect = sqlite3.connect('database.db')
        cursor = connect.cursor()
        cursor.execute("""UPDATE message SET login = ?, category = ?, 
        details = ?, coordinates = ?, photo = ? WHERE id = ?""",
                       (self.login, self.category.text(), self.message.toPlainText(),
                        self.coord, self.photos, self.id_m))
        connect.commit()
        connect.close()
        self.close()


class StatusMessageWindow(QMainWindow, StatusWindowUi):  # окно статуса сообщений
    def __init__(self, login):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet("#MainWindow{border-image:url(Background/Background_status_message.png)}")
        self.login = login
        self.database.setColumnCount(4)
        self.database.setHorizontalHeaderLabels(['id', 'Название', 'Описание', 'Статус'])
        self.database.resizeColumnsToContents()
        self.database.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)  # запрет редактирования
        connect = sqlite3.connect('database.db')
        cursor = connect.cursor()
        self.result_2 = cursor.execute('''SELECT id, category, details, status FROM message 
                            WHERE login = ?''', (self.login,)).fetchall()
        connect.commit()
        connect.close()
        self.database.setRowCount(len(self.result_2))
        for i in range(len(self.result_2)):  # заполнение таблицы данными из бд
            for j in range(4):
                self.database.setItem(i, j, QTableWidgetItem(str(self.result_2[i][j])))


class AdminWindow(QMainWindow, Admin_Ui):  # окно администратора
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet("#MainWindow{border-image:url(Background/Background_admin.png)}")
        connect = sqlite3.connect('database.db')
        cursor = connect.cursor()
        # все необходимые запросы
        self.result = cursor.execute('''SELECT * FROM message''').fetchall()
        self.coords = cursor.execute('''SELECT login, coordinates FROM message''').fetchall()
        self.database.setColumnCount(7)
        self.database.resizeColumnsToContents()
        self.database.setHorizontalHeaderLabels(['id', 'login', 'category', 'details',
                                                 'coordinates', 'photo', 'status'])
        self.database.setRowCount(len(self.result))
        for i in range(len(self.result)):
            for j in range(7):  # заполнение таблицы данными из бд
                self.database.setItem(i, j, QTableWidgetItem(str(self.result[i][j])))
        self.database.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.download.clicked.connect(self.downloading)
        connect.close()
        self.fill_map()

    def downloading(self):  # скачать таблицу в csv формате
        self.place = QFileDialog.getExistingDirectory(self, 'Выбрать папку', '')
        with open(f'{self.place}/loading.csv', 'w', encoding='windows-1251', newline='') as csvfile:
            writer = csv.writer(
                csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['id', 'login', 'category', 'details', 'coordinates', 'photo', 'status'])
            for i in self.result:
                writer.writerow(i)

    def fill_map(self):
        map = folium.Map(location=[55.753215, 37.622504], zoom_start=4)
        for i in self.coords:
            folium.Marker(location=[float(i) for i in i[-1].split(' ')],
                          popup=i[0]).add_to(map)
        draw = Draw(
            draw_options={
                'polyline': False,
                'rectangle': False,
                'polygon': False,
                'circle': False,
                'marker': True,
                'circlemarker': False},
            edit_options={'edit': False})
        map.add_child(draw)
        data = io.BytesIO()
        map.save(data, close_file=False)
        self.page = WebEnginePage(self.map)
        self.map.setPage(self.page)
        self.map.setHtml(data.getvalue().decode())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.showMaximized()
    sys.excepthook = except_hook
    sys.exit(app.exec())

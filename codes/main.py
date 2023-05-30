from PyQt5 import QtCore, QtGui, QtWidgets
from googletrans import LANGUAGES,Translator


list_language = []

def languages():
    for i in LANGUAGES:
        list_language.append(i) 
    return list_language


class Tranlate():
        def __init__(self):
                self.word_mean = None
         
        def translatei(self,word,src_lang,dest_lang):
                trans = Translator()
                translate = trans.translate(word,src=src_lang,dest=dest_lang)
                self.word_mean = translate.text
                return self.word_mean
                

translator_ = Tranlate()


class Ui_Page(object):
        
        def __init__(self):
                self.setupUi
                languages()


        def setupUi(self, Page):
                Page.setObjectName("Page")
                Page.resize(614, 297)
                Page.setStyleSheet("background-color: rgb(217, 217, 217);")

                self.src_word = QtWidgets.QLineEdit(Page)
                self.src_word.setGeometry(QtCore.QRect(30, 30, 191, 31))
                self.src_word.setStyleSheet("background-color: rgb(221, 221, 221);\n"
        "font: 10pt \"Arial\";")
                self.src_word.setObjectName("src_word")

                self.src_combo = QtWidgets.QComboBox(Page)
                self.src_combo.setGeometry(QtCore.QRect(220, 30, 61, 31))
                
                self.word_mean = QtWidgets.QLineEdit(Page)
                self.word_mean.setGeometry(QtCore.QRect(350, 30, 191, 31))
                self.word_mean.setStyleSheet("background-color: rgb(215, 209, 209);\ncolor: rgb(209, 0, 0);"
        "font: 10pt \"Arial\";")

                self.mean_combo = QtWidgets.QComboBox(Page)
                self.mean_combo.setGeometry(QtCore.QRect(540, 30, 61, 31))
                
                self.translate = QtWidgets.QPushButton(Page)
                self.translate.setGeometry(QtCore.QRect(30, 70, 571, 28))
                self.translate.setStyleSheet("background-color: rgb(135, 135, 255);")
                
                self.word_save = QtWidgets.QPushButton(Page)
                self.word_save.setGeometry(QtCore.QRect(32, 100, 571, 28))
                self.word_save.setStyleSheet("background-color: rgb(135, 135, 255);")

                self.sentence_mean = QtWidgets.QLineEdit(Page)
                self.sentence_mean.setGeometry(QtCore.QRect(70,180,531,31))
                self.sentence_mean.setStyleSheet("background-color: rgb(215, 209, 209);\ncolor: rgb(209, 0, 0);"
        "font: 10pt \"Arial\";")

                self.change_lang = QtWidgets.QPushButton(Page)
                self.change_lang.setGeometry(QtCore.QRect(290, 30, 51, 31))
                self.change_lang.setIcon(QtGui.QIcon(r"change_sym.png"))
                self.change_lang.clicked.connect(self.change_lang_opp)

                self.save = QtWidgets.QPushButton(Page)
                self.save.setGeometry(QtCore.QRect(360,220,241,28))
                self.save.setStyleSheet("background-color: rgb(135, 135, 255);")

                self.new_translatei = QtWidgets.QPushButton(Page)
                self.new_translatei.setGeometry(QtCore.QRect(142,220,221,28))
                self.new_translatei.setStyleSheet("background-color: rgb(135, 135, 255);")

                self.open_save_words = QtWidgets.QPushButton(Page)
                self.open_save_words.setGeometry(QtCore.QRect(10, 260, 591, 28))
                self.open_save_words.setStyleSheet("background-color: rgb(96, 96, 255);")
                self.open_save_words.clicked.connect(self.second_menu)

                self.src_sentence = QtWidgets.QPlainTextEdit(Page)
                self.src_sentence.setGeometry(QtCore.QRect(70,140,531,31))
                self.src_sentence.setStyleSheet("background-color: rgb(220, 220, 220);\n"
        "font: 10pt \"Arial\";")

                self.label = QtWidgets.QLabel(Page)
                self.label.setGeometry(QtCore.QRect(90, 6, 51, 20))
                self.label.setStyleSheet("background-color: rgb(191, 191, 191);\n"
        "font: 10pt \"Arial\";")

                self.label_2 = QtWidgets.QLabel(Page)
                self.label_2.setGeometry(QtCore.QRect(430, 6, 51, 21))
                self.label_2.setStyleSheet("background-color: rgb(191, 191, 191);\n"
        "font: 10pt \"Arial\";")

                self.label_3 = QtWidgets.QLabel(Page)
                self.label_3.setGeometry(QtCore.QRect(10,140, 51, 31))
                self.label_3.setStyleSheet("background-color: rgb(191, 191, 191);\n"
        "font: 10pt \"Arial\";")
                
                self.label_4 = QtWidgets.QLabel(Page)
                self.label_4.setGeometry(QtCore.QRect(10,180,51 ,31))
                self.label_4.setStyleSheet("background-color: rgb(191, 191, 191);\n"
        "font: 10pt \"Arial\";")

                self.new_translatei.clicked.connect(self.function_1)
                self.translate.clicked.connect(self.translateiBtn)
                self.word_save.clicked.connect(self.save_sentence)
                self.save.clicked.connect(self.last_saver)

                self.combo_content()
                self.mean_combo.setCurrentIndex(96)
                self.src_combo.setCurrentIndex(21)

                self.sentence_mean.hide()
                self.src_sentence.hide()
                self.label_3.hide()
                self.label_4.hide()
                self.save.hide()
                self.new_translatei.hide()

                self.retranslateUi(Page)
                QtCore.QMetaObject.connectSlotsByName(Page)

                self.words_menu = Form()
                self.words_menu.pushButton.clicked.connect(self.close_main_save)


        def retranslateUi(self, Page):
                _translate = QtCore.QCoreApplication.translate
                Page.setWindowTitle(_translate("Page", "Notebook"))
                self.translate.setText(_translate("Page", "TRANSLATE"))
                self.word_save.setText(_translate("Page", "SAVE WORD"))
                self.save.setText(_translate("Page", "SAVE"))
                self.open_save_words.setText(_translate("Page", "SEE SAVED WORDS"))
                self.label.setText(_translate("Page", "Word"))
                self.label_2.setText(_translate("Page", "Mean"))
                self.label_3.setText(_translate("Page", "Sntnc"))
                self.label_4.setText(_translate("Page", "Mean"))
                self.new_translatei.setText(_translate("Page", "New Tranlate"))

        def second_menu(self):
                if self.words_menu.isHidden():
                        self.words_menu.content()
                        self.words_menu.show()
                else:
                        self.words_menu.hide()

        def close_main_save(self):
                self.words_menu.close_save()
                self.words_menu.hide()

        def combo_content(self):
                for i in list_language:
                        self.src_combo.addItem(i)
                        self.mean_combo.addItem(i)

        
        def translateiBtn(self):
                try:
                        src_word = self.src_word.text()
                        src_lang = list_language[self.src_combo.currentIndex()]
                        des_lang = list_language[self.mean_combo.currentIndex()]
                        mean = translator_.translatei(src_word,src_lang,des_lang)
                        self.word_mean.setText(mean)
                except:
                        self.src_sentence.clear()
                        self.src_word.clear()

        def change_lang_opp(self):
                src = self.src_combo.currentIndex()
                mean = self.mean_combo.currentIndex()
                self.src_combo.setCurrentIndex(mean)
                self.mean_combo.setCurrentIndex(src)

        def save_sentence(self):
                self.sentence_mean.show()
                self.src_sentence.show()
                self.label_3.show()
                self.label_4.show()
                self.save.show()
                self.new_translatei.show()
        
        def last_text(self):
                src_word = self.src_word.text()
                word_mean = self.word_mean.text()
                src_sentence = self.src_sentence.toPlainText()
                sentence_mean = self.sentence_mean.text()
                
                with open(r"saved_words.txt","a",encoding="utf-8") as file:
                        text = "> "+ src_word +" = " + word_mean+"\n"
                        text2 = "      > "+src_sentence+"\n"
                        text3 = "      >"+sentence_mean+"\n"
                        file.write(text)
                        file.write(text2)
                        file.write(text3)


        def last_saver(self):
                try:
                        self.translateiBtn()
                        src_word_2 = self.src_sentence.toPlainText()
                        src_lang_2 = list_language[self.src_combo.currentIndex()]
                        des_lang_2 = list_language[self.mean_combo.currentIndex()]
                        mean_2 = translator_.translatei(src_word_2,src_lang_2,des_lang_2)
                        self.sentence_mean.setText(mean_2)
                except:
                        pass
                self.last_text()

        def function_1(self):
                self.sentence_mean.hide()
                self.src_sentence.hide()
                self.label_3.hide()
                self.label_4.hide()
                self.save.hide()
                self.new_translatei.hide()

                self.src_word.clear()
                self.word_mean.clear()
                self.src_sentence.clear()
                self.sentence_mean.clear()



class Form(QtWidgets.QMainWindow):

        def __init__(self):
                super().__init__()

                self.setObjectName("Saved Words")
                self.resize(702, 431)
                self.setStyleSheet("background-color: rgb(217, 217, 217);")


                self.plainTextEdit = QtWidgets.QPlainTextEdit(self)
                self.plainTextEdit.setGeometry(QtCore.QRect(20, 10, 661, 371))
                self.plainTextEdit.setStyleSheet("background-color: rgb(230, 230, 230);\n"
        "font: 10pt \"Arial\";")
                self.plainTextEdit.setObjectName("plainTextEdit")


                self.pushButton = QtWidgets.QPushButton(self)
                self.pushButton.setGeometry(QtCore.QRect(20, 390, 661, 28))
                self.pushButton.setStyleSheet("background-color: rgb(150, 150, 150);")
                self.pushButton.setObjectName("pushButton")

                self.setWindowTitle("Saved Words")
                self.pushButton.setText("Save and Close")

                self.content()
                


        def content(self):
                with open(r"saved_words.txt","r",encoding="utf-8") as file:
                        text = file.read()
                        self.plainTextEdit.setPlainText(text)





        def close_save(self):
                text = self.plainTextEdit.toPlainText()
                self.plainTextEdit.clear()
                with open(r"saved_words.txt","w",encoding="utf-8") as file:
                        file.write(text)


        
if __name__ == "__main__":
        import sys

        app = QtWidgets.QApplication(sys.argv)
        Page = QtWidgets.QWidget()
        ui = Ui_Page()
        ui.setupUi(Page)
        Page.show()
        sys.exit(app.exec_())

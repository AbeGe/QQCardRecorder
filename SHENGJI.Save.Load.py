# -*- coding: cp936 -*-
import time

##################### save / load
def getFileNameForSave():
        timestamp = time.strftime('%y.%m.%d.%H.%M',time.localtime(time.time()))
        return 'game.recored.'+timestamp+'.txt'

def saveGame(anal):
        name = getFileNameForSave()
        saveGameHistory(anal['HISTORY'], name)
        return name

def friendHistory(history):
        for x in history:
                y = history[x]
                history[x] = ''.join(y)
        return history

def saveGameHistory(history, name):
        try:
                with open(name, 'w') as out:
                        printGameHistoryToFile(friendHistory(history), out)
        except IOError as err:
                print('failed to save file' + str(err))

def printGameHistoryToFile(friendlyHistory, outFile):
        attrs = ['SXD', '����', '�¼�', '�Լ�', '�ϼ�']
        for x in attrs:
                print(x+':'+friendlyHistory[x], file=outFile)

def uploadFile(name):
        pass # TODO

##################### we start to read data from game and handle now.
if __name__ == '__main__':
        history = {'�¼�': ['��Q', '��4', '��3', '��3', '|', '��6', '|', '÷6', '÷6', '|', '÷9', '÷4', '|', '��4', '��4', '|', '÷A', '÷5', '|', '��2', '|', '��4', '��4', '|', '��ʮ', '|', '��6', '|', '÷2', '|', '��5', '|', '��J', '��7', '��7', '|'], 'SXD': ['����', '|', '����', '|', '����', '|', '����', '|', '����', '|', '����', '|', '����', '|', '�Լ�', '|', '�Լ�', '|', '����', '|', '�ϼ�', '|', '�¼�', '|', '����', '|'], '�ϼ�': ['��A', '��K', '��J', '��5', '|', '��3', '|', '÷J', '÷9', '|', '÷ʮ', '��J', '|', '��3', '��3', '|', '��Q', '��5', '|', '��6', '|', '��A', '��ʮ', '|', '��K', '|', '��2', '|', '��8', '|', '÷2', '|', '��2', '��Q', '��9', '|'], '����': ['��8', '��8', '��7', '��7', '|', '��A', '|', '÷Q', '÷Q', '|', '÷7', '÷7', '|', '��A', '��A', '|', '÷3', '÷3', '|', '��8', '|', '��K', '��Q', '|', '��2', '|', '��5', '|', '��J', '|', '��2', '|', '÷K', '÷J', '÷5', '|'], '�Լ�': ['��9', '��9', '��6', '��6', '|', '��6', '|', '÷8', '÷8', '|', '÷K', '÷ʮ', '|', '��ʮ', '��9', '|', '÷A', '÷4', '|', 'С��', '|', '��9', '��9', '|', '��7', '|', '��2', '|', '��Q', '|', '��ʮ', '|', '��A', '��J', '��8', '|']}
        
        saveGameHistory(history, 'test.~')

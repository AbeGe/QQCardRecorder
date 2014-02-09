# -*- coding: cp936 -*-
from ctypes import *
from ctypes.wintypes import *
from time import sleep
import psutil
import SHENGJI.py

utarray = []

def testCaptureMem():
        global readByteAsInt
        global readACardAsString
        readByteAsIntBackUP = readByteAsInt
        readACardAsStringBackUP = readACardAsString

        readByteAsInt = lambda x : 3
        readACardAsString = lambda x : '��2'

        captureMem()

        readACardAsString = readACardAsStringBackUP
        readByteAsInt = readByteAsIntBackUP
utarray.append(testCaptureMem)

def testResetHistory():
        ret = resetHistory()
        assert len(ret) == 4
utarray.append(resetHistory)

def testConvertToFEN():
        assert convertToFEN('��5') == 5
        assert convertToFEN('��ʮ') == 10
        assert convertToFEN('��K') == 10
        assert convertToFEN('��Q') == 0
utarray.append(testConvertToFEN)

def testResetREN():
        ret = resetFEN()
        assert len(ret) == 24
        assert 200 == sum([convertToFEN(x) for x in ret])
utarray.append(testResetREN)

def testMakeACard():
        assert makeACard('��', '3') == '��3'
        assert makeACard('��', '����') == '����'
        assert makeACard('��', 'С��') == 'С��'
        assert makeACard('��', '3') == '��3'
utarray.append(testMakeACard)

def testGetHs():
        assert getHsOfCard("����") == "��"
        assert getHsOfCard("С��") == "��"
        assert getHsOfCard("��3") == "��"
        assert getHsOfCard("��3") == "��"
utarray.append(testGetHs)

def testGetPm():
        assert getPmOfCard("����") == "����"
        assert getPmOfCard("С��") == "С��"
        assert getPmOfCard("��J") == "J"
utarray.append(testGetPm)

def testHasPair():
        assert getPairList(['����','����']) == ['��']
        assert getPairList(['����','����', '��3', '��3']) == ['��', '��']
        assert getPairList(['��4', '����','����']) == ['��']
        assert getPairList(['����']) == []
        assert getPairList(['С��','����']) == []
utarray.append(testHasPair)

def testMatchPairList():
        assert matchesPairList(['��'], ['��'])
        assert not matchesPairList(['��'], ['��'])
        assert not matchesPairList(['��'], ['��', '��'])
utarray.append(testMatchPairList)

def testAnalSylCategory():
        anal = resetAnal('��', '2')
        anal['SYL_SXD'] = '�¼�'
        anal['SYL'] = {}
        anal['SYL']['����'] = ['��3']
        anal['SYL']['�¼�'] = ['��4']
        anal['SYL']['�Լ�'] = ['÷5']
        anal['SYL']['�ϼ�'] = ['��6']

        analOnceRoundFinished(anal)

        assert anal['sylCategory'] == '��'
utarray.append(testAnalSylCategory)
def testLackOfColorBasic():
        anal = resetAnal('��', '2')
        anal['SYL_SXD'] = '�¼�'
        anal['SYL'] = {}
        anal['SYL']['����'] = ['��3']
        anal['SYL']['�¼�'] = ['��4']
        anal['SYL']['�Լ�'] = ['÷5']
        anal['SYL']['�ϼ�'] = ['��6']

        analOnceRoundFinished(anal)

        assert '�����޺�' in anal['conclusions']
        assert '�Լ��޺�' in anal['conclusions']
        assert '�ϼ��޺�' in anal['conclusions']
utarray.append(testLackOfColorBasic)
def testLackOfColorComplex():
        anal = resetAnal('��', '2')
        anal['SYL_SXD'] = '�¼�'
        anal['SYL'] = {}
        anal['SYL']['����'] = ['��3', '��3']
        anal['SYL']['�¼�'] = ['��4', '��5']
        anal['SYL']['�Լ�'] = ['÷5', '��5']
        anal['SYL']['�ϼ�'] = ['��6', '��6']

        analOnceRoundFinished(anal)

        assert '�����޺�' in anal['conclusions']
        assert '�Լ��޺�' in anal['conclusions']
        assert '�ϼ��޺�' in anal['conclusions']
utarray.append(testLackOfColorComplex)
def testLackOfZP():
        anal = resetAnal('��', '2')
        anal['SYL_SXD'] = '�¼�'
        anal['SYL'] = {}
        anal['SYL']['����'] = ['��3']
        anal['SYL']['�¼�'] = ['��4']
        anal['SYL']['�Լ�'] = ['÷5']
        anal['SYL']['�ϼ�'] = ['��6']

        analOnceRoundFinished(anal)

        assert '��������' in anal['conclusions']
        assert '�Լ�����' in anal['conclusions']
        assert '�ϼ�����' in anal['conclusions']
utarray.append(testLackOfZP)
def testLackOfZP2():
        anal = resetAnal('��', '2')
        anal['SYL_SXD'] = '�¼�'
        anal['SYL'] = {}
        anal['SYL']['����'] = ['��3']
        anal['SYL']['�¼�'] = ['����']
        anal['SYL']['�Լ�'] = ['÷5']
        anal['SYL']['�ϼ�'] = ['��6']

        analOnceRoundFinished(anal)

        assert '��������' in anal['conclusions']
        assert '�Լ�����' in anal['conclusions']
        assert '�ϼ�����' in anal['conclusions']
utarray.append(testLackOfZP2)
def testLackOfPair():
        anal = resetAnal('��', '2')
        anal['SYL_SXD'] = '�¼�'
        anal['SYL'] = {}
        anal['SYL']['����'] = ['��8', '��3']
        anal['SYL']['�¼�'] = ['��4', '��4']
        anal['SYL']['�Լ�'] = ['��9', '��5']
        anal['SYL']['�ϼ�'] = ['��J', '��6']

        analOnceRoundFinished(anal)
        assert '�����޺��' in anal['conclusions']
        assert '�Լ��޺��' in anal['conclusions']
        assert '�ϼ��޺��' in anal['conclusions']
utarray.append(testLackOfPair)
def testLackOfPairComplex():
        anal = resetAnal('��', '2')
        anal['SYL_SXD'] = '�¼�'
        anal['SYL'] = {}
        anal['SYL']['����'] = ['��8', '��3']
        anal['SYL']['�¼�'] = ['��4', '��4']
        anal['SYL']['�Լ�'] = ['��5', '��5']
        anal['SYL']['�ϼ�'] = ['��J', '��6']

        analOnceRoundFinished(anal)
        assert '�����޺��' in anal['conclusions']
        assert '�Լ��޺��' in anal['conclusions']
        assert '�ϼ��޺��' in anal['conclusions']
utarray.append(testLackOfPairComplex)

def testAnalSxd():
        mem = {}
        mem['CPS_BL'] = {}
        def f(x,y): mem['CPS_BL'][XS[x]]=y
        def g(y1,y2,y3,y4):
                f(1,y1)
                f(2,y2)
                f(3,y3)
                f(4,y4)
        g(0,0,0,1)
        assert analSxd(mem) == '�ϼ�'
        g(0,0,1,1)
        assert analSxd(mem) == '�Լ�'
        g(0,1,1,1)
        assert analSxd(mem) == '�¼�'
        g(1,0,0,0)
        assert analSxd(mem) == '����'
        g(1,0,0,1)
        assert analSxd(mem) == '�ϼ�'
        g(1,0,1,1)
        assert analSxd(mem) == '�Լ�'
utarray.append(testAnalSxd)

def testGetCatogory():
        anal = {}
        anal['zp'] = '��2'
        assert getCatogoryFromTotalCards(anal, '��2') == '��'
        assert getCatogoryFromTotalCards(anal, '��2') == '��'
        assert getCatogoryFromTotalCards(anal, '��3') == '��'
        assert getCatogoryFromTotalCards(anal, '����') == '��'
        assert getCatogoryFromTotalCards(anal, 'С��') == '��'
        assert getCatogoryFromTotalCards(anal, '��3') == '��'
        anal['zp'] = '��2'
        assert getCatogoryFromTotalCards(anal, '��2') == '��'
        assert getCatogoryFromTotalCards(anal, '��3') == '��'
        assert getCatogoryFromTotalCards(anal, '����') == '��'
        assert getCatogoryFromTotalCards(anal, 'С��') == '��'
utarray.append(testGetCatogory)


testing = 1==0
if testing:
        for ut in utarray:
                ut()
        print('ut passed')


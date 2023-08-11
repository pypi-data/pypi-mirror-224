from PySide6 import QtCore, QtGui, QtWidgets


class QCrossItem(QtCore.QObject):
    def __init__(self, parent=None, size=10, color=None):
        super().__init__(parent)
        self.__call__(size=size, color=color)

    def __call__(self, size=10, color=None):
        if color is None:
            color = QtGui.QColor(255, 0, 0, 150) # 默认红色, 半透明, 150
        self.CrossItemIsAdd = False
        # 初始化十字叉丝, 十字叉丝的图元为两条线段
        self.Cross_1 = QtWidgets.QGraphicsLineItem()
        self.Cross_2 = QtWidgets.QGraphicsLineItem()
        # 设置十字叉丝的大小
        self.Cross_1.setLine(-size, 0, size, 0)
        self.Cross_2.setLine(0, -size, 0, size)
        # 设置十字叉丝的层级
        self.Cross_1.setZValue(1)
        self.Cross_2.setZValue(1)
        # 设置十字叉丝的颜色
        pen = self.Cross_1.pen()
        pen.setColor(QtGui.QColor(255, 0, 0, 150))
        self.Cross_1.setPen(pen)
        self.Cross_2.setPen(pen)

    def addCrossWire(self, TargetScene):
        # 将十字叉丝加入到场景中去
        if self.CrossItemIsAdd == False:
            TargetScene.addItem(self.Cross_1)
            TargetScene.addItem(self.Cross_2)
            self.CrossItemIsAdd == True
            self.ParentScene = TargetScene

    def updateCrossWire(self, QPointF):
        # 在场景中更新十字叉丝的位置
        QPointF = (int(QPointF.x()), int(QPointF.y()))
        self.Cross_1.setPos(QPointF[0] + 0.5, QPointF[1] + 0.5)  # 设置十字中心位置
        self.Cross_2.setPos(QPointF[0] + 0.5, QPointF[1] + 0.5)  # 设置十字中心位置

    def removeCrossWire(self):
        # 从场景中移除十字叉丝
        if self.CrossItemIsAdd:
            self.ParentScene.removeItem(self.Cross_1)
            self.ParentScene.removeItem(self.Cross_2)

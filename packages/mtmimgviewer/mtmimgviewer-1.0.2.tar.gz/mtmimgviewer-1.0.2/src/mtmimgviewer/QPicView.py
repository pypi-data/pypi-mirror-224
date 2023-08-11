from PySide6 import QtCore, QtGui, QtWidgets
from .QCrossItem import QCrossItem
import typing

class QPicView(QtWidgets.QGraphicsView):
    KeyEvent = QtCore.Signal(QtGui.QKeyEvent)

    def __init__(self, scene: QtWidgets.QGraphicsScene = None, parent: typing.Optional[QtWidgets.QWidget] = ...) -> None:
        if scene is None:
            scene = QtWidgets.QGraphicsScene()
        super().__init__(scene, parent=parent)

        self.iscene = scene
        self.CrossItemObject = QCrossItem()
        self.CrossItemObject.addCrossWire(self.iscene)
        self.setAlignment(QtCore.Qt.AlignCenter)  #默认为场景在中心显示
        self.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CrossCursor))  # 设置鼠标光标显示

    def mousePressEvent(self, QMouseEvent):
        QPointF = self.mapToScene(QMouseEvent.pos())
        self.CrossItemObject.updateCrossWire(QPointF)
        self.viewport().update()  # 更新,避免出现残留影像
        if QMouseEvent.buttons() == QtCore.Qt.LeftButton:  # 中键开始拖动
            self.Drag = True
            self.CenterScenePos = self.mapToScene(QMouseEvent.pos())
        return super().mousePressEvent(QMouseEvent)

    def mouseMoveEvent(self, QMouseEvent):
        QPointF = self.mapToScene(QMouseEvent.pos())
        self.CrossItemObject.updateCrossWire(QPointF)
        self.viewport().update()  # 更新,避免出现残留影像

        if self.Drag == True:
            CenterP = self.mapToScene(self.viewport().rect().center())
            MouseP = self.mapToScene(QMouseEvent.pos())
            self.CenterOnUnderMouse_SceneScaleNoChange(self.CenterScenePos, CenterP, MouseP)
        # return super().mouseMoveEvent(QMouseEvent)

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        self.KeyEvent.emit(event)
        # return super().keyPressEvent(event)

    def mouseReleaseEvent(self, QMouseEvent):
        self.Drag = False
        # return super().mouseReleaseEvent(QMouseEvent)
    def wheelEvent(self, event):
        # Set parameter
        zoomInFactor = 1.1  # 每次的缩放倍数
        zoomOutFactor = 1 / zoomInFactor
        mySceneRect = self.sceneRect()  # 记录缩放前的场景矩形值

        OldMouseP = event.points()[0].pos()  # 记录缩放前的场景鼠标坐标
        OldMouseP = self.mapToScene(OldMouseP.toPoint())
        # Zoom
        if event.angleDelta().y() > 0:
            zoomFactor = zoomInFactor
        else:
            zoomFactor = zoomOutFactor
        self.scale(zoomFactor, zoomFactor)  # 根据缩放参数进行缩放

        # Set SceneRect
        self.setSceneRect(mySceneRect)  # 设置场景矩形值，使得缩小后图形始终在中央显示，避免滚动条的出现
        NewCenterP = self.viewport().rect().center()
        NewCenterP = self.mapToScene(NewCenterP)  # 记录缩放后的场景中心坐标
        NewMouseP = event.points()[0].pos()
        NewMouseP = self.mapToScene(NewMouseP.toPoint())  # 记录缩放后的场景鼠标坐标
        self.CenterOnUnderMouse_SceneScaleNoChange(OldMouseP, NewCenterP, NewMouseP)

    def CenterOnUnderMouse_SceneScaleNoChange(self, OldMouseP, NewCenterP, NewMouseP):
        DIff = NewMouseP - NewCenterP
        SetCenterP = OldMouseP - DIff
        self.centerOn(SetCenterP)

    def paint_pic(self, img):
        '''
        @img: RGB格式图像
        '''
        if type(img) == str:
            self.png = QtGui.QPixmap(img)
            width = self.png.width()
            height = self.png.height()
        else:
            self.png = img.toqpixmap()  # 读取像素图
            width, height = img.width, img.height
        self.iscene.clear()
        # 增加十字叉丝
        self.CrossItemObject = QCrossItem()
        self.CrossItemObject.addCrossWire(self.iscene)
        self.IsPloted = True
        self.iscene.addPixmap(self.png)  # 在场景里加入像素图
        self.setSceneRect(0, 0, width, height)
        self.iscene.setSceneRect(0, 0, width, height)
        self.update()
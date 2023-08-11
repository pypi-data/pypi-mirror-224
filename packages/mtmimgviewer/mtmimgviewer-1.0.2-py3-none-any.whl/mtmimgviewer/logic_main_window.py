from PySide6 import QtCore, QtGui, QtWidgets
from .QPicView import QPicView
from PIL import Image
import os


class Interface_mainWindow(QtWidgets.QWidget):
    def __init__(self, pic_lists: list[list], window_size=None, window_title=None, **kwargs):
        super(Interface_mainWindow, self).__init__()
        self.pic_lists = pic_lists
        self.length = len(pic_lists[0]) if len(pic_lists) and len(pic_lists[0]) else 0
        if window_size is not None:
            self.resize(*window_size)
        if window_title is not None:
            self.setWindowTitle(window_title)
        self.__sequence_dict__ = {}
        self.listWidget = None
        pass

    def recur_load(self, struct, node):
        for item in struct:
            if isinstance(item, int):
                Component_rootnode, Component_childnode = self.create_view()
                node.addLayout(Component_rootnode)
                self.__sequence_dict__[item] = Component_childnode
            if isinstance(item, str):
                if item in ["HBoxLayout", "VBoxLayout"]:
                    if item == "HBoxLayout":
                        newnode = QtWidgets.QHBoxLayout(self) if node is None else QtWidgets.QHBoxLayout()
                    if item == "VBoxLayout":
                        newnode = QtWidgets.QVBoxLayout(self) if node is None else QtWidgets.QVBoxLayout()
                    newnode.setContentsMargins(0, 0, 0, 0)
                    self.recur_load(struct[item], newnode)
                    if node is not None:
                        node.addLayout(newnode)
                elif item == "setStretch":
                    node.setStretch(*struct[item])
                if item == "ListWidget":
                    newnode = QtWidgets.QListWidget(self) if node is None else QtWidgets.QListWidget()
                    node.addWidget(newnode)
                    newnode.setContentsMargins(0, 0, 0, 0)
                    self.listWidget = newnode
                    self.listWidget.addItems([str(i) for i in list(range(self.length))])
                    self.listWidget.itemClicked.connect(self.func_update_pic)

            if isinstance(item, dict):
                self.recur_load(item, node)

    def __init_interface__(self, struct: dict):
        self.gV = []
        self.labels = []
        self.recur_load(struct, None)
        for key in sorted(self.__sequence_dict__.keys()):
            self.gV.append(self.__sequence_dict__[key][0])
            self.labels.append(self.__sequence_dict__[key][1])

    def create_view(self):
        verticalLayout = QtWidgets.QVBoxLayout()
        gV = QPicView(None, parent=self)
        gV.KeyEvent.connect(self.keyPressEvent)
        verticalLayout.addWidget(gV)
        label = QtWidgets.QLabel(self)
        label.setScaledContents(True)
        label.setAlignment(QtCore.Qt.AlignCenter)
        verticalLayout.addWidget(label)
        return verticalLayout, [gV, label]

    def keyPressEvent(self, event):
        if event.key() == QtGui.Qt.Key_Left:
            self.idx = self.idx - 1 if self.idx > 0 else (self.length - 1 if self.length > 0 else 0)
            self.func_update_pic()
        if event.key() == QtGui.Qt.Key_Right:
            self.idx = self.idx + 1 if self.idx < self.length - 1 else 0
            self.func_update_pic()

    def func_update_pic(self, idx=None):
        if idx is not None:
            if type(idx) == int:
                self.idx = idx
            else:
                self.idx = int(idx.text())
        if len(self.pic_lists) > 0 and len(self.pic_lists[0]) > 0:
            self.length = len(self.pic_lists[0])
            for idx, pic_list in enumerate(self.pic_lists):
                self.gV[idx].paint_pic(pic_list[self.idx])
                # self.func_paint_pic(self.gV[idx], pic_list[self.idx])
                self.func_text_set(self.labels[idx], f"{self.idx}: " + os.path.basename(pic_list[self.idx]))  #
        self.listWidget.setCurrentRow(self.idx)

    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:
        if event.type() == event.KeyPress:
            return self.keyPressEvent(event)
        return super().eventFilter(watched, event)

    def func_text_set(self, obj: QtWidgets.QLabel, text):
        obj.setText(text)

from PySide2 import QtCore, QtWidgets, QtWebEngineWidgets
from PySide2.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from activity_browser.layouts.tabs import PluginTab
from activity_browser.ui.style import horizontal_line, header

class RightTab(PluginTab):
    def __init__(self, plugin,parent=None):
        super(RightTab, self).__init__(plugin=plugin, panel="right", parent=parent)
        self.layout = QtWidgets.QGridLayout()
        self.main_view = QWebEngineView()
        self.main_view.setUrl("http://localhost:9000/")
        self.layout.addWidget(self.main_view,0,0)
        self.setLayout(self.layout)    

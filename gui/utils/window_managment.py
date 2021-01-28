from PySide6 import QtCore, QtGui


def adjust_by_screen(window, ratio=1.5):
    screen = QtGui.QGuiApplication.primaryScreen()
    screen_center = screen.availableGeometry().center()

    adj_win_size = screen.size() / ratio
    win_size = window.size().scaled(adj_win_size, QtCore.Qt.KeepAspectRatio)
    app_middle = QtCore.QPoint(win_size.width() / 2,
                               win_size.height() / 2)

    new_place = screen_center - app_middle

    window.resize(win_size)
    window.move(new_place)

# def set_mergins(window, layout, w_ratio=0.2, y_ratio=0):
# 
#     w_margins = QtCore.QMargins(1, 0, 1, 0) \
#                 * window.parent().size().width() * w_ratio
# 
#     h_margins = QtCore.QMargins(0, 1, 0, 1) \
#                 * window.parent().size().height() * y_ratio
# 
#     margins = w_margins + h_margins
#     layout.setContentsMargins(margins)

def set_mergins(window, layout, w_ratio=0.2, y_ratio=0):

    w_margins = QtCore.QMargins(1, 0, 1, 0) \
                * window.size().width() * w_ratio

    h_margins = QtCore.QMargins(0, 1, 0, 1) \
                * window.size().height() * y_ratio

    margins = w_margins + h_margins
    layout.setContentsMargins(margins)

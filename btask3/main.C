#include <QApplication>

#include "MainWindow.H"

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    MainWindow imageWin;
    imageWin.resize(400, 300);
    imageWin.show();
    return app.exec();
}

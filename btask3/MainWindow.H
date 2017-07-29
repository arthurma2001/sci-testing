#ifndef IMAGEWINDOW_H
#define IMAGEWINDOW_H

#include <QMainWindow>

class QAction;
class QLabel;
class QMenu;
class QMdiArea;
class QActionGroup;
class ImageWindow;

class MainWindow : public QMainWindow
{
  Q_OBJECT

public:
  MainWindow();

  ImageWindow *activeImageWindow();
  void addImageWindow(ImageWindow *editor);

protected:
  void closeEvent(QCloseEvent *event);
                                  
private slots:
  void open();
  void updateActions();

private:
  void createActions();
  void createMenus();
  bool okToContinue();
  void loadFile(const QString &fileName);
  void saveFile(const QString &fileName);
  void setCurrentFile(const QString &fileName);
  QString strippedName(const QString &fullFileName);
  
  QMdiArea *mdiArea;
  QByteArray imageFormat;
  QString curFile;

  QMenu *fileMenu;
  QAction *openAction;
  QAction *exitAction;

  QMenu *windowMenu;
  QActionGroup *windowActionGroup;
  QAction *closeAction;
  QAction *closeAllAction;
  QAction *tileAction;
  QAction *cascadeAction;
  QAction *nextAction;
  QAction *previousAction;
};

#endif

#include <QtGui>
#include "MainWindow.H"
#include "ImageWindow.H"

MainWindow::MainWindow()
{
  mdiArea = new QMdiArea;
  setCentralWidget(mdiArea);
  connect(mdiArea, SIGNAL(subWindowActivated(QMdiSubWindow*)),
          this, SLOT(updateActions()));

  createActions();
  createMenus();

  statusBar()->showMessage(tr("Ready"), 2000);
  setCurrentFile("");
}

void MainWindow::closeEvent(QCloseEvent *event)
{
  if (okToContinue()) {
    event->accept();
  } else {
    event->ignore();
  }
}

void MainWindow::open()
{
  if (okToContinue()) {
    QString fileName = QFileDialog::getOpenFileName(this);
    if (!fileName.isEmpty())
      loadFile(fileName);
  }
}

void MainWindow::createActions()
{
  openAction = new QAction(tr("&Open..."), this);
  openAction->setShortcut(QKeySequence::Open);
  openAction->setStatusTip(tr("Open an existing image file"));
  connect(openAction, SIGNAL(triggered()), this, SLOT(open()));

  exitAction = new QAction(tr("E&xit"), this);
  exitAction->setShortcut(tr("Ctrl+Q"));
  exitAction->setStatusTip(tr("Exit the application"));
  connect(exitAction, SIGNAL(triggered()), this, SLOT(close()));

  closeAction = new QAction(tr("Cl&ose"), this);
  closeAction->setShortcut(QKeySequence::Close);
  closeAction->setStatusTip(tr("Close the active window"));
  connect(closeAction, SIGNAL(triggered()),
          mdiArea, SLOT(closeActiveSubWindow()));

  closeAllAction = new QAction(tr("Close &All"), this);
  closeAllAction->setStatusTip(tr("Close all the windows"));
  connect(closeAllAction, SIGNAL(triggered()), this, SLOT(close()));

  tileAction = new QAction(tr("&Tile"), this);
  tileAction->setStatusTip(tr("Tile the windows"));
  connect(tileAction, SIGNAL(triggered()),
          mdiArea, SLOT(tileSubWindows()));

  cascadeAction = new QAction(tr("&Cascade"), this);
  cascadeAction->setStatusTip(tr("Cascade the windows"));
  connect(cascadeAction, SIGNAL(triggered()),
          mdiArea, SLOT(cascadeSubWindows()));
  nextAction = new QAction(tr("Ne&xt"), this);
  nextAction->setShortcut(QKeySequence::NextChild);
  nextAction->setStatusTip(tr("Move the focus to the next window"));
  connect(nextAction, SIGNAL(triggered()),
          mdiArea, SLOT(activateNextSubWindow()));

  previousAction = new QAction(tr("Pre&vious"), this);
  previousAction->setShortcut(QKeySequence::PreviousChild);
  previousAction->setStatusTip(tr("Move the focus to the previous "
                                  "window"));
  connect(previousAction, SIGNAL(triggered()),
          mdiArea, SLOT(activatePreviousSubWindow()));
  windowActionGroup = new QActionGroup(this);
}

void MainWindow::createMenus()
{
  fileMenu = menuBar()->addMenu(tr("&File"));
  fileMenu->addAction(openAction);
  fileMenu->addSeparator();
  fileMenu->addAction(exitAction);
  
   windowMenu = menuBar()->addMenu(tr("&Window"));
   windowMenu->addAction(closeAction);
   windowMenu->addAction(closeAllAction);
   windowMenu->addSeparator();
   windowMenu->addAction(tileAction);
   windowMenu->addAction(cascadeAction);
   windowMenu->addSeparator();
   windowMenu->addAction(nextAction);
   windowMenu->addAction(previousAction);
}

bool MainWindow::okToContinue()
{
  return true;
}

void MainWindow::loadFile(const QString &fileName)
{
  QImage newImage;
  QApplication::setOverrideCursor(Qt::WaitCursor);
  bool loaded = newImage.load(fileName);
  QApplication::restoreOverrideCursor();

  if (loaded) {
    ImageWindow *editor = new ImageWindow (this);
    editor->setImage (fileName, newImage);
    addImageWindow(editor);
    setCurrentFile(fileName);
    statusBar()->showMessage(tr("File loaded"), 2000);
  } else {
    QMessageBox::warning(this, tr("Image Pro"),
                         tr("Error when loading image."));
    statusBar()->showMessage(tr("Loading canceled"), 2000);
  }
}

void MainWindow::setCurrentFile(const QString &fileName)
{
  curFile = fileName;
  setWindowModified(false);

  bool hasImage = !curFile.isEmpty();

  if (hasImage) {
    setWindowTitle(tr("%1[*] - %2").arg(strippedName(curFile))
                   .arg(tr("Image Pro")));
  } else {
    setWindowTitle(tr("Image Pro"));
  }
}

QString MainWindow::strippedName(const QString &fullFileName)
{
  return QFileInfo(fullFileName).fileName();
}

void MainWindow::updateActions()
{
    bool hasEditor = (activeImageWindow() != 0);
}

ImageWindow *MainWindow::activeImageWindow()
{
    QMdiSubWindow *subWindow = mdiArea->activeSubWindow();
    if (subWindow)
        return qobject_cast<ImageWindow *>(subWindow->widget());
    return 0;
}

void MainWindow::addImageWindow(ImageWindow *editor)
{
    QMdiSubWindow *subWindow = mdiArea->addSubWindow(editor);
    windowMenu->addAction(editor->windowMenuAction());
    windowActionGroup->addAction(editor->windowMenuAction());
    subWindow->show();
}

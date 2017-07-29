#include <string.h>
#include <iostream>
using namespace std;
#include <QAction>
#include <QCloseEvent>
#include <QPainter>
#include <QStatusBar>
#include <QMainWindow>
#include "ImageWindow.H"
#include "ImageWidget.H"

class ImageWindowImp
{
public:
  ImageWindowImp (ImageWindow *ins);
  virtual ~ImageWindowImp ();
  
  void init0 ();
  void clear ();
  void draw (QPainter *painter);
  
public:
  ImageWindow *myIns;
  QAction *m_action;
  ImageWidget *m_image_widget;
  QMainWindow *m_main_window;
};
  
ImageWindow::ImageWindow (QWidget *parent, Qt::WindowFlags f):
  QScrollArea (parent)
{
  myImp = new ImageWindowImp (this);
  myImp->m_main_window = dynamic_cast<QMainWindow *>(parent);

  myImp->m_action = new QAction(this);
  myImp->m_action->setCheckable(true);
  connect(myImp->m_action, SIGNAL(triggered()), this, SLOT(show()));
  connect(myImp->m_action, SIGNAL(triggered()), this, SLOT(setFocus()));
  
  myImp->m_image_widget = new ImageWidget (this);
  setWidget (myImp->m_image_widget);
  setWidgetResizable (true);

  connect(myImp->m_image_widget, SIGNAL(cursorFeedback(const QString &)), this, SLOT(onCursorFeedback (const QString &)));
}
  
ImageWindow::~ImageWindow ()
{
  delete myImp;
}

QSize ImageWindow::sizeHint() const
{
  return QSize (640, 480);
}

void ImageWindow::closeEvent(QCloseEvent *event)
{
    if (okToContinue()) {
        event->accept();
    } else {
        event->ignore();
    }
}

bool ImageWindow::okToContinue()
{
  return true;
}

QAction *ImageWindow::windowMenuAction() const
{
  return myImp->m_action;
}

void ImageWindow::setImage (const QString &fname, const QImage &newImage)
{
  int w = newImage.width();
  int h =  newImage.height();
  QSize new_size = QSize (w, h);
  
  myImp->m_image_widget->setImage (fname, newImage);
  myImp->m_image_widget->setMinimumSize (new_size);
  
  myImp->m_action->setText (fname);
  setWindowTitle (fname);
}

void ImageWindow::onCursorFeedback (const QString &msg)
{
  myImp->m_main_window->statusBar()->showMessage (msg);
}

/**
 * Helper
 */
ImageWindowImp::ImageWindowImp (ImageWindow *ins)
{
  myIns = ins;
  init0 ();
}
  
ImageWindowImp::~ImageWindowImp ()
{
  clear ();
}
  
void ImageWindowImp::init0 ()
{
}
  
void ImageWindowImp::clear ()
{
}

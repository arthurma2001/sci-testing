#include <string.h>
#include <iostream>
using namespace std;
#include <QAction>
#include <QCloseEvent>
#include <QPainter>
#include "ImageWidget.H"

class ImageWidgetImp
{
public:
  ImageWidgetImp (ImageWidget *ins);
  virtual ~ImageWidgetImp ();
  
  void init0 ();
  void clear ();
  void draw (QPainter *painter);
  const QString buildFeedback (const QPoint &pos);
  
public:
  ImageWidget *myIns;
  QImage m_image;
  bool m_isUntitled;
};
  
ImageWidget::ImageWidget (QWidget *parent, Qt::WindowFlags f):
  QWidget (parent, f)
{
  myImp = new ImageWidgetImp (this);
  myImp->m_isUntitled = true;
  setMouseTracking(true);
}
  
ImageWidget::~ImageWidget ()
{
  delete myImp;
}

QSize ImageWidget::sizeHint() const
{
  if (myImp->m_isUntitled)
    return QSize (640, 480);
  int w = myImp->m_image.width();
  int h = myImp->m_image.height();
  return QSize (w, h);
}

void ImageWidget::setImage (const QString &fname, const QImage &newImage)
{
  myImp->m_image = newImage;
  myImp->m_isUntitled = false;
}

void ImageWidget::paintEvent(QPaintEvent * event)
{
  QPainter painter(this);
  painter.setRenderHint(QPainter::Antialiasing, true);
  myImp->draw (&painter);
}

void ImageWidget::mouseMoveEvent(QMouseEvent *event)
{
  QPoint pos = event->pos();
  QString msg = myImp->buildFeedback (pos);
  cursorFeedback (msg);
}

void ImageWidget::mousePressEvent(QMouseEvent *event)
{
  QPoint pos = event->pos();
  QString msg = myImp->buildFeedback (pos);
  cursorFeedback (msg);
}

void ImageWidget::mouseReleaseEvent(QMouseEvent *event)
{
}

/**
 * Helper
 */
ImageWidgetImp::ImageWidgetImp (ImageWidget *ins)
{
  myIns = ins;
  init0 ();
}
  
ImageWidgetImp::~ImageWidgetImp ()
{
  clear ();
}
  
void ImageWidgetImp::init0 ()
{
}
  
void ImageWidgetImp::clear ()
{
}

void ImageWidgetImp::draw (QPainter *painter)
{
  painter->drawImage (0, 0, m_image);
}

const QString ImageWidgetImp::buildFeedback (const QPoint &pos)
{
  //fprintf (stderr, "mousePressEvent () - (%d, %d)\n", pos.x(), pos.y());
  int x = pos.x();
  int y = pos.y();
  if (x >= 0 && x < m_image.width() &&
      y >= 0 && y < m_image.height()) {
    QRgb cl = m_image.pixel (pos);
    int r = qRed (cl);
    int g = qGreen (cl);
    int b = qBlue(cl);
    int a = qAlpha(cl);
    char msg[256];
    sprintf (msg, "position=(%d,%d), rgba=(%d,%d,%d,%d)", pos.x(), pos.y(), r, g, b, a);
    return QString (msg);
  }
  return QString("");
}

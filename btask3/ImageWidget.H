#ifndef __ImageWidget_hpp__
#define __ImageWidget_hpp__
#include <QWidget>

class QCloseEvent;
class ImageWidgetImp;

class ImageWidget : public QWidget
{
  Q_OBJECT
public:
  ImageWidget (QWidget *parent = 0, Qt::WindowFlags f = 0);
  virtual ~ImageWidget ();

  void setImage (const QString &fname, const QImage &newImage);
  QSize sizeHint() const;
  
signals:
  void cursorFeedback (const QString &msg);
  
protected:
  virtual void 	paintEvent(QPaintEvent * event);
  virtual void   mouseMoveEvent(QMouseEvent *event);
  virtual void   mousePressEvent(QMouseEvent *event);
  virtual void   mouseReleaseEvent(QMouseEvent *event);

private:
  ImageWidget (const ImageWidget &x);
  ImageWidget & operator=(const ImageWidget &x);
  
private:
  friend class ImageWidgetImp;
  ImageWidgetImp *myImp;
};

#endif

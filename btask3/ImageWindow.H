#ifndef __ImageWindow_hpp__
#define __ImageWindow_hpp__
#include <QScrollArea>

class QCloseEvent;
class ImageWindowImp;

class ImageWindow : public QScrollArea
{
  Q_OBJECT
public:
  ImageWindow (QWidget *parent = 0, Qt::WindowFlags f = 0);
  virtual ~ImageWindow ();

  QAction *windowMenuAction() const;
  void setImage (const QString &fname, const QImage &newImage);
  QSize sizeHint() const;
                        
public slots:
  void onCursorFeedback (const QString &msg);

protected:
  bool okToContinue();
  void closeEvent(QCloseEvent *event);
    
private:
  ImageWindow (const ImageWindow &x);
  ImageWindow & operator=(const ImageWindow &x);
  
private:
  friend class ImageWindowImp;
  ImageWindowImp *myImp;
};

#endif

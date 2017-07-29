#ifndef __CircularArray_hpp__
#define __CircularArray_hpp__
#include <vector>
#include <iostream>
using namespace std;

template<typename T>
class CircularArray
{
  int m_N;
  vector<T> m_data;
public:
  CircularArray (int n, T init_val) {
    m_N = n;
    vector<T> d (n, init_val);
    swap(m_data, d);
  }
    
  ~CircularArray () {
  }
  
  size_t size () const {
    return m_N;
  }
  
  T& operator[] (int i0) {
    int i = i0 % m_N;
    if (i < 0) i += m_N;
    //cout << "i=" << i << endl;
    return m_data[i];
  }
  
  const T& operator[] (int i0) const  {
    int i = i0 % m_N;
    if (i < 0) i += m_N;
    //cout << "i=" << i << endl;
    return m_data[i];
  }
};

template<typename T>
class CircularArrayIter
{
  int index;
  int init_index;
  CircularArray<T> *buf;
public:
  CircularArrayIter(CircularArray<T> *s, int begin_idx)
  {
    buf = s;
    init_index = begin_idx;
  }

  void first()
  {
    index = init_index;
  }

  void next()
  {
    index++;
  }
  
  bool isDone()
  {
    return (index - init_index) == buf->size();
  }
  
  T currentItem()
  {
    return (*buf)[index];
  }
};

#endif

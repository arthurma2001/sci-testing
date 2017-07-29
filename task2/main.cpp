#include <assert.h>
#include "CircularArray.H"

// basic test
static void test001 ()
{
  CircularArray<float> fa(12, 0);
  fa[12] = 5;
  assert (fa[0] == fa[12]);
  fa[-1]=101;
  assert (fa[-1] == fa[11]);
}

// iterator test
static void test002 ()
{
  int N = 10;
  CircularArray<float> fa(N, 0);
  for (int i = 0; i < N; i++) fa[i] = i;

  int init_index = 101;
  CircularArrayIter<float> it(&fa, init_index);
  
  it.first();
  int i = init_index;
  while (! it.isDone()) {
    cout << "i=" << i++ << ", " << it.currentItem() << endl;
    it.next();
  }
}

int main ()
{
  test001 ();
  test002 ();
}

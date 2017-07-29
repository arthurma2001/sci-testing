This demo program can load multiple images and display them as MDI.

1. menu File 
  load --> load file
  exit
2. menu Window -- control MDI display
  close
  closeAll
  Tile
  Cascade
  Next
  Previous
  image filename
  ...
  
3. For feedback - move Mouse over image
  display "position=(x,y), rgba=(r,g,b,a)" to statusBar
4. Add scrollBars to give a better size/fit view for image window 
  (each ImageWindow is a subclass of QScrollArea and show scrollbars automatically as
  needed)

Possible future development
  1. select area of interest, then copy and paste to intended location.
  2. add image processing functions like resize, flip and etc.

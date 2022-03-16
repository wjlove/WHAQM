digits = [[[1,1,1,1,1,1,1,0],
       [1,1,1,1,1,1,1,0],
       [1,1,0,0,0,1,1,0],
       [1,1,0,0,0,1,1,0],
       [1,1,0,0,0,1,1,0],
       [1,1,0,0,0,1,1,0],
       [1,1,1,1,1,1,1,0],
       [1,1,1,1,1,1,1,0]],      
       [[0,1,1,1,0,0,0,0],
       [0,1,1,1,0,0,0,0],
       [0,0,1,1,0,0,0,0],
       [0,0,1,1,0,0,0,0],
       [0,0,1,1,0,0,0,0],
       [0,0,1,1,0,0,0,0],
       [1,1,1,1,1,1,0,0],
       [1,1,1,1,1,1,0,0]],
       [[1,1,1,1,1,1,1,0],
       [1,1,1,1,1,1,1,0],
       [0,0,0,0,0,1,1,0],
       [1,1,1,1,1,1,1,0],
       [1,1,1,1,1,1,1,0],
       [1,1,0,0,0,0,0,0],
       [1,1,1,1,1,1,1,0],
       [1,1,1,1,1,1,1,0]],
       [[1,1,1,1,1,1,1,0],
       [1,1,1,1,1,1,1,0],
       [0,0,0,0,0,1,1,0],
       [1,1,1,1,1,1,1,0],
       [1,1,1,1,1,1,1,0],
       [0,0,0,0,0,1,1,0],
       [1,1,1,1,1,1,1,0],
       [1,1,1,1,1,1,1,0]],
       [[1,1,0,0,0,0,0,0],
       [1,1,0,1,1,0,0,0],
       [1,1,0,1,1,0,0,0],
       [1,1,1,1,1,1,1,0],
       [1,1,1,1,1,1,1,0],
       [0,0,0,1,1,0,0,0],
       [0,0,0,1,1,0,0,0],
       [0,0,0,1,1,0,0,0]],
       [[1,1,1,1,1,1,1,0],
       [1,1,1,1,1,1,1,0],
       [1,1,0,0,0,0,0,0],
       [1,1,1,1,1,1,1,0],
       [1,1,1,1,1,1,1,0],
       [0,0,0,0,0,1,1,0],
       [1,1,1,1,1,1,1,0],
       [1,1,1,1,1,1,1,0]],
       [[1,1,1,1,1,1,1,0],
       [1,1,1,1,1,1,1,0],
       [1,1,0,0,0,0,0,0],
       [1,1,1,1,1,1,1,0],
       [1,1,1,1,1,1,1,0],
       [1,1,0,0,0,1,1,0],
       [1,1,1,1,1,1,1,0],
       [1,1,1,1,1,1,1,0]],
       [[1,1,1,1,1,1,1,0],
       [1,1,1,1,1,1,1,0],
       [0,0,0,0,0,1,1,0],
       [0,0,0,0,1,1,0,0],
       [0,0,0,1,1,0,0,0],
       [0,0,1,1,0,0,0,0],
       [0,1,1,0,0,0,0,0],
       [1,1,0,0,0,0,0,0]],   
       [[1,1,1,1,1,1,1,0],
       [1,1,1,1,1,1,1,0],
       [1,1,0,0,0,1,1,0],
       [1,1,1,1,1,1,1,0],
       [1,1,1,1,1,1,1,0],
       [1,1,0,0,0,1,1,0],
       [1,1,1,1,1,1,1,0],
       [1,1,1,1,1,1,1,0]],
       [[1,1,1,1,1,1,1,0],
       [1,1,1,1,1,1,1,0],
       [1,1,0,0,0,1,1,0],
       [1,1,1,1,1,1,1,0],
       [1,1,1,1,1,1,1,0],
       [0,0,0,0,0,1,1,0],
       [1,1,1,1,1,1,1,0],
       [1,1,1,1,1,1,1,0]]]
 
# icons are [PM1, PM2, CO2, VOC, ??] - each two characters wide
icons = [[[1,0,0,0,0,0,0,0],
       [1,0,1,1,1,0,1,0],
       [1,0,1,0,1,0,1,1],
       [1,0,1,1,1,0,1,0],
       [1,0,1,0,0,0,1,0],
       [1,0,1,0,0,0,1,0],
       [1,0,0,0,0,0,0,0],
       [1,1,1,1,1,1,1,1]],      
       [[0,0,0,0,0,0,0,1],
       [0,0,1,0,0,1,0,1],
       [0,1,1,0,0,1,0,1],
       [1,0,1,0,0,1,0,1],
       [0,0,1,0,0,1,0,1],
       [0,0,1,0,0,1,0,1],
       [0,0,0,0,0,0,0,1],
       [1,1,1,1,1,1,1,1]],
       [[1,0,0,0,0,0,0,0],
       [1,0,1,1,1,0,1,0],
       [1,0,1,0,1,0,1,1],
       [1,0,1,1,1,0,1,0],
       [1,0,1,0,0,0,1,0],
       [1,0,1,0,0,0,1,0],
       [1,0,0,0,0,0,0,0],
       [1,1,1,1,1,1,1,1]],      
       [[0,0,0,0,0,0,0,1],
       [0,0,1,0,1,1,0,1],
       [0,1,1,0,0,1,0,1],
       [1,0,1,0,1,1,0,1],
       [0,0,1,0,1,0,0,1],
       [0,0,1,0,1,1,0,1],
       [0,0,0,0,0,0,0,1],
       [1,1,1,1,1,1,1,1]],      
       [[1,0,0,0,0,0,0,0],
       [1,0,1,1,1,0,1,1],
       [1,0,1,0,0,0,1,0],
       [1,0,1,0,0,0,1,0],
       [1,0,1,0,0,0,1,0],
       [1,0,1,1,1,0,1,1],
       [1,0,0,0,0,0,0,0],
       [1,1,1,1,1,1,1,1]],      
       [[0,0,0,0,0,0,0,1],
       [1,1,0,1,1,1,0,1],
       [0,1,0,0,0,1,0,1],
       [0,1,0,1,1,1,0,1],
       [0,1,0,1,0,0,0,1],
       [1,1,0,1,1,1,0,1],
       [0,0,0,0,0,0,0,1],
       [1,1,1,1,1,1,1,1]],
       [[1,0,0,0,0,0,0,0],
       [1,0,1,0,0,0,1,0],
       [1,0,1,0,0,0,1,0],
       [1,0,1,0,0,0,1,0],
       [1,0,0,1,0,1,0,0],
       [1,0,0,0,1,0,0,0],
       [1,0,0,0,0,0,0,0],
       [1,1,1,1,1,1,1,1]],      
       [[0,0,0,0,0,0,0,1],
       [1,1,1,0,1,1,0,1],
       [1,0,1,0,1,0,0,1],
       [1,0,1,0,1,0,0,1],
       [1,0,1,0,1,0,0,1],
       [1,1,1,0,1,1,0,1],
       [0,0,0,0,0,0,0,1],
       [1,1,1,1,1,1,1,1]],
       [[1,0,1,1,1,1,0,0],
       [1,0,0,0,0,1,0,0],
       [1,0,0,1,1,1,0,0],
       [1,0,0,1,0,0,0,0],
       [1,0,0,0,0,0,0,0],
       [1,0,0,1,0,0,0,0],
       [1,0,0,0,0,0,0,0],
       [1,1,1,1,1,1,1,1]],      
       [[0,0,1,1,1,1,0,1],
       [0,0,0,0,0,1,0,1],
       [0,0,0,1,1,1,0,1],
       [0,0,0,1,0,0,0,1],
       [0,0,0,0,0,0,0,1],
       [0,0,0,1,0,0,0,1],
       [0,0,0,0,0,0,0,1],
       [1,1,1,1,1,1,1,1]]]
   

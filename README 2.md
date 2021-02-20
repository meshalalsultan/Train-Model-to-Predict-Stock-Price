# Train Model to Predict Stock Price
Train and test Artificial neural networks To Predict Stock Price with LSTM - Long short term memory  


## Build Simpelst Artificial neural networks (RNN)

With help of Keras as Tensorflow backend build Sequential RNN model :
1- Get the data with investpy model
2- Save the data on the path
3- Get the data and plot the close price
4- Scale the data on one scale by sklearn MinMaxScaler to be from 0 to 1 - to help the model to train on one scale
5- Divid the data to training and testing , by 70% of the data training and 30% to test the model .
6- build the model Sequential 256 AND 1 with loss ='mean_squared_error' , optimizer = 'adam' .

### The Model on Tesla stock. = tsla

the model itorate 1 epch and give 
Keras model loss =  0.0013431763921056313
Keras model accuracy =  0.0005977286491543055
on training predict

[[0.0439623 ]
 [0.04322571]
 [0.04217923]
 ...
 [0.29527825]
 [0.27766758]
 [0.28299353]]
[[11.389302]
 [11.25142 ]
 [11.05553 ]
 ...
 [58.43314 ]
 [55.136597]
 [56.13356 ]]
 
 
 ## TO USE 
 *note : you must have tensorfloe = 2.0
 
 
 - clone the repo by git clone https://github.com/meshalalsultan/Train-Model-to-Predict-Stock-Price.git
 - cd Stock Pred With Keras
 - go to get_data.py on any IDE and write the stock ticker you want and save all .
 - on terminal python get_data.py to get and save the data .
 - python price_pred.py to get the loss and figure


 

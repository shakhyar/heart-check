Cardiovascular diseases accounted for 28.1% of total deaths in India. 



Most people had this diseases because of unhealthy diets, less precautions and late diagnosis. 
If people have been diagnosed earlier, they would be safe. But since heart disease diagnosis is 
quite expensive, and since the best doctors are busy with active heart disease patients, many patients with less symptoms get
ignored as well sometimes. This is actually a big problem. But there is a solution for everything. 
Because of the tremendous  advancement in artificial intelligence in the past 2 decades, we can now 
predict whether people are going to have a heart disease or not beforehand. I have built the same heart disease ML classifier with Decision Tree Architecture with an accuracy of 88.7%, and hosted it on web for anyone to check themselves if they 
have a heart disease or not. The model not only predicts whether you have a disease or not, but also predicts the rate of intensity of your disease. The scope of this approach was to encourage people to take a quick survey that can be a life saver, and it's totally free. The site is up and running at: https://http://heartcheck.pythonanywhere.com/, and this project is totally open source, so it's up at github at https://github.com/shakhyar/heart-check/


As I hosted this website for free, I couldn't get much CPU and RAM. Therefore I worked with a smaller dataset because deep learning needs advanced hardwares for faster predictions. 
I have used Python3 for this project, Flask for connecting the front-end with backend, tailwind css for the the front-end, numpy and pandas for data preprocessing, and sklearn for Machine Learning. 
The test has been made on multiple Architectures like KNN, SVM, SGD, Naive Bayes, Random Forest, Decision Tree. KNN was giving good accuracy as well but when the neighbors increased, the accuracy decreased. Also the  Decision Tree was more accurate, and was more light weight. 
Also if we keep scaling the model with bigger data, the KNN model might struggle at some point as this data was very noisy, and will be more CPU intensive in future. 
Furthermore in future, we can use good cloud computing services like Google Cloud or AWS and use deep learning for better results. Since we just want to have the appropriate predictions done, this is the best version for now and is highly scalable. 


This project is documented more extensively on my github repo https://github.com/shakhyar/heart-check/

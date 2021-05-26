## Spam_Classifier_Flask_deploy

### About
Spam/Ham Classifier creation and its deployment using Flask, Frontend creation using Flasgger and URL generation using Ngrok<br />

### Model Training and Pickling
We have used a small training dataset of around 1400 instances of Spam and Ham SMS to train our model (Naive Byes Classifier). The Dataset can be found at spam1.csv<br />
After training we have created a pickle file of the classifier that can be found at classifier.pkl<br />

### App Deployment
We have used the Flask framework for the deployment and the Flasgger library to create an instantaneous Frontend UI. Since we have used the Colab Notebook to run the app, we were unable to access localhost that's why we have used ngrok library to create a URL.<br />
<br />
![url illustration](url_illus.jpg)<br />
<br />
Add "/apidocs" at the end of the second URL and run on your browser.<br />

### Flasgger
After opening the URL, the homepage would look something like this:<br />
<br />
![Flasgger home page illustration](flasgger_home.jpg)<br />
<img src="flasgger_home.jpg" width="48"><br />

Type some texts to check their category:<br /><br />
![Spam illustration](spam_illus.jpg)<br /><br />
![Ham illustration](ham_illus.jpg)<br />

### Tools used:

Classifier Model : Naive Bayes<br />
App Framework    : Flask<br />
Frontend UI      : Flasgger<br />
URL Generation   : Ngrok<br />

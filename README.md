## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves).
* The dataset contains +4 thousand images taken from client's crop fields. The images show cherry leaves that are healthy and cherry leaves that contain powdery mildew, which is a fungal disease that affects a wide range of plants. The cherry plantation crop is one of their finest products in the portfolio and the company is concerned about supplying the market with a product of compromised quality.



## Business Requirements
The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is to manually verify if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If it has powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees located in multiple farms across the country. As a result, this manual process is not scalable due to time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that is capable of detecting instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project to all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.


* 1 - The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy and that contains powdery mildew.
* 2 - The client is interested to predict if a cherry leaf is healthy or contains powdery mildew.


## Hypothesis and how to validate?
* We suspected powdery mildew leaves to have clear signs.
An Image Montage shows that typically a leaf had a white powdery like covering on it.
* Average Image, Variability Image and Difference between Averages studies did reveal clear a pattern to differentiate the leaves.
* Powdery mildew leaves clearly have the white shadow covering on them.


## Rationale to map the business requirements to the Data Visualizations and ML tasks
* **Business Requirement 1**: Data Visualization 
	* We will display the "mean" and "standard deviation" images for healthy and powdery mildew leaves.
 	* We will display the difference between an average healthy leaf and an average powdery mildew leaf.
	* We will display a image montage for either healthy or powdery mildew leaves.
	
	

* **Business Requirement 2**:  Classification
	* We want to predict if a given leaf is effected or not by powdery mildew. 
	* We want to build a binary classifier and generate reports.


## ML Business Case
* We want a ML model to predict if a leaf is effected by powdery mildew or not, based on historical image data. It is a supervised model, a 2-class, single-label, classification model.
* Our ideal outcome is provide the Farmy & Foods team with a faster and reliable diagnostic if a given cell is effected or not by powdery mildew.
* The model success metrics are
	* Accuracy of 97% or above on the test set.
* The model output is defined as a flag, indicating if the leaf has powdery mildew or not and the associated probability of being effected or not. The Farmy & Foods team will do the testing workflow as usual and upload the picture to an App. The prediction can be made on the fly (not in batches).
* Heuristics: The current diagnostic needs an experienced staff and detailed inspection to distinguish effected and not effected leaves. A leaf sample is collected and examined. Visual criteria are used to detect powdery mildew. It leaves room to produce inaccurate diagnostics due to human errors. On top of that, there is a significant time loss due to the manual process.
* We have extracted the data of 4208 images from this dataset and saved it to [kaggle dataset directory](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves) for model training.
	* Train data - target: powdery mildew or not; features: all images


## Dashboard Design (Streamlit App User Interface)

### Page 1: Quick Project Summary
* Quick project summary
	* General Information
        * Powdery mildew is a fungal disease of the foliage, stems and occasionally flowers and fruit where a superficial fungal growth covers the surface of the plant.
        * A leaf is collected and examined and visual criteria are used to detect powdery mildew.
	* Project Dataset
		The dataset contains 4208 cherry leaves images provided by Farmy & Foods, taken from their crops.
	* Business requirements
		*  The client is interested to have a study to visually differentiate between a healthy  and powdery mildew leaf.
		*  The client is interested to tell whether a given leaf is effected by powdery mildew or not.

### Page 2: Cells Visualizer
* It will answer business requirement 1
	* Checkbox 1 - Difference between average and variability image
	* Checkbox 2 - Differences between average healthy and average powdery mildew leaves
	* Checkbox 3 - Image Montage

### Page 3: Malaria Detector
* Business requirement 2 information - "The client is interested to tell whether a given leaf contains powdery mildew or not."
* Link to download a set of healthy and powdery mildew leaf images for live prediction. [kaggle dataset directory](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)
* User Interface with a file uploader widget. The user can upload multiple leaf images. It will display the image and a prediction statement, indicating if the leaf is effected or not with powdery mildew and the probability associated with this statement. 
* Table with image name and prediction results.
* Download button to download table.

### Page 4: Project Hypothesis and Validation
* Block for the project hypothesis, describe the conclusion and validation.

### Page 5: ML Performance Metrics
* Label Frequencies for Train, Validation and Test Sets
* Model History - Accuracy and Losses
* Model evaluation result


## Unfixed Bugs
    No Known bugs

## Deployment
### Heroku

* The App live link is: https://mildew-detection-live.herokuapp.com/ 
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly in case all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.


## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries you used in the project and provide example(s) on how you used these libraries.


## Credits 

* All the functions that has the comment
    * "# This function is from the Code Institutes walkthrough project"
was taken from the code intitute walkthrough project
* The dashboard is inspired by the code instute walkthrough project because their context is very similar

### Content 

- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media
- the images are from this [kaggle dataset directory](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)



## Acknowledgements (optional)
- The code instatue walkthrough project resourses were a big help
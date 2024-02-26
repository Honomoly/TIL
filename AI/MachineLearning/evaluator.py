from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, mean_squared_error, r2_score
import numpy as np

# Classifier의 평가 지표 출력 함수 
def get_clf_eval(y_test, y_pred, y_pred_proba=None):
    confusion = confusion_matrix( y_test, y_pred)
    accuracy = accuracy_score(y_test , y_pred)
    precision = precision_score(y_test , y_pred)
    recall = recall_score(y_test , y_pred)    
    f1 = f1_score(y_test,y_pred)   
    roc_auc = roc_auc_score(y_test, y_pred_proba)
    
    print('< Confusion Matrix >')
    print(confusion)
    print('Accuracy : {0:.4f}, Precision : {1:.4f}, Recall : {2:.4f}, F1 Score : {3:.4f}, ROC_AUC : {4:.4f}'.format(accuracy, precision, recall, f1, roc_auc))

# Regression의 MSE, RMSE, R2를 출력하는 함수
def get_reg_eval(y_test, y_pred):
    mse = mean_squared_error(y_test, y_pred)
    print('MSE : %.6f'%mse)
    print('RMSE : %.6f'%np.sqrt(mse))
    print('R2 : %.6f'%r2_score(y_test, y_pred))

# 학습된 Regression 모델과 데이터셋을 입력받아 평가수치를 보여주는 함수
def get_eval(model, X_test, y_test):
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print('MSE : %.6f'%mse)
    print('RMSE : %.6f'%np.sqrt(mse))
    print('R2 : %.6f'%r2_score(y_test, y_pred))

# 리스트를 주축으로 가진 딕셔너리를 모든 경우의 수로 분리한다
def grid_decomp(dict_input):
    keys = list(dict_input.keys())
    lengths = [len(dict_input[key]) for key in keys]
    index = [0 for key in keys]
    pt = 0 # pointer
    keys_len = len(keys)
    result = list()
    do_append = True
    while pt < keys_len:
        if do_append:
            elt = {keys[i]:dict_input[keys[i]][index[i]] for i in range(keys_len)}
            result.append(elt)
            
        index[pt] += 1
        if index[pt] >= lengths[pt]:
            do_append = False
            index[pt] = 0
            pt += 1
        else:
            do_append=True
            pt = 0
    return result
        
        
        
        
        
        
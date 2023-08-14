import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import time

class dtex:

    #INTRO
    def dtex():
        print('dtex..., hlo this is open source data prepration library to assist in data preprocessing for Machine Learning')

    #FEATURE_ENGINEERING
    def auto_fillmt(data, features = None, categorical = None, print_time = True):
        start = time.time()
        data = data.copy()
        if features == None:
            features = data.columns
        if categorical == None:
            for feature in features:
                if data[feature].dtype == 'O':
                    mt_list = np.where(data[feature].isnull())[0]
                    data.loc[mt_list, feature] = 'missing'
                elif data[feature].dtype != 'O':
                    mt_list = np.where(data[feature].isnull())[0]
                    data.loc[mt_list, feature] = data[feature].median()
            end = time.time()
            if print_time:
                t = end-start
                print(str(np.round(t, 5))+'s...')
            return data
        else:
            for feature, category in zip(features, categorical):
                mt_list = np.where(data[feature].isnull())[0]
                if category == True:
                    data.loc[mt_list, feature] = data[feature].mode()[0]
                    data[feature] = data[feature].astype(np.int64)
                else:
                    data.loc[mt_list, feature] = data[feature].median()
            end = time.time()
            t = end-start
            print(str(np.round(t, 5))+'s...')
            return data

    #FEATURE_ENGINEERING
    def fillmt(data, features = [], categorical = True, print_time = True):
        start = time.time()
        data = data.copy()
        for feature in features:
            if categorical == True:
                data[feature] = np.where(data[feature].isnull(), 'missing', data[feature])
            else:
                data[feature] = np.where(data[feature].isnull(), data[feature].median(), data[feature])
                # data.loc[mt, feature] = data[feature].median()
        if print_time:
            end = time.time()
            t = end-start
            print(str(np.round(t, 5))+'s...')
        return data

    #FEATURE ENGINEERING
    def category_processing(data, features = [], verbose = True, print_time = False):
        start = time.time()
        data = data.copy()
        for feature in features:
            unique_list = data[feature].unique()
            if verbose:
                print(feature)
            for m, l in enumerate(unique_list):
                l_loc = np.where(data[feature] == l)[0]
                data.loc[l_loc, feature] = m
                if verbose:
                    print('\t'+str(l)+':', str(m))
        if print_time:
            end = time.time()
            t = end-start
            print(str(np.round(t, 5))+'s...')
        return data

    #FEATURE_ENGINEERING
    def category_mapping(data, features = [], target_feature = '', verbose = True, print_time = False):
        start = time.time()
        data = data.copy()
        for feature in features:
            i = data.groupby([feature])[target_feature].mean().sort_values().index
            i = {l:n for n, l in enumerate(i, 0)}
            data[feature] = data[feature].map(i)
            if verbose == 1:
                print(i)
        if print_time:
            end = time.time()
            t = end-start
            print(str(np.round(t, 5))+'s...')
        return data

    #EDA
    def missing_percentage(data, print_time = False):
        start = time.time()
        data = data.copy()
        features = [feature for feature in data.columns if True in data[feature].isnull().to_list()]
        for feature in features:
            # print(feature, 'has', (len(np.where(data[feature].isnull())[0]))*100)/len(data[feature], '% missing values')
            print(feature, 'has', np.round(np.where(data[feature].isnull(), 1, 0).mean()*100, 4), '% missing values')
        if print_time:
            end = time.time()
            t = end-start
            print(str(np.round(t, 5))+'s...')

    #EDA
    def null_relations(data, target_feature, target_feature_catogory = True, print_time = True):
        start = time.time()
        data = data.copy()
        features = data.columns
        if target_feature_catogory == True:
            pass
        elif target_feature_catogory == False:
            features = [feature for feature in features if True in data[feature].isnull().to_list()]
            for feature in features:
                data[feature] = np.where(data[feature].isnull(), 1, 0)
                data.groupby([feature])[target_feature].median().plot.bar()
                plt.title(feature)
                plt.ylabel(target_feature)
                plt.xlabel(feature)
                plt.axis(True)
                plt.grid(False)
                plt.show()
            if print_time:
                end = time.time()
                t = end-start
                print(str(np.round(t, 5))+'s...')

    def feature_distribution(data, threshold_for_deciding_continous_discrete = 25, temporal_features = None, print_features = True, print_time = False):
        start = time.time()
        dict = {}
        data = data.copy()
        features = data.columns
        object_features = [feature for feature in features if data[feature].dtype == 'O']
        numerical_features = [feature for feature in features if data[feature].dtype != 'O']
        if temporal_features != None:
            temporal_object_features = [feature for feature in temporal_features if data[feature].dtype == 'O']
        else:
            temporal_object_features = [feature for feature in object_features if 'Yr' in feature or 'Year' in feature or 'Dt' in feature or 'Id' in feature]
        discrete_object_features = [feature for feature in object_features if feature not in temporal_object_features]
        if temporal_features != None:
            temporal_numerical_features = [feature for feature in temporal_features if data[feature].dtype != 'O']
        else:
            temporal_numerical_features = [feature for feature in numerical_features if 'Yr' in feature or 'Date' in feature or 'Year' in feature or 'Dt' in feature]
            temporal_features = temporal_object_features+temporal_numerical_features
        continous_features = [feature for feature in numerical_features if len(data[feature].unique()) > threshold_for_deciding_continous_discrete and feature not in temporal_features]
        discrete_numerical_features = [feature for feature in numerical_features if feature not in temporal_numerical_features and feature not in continous_features]
        discrete_features = discrete_object_features+discrete_numerical_features
        dict['Object Features'] = object_features
        dict['Numerical Feature'] = numerical_features
        dict['Temporal Object Features'] = temporal_object_features
        dict['Temporal Numerical Features'] = temporal_numerical_features
        dict['Temporal Features'] = temporal_features
        dict['Discrete Object Features'] = discrete_object_features
        dict['Discrete Numerical Features'] = discrete_numerical_features
        dict['Discrete Features'] = discrete_features
        dict['Continous Features'] = continous_features
        if print_features:
            for key in dict.keys():
                print(key+':', dict[key])
        if print_time:
            end = time.time()
            t = end-start
            print(str(np.round(t, 5))+'s...')
        return dict

    #EDA
    def discrete_relations(data, target_feature, discrete_features = [], target_feature_catogory = False, print_time = True):
        start = time.time()
        data = data.copy()
        if target_feature_catogory == True:
            pass
        elif target_feature_catogory == False:
            for feature in discrete_features:
                data.groupby([feature])[target_feature].median().plot.bar()
                plt.title(feature)
                plt.ylabel(target_feature)
                plt.xlabel(feature)
                plt.grid(False)
                plt.axis(True)
                plt.show()
            if print_time:
                end = time.time()
                t = end-start
                print(str(np.round(t, 5))+'s...')

    #EDA
    def continous_plot(data, continous_features = [], histplot = True, bins_no = 15, kde = True, print_skewness = True, print_time = False):
        start = time.time()
        data = data.copy()
        if histplot:
            for feature in continous_features:
                if kde == True:
                    sns.histplot(data[feature], bins = bins_no, kde = True)
                else:
                    sns.histplot(data[feature], bins = bins_no)
                plt.xlabel(feature)
                plt.title(feature)
                plt.grid(False)
                plt.axis(True)
                plt.show()
                if print_skewness:
                    print('Skewness of', feature+':', data[feature].skew())
        else:
            for feature in continous_features:
                plt.plot(data[feature])
                plt.xlabel(feature)
                plt.title(feature)
                plt.grid(False)
                plt.axis(True)
                plt.show()
                if print_skewness:
                    print('Skewness of', feature+':', data[feature].skew())
        if print_time:
            end = time.time()
            t = end-start
            print(str(np.round(t, 5))+'s...')

    #EDA
    def temporal_relations(data, temporal_numerical_features = [], target_feature = '', target_feature_categorical = False, print_time = False):
        start = time.time()
        data = data.copy()
        if target_feature_categorical == False:
            for feature in temporal_numerical_features:
                data.groupby(feature)[target_feature].median().plot()
                plt.grid(False)
                plt.axis(True)
                plt.title(str(feature))
                plt.xlabel(str(feature))
                plt.ylabel('Median', str(target_feature))
                plt.show()
        else:
            pass
        if print_time: print(str(np.round(time.time()-start, 5))+'s...')

    #EDA
    def continous_relations(data, continous_features = [], target_feature = '', print_time = False):
        start = time.time()
        data = data.copy()
        for feature in continous_features:
            plt.scatter(data[feature], data[target_feature])
            plt.grid(False)
            plt.axis(True)
            plt.ylabel(target_feature)
            plt.xlabel(feature)
            plt.title(feature)
            plt.show()
        if print_time:
            print(str(np.round(time.time()-start, 5))+'s...')

    #EDA
    def outliers_vis(data, continous_features = [], verbose = 1, print_time = False):
        start = time.time()
        data = data.copy()
        dict = {}
        dict['Min'] = []
        dict['25th Percentile'] = []
        dict['Median'] = []
        dict['75th Percentile'] = []
        dict['Max'] = []
        for feature in continous_features:
            q1, q3 = np.percentile(data[feature], [25, 75])
            iqr = q3-q1
            lowerThresh = q1-(1.5*iqr)
            upperThresh = q3+(1.5*iqr)
            plt.boxplot(data[feature])
            plt.grid(True)
            plt.axis(True)
            plt.xlabel('Density')
            plt.ylabel(feature)
            plt.title(feature)
            plt.show()
            print(str(feature), 'has', str((len(np.where(~(data[feature]<upperThresh) | ~(data[feature]>lowerThresh))[0])*100)/len(data[feature]))+'%')
            dict['Min'].append(lowerThresh)
            dict['25th Percentile'].append(q1)
            dict['Median'].append(data[feature].median())
            dict['75th Percentile'].append(q3)
            dict['Max'].append(upperThresh)
        outlier_summary = pd.DataFrame(dict, index=continous_features)
        if verbose == 1:
            print(outlier_summary)
        if print_time:
            print(str(np.round(time.time()-start, 5))+'s...')

    #FEATURE ENGINEERING
    def rare_categorical(data, discrete_features = [], drop_missing = False, print_time = False):
        start = time.time()
        data = data.copy()
        for feature in discrete_features:
            i = data.groupby([feature])[feature].count()/len(data)
            if drop_missing:
                i.drop('missing', inplace = True)
            i = i[i<=0.01].index
            data[feature] = np.where(data[feature].isin(i), 'rare-var', data[feature])
            print('Rare features are marked "rare-var"')
        if print_time:
            print(str(np.round(time.time()-start, 5))+'s...')
        return data

    # def skewness_removal(data, continous_features = [], ):

    # def split_columns(data, numerical, categorical, temporal):
    #     data = data.copy()
    #     data_nu = data[feature for feature in numerical].copy()

    #EDA
    def eda(data, temporal_features = [], thresh = 15, target_feature = '', target_feature_category = False, temporal_f = None, temporal_relations = False, print_time = True):
        start = time.time()
        data = data.copy()
        dtex.missing_percentage(data)
        dict = dtex.feature_distribution(data, thresh, temporal_features)
        print('\nNumerical Variables\n')
        print('\nContinous\n')
        dtex.continous_plot(data, dict['Continous Features'])
        print('\nContinous-Target\n')
        dtex.continous_relations(data, dict['Continous Features'], target_feature = target_feature)
        print('\nDiscrete-Target\n')
        dtex.discrete_relations(data, target_feature = target_feature, discrete_features = dict['Discrete Features'])
        if temporal_relations:
            print('\nTemporal-Target\n')
            if temporal_f == None:
                for feature in dict['Temporal Numerical Features']:                
                    plt.plot(data[target_feature], data[feature])
            else:
                for feature in temporal_f:
                    plt.plot(data[target_feature], data[feature])
        print('\nOoutliers Visualization\n')
        dtex.outliers_vis(data, dict['Continous Features'])

    def data_report():
        pass

class dimg:
    def dimg():
        print('dimg')

class daud:
    def daud():
        print('daud')

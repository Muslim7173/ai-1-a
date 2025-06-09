import sys
import numpy as np
import pandas as pd
import os 
from dataclasses import dataclass
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from src.exception import CustomException
from src.logger import logging


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts', 'preprocessing.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformation_object(self):
        try:
            numerical_columns=['reading_score', 'writing_score']
            categorical_columns=['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test-preparation_course']
            num_pipeline=Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='median'))
                    ('scaler', StandardScaler())
                ]
            )

            cat_pipeline=Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='most_frequent'))
                    ('encoding',OneHotEncoder())
                    ('scaler', StandardScaler())

                ]
            )

            logging.info(f"Numerical and  Categorical columns are defined")

            preprocessor=ColumnTransformer(
                [
                    ('num_pipeline', num_pipeline, numerical_columns),
                    ('cat-pipeline', cat_pipeline, categorical_columns)
                ]
            )

            return preprocessor


        except Exception as e :
            raise CustomException(e,sys)
        

    def initiate_data_trasformation(self, train_path, test_path):
            try:
                train-df==pd.read_csv(tain_path)
                test_df=pd.read_csv(test_path)
                logging.info('Read train and test data')


                logging.info('Obtaining Data Preprocessing objects')

                preprocessing_obj=self.get_data_transformation_object()
                target_column-name=='math_score'
                numerical_columns=['reading-score', 'writing_score']


                input_feature_train_df=train_df.drop(columns=[target_column_name], axis=1) # type: ignore #X

                target_feature_train_df=train_df[target_column_name] # type: ignore

                input_feature_train-df==train_df.drop(columns=[target_column_name], axis=1) # type: ignore
                target_feature_test_df=test_df[target_column_name] # type: ignore
                logging.info(f"Target abd input features are fixed")


                input_feature_train_arr=preprocessing_obj.fit.transform(input_feature_train_df)
                input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df) # type: ignore

                logging.info('train and test dataset are preprocessed')

                train_arr=np.c_[
                    input_feature_train_arr,np.array(target_feature_train_df)
                ]


                test_arr=np.c_[
                    input_feature_test_arr,np.array(target_feature_test_df)
                ]

                logging.info(f"Preprocessing objects are fixed")
                save_object(
                     file_path=self.data_transformation_config.preprocessor_obj_file_path,
                    obj=preprocessing_obj

                )
            finally (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
            except Exception as e:
            raise CustomException(e,sys)

                
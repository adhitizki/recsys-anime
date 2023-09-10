import pandas as pd
import numpy as np
from surprise import SVD
import pickle

# load model
with open('model/model_svd.pkl', 'rb') as f:
    MODEL = pickle.load(f)

class AnimeRecSys:
    def __init__(self, user_id) -> None:
        self.user_id = user_id

    def load_dataset(self):
        # Load data rating
        df_rating = pd.read_csv('data/data_2/rating.csv')
        df_rating = df_rating[df_rating['rating']>-1].reset_index(drop=True)

        # User minimum watch 10 animes
        user_id = df_rating['user_id'].value_counts()
        user_id = user_id[user_id >= 10].index
        df_rating = df_rating[df_rating['user_id'].isin(user_id)]

        self.df_rating = df_rating.reset_index(drop=True)

        # Load data anime
        self.df_anime = pd.read_csv('data/data_2/anime.csv')

    def get_unrated_item(self): ### credit pacmann
        """
        Get unrated item id from a user id

        Returns
        -------
        unrated_item_id : set
            The unrated item id
        """
        # Find the whole item id
        unique_item_id = set(self.df_rating['anime_id'])

        # Find the item id that was rated by user id
        rated_item_id = set(self.df_rating.loc[self.df_rating['user_id']==self.user_id, 'anime_id'])

        # Find the unrated item id
        unrated_item_id = unique_item_id.difference(rated_item_id)

        # Filter only anime that in anime list
        anime_id = self.df_anime['anime_id']
        self.unrated_item_id = [i for i in unrated_item_id if i in anime_id]
    
    def get_pred_unrated_item(self): ### credit pacmann
        """
        Get the predicted unrated item id from user id

        Returns
        -------
        pred_data : pandas Dataframe
            The predicted rating of unrated item of user id
        """
        # Initialize dict
        pred_dict = {
            'user_id': self.user_id,
            'anime_id': [],
            'predict_rating': []
        }

        # Loop for over all unrated movie Id
        for id in self.unrated_item_id:
            # Create a prediction
            pred_id = MODEL.predict(uid = pred_dict['user_id'],
                                        iid = id)

            # Append
            pred_dict['anime_id'].append(id)
            pred_dict['predict_rating'].append(pred_id.est)

        # Create a dataframe
        self.predicted_unrated_item = pd.DataFrame(pred_dict).sort_values('predict_rating',
                                                        ascending = False)
    
    def top_predict(self, k=10):  ## credit pacmann
        """
        Get top k highest of unrated movie from a Surprise estimator RecSys

        Parameters
        ----------
        k : int
            The number of Recommendations

        Returns
        -------
        top_item_pred : pandas DataFrame
            The top items recommendations
        """
        # Load datase
        self.load_dataset()

        # Get the unrated item id of a user id
        self.get_unrated_item()

        # Create prediction from estimator to all unrated item id
        self.get_pred_unrated_item()

        # Sort & add meta data
        top_item_pred = self.predicted_unrated_item.head(k).copy()
        top_item_pred['name'] = self.df_anime.loc[top_item_pred['anime_id'], 'name'].values
        top_item_pred['genre'] = self.df_anime.loc[top_item_pred['anime_id'], 'genre'].values

        return top_item_pred.reset_index(drop=True)
    
    def predict(self, anime_id):
        return MODEL.predict(self.user_id, anime_id).est
    


if __name__=="__main__":
    test = AnimeRecSys(10)
    res = test.top_predict(10)

    print(res)